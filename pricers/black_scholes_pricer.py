import numpy as np
import scipy.stats as stats
from models.models import Stock, Option

def black_scholes_with_dividend(stock, option, r):
    T = option.expiry
    K = option.strike_price
    S = stock.price
    sigma = stock.volatility
    q = stock.dividend_yield_per_payout()

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option.type == 'call':
        option_price = S * np.exp(-q * T) * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)
    elif option.type == 'put':
        option_price = K * np.exp(-r * T) * stats.norm.cdf(-d2) - S * np.exp(-q * T) * stats.norm.cdf(-d1)
        
    return option_price

if __name__ == "__main__":
    price = black_scholes_with_dividend(Stock(1.0, 0.25, 0.0075, 0.2186), Option(306/365, 1.0, 'call'), 0.0529)
    print("Option Price:", price)