import math
import random
import joblib
import numpy as np
import pandas as pd
from tensorflow.python.keras.models import load_model

random.seed(10)

# load model from the model file
def loadmodel():
    CNN_model_path = "./model/CNN_N60"
    XGB_model_path = "./model/XGB_model.pkl"
    CNN_model = load_model(CNN_model_path)
    XGB_model = joblib.load(XGB_model_path)
    return CNN_model, XGB_model

# make the prediction based on CNN model and XGBoost model
def prediction():
    output = dict()
    X_CNN = pd.read_csv("./features/CNN_features.csv", index_col=0)
    X_XGB = pd.read_csv("./features/XGB_features.csv", header=None).iloc[587:, 1:]
    label = X_CNN.index
    CNN_model, XGB_model = loadmodel()
    output["CNN"] = CNN_model.predict(X_CNN).T[0]
    output["XGB"] = XGB_model.predict_proba(X_XGB)[:, 1]
    df_level1 = pd.DataFrame(output,index=label)
    df_level1["mean"] = 0.5 * df_level1["CNN"] + 0.5 * df_level1["XGB"]
    df_level1["pred"] = np.rint(df_level1["mean"])
    return df_level1


if __name__ == "__main__":
    print(prediction())
