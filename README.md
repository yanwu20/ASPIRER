# ASPIRER: Non-classical secretion protein predictor based on deep learning

## Introduction

<!-- Protein secretion has a pivotal role in maintaining life activities and communication, from the cytoplasm to the host or external environment. Gram-positive bacteria can secrete proteins through multiple secretion pathways. The non-classical secretion pathway has recently received an increasing attention among these secretion pathways, but its mechanism is still unclear.Here, we propose a new hybrid deep learning framework, termed ASPIRER, for non-classical secreted protein (NCSP) identification from amino acid sequences. ASPIRER combines a whole sequence-based XGBoost model and a N-terminal sequence-based convolutional neural network model.
 -->
Protein secretion has a pivotal role in many biological processes and is particularly important for intercellular communication, from the cytoplasm to the host or external environment. Gram-positive bacteria can secrete proteins through multiple secretion pathways. The non-classical secretion pathway has recently received increasing attention among these secretion pathways, but its exact mechanism remains unclear. Non-classical secreted proteins (NCSPs) are a class of secreted proteins lacking signal peptides and motifs. Several NCSP predictors have been proposed to identify NCSPs and most of them employed the whole amino acid sequence of NCSPs to construct the model. However, the sequence length of different proteins varies greatly. In addition, not all regions of the protein are equally important and some local regions are not relevant to the secretion. The functional regions of the protein, particularly in the N- and C-terminal regions, contain important determinants for secretion. In this study, we propose a new hybrid deep learning-based framework, referred to as ASPIRER, which improves the prediction of NCSPs from amino acid sequences. More specifically, it combines a whole sequence-based XGBoost model and an N-terminal sequence-based convolutional neural networkmodel; 5-fold cross-validation and independent tests demonstrate that ASPIRER achieves superior performance than existing state-of-the-art approaches. 

<div align=center><img  src ="https://user-images.githubusercontent.com/49023946/144698328-5afae075-537b-4747-9b6d-53c434478adf.png" alt="Framework of ASPIRER"></div>


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
* Make the prediction for customize data and threshold
```
python ASPIRER.py --type predict --Fasta_file <Fasta_file> --PSSM_file <PSSM_file> --output_name <output_name> --threshold <threshold>
```
The Pse-PSSM file can be generated from [POSSUM webserver](https://possum.erc.monash.edu/)


* output results format

||CNN|XGB|mean|pred|
| ---------- | :-----------:  | :-----------: | :-----------: | :-----------: |
|sequence name|score of CNN model|score of XGB model|final score|predict class|

## Reference
* Wang, X. et al., ASPIRER: a new computational approach for identifying non-classical secreted proteins based on deep learning, submitted for publication
