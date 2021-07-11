# ASPIERE: Non-classical secretion protein predictor based on deep learning

## Introduction

ASPIRER is a non-calssical secretion protein predictor, which consists of XGBoost based whole sequence model and CNN based N-terminal sequence model. ASPIRER is anticipated to be explored as a useful tool for predicting novel potential non-classical proteins from sequences information and prioritizing target proteins for follow-up experimental validation.


![image](https://user-images.githubusercontent.com/49023946/124868670-69d4a780-e003-11eb-9d86-a145fb88f880.png)


## How to running

Users can run the main.py to identify the non-classical secretion proteins. 

featureGenerator.py is implemented for feature generation. 

The features descriptors including Amino Acid Composition(AAC), the composition of k-spaced amino acid pairs(CKSAAP), Tri-Peptide composition(TPC), Di-Peptide Composition(DPC),the Composition(CTDC), Transition(CTDT), Distribution(CTDD), Conjoint Triad (CTriad), Pseudo Position-Specific Score Matrix (Pse-PSSM), Grouped amino acid composition(GAAC), Grouped Di-Peptide Composition(GDPC) and Moran correlation descriptor.

predicton.py can be used for the final prediction.

The dataset fold contains fasta file of the training set and testing set, while the features fold contains the generated features file.

## Requirement 
python 3.8
xgboost 0.90
scikit_learn 0.22.2 post1
