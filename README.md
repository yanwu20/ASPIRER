# ASPIERE: Non-classical secretion protein predictor based on deep learning

## Introduction

ASPIRER is a non-calssical secretion protein predictor, which combines a whole sequence-based XGBoost model and a N-terminal sequence-based convolutional neural network model. ASPIRER is anticipated to be a valuable tool for predicting novel potential non-classical proteins from sequences information and prioritising target proteins for follow-up experimental validation.

![image](https://user-images.githubusercontent.com/49023946/124868670-69d4a780-e003-11eb-9d86-a145fb88f880.png)


## Code detials

Users can run the main.py to identify the non-classical secretion proteins. 

featureGenerator.py is implemented for feature generation. 

The features descriptors including Amino Acid Composition (AAC), the Composition of K-Spaced Amino Acid Pairs (CKSAAP), Di-Peptide Composition (DPC), Tri-Peptide composition (TPC), and Dipeptide Deviation from Expected Mean (DDE),the Composition(CTDC), Transition(CTDT), Distribution(CTDD), Conjoint Triad (CTriad), Pseudo Position-Specific Score Matrix (Pse-PSSM), Grouped amino acid composition(GAAC), Grouped Di-Peptide Composition(GDPC) and Moran correlation descriptor.

predicton.py can be used for the final prediction.

The dataset fold contains fasta file of the training set and testing set, while the features fold contains the generated features file.

## Dependency
* python 3.8
* xgboost 0.90
* scikit_learn 0.22.2 post1

## Dataset
* PeNGaRoo_train_P.fasta 
* PeNGaRoo_train_N.fasta
* PeNGaRoo_independent_test_P.fasta
* PeNGaRoo_independent_test_N.fasta


## Usage
You can test the 
* python predicton.py

