import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jiten112002",
    database="retail_project"
)

# SALES BY CATEGORY

def sales_by_category():
    query = """
    SELECT Category, ROUND(SUM(Sales),2) AS Total_Sales
    FROM superstore
    GROUP BY Category
    """

    df = pd.read_sql(query, conn)

    print("\n--- SALES BY CATEGORY ---")
    print(df)

    plt.figure(figsize=(6,4))
    sns.barplot(x="Category", y="Total_Sales", data=df)
    plt.title("Sales by Category")
    plt.show()

    print("INSIGHT: Technology / Furniture / Office Supplies performance comparison")



# TOP PRODUCTS

def top_products():
    query = """
    SELECT product_name, ROUND(SUM(Sales),2) AS Total_Sales
    FROM superstore
    GROUP BY product_name
    ORDER BY Total_Sales DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    print("\n--- TOP PRODUCTS ---")
    print(df)

    plt.figure(figsize=(10,5))
    sns.barplot(x="Total_Sales", y="product_name", data=df)
    plt.title("Top 10 Products")
    plt.show()

    print("INSIGHT: Few products dominate revenue")


# PROFIT BY REGION

def profit_by_region():
    query = """
    SELECT Region, ROUND(SUM(Profit),2) AS Total_Profit
    FROM superstore
    GROUP BY Region
    """

    df = pd.read_sql(query, conn)

    print("\n--- PROFIT BY REGION ---")
    print(df)

    sns.barplot(x="Region", y="Total_Profit", data=df)
    plt.title("Profit by Region")
    plt.show()

    print("INSIGHT: Some regions are more profitable than others")


print("\n==============================")
print("RETAIL SUPERSTORE ANALYSIS")
print("==============================")

sales_by_category()
top_products()
profit_by_region()

conn.close()



