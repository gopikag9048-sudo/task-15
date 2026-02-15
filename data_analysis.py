import pandas as pd
df=pd.read_csv("data.csv")
print("===== FIRST 5 ROWS =====")
print(df.head())
print("\n===== DATA INFO =====")
print(df.info())
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())
df.fillna(df.mean(numeric_only=True),inplace=True)
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0],inplace=True)
print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df.isnull().sum())
if"Sales"in df.columns:
    filtered_df=df[df["Sales"]>1000]
    sorted_df=filtered_df.sort_values(by="Sales",ascending=False)
    print("\n===== FILTERED & SORTED DATA =====")
    print(sorted_df.head())
if"Category"in df.columns and"Sales"in df.columns:
    group_data=df.groupby("Category")["Sales"].agg(["sum","mean","count"])
    print("\n===== GROUPED DATA =====")
    print(group_data)
if"Profit"in df.columns and"Sales"in df.columns:
    df["Profit_Percentage"]=(df["Profit"]/df["Sales"])*100
    print("\n===== NEW COLUMN ADDED =====")
    print(df.head())
df.to_csv("cleaned_data.csv",index=False)
print("\nCleaned data exported to cleaned_data.csv")
print("\n===== BASIC INSIGHTS =====")
print("Total Rows:",df.shape[0])
print("Total Columns:",df.shape[1])
if"Sales"in df.columns:
    print("Total Sales:",df["Sales"].sum())
    print("Average Sales:",df["Sales"].mean())