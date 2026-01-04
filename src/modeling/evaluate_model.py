from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

def evaluate(model, X_test, y_test):
    y_pred = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred)

    fpr, tpr, _ = roc_curve(y_test, y_pred)
    plt.plot(fpr, tpr)
    plt.savefig("outputs/metrics/roc_curve.png")

    with open("outputs/metrics/auc_score.txt", "w") as f:
        f.write(str(auc))

    return auc
