import sys

import pandas as pd
import numpy as np
import readFasta
from features_code import *

# this file is used to generate features file.
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


def XGB_inputGenterator(fasta, **kw):
    features = ["AAC", "CKSAAP", "Pse_pssm", "CTDC", "CTDT", "CTDD", "CTriad", "DDE", "GAAC", "GDPC", "Moran", "DPC",
                "TPC"]
    feature_dict = {}
    feature_list = []
    for i in features:
        if i == "Pse_pssm" and kw["PSSM"]:
            feature_list.append(pd.read_csv(kw["PSSM"]))
        else:
            cmd = i + '.' + i + '(fasta, **kw)'
            encoding = eval(cmd)
            content, index = todataframe(encoding)
            feature_dict[i] = pd.DataFrame(content, columns=encoding[0][1:])
            feature_list.append(pd.DataFrame(content, columns=encoding[0][1:]))
    df = pd.concat(feature_list, axis=1)
    print(df)
    return df


def generator(PSSM_file=None, fasta_file=None, output_name=""):
    if not PSSM_file and not fasta_file:
        PSSM_file = "./features/pse_pssm_test.csv"
        fasta_N = readFasta.readfasta("./dataset/PeNGaRoo_independent_test_N.fasta")
        fasta_P = readFasta.readfasta("./dataset/PeNGaRoo_independent_test_P.fasta")
        fasta = fasta_N + fasta_P
    elif PSSM_file and fasta_file:
        fasta = readFasta.readfasta(fasta_file)
    else:
        print("Missing input files")
        sys.exit(1)
    kw = {'order': 'ACDEFGHIKLMNPQRSTVWY', 'PSSM': PSSM_file}
    CNN_index, CNN_input = CNN_inputGenterator(fasta)
    df_cnn = pd.DataFrame(CNN_input, index=CNN_index)
    df_XGB = XGB_inputGenterator(fasta, **kw)
    if not output_name:
        df_cnn.to_csv("./features/CNN_features.csv")
        df_XGB.to_csv("./features/XGB_features.csv", index=False, header=False)
    else:
        df_cnn.to_csv("./features/CNN_features_%s.csv" % output_name)
        df_XGB.to_csv("./features/XGB_features_%s.csv" % output_name, index=False, header=False)


if __name__ == "__main__":
    generator()
