from sklearn.linear_model import LogisticRegression
import joblib

def train_pd_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def save_model(model):
    joblib.dump(model, "models/logistic_pd_model.pkl")
