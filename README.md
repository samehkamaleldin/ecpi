# Predicting The Biological Effects of Chemical Protein Interactions

## Overview
This code contain scripts and data for and AMIA Informatics summit 2020 paper submission which studies the prediction of biological effects of chemical-protein interactions.

## Requirements
This repository only require the installation of `tensorflow` (standard or gpu) and the [LibKGE library](https://github.com/samehkamaleldin/libkge). 

## Usage
You can train a KGE models on the CTD38E dataset by running its corresponding training script from the src directory as follows:
``` bash
cd src
python experiment_TriVec.py
```
The script will then run and evaluate the model as follows:

```
Importing dataset files ...
Initializing the knowledge graph embedding model...
Training ...
2019-12-03 14:39:28,722 - TriModel - DEBUG - Logging model parameters ...
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] _predict_pipeline_on: False
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] batch_size          : 5000
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] em_size             : 100
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] initialiser         : xavier_uniform
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] log_interval        : 10
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] loss                : default
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] lr                  : 0.01
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] nb_ents             : 38
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] nb_epochs           : 100
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] nb_negs             : 2
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] nb_rels             : 38
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] optimiser           : AMSgrad
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] predict_batch_size  : 40000
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] reg_wt              : 0.01
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] seed                : 1234
2019-12-03 14:39:28,722 - TriModel - DEBUG - [Parameter] verbose             : 2
2019-12-03 14:39:28,722 - TriModel - DEBUG - Model training started ...
2019-12-03 14:39:28,722 - TriModel - DEBUG - Training model [ 639965 #Instances - 38 #Entities - 38 #Relations ]
2019-12-03 14:39:30,139 - TriModel - DEBUG - Initialising tensorflow session
2019-12-03 14:39:31,320 - TriModel - DEBUG - Executing tensorflow global variable initialiser
2019-12-03 14:39:32,399 - TriModel - DEBUG - [Training] Epoch # 1    - Speed: 608.626 (k. record/sec) - Loss: 0.6925 - Avg(Loss): 0.6925 - Std(Loss): 0.0004
2019-12-03 14:39:41,246 - TriModel - DEBUG - [Training] Epoch # 10   - Speed: 644.637 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0003
2019-12-03 14:39:51,172 - TriModel - DEBUG - [Training] Epoch # 20   - Speed: 643.619 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0003
2019-12-03 14:40:01,135 - TriModel - DEBUG - [Training] Epoch # 30   - Speed: 644.524 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:40:11,075 - TriModel - DEBUG - [Training] Epoch # 40   - Speed: 643.351 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:40:20,948 - TriModel - DEBUG - [Training] Epoch # 50   - Speed: 642.839 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:40:30,787 - TriModel - DEBUG - [Training] Epoch # 60   - Speed: 644.784 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:40:40,600 - TriModel - DEBUG - [Training] Epoch # 70   - Speed: 648.451 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:40:50,458 - TriModel - DEBUG - [Training] Epoch # 80   - Speed: 646.412 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:41:00,302 - TriModel - DEBUG - [Training] Epoch # 90   - Speed: 666.808 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:41:10,182 - TriModel - DEBUG - [Training] Epoch # 100  - Speed: 655.118 (k. record/sec) - Loss: 0.6922 - Avg(Loss): 0.6922 - Std(Loss): 0.0002
2019-12-03 14:41:10,185 - TriModel - DEBUG - [Reporting] Finished (100 Epochs) - Avg(Speed): 647.857 (k. record/sec) - Avg(Loss): 0.6922 - Std(Loss): 0.0002
[1] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 165]    REL:increases__O-linked_glycosylation
[2] N1:AUROC 0.9968 - N1:AUPR 0.9968    N10:AUROC 0.9994 - N10:AUPR 0.9936      N50:AUROC 0.9995 - N50:AUPR 0.9750      [Count: 312]    REL:affects__localization
[3] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 651]    REL:increases__chemical_synthesis
[4] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 284]    REL:decreases__phosphorylation
[5] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 18600]  REL:decreases__expression
[6] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 367]    REL:increases__response_to_substance
[7] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 542]    REL:affects__reaction
[8] N1:AUROC 0.2993 - N1:AUPR 0.5880    N10:AUROC 0.3102 - N10:AUPR 0.1266      N50:AUROC 0.3069 - N50:AUPR 0.0280      [Count: 137]    REL:increases__uptake
[9] N1:AUROC 1.0000 - N1:AUPR 1.0000    N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 359]    REL:decreases__response_to_substance
[10] N1:AUROC 0.9083 - N1:AUPR 0.9160   N10:AUROC 0.9028 - N10:AUPR 0.5070      N50:AUROC 0.8767 - N50:AUPR 0.1396      [Count: 109]    REL:increases__degradation
[11] N1:AUROC 0.4754 - N1:AUPR 0.6559   N10:AUROC 0.4656 - N10:AUPR 0.1576      N50:AUROC 0.4961 - N50:AUPR 0.0382      [Count: 61]     REL:increases__localization
[12] N1:AUROC 0.9767 - N1:AUPR 0.9773   N10:AUROC 0.9798 - N10:AUPR 0.8323      N50:AUROC 0.9809 - N50:AUPR 0.5109      [Count: 258]    REL:increases__abundance
[13] N1:AUROC 0.9937 - N1:AUPR 0.9937   N10:AUROC 0.9924 - N10:AUPR 0.9296      N50:AUROC 0.9926 - N50:AUPR 0.7287      [Count: 317]    REL:increases__cleavage
[14] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 829]    REL:decreases__methylation
[15] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 1996]   REL:affects__binding
[16] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 50]     REL:affects__splicing
[17] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 199]    REL:increases__metabolic_processing
[18] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 0.9992 - N50:AUPR 0.9615      [Count: 50]     REL:increases__reduction
[19] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 102]    REL:affects__activity
[20] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 570]    REL:affects__response_to_substance
[21] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 72]     REL:increases__mutagenesis
[22] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 432]    REL:affects__methylation
[23] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 1162]   REL:increases__methylation
[24] N1:AUROC 0.8961 - N1:AUPR 0.9059   N10:AUROC 0.9143 - N10:AUPR 0.5385      N50:AUROC 0.9169 - N50:AUPR 0.1940      [Count: 77]     REL:increases__glucuronidation
[25] N1:AUROC 0.0266 - N1:AUPR 0.5067   N10:AUROC 0.0185 - N10:AUPR 0.0925      N50:AUROC 0.0186 - N50:AUPR 0.0200      [Count: 753]    REL:increases__phosphorylation
[26] N1:AUROC 0.0187 - N1:AUPR 0.5047   N10:AUROC 0.0299 - N10:AUPR 0.0934      N50:AUROC 0.0290 - N50:AUPR 0.0202      [Count: 107]    REL:decreases__secretion
[27] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 0.9989 - N50:AUPR 0.9495      [Count: 94]     REL:affects__metabolic_processing
[28] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 78]     REL:increases__oxidation
[29] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 101]    REL:increases__transport
[30] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 9094]   REL:affects__cotreatment
[31] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 4109]   REL:decreases__reaction
[32] N1:AUROC 0.9993 - N1:AUPR 0.9994   N10:AUROC 0.9993 - N10:AUPR 0.9981      N50:AUROC 0.9993 - N50:AUPR 0.9976      [Count: 1172]   REL:decreases__activity
[33] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 1483]   REL:increases__reaction
[34] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 59]     REL:decreases__abundance
[35] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 3778]   REL:affects__expression
[36] N1:AUROC 0.9994 - N1:AUPR 0.9994   N10:AUROC 0.9987 - N10:AUPR 0.9872      N50:AUROC 0.9993 - N50:AUPR 0.9650      [Count: 1544]   REL:increases__activity
[37] N1:AUROC 0.0979 - N1:AUPR 0.5257   N10:AUROC 0.0823 - N10:AUPR 0.0983      N50:AUROC 0.0784 - N50:AUPR 0.0212      [Count: 429]    REL:increases__secretion
[38] N1:AUROC 1.0000 - N1:AUPR 1.0000   N10:AUROC 1.0000 - N10:AUPR 1.0000      N50:AUROC 1.0000 - N50:AUPR 1.0000      [Count: 20585]  REL:increases__expression
-----------------------------------------------------------------------------------------------------------
N1:AUROC 0.8865 - N1:AUPR 0.9360        N10:AUROC 0.8867 - N10:AUPR 0.8514      N50:AUROC 0.8866 - N50:AUPR 0.8039 = [AVERAGE]
```

## Citation
If you use the code or the dataset in this repository, please cite the following study
```
@article{MohamedAMIA20ECPI,
  title={Predicting The Effects of Chemical--Protein Interactions On Proteins Using Tensor Factorisation.},
  author={Sameh K. Mohamed and Aayah Nounu},
  journal={AMIA Joint Summits on Translational Science proceedings. AMIA Joint Summits on Translational Science},
  year={2020},
  volume={2020},
  pages={?-?}
}
```
