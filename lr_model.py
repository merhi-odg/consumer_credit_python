# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import pandas as pd
import numpy as np
import pickle
from scipy.special import logit
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix


# modelop.init
def begin():
    global lr_model, threshold, features
    model_artifacts = pickle.load(open("model_artifacts.pkl", "rb"))
    lr_model = model_artifacts["lr_model"]
    threshold = model_artifacts["threshold"]
    features = model_artifacts["features"]


# modelop.score
def action(datum):
    datum = pd.DataFrame([datum])
    prep_datum = preprocess(datum)
    datum = pd.concat([datum, prep_datum], axis=1)
    datum["probability"] = prediction(datum)
    datum["score"] = datum.probability.apply(lambda x: x > threshold).astype(int)
    yield datum.loc[
        :,
        [
            "id",
            "loan_amnt",
            "home_ownership",
            "annual_inc",
            "dti",
            "int_rate",
            "tax_liens",
            "credit_age",
            "age",
            "loan_status",
            "probability",
            "score",
        ],
    ].to_dict(orient="records")[0]

    
# modelop.metrics
def metrics(data):
    
    # dictionary to hold final metrics
    metrics = {}

    # calculate metrics
    f1 = f1_score(data["loan_status"], data["score"])
    auc_val = roc_auc_score(data["loan_status"], data["probability"])
    cm = confusion_matrix(data["loan_status"], data["score"])
    labels = ["Default", "Pay Off"]
    cm = matrix_to_dicts(cm, labels)

    # Assigning metrics to output dictionary
    # Top-level metrics
    metrics["f1_score"] = f1
    metrics["auc"] = auc_val
    
    metrics["performance"] = [
        {
            "test_name": "Classification Metrics",
            "test_category": "performance",
            "test_type": "classification_metrics",
            "test_id": "performance_classification_metrics",
            "values": {"f1_score": f1, "auc": auc_val, "confusion_matrix": cm},
        }
    ]

    
    # MOC expects the action function to be a *yield* function
    yield metrics


def preprocess(data):
    prep_data = pd.DataFrame(index=data.index)
    prep_data["logit_int_rate"] = data.int_rate.apply(logit)
    prep_data["log_annual_inc"] = data.annual_inc.apply(np.log)
    prep_data["log_credit_age"] = data.credit_age.apply(np.log)
    prep_data["log_loan_amnt"] = data.loan_amnt.apply(np.log)
    prep_data["rent_indicator"] = data.home_ownership.isin(["RENT"]).astype(int)
    return prep_data


def prediction(data):
    return lr_model.predict_proba(data.loc[:, features])[:, 1]


def matrix_to_dicts(matrix, labels):
    cm = []
    for idx, label in enumerate(labels):
        cm.append(dict(zip(labels, matrix[idx, :].tolist())))
    return cm
