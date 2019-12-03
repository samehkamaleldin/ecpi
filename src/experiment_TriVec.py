# -*- coding: utf-8 -*-

import os
import itertools
import gzip
import numpy as np
from sklearn.pipeline import Pipeline
from tqdm import tqdm
from libkge.embedding import TransE, DistMult, ComplEx, TriModel, DistMult_MCL, ComplEx_MCL, TriModel_MCL
from libkge import KgDataset
from libkge.io import load_kg_file
from libkge.embedding.train import generate_batches
from libkge.metrics.ranking import precision_at_k, average_precision
from libkge.metrics.classification import auc_roc, auc_pr


def main():
    seed = 1234
    data_name = "cpf"
    kg_dp_path = "../data/"

    print("Importing dataset files ... ")
    train_data_raw = load_kg_file(os.path.join(kg_dp_path, "train.txt"))
    test_data_raw = load_kg_file(os.path.join(kg_dp_path, "test.txt"))

    all_data = np.array([[s, p, o] for s, p, o in np.concatenate([train_data_raw, test_data_raw])])

    chemicals_list = set(list(all_data[:, 0]))
    effects_list = set(list(all_data[:, 1]))
    proteins_list = set(list(all_data[:, 2]))

    dataset = KgDataset(name=data_name)
    dataset.load_triples(train_data_raw, tag="train")
    dataset.load_triples(test_data_raw, tag="test")

    nb_rels = dataset.get_rels_count()
    nb_ents = dataset.get_rels_count()

    train_data = dataset.data["train"]
    test_data = dataset.data["test"]

    fn_known_facts = {k: set() for k in range(nb_rels)}
    for s, p, o in all_data:
        fn_known_facts[p].add((s, o))

    fn_test_dict = {k: [] for k in np.unique(test_data[:, 1])}
    for s, p, o in test_data:
        fn_test_dict[p].append([s, p, o])

    print("Initializing the knowledge graph embedding model... ")
    # model pipeline definition
    model = TriModel(seed=seed, verbose=2)
    pipe_model = Pipeline([('kge_model', model)])

    # set model parameters
    model_params = {
        'kge_model__em_size': 100,
        'kge_model__lr': 0.01,
        'kge_model__optimiser': "AMSgrad",
        'kge_model__log_interval': 10,
        'kge_model__nb_epochs': 100,
        'kge_model__batch_size': 5000,
        'kge_model__initialiser': 'xavier_uniform',
        'kge_model__nb_ents': nb_ents,
        'kge_model__nb_rels': nb_rels
    }

    # add parameters to the model then call fit method
    pipe_model.set_params(**model_params)

    print("Training ... ")
    pipe_model.fit(X=train_data, y=None)

    metrics_per_se = {se_idx: {"ap": .0, "auc-roc": .0, "auc-pr": .0, "p@50": .0} for se_idx in pse_indices}

    se_ap_list = []
    se_auc_roc_list = []
    se_auc_pr_list = []
    se_p50_list = []

    print("================================================================================")

    def generate_fn_negatives(fn_idx, neg_data_size):
        """

        :param fn_idx:
        :param neg_data_size:
        :return:
        """
        candidate_neg_size = int(neg_data_size * 1.2)
        candidate_subs = np.random.randint(0, nb_rels, [candidate_neg_size, 1])
        candidate_rel = np.ones([candidate_neg_size, 1]) * fn_idx
        candidate_objs = np.random.randint(0, nb_rels, [candidate_neg_size, 1])
        candidate_negs = np.concatenate([candidate_subs, candidate_rel, candidate_objs], axis=1)
        true_negs = []
        for s, p, o in candidate_negs:
            if (s, o) not in fn_known_facts[rel_idx]:
                true_negs.append([s, p, o])
        true_negs = np.array(true_negs)
        return true_negs[:neg_data_size, :]

    rel_results = []
    for idx, rel_idx in enumerate(fn_test_dict):
        rel_name = dataset.get_relations([rel_idx])[0]
        rel_test_data_pos = np.array(fn_test_dict[rel_idx])
        rel_test_size = len(rel_test_data_pos)

        rel_pos_scores = pipe_model.predict(rel_test_data_pos)

        res = {1: {"auroc": 0.0, "aupr": 0.0}, 10: {"auroc": 0.0, "aupr": 0.0}, 50: {"auroc": 0.0, "aupr": 0.0}}

        for neg_ratio in [1, 10, 50]:
            rel_test_data_neg = generate_fn_negatives(rel_idx, rel_test_size * neg_ratio)

            neg_scores = []
            for rel_test_data_neg_batch in generate_batches(rel_test_data_neg, batch_size=10000):
                batch_scores = pipe_model.predict(rel_test_data_neg_batch)
                neg_scores.extend(batch_scores)
            rel_neg_scores = np.array(neg_scores)

            rel_all_scores = np.concatenate([rel_pos_scores, rel_neg_scores])
            rel_all_labels = np.concatenate([np.ones([len(rel_pos_scores), ]), np.zeros([len(rel_neg_scores), ])])
            rel_aupr = auc_pr(rel_all_labels, rel_all_scores)
            rel_auroc = auc_roc(rel_all_labels, rel_all_scores)
            res[neg_ratio]["aupr"] = rel_aupr
            res[neg_ratio]["auroc"] = rel_auroc

        print("[%d] N1:AUROC %1.4f - N1:AUPR %1.4f\tN10:AUROC %1.4f - N10:AUPR %1.4f\tN50:AUROC %1.4f - N50:AUPR %1.4f"
              "\t[Count: %d]\tREL:%s" % (idx + 1, res[1]["auroc"], res[1]["aupr"], res[10]["auroc"], res[10]["aupr"],
                                         res[50]["auroc"], res[50]["aupr"], rel_test_size, rel_name))
        rel_results.append([res[1]["auroc"], res[1]["aupr"], res[10]["auroc"], res[10]["aupr"], res[50]["auroc"],
                            res[50]["aupr"]])
    rel_results = np.array(rel_results)
    n1_au_roc = np.mean(rel_results[:, 0])
    n1_au_pr = np.mean(rel_results[:, 1])
    n3_au_roc = np.mean(rel_results[:, 2])
    n3_au_pr = np.mean(rel_results[:, 3])
    n10_au_roc = np.mean(rel_results[:, 4])
    n10_au_pr = np.mean(rel_results[:, 5])
    print("-----------------------------------------------------------------------------------------------------------")
    print(
        "N1:AUROC %1.4f - N1:AUPR %1.4f\tN10:AUROC %1.4f - N10:AUPR %1.4f\tN50:AUROC %1.4f - N50:AUPR %1.4f = [AVERAGE]"
        % (n1_au_roc, n1_au_pr, n3_au_roc, n3_au_pr, n10_au_roc, n10_au_pr))
    print("-----------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()

