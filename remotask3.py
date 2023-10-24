# import numpy as np
# from sklearn.linear_model import LinearRegression


# # Sample data (replace with your own data)
# N = 10  # Number of data points
# d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Days
# m = np.array([50, 90, 120, 150, 180, 220, 250, 280, 310, 340])  # Money spent


# # Reshape the data for regression
# d = d.reshape(-1, 1)


# # Create a linear regression model
# model = LinearRegression()


# # Fit the model to the data
# model.fit(d, m)


# # Project the amount of money you will have at the end of January (31 days)
# days_in_january = 31
# projected_money = model.predict(np.array([[days_in_january]]))[0]


# # Calculate the remaining money
# initial_money = 500  # Replace with your initial amount
# remaining_money = initial_money - projected_money


# print(f"Projected money at the end of January: ${projected_money:.2f}")
# print(f"Remaining money at the end of January: ${remaining_money:.2f}")


import numpy as np
from sklearn.linear_model import LinearRegression

# number of elements
num_days = int(input("Enter target number of days: "))
N = int(input("Enter number of points: "))

# Below line read inputs from user using map() function and convert to array
d = np.array(list(map(int, input("\nEnter the day number: ").strip().split()))[:N])
m = np.array(
    list(
        map(
            int,
            input("\nEnter the total money for corresponding day: ").strip().split(),
        )
    )[:N]
)

# Reshape the data for regression
d = d.reshape(-1, 1)


# Create a linear regression model
model = LinearRegression()


# Fit the model to the data
model.fit(d, m)


# Project the amount of money you will have after num_days
projected_money = model.predict(np.array([[num_days]]))[0]


# Calculate the remaining money
initial_money = 500  # Replace with your initial amount
remaining_money = initial_money - projected_money


print(f"Projected money at the end of January: ${projected_money:.2f}")
print(f"Remaining money at the end of January: ${remaining_money:.2f}")
