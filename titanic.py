import pandas as pd
from catboost.datasets import titanic


titanic_df, _ = titanic()

titanic_dataset = titanic_df.copy()
titanic_dataset.to_csv("titanic_dataset.csv", index=False)

