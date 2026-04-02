import pandas as pd
df = pd.read_csv("Titanic.csv")
# print(df)
# print(df.to_string())
# print(df.head())

# print first 5 rows
# first_5 = df.head()
# print(first_5)

# print last 5 rows
# last_5 = df.tail()
# print(last_5)

# print(df.info())
# print(df.describe())

# Data cleaning parttttttttttttttttttttttttttt
# print(df["Age"])

# if there is NaN data then age ma total garera find average

# way 1
# new_df= df["Age"].fillna(df["Age"].median(),inplace=True)
# print(new_df)

# way 2
# df.fillna({"Age":df["Age"].median()},inplace = True)

# print(df["Age"])

# dropping column
df.drop(columns = ['Cabin', 'Ticket'], inplace = True)
# print(df)

df["Sex"] = df["Sex"].map({"male":0,"female":1})
# print(df)

df.rename(columns={'Sex':'Gender'},inplace = True)

# Exploratory Data Analysis
# filtering
# print(df[(df['Gender']==1) & (df['Pclass']==1)])

#grouping
# print(df.groupby('Pclass')['Survived'].mean())

# print(df["Gender"])

# print(df.sort_values("Age",ascending=False))
# print(df["Age"])

# print(df.loc[df["Age"]>60,['Name','Age','Fare']].head(10))
# print(df[["Age","Gender"]])

