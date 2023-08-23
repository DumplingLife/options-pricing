from pricers.binomial_pricer import binomial_option_price
from core.models import Stock, Option

price = binomial_option_price(Stock(1.0, 0.25, 0.0075, 0.2186), Option(306/365, 1.0, 'call'), 0.0529, 84)
print("Option Price:", price)