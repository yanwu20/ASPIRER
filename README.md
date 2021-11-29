# ASPIERE: Non-classical secretion protein predictor based on deep learning

## Introduction

Protein secretion has a pivotal role in maintaining life activities and communication, from the cytoplasm to the host or external environment. Gram-positive bacteria can secrete proteins through multiple secretion pathways. The non-classical secretion pathway has recently received an increasing attention among these secretion pathways, but its mechanism is still unclear.Here we propose a new hybrid deep learning framework, termed ASPIRER, for NCSP identification from amino acid sequences. ASPIRER combines a whole sequence-based XGBoost model and a N-terminal sequence-based convolutional neural network model.

<div align=center><img  src ="https://user-images.githubusercontent.com/49023946/124868670-69d4a780-e003-11eb-9d86-a145fb88f880.png" alt="Framework of ASPIRER"></div>

ASPIRER is anticipated to be a valuable tool for predicting novel potential non-classical proteins from sequences information and prioritising target proteins for follow-up experimental validation.


## Code details

* Users can run the ASPIRER.py to identify the non-classical secretion proteins. 

* featureGenerator.py is implemented for feature generation. 

The features descriptors including Amino Acid Composition (AAC), the Composition of K-Spaced Amino Acid Pairs (CKSAAP), Di-Peptide Composition (DPC), Tri-Peptide composition (TPC), and Dipeptide Deviation from Expected Mean (DDE),the Composition(CTDC), Transition(CTDT), Distribution(CTDD), Conjoint Triad (CTriad), Pseudo Position-Specific Score Matrix (Pse-PSSM), Grouped amino acid composition(GAAC), Grouped Di-Peptide Composition(GDPC) and Moran correlation descriptor.

* predicton.py can be used for the final prediction based on the generated features.


## Dependency
* python 3.8
* xgboost 0.90
* scikit_learn 0.22.2 post1

## Dataset
* PeNGaRoo_train_P.fasta: postives samples for training 
* PeNGaRoo_train_N.fasta: negative samples for training
* PeNGaRoo_independent_test_P.fasta: postives samples for testing 
* PeNGaRoo_independent_test_N.fasta: negative samples for testing
* CNN_features_test.csv and XGB_features_test.csv: generated feature files of test dataset
* pse_pssm_train.csv and pse_pssm_test.csv: Pse-PSSM file of training set and testing set

**The customized file should be consistant with the example files



## Installation Guide

*  Install from Github 
```python
git clone https://github.com/yanwu20/ASPIRER.git
cd ASPIRER
pip install -r requirements.txt
```

## Usage

* Run the default dataset
```
python ASPIRER.py --type benchmark
```
* Make the prediction for customize data
```
python ASPIRER.py --type predict --Fasta_file <Fasta_file> --PSSM_file <PSSM_file> --output_name <output_name>
```
The Pse-PSSM file can be generated from [POSSUM webserver](https://possum.erc.monash.edu/)


* output results format

||CNN|XGB|mean|pred|
| ---------- | :-----------:  | :-----------: | :-----------: | :-----------: |
|sequence name|score of CNN model|score of XGB model|final score|predict class|

## Reference
* XXXXX
