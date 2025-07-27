
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('sales_data.csv')

# Data Overview
print("First 5 Rows:")
print(df.head())
print("\nData Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])

# ----------------------------- #
# Revenue Over Time
plt.figure(figsize=(10,6))
df.set_index('Date')['Revenue'].plot(title='Revenue Over Time', color='green')
plt.ylabel('Revenue')
plt.show()

# ----------------------------- #
# Sales by Region
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
region_revenue.plot(kind='bar', color='skyblue', title='Revenue by Region')
plt.ylabel('Total Revenue')
plt.show()

# ----------------------------- #
# Product Performance
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=product_revenue.values, y=product_revenue.index, palette='coolwarm')
plt.title('Top Products by Revenue')
plt.xlabel('Revenue')
plt.show()

# ----------------------------- #
# Monthly Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(10,6))
monthly_revenue.plot(marker='o', color='purple', title='Monthly Revenue Trend')
plt.ylabel('Revenue')
plt.show()

# ----------------------------- #
# Insights Summary
print("\nInsights:")
print(f"Top Region by Revenue: {region_revenue.idxmax()} - {region_revenue.max()}")
print(f"Top Product by Revenue: {product_revenue.idxmax()} - {product_revenue.max()}")
print(f"Best Month by Revenue: {monthly_revenue.idxmax()} - {monthly_revenue.max()}")
