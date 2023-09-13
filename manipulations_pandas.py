# Import needed libraries
import pandas as pd

############################################################
# Read csv file
df = pd.read_csv("file.csv")

# Check some data
print(df.head())
print(df.tail())

# Extract data
shipping_1day = df[df["Shipping Type"] == "1 Day"]
shipping_2day = df[df["Shipping Type"] == "2 Day"]
shipping_5day = df[df["Shipping Type"] == "5 Day"]

# Export Data
shipping_1day.to_csv("shipping-1.csv")
############################################################
