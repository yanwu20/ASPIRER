import pandas as pd
import numpy as np
import readFasta
from features_code import *

filePath = "../dataset"


def todataframe(encoding):
    index_list = []
    new_list = []
    for i in encoding[1:]:
        new_list.append(i[1:])
        index_list.append(i[0])
    return new_list, index_list


def CNN_inputGenterator(fasta, length=60):
    encoding = []
    index = []
    amino_acids = "XACDEFGHIKLMNPQRSTVWY"
    aa2int = dict((c, i) for i, c in enumerate(amino_acids))
    for name, seqence in fasta:
        index.append(name)
        encoding.append([aa2int[aa] for aa in seqence[:length]])
    return index, encoding


fasta1= readFasta.readfasta("./dataset/PeNGaRoo_independent_test_N.fasta")
fasta2= readFasta.readfasta("./dataset/PeNGaRoo_independent_test_P.fasta")
# features = ["AAC", "CKSAAP", "Pse_pssm", "CTDC", "CTDT", "CTDD", "CTriad", "DDE", "GAAC", "GDPC", "Moran", "DPC", "TPC"]
features = ["AAC", "CKSAAP", "CTDC", "CTDT", "CTDD", "CTriad", "DDE", "GAAC", "GDPC", "Moran", "DPC", "TPC"]
kw = {'order': 'ACDEFGHIKLMNPQRSTVWY'}
feature_dict = {}
feature_list=[]
for i in features:
    cmd = i + '.' + i + '(fasta, **kw)'
    encoding = eval(cmd)
    content, index = todataframe(encoding)
    feature_dict[i] = pd.DataFrame(content, columns=encoding[0][1:], index=index)
    feature_list.append(pd.DataFrame(content, columns=encoding[0][1:], index=index))

df = pd.concat(feature_list, axis=1)
print(df)

fasta = fasta1+fasta2

CNN_index, CNN_input = CNN_inputGenterator(fasta)
df_cnn = pd.DataFrame(CNN_input, index=CNN_index)
df_cnn.to_csv("./features/CNN_features.csv")

