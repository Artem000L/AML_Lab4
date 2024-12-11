import pandas as pd
from catboost.datasets import titanic


titanic_df, _ = titanic()

titanic_dataset = titanic_df.copy()

# titanic_dataset.to_csv("titanic_dataset.csv", index=False)

# titanic_dataset = titanic_dataset[['Pclass', 'Sex', 'Age']]
# titanic_dataset.to_csv("titanic_dataset_cut.csv", index=False)

titanic_dataset['Age'].fillna(titanic_dataset['Age'].mean(), inplace=True)
titanic_dataset.to_csv("titanic_dataset_notnanage.csv", index=False)