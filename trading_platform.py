events = [
    "BUY stock2 2",
    "BUY stock1 4",
    "CHANGE stock2 -8",
    "SELL stock 1 2",
    "BUY stock3 3",
    "QUERY",
    # "BUY googl 20",
    # "BUY aapl 50",
    # "CHANGE googl 6",
    # "QUERY",
    # "SELL aapl 10",
    # "CHANGE aapl -2",
    # "QUERY",
]

# Get Stocks

stock_list = []

for event in events:
    event_list = event.split()
    try:
        if event_list[1] not in stock_list:
            stock_list.append(event_list[1])
    except IndexError:
        continue


stock_dict = {stock: 0 for stock in stock_list}
result = []
profit = 0

for event in events:
    event_split = event.split()
    if event_split[0] == "BUY":
        stock_dict[event_split[1]] += int(event_split[2])
    elif event_split[0] == "SELL":
        stock_dict[event_split[1]] -= int(event_split[2])
    elif event_split[0] == "CHANGE":
        profit += stock_dict[event_split[1]] * int(event_split[2])
    elif event_split[0] == "QUERY":
        result.append(profit)

print(result)
print(profit)

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# #
# # Complete the 'getNetProfit' function below.
# #
# # The function is expected to return a LONG_INTEGER_ARRAY.
# # The function accepts STRING_ARRAY events as parameter.
# #

# def getNetProfit(events):
#     # Write your code here

#     # Declare a list to store the stocks bought/sold
#     stock_list = []

#     for event in events:
#         event_list = event.split()
#         try:
#             if event_list[1] not in stock_list:
#                 stock_list.append(event_list[1])
#         except IndexError:
#             continue

#     # Create dictionary to store stock holdings
#     stock_dict = {stock: 0 for stock in stock_list}

#     profit = 0
#     result = []

#     for event in events:
#         event_split = event.split() # Split string input for better querying
#         if event_split[0] == "BUY":
#             stock_dict[event_split[1]] += int(event_split[2])
#         elif event_split[0] == "SELL":
#             stock_dict[event_split[1]] -= int(event_split[2])
#         elif event_split[0] == "CHANGE":
#             profit += stock_dict[event_split[1]] * int(event_split[2])
#         elif event_split[0] == "QUERY":
#             result.append(profit)

#     return result

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     events_count = int(input().strip())

#     events = []

#     for _ in range(events_count):
#         events_item = input()
#         events.append(events_item)

#     result = getNetProfit(events)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
