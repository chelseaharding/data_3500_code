import pandas as pd

# read a csv file
df = pd.read_csv("/workspaces/data_3500_code/week10/content_videos/titanic.csv")

print(df.head())

# explore data structure
print(df.info())
print(df.describe(include="all"))
print(df.isna().sum())

# handle missing values
df[["Age", "Embarked"]].isna().sum()
# drop missing rows or fill missing rows
df_drop = df.dropna(subset=["Age", "Embarked"])
# Fill missing ages with median
df["Age"].fillna(df["Age"].median())

# Fill missing embarkation ports with the most common one
df["Embarked"].fillna(df["Embarked"].mode()[0])

# change column names and types where applicable
df.rename(columns={'Pclass': 'Class'}, inplace=True)


df["Class"] = df["Class"].astype("category")
df["Survived"] = df["Survived"].astype("bool")
print(df.dtypes)

# show info again
print(df.info())
print(df.head())
