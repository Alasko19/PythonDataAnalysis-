import pandas as pd
import matplotlib.pyplot as plt

sales_record = pd.read_csv("sales.csv")

# print(sales_record)

# Get the sales column by multiplying price and quantity
sales_record["sales"] = sales_record["Price"] * sales_record["Quantity"]
print(sales_record)



# reorder columns (moves sales after quantity)
cols = list(sales_record.columns)

# remove sales first
cols.remove("sales")

# insert sales after quantity
quantity_index = cols.index("Quantity")
cols.insert(quantity_index + 1, "sales")

sales = sales_record[cols]

print(sales.head())

# total sales
total_sales = sales_record["sales"].sum()
print(total_sales)

# product and price chat
sales_record.plot(x="product" , y="Price" , kind="pie")
plt.show()

