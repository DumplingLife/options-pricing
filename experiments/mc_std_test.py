import numpy as np
import matplotlib.pyplot as plt
from models.models import Stock, Option
from pricers.mc_pricer import LSM_american_option_price

stock = Stock(1.0, 0.25, 0.0075, 0.2186)
option = Option(306/365, 1.0, 'call')
r = 0.0529
n = 100

# for performance, do more than 1 run at a time (becuase of parallelization), but tune down total # simulations
num_runs = 100
num_simulations_each = 100

prices = [LSM_american_option_price(stock, option, r, n, num_simulations_each) for _ in range(num_runs)]

mean_price = np.mean(prices)
std_dev = np.std(prices)

print(f"Mean Option Price: {mean_price}")
print(f"Standard Deviation: {std_dev}")

plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20)
plt.xlabel('Option price')
plt.ylabel('Frequency')
plt.show()