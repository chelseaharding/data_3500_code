# import pandas
import pandas as pd

# create a small dataset

data = {
    "Name": ["Big Blue", "Bob", "Sally", "James"],
    "Age": [23, 45, 53, 95],
    "Score": [90, 88, 94, 79]
}

df = pd.DataFrame(data)
print("df:", df)

# index
print(df["Age"])
print(df["Age"].mean())

print(sum(df["Age"]) / len(df["Age"]))

# new column
df["Score_Percent"] = df["Score"]/100
print(df)

# summary information
print(df.describe())