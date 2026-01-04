import pandas as pd
from sklearn.preprocessing import StandardScaler

def encode_and_scale(df):
    X = df.drop("default", axis=1)
    y = df["default"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
