# Consumer Credit Python
This is a model that flexes many aspects of ModelOp Center Monitoring.

The model has a built-in **score** function. Possible inputs files are:
* `sample_data.csv`, `baseline_data.csv`

Scoring jobs should be run on a runtime with **Python >= 3.7** (numpy version requirement; see https://github.com/numpy/numpy/releases/tag/v1.21.2).

## Scoring Jobs

### Sample Inputs

Choose **one** of the following files for a sample scoring job:
 - `sample_data.csv` (small file; processes fast)
 - `baseline_data.csv` (large file; take a **long** time - ~10 min- to score)

### Schema Checking

 - Input schema checking should be **disabled** pending a bug fix.
 - Output schema checking can be either enabled or disabled.

### Sample Output

The output of the scoring job when the input data is `sample_data.csv` is either a `.json` file (JSON-lines) or a `.csv` file (type is set by extension on job output).

Sample records from a `.json` output file:
```json
{"id": 66301, "loan_amnt": 5000.0, "home_ownership": "RENT", "annual_inc": 60000.0, "dti": 8.1, "int_rate": 0.1235, "tax_liens": 0, "credit_age": 6656, "age": "UNDER_FORTY", "loan_status": 0, "probability": 0.43978524836126964, "score": 0}
{"id": 66441, "loan_amnt": 8875.0, "home_ownership": "MORTGAGE", "annual_inc": 75000.0, "dti": 4.93, "int_rate": 0.1885, "tax_liens": 0, "credit_age": 4494, "age": "OVER_FORTY", "loan_status": 0, "probability": 0.5441736295748621, "score": 0}
{"id": 66500, "loan_amnt": 9000.0, "home_ownership": "MORTGAGE", "annual_inc": 52000.0, "dti": 26.98, "int_rate": 0.1155, "tax_liens": 0, "credit_age": 7507, "age": "UNDER_FORTY", "loan_status": 0, "probability": 0.4797000258659076, "score": 0}
```

Sample records from a `.csv` output file:
|id   |loan_amnt|home_ownership|annual_inc|dti  |int_rate|tax_liens|credit_age|age        |loan_status|probability        |score|
|-----|---------|--------------|----------|-----|--------|---------|----------|-----------|-----------|-------------------|-----|
|66301|5000.0   |RENT          |60000.0   |8.1  |0.1235  |0        |6656      |UNDER_FORTY|0          |0.43978524836126964|0    |
|66441|8875.0   |MORTGAGE      |75000.0   |4.93 |0.1885  |0        |4494      |OVER_FORTY |0          |0.5441736295748621 |0    |
|66500|9000.0   |MORTGAGE      |52000.0   |26.98|0.1155  |0        |7507      |UNDER_FORTY|0          |0.4797000258659076 |0    |
