import pandas as pd

df = pd.read_csv("superstore.csv", encoding="latin1")

print(df.head())

# REMOVE NULL VALUES
df = df.dropna()

# REMOVE DUPLICATES
df = df.drop_duplicates()

print("Data cleaned successfully")


# CATEGORY SALES
category_sales = df.groupby("Category")["Sales"].sum()

# REGION PROFIT
region_profit = df.groupby("Region")["Profit"].sum()

print("\nTop Category:", category_sales.idxmax())
print("Top Region:", region_profit.idxmax())


import matplotlib.pyplot as plt

category_sales.plot(kind="bar", color="skyblue")
plt.title("Sales by Category")
plt.show()

region_profit.plot(kind="bar", color="green")
plt.title("Profit by Region")
plt.show()

import seaborn as sns

sns.scatterplot(data=df, x="Discount", y="Profit")
plt.title("Discount vs Profit")
plt.show()

print("\n===== BUSINESS INSIGHTS =====")

print("Most Selling Category:", df.groupby("Category")["Sales"].sum().idxmax())
print("Most Profitable Region:", df.groupby("Region")["Profit"].sum().idxmax())

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved")

category_sales.plot(kind="bar")

plt.title("Sales by Category")

plt.savefig("output/category.png")   # 👈 SAVE LINE

plt.show()


region_profit.plot(kind="bar", color="green")

plt.title("Profit by Region")

plt.savefig("output/region.png")   # 👈 SAVE LINE

plt.show()

sns.scatterplot(data=df, x="Discount", y="Profit")

plt.title("Discount vs Profit")

plt.savefig("output/discount.png")  # 👈 SAVE LINE

plt.show()

