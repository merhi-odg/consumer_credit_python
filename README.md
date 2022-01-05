# Consumer Credit Python
This is a model that flexes many aspects of ModelOp Center Monitoring.

## Scoring Jobs

Scoring jobs should be run on a runtime with **Python >= 3.7, < 3.9** (numpy version requirement; see https://github.com/numpy/numpy/releases/tag/v1.21.2).

### Sample Inputs

Choose **one** of the following files for a sample scoring job:
 - `sample_data.csv` (small file; processes fast)
 - `baseline_data.csv` (large file; take a **long** time - ~10 min- to score)

### Schema Checking

 - Input schema checking should be **disabled** (pending a bug fix).
 - Output schema checking can be either enabled or disabled.

### Sample Output

The output of the scoring job when the input data is `sample_data.csv` is a JSONS (.json) file (one-line JSON records). Here are the first three output records:


```json
{"id": 66301, "loan_amnt": 5000.0, "home_ownership": "RENT", "annual_inc": 60000.0, "dti": 8.1, "int_rate": 0.1235, "tax_liens": 0, "credit_age": 6656, "age": "UNDER_FORTY", "loan_status": 0, "probability": 0.43978524836126964, "score": 0}
{"id": 66441, "loan_amnt": 8875.0, "home_ownership": "MORTGAGE", "annual_inc": 75000.0, "dti": 4.93, "int_rate": 0.1885, "tax_liens": 0, "credit_age": 4494, "age": "OVER_FORTY", "loan_status": 0, "probability": 0.5441736295748621, "score": 0}
{"id": 66500, "loan_amnt": 9000.0, "home_ownership": "MORTGAGE", "annual_inc": 52000.0, "dti": 26.98, "int_rate": 0.1155, "tax_liens": 0, "credit_age": 7507, "age": "UNDER_FORTY", "loan_status": 0, "probability": 0.4797000258659076, "score": 0}
```