import matplotlib.pyplot as plt
from models.models import Stock, Option
from pricers.mc_pricer import LSM_american_option_price

stock = Stock(1.0, 0.25, 0.0075, 0.2186)
option = Option(306/365, 1.0, 'call')
r = 0.0529
num_simulations = 10000

num_timesteps_list = [10, 50, 100, 500, 1000, 5000, 10000]

prices = [LSM_american_option_price(stock, option, r, n, num_simulations) for n in num_timesteps_list]

plt.figure(figsize=(10, 6))
plt.plot(num_timesteps_list, prices, 'o-', markerfacecolor='red')
plt.xlabel('# timesteps')
plt.ylabel('Option price')
plt.grid(True)
plt.show()