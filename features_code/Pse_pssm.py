import sys
from os import listdir
from os.path import isfile, join

import numpy as np
import math
import re
import fileinput


def Pse_pssm(fasta, **kw):
    pssmdir = kw['path']
    if pssmdir is None:
        print('Error: please specify the directory of predicted protein disorder files by "--path" \n\n')
        return 0

    onlyfiles = [f for f in listdir(pssmdir) if isfile(join(pssmdir, f))]
    fastaDict = {}

    for fi in onlyfiles:
        cntnt = ''
        pssmContentMatrix = readToMatrix(fileinput.input(pssmdir + '/' + fi))
        pssmContentMatrix = np.array(pssmContentMatrix)
        sequence = pssmContentMatrix[:, 0]
        seqLength = len(sequence)
        for i in range(seqLength):
            cntnt += sequence[i]
        if cntnt in fastaDict:
            continue
        fastaDict[cntnt] = fi

    finalist = []
    for name, seq in fasta:
        finalist.append(pssmdir + '/' + fastaDict[seq])

    for fi in finalist:
        input_matrix = fileinput.input(fi)
        feature_vector = pse_pssm(input_matrix)

    return feature_vector


def pse_pssm(input_matrix, ALPHA=1):
    # print "start pse_pssm function"
    # ALPHA=1
    pse_pssm_matrix = handleMixed(input_matrix, ALPHA)
    # print "end pse_pssm function"
    return pse_pssm_matrix


def handleMixed(PSSM, ALPHA):
    row1 = [0.0] * 20
    row2 = [0.0] * 20

    matrix_final = [[0.0] * 40] * 1
    row1 = np.array(row1)
    row2 = np.array(row2)
    matrix_final = np.array(matrix_final)

    PSSM_norm = normalizePSSM(PSSM)
    seq_cn = np.shape(PSSM)[0]
    for i in range(seq_cn):
        row1 = map(sum, zip(row1, PSSM_norm[i]))
    row1 = np.divide(row1, seq_cn)

    for j in range(20):
        for i in range(seq_cn - ALPHA):
            row2[j] += (PSSM_norm[i][j] - PSSM_norm[i + ALPHA][j]) * (PSSM_norm[i][j] - PSSM_norm[i + ALPHA][j])
    row2 = np.divide(row2, seq_cn - ALPHA)

    row = np.hstack((row1, row2))
    matrix_final[0] = row
    return matrix_final


def normalizePSSM(PSSM):
    PSSM = PSSM[:, 1:21]
    PSSM = PSSM.astype(float)
    PSSM = np.array(PSSM)
    seq_cn = np.shape(PSSM)[0]
    PSSM_norm = [[0.0] * 20] * seq_cn
    PSSM_norm = np.array(PSSM_norm)
    mean_matrix = np.mean(PSSM, axis=1)
    std_matrix = np.std(PSSM, axis=1)

    for i in range(seq_cn):
        for j in range(20):
            if std_matrix[i] == 0.0:
                PSSM_norm[i][j] = PSSM[i][j] - mean_matrix[i]
            else:
                PSSM_norm[i][j] = (PSSM[i][j] - mean_matrix[i]) / std_matrix[i]
    return PSSM_norm


def readToMatrix(input_matrix):
    # print "start to read PSSM matrix"
    PSSM = []
    p = re.compile(r'-*[0-9]+')
    for line, strin in enumerate(input_matrix):
        if line > 2:
            str_vec = []
            overall_vec = strin.split()
            if len(overall_vec) == 0:
                break
            str_vec.extend(overall_vec[1])
            if len(overall_vec) < 44:
                print("There is a mistake in the pssm file")
                print("Try to correct it")
                for cur_str in overall_vec[2:]:
                    str_vec.extend(p.findall(cur_str))
                    if len(str_vec) >= 21:
                        if (len(str_vec)) > 21:
                            exit(1)
                        break;
                print("Done")
            else:
                str_vec = strin.split()[1:42]
            if len(str_vec) == 0:
                break
            PSSM.append(str_vec)
    fileinput.close()
    # print "finish to read PSSM matrix"
    PSSM = np.array(PSSM)
    return PSSM

kw = {"path":"../features"}
Pse_pssm([12,"kmmm"], **kw)
