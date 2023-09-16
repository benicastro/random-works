# Import needed libraries
import pandas as pd

############################################################
# # Read csv file
# df = pd.read_csv("file.csv")

# # Check some data
# print(df.head())
# print(df.tail())

# # Extract data
# shipping_1day = df[df["Shipping Type"] == "1 Day"]
# shipping_2day = df[df["Shipping Type"] == "2 Day"]
# shipping_5day = df[df["Shipping Type"] == "5 Day"]

# # Export Data
# shipping_1day.to_csv("shipping-1.csv")
############################################################
import os

files = os.listdir(os.getcwd())

# csv_files = []

# for file in files:
#     if file[-3:] == "csv":
#         csv_files.append(file)

csv_files = [file for file in files if file[-3:] == "csv"]

df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True, sort=False)

# print(df.dtypes)
df.qty = df.qty.astype("int64")
df.dropna(inplace=True)

item_pivot = pd.pivot_table(df, index=["item", "size"], values=["qty"], aggfunc=sum)
country_pivot = pd.pivot_table(df, index=["country"], values=["qty"], aggfunc=sum)

item_pivot.to_csv("item-sold.csv")


############################################################


############################################################


############################################################
