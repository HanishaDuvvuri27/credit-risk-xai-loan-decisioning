from lime.lime_tabular import LimeTabularExplainer

def lime_instance(model, X_train, instance):
    explainer = LimeTabularExplainer(
        X_train,
        mode="classification"
    )
    return explainer.explain_instance(instance, model.predict_proba)
