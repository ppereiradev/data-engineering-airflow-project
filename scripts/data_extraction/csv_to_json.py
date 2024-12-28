import pandas as pd

df = pd.read_csv("/airflow-core/data/raw/data.csv")

df.to_json("/airflow-core/data/raw/data.json", orient="records")

