import random

import tensorflow as tf
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
# from keras.layers.embeddings import Embedding
# from keras.layers.convolutional import Conv1D, MaxPooling1D
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.layers import Reshape, Dense
from tensorflow.python.keras.models import Sequential
from xgboost import XGBClassifier
import pandas as pd
import joblib

tf.random.set_seed(123)


# def CNN_model():
#     # Model params
#     embedding_vector_length = 64
#     nbf = 10  # No. Conv Filters
#     flen = 16  # Conv Filter length
#     nlstm = 100  # No. LSTM layers
#     ndrop = 0.1  # LSTM layer dropout
#     nbatch = 32  # Fit batch No.
#     nepochs = 60  # No. training rounds
#
#     model = Sequential()
#     model.add(Embedding(21, embedding_vector_length, input_length=max_length))
#     model.add(Conv1D(filters=nbf, kernel_size=flen, padding="same", activation='relu'))
#     model.add(MaxPooling1D(pool_size=5))
#     model.add(Conv1D(filters=nbf // 2, kernel_size=flen, padding="same", activation='relu'))
#     model.add(MaxPooling1D(pool_size=5))
#     model.add(Reshape((5 * 2,)))
#     model.add(Dense(1, activation='sigmoid'))
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['AUC'])
#
#     return model


def XGB_model():
    pipeline = Pipeline(steps=[('scaler', MinMaxScaler()), ('featureSelection', SelectKBest(chi2, k=900)),
                               ('sampling', SMOTE(random_state=0)),
                               ('classifier', XGBClassifier(alpha=10, base_score=0.5, booster='gbtree',
                                                            colsample_bylevel=1, colsample_bynode=1,
                                                            colsample_bytree=0.8, gamma=0, learning_rate=0.1,
                                                            max_delta_step=0, max_depth=7,
                                                            min_child_weight=1,
                                                            n_estimators=100, n_jobs=1, nthread=None,
                                                            objective='binary:logistic', random_state=0,
                                                            reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
                                                            seed=None, silent=None, subsample=0.6,
                                                            verbosity=1))]
                        )
    return pipeline


X_XGB = pd.read_csv("./features/XGB_features.csv", header=None)
X_train, y_train = X_XGB.iloc[:587, 1:], X_XGB.iloc[:587, 0]
XGB_model = XGB_model().fit(X_train, y_train)
joblib.dump(XGB_model, "./model/XGB_model.pkl")
