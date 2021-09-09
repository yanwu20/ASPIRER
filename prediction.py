import math
import random
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_auc_score, average_precision_score
from tensorflow.python.keras.models import load_model

random.seed(10)


# load model from the model file
def loadmodel():
    CNN_model_path = "./model/CNN_N60"
    XGB_model_path = "./model/XGB_model.pkl"
    CNN_model = load_model(CNN_model_path)
    XGB_model = joblib.load(XGB_model_path)
    return CNN_model, XGB_model


def valiadation(y_test, y_pred, y_score):
    con_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1])
    tn, fp, fn, tp = con_matrix.ravel()
    acc = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    f1_score = 2 * (recall * precision) / (recall + precision)
    mcc = (tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    AUROC = roc_auc_score(y_test, y_score)
    AUPRC = average_precision_score(y_test, y_score)
    performance = [recall, specificity, precision, acc, mcc, f1_score, AUROC, AUPRC]
    return performance


# make the prediction based on CNN model and XGBoost model
def prediction(output_name=""):
    if output_name:
        X_XGB = pd.read_csv("./features/XGB_features_%s.csv" % output_name, header=None)
        X_CNN = pd.read_csv("./features/CNN_features_%s.csv" % output_name, index_col=0)
        output_file = "./output/%s.csv" % output_name
    else:
        X_XGB = pd.read_csv("./features/XGB_features_test.csv", header=None)
        X_CNN = pd.read_csv("./features/CNN_features_test.csv", index_col=0)
        output_file = "./output/ASPIERE_result.csv"
    output = dict()
    label = X_CNN.index
    CNN_model, XGB_model = loadmodel()
    output["CNN"] = CNN_model.predict(X_CNN).T[0]
    output["XGB"] = XGB_model.predict_proba(X_XGB)[:, 1]
    df_level1 = pd.DataFrame(output, index=label)
    df_level1["mean"] = 0.5 * df_level1["CNN"] + 0.5 * df_level1["XGB"]
    df_level1["pred"] = np.rint(df_level1["mean"])
    df_level1.to_csv(output_file)
    # y_test = np.append(np.zeros(34), np.ones(34))
    # print(valiadation(y_test,df_level1["pred"],df_level1["mean"]))
    print(df_level1)
    return df_level1


if __name__ == "__main__":
    prediction()
