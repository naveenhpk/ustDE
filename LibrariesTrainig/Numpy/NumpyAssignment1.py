import numpy as np

# create an array with 30 days with 10 random values each
data = np.random.randint(100, 1000, size=(30, 10))
print("Data Set", data)

# list to add all closing price
closing_price = []
for i in data:
    for item in i:
        closing_price.append(i[-1])
        break
print("Close price of Each days", closing_price)

#Standard  Deviation
standdev = np.std(closing_price)
print("Standard Deviation of Closing Days", standdev)

#Calculating the maximum closing price day
day = np.argmax(closing_price)+1

#Calculating the maximum closing price
day_value = np.max(closing_price)
print("Day which has Highest Value:", day)
print("Highest value", day_value)

#Day in which increased by )=0.5%
increased_days = []
for i in range(len(closing_price)-1):
    x = (closing_price[i]*0.05)+closing_price[i]
    if x < closing_price[i+1]:
        y = i+2
        increased_days.append(y)

print("Days in which Closing day Increased by 0.5%", increased_days)
