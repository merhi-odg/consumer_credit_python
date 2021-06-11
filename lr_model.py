# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import pandas as pd
import numpy as np
from scipy.special import logit
import pickle


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
    ].to_dict(orient="records")


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
