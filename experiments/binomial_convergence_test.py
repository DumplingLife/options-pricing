import matplotlib.pyplot as plt
from core.models import Stock, Option
from pricers.binomial_pricer import binomial_option_price

stock = Stock(1.0, 0.25, 0.0075, 0.2186)
option = Option(306/365, 1.0, 'call')
r = 0.0529

num_timesteps_list = [10, 20, 50, 100, 200, 500, 1000]

prices = [binomial_option_price(stock, option, r, n) for n in num_timesteps_list]

plt.figure(figsize=(10, 6))
plt.plot(num_timesteps_list, prices, 'o-', markerfacecolor='red')
plt.xlabel('# timesteps')
plt.ylabel('Option price')
plt.grid(True)
plt.show()