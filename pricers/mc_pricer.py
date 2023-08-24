import numpy as np
from models.models import Stock, Option

def generate_paths(S, r, q, sigma, T, n, num_simulations, dividend_dates):
    delta_t = T/n
    paths = np.zeros((n+1, num_simulations))
    paths[0] = S
    for i in range(1, n+1):
        random_numbers = np.random.randn(num_simulations)
        if i in dividend_dates:
            paths[i] = paths[i-1] * np.exp((r - 0.5*sigma**2)*delta_t + sigma*np.sqrt(delta_t)*random_numbers) * (1-q)
        else:
            paths[i] = paths[i-1] * np.exp((r - 0.5*sigma**2)*delta_t + sigma*np.sqrt(delta_t)*random_numbers)
    return paths

def LSM_american_option_price(stock, option, r, n, num_simulations=10000):
    T = option.expiry
    K = option.strike_price
    S = stock.price
    sigma = stock.volatility
    q = stock.dividend_yield_per_payout()
    dividend_timesteps = stock.get_dividend_timesteps(T, n)

    delta_t = T/n
    paths = generate_paths(S, r, q, sigma, T, n, num_simulations, dividend_timesteps)
    
    if option.type == 'call':
        h = np.maximum(paths - K, 0)
    elif option.type == 'put':
        h = np.maximum(K - paths, 0)
    
    # values
    V = np.zeros_like(h)
    V[-1] = h[-1]
    
    for t in range(n-1, 0, -1):
        in_the_money = (h[t] > 0)
        X = paths[t, in_the_money]
        Y = V[t+1, in_the_money] * np.exp(-r*delta_t)
        
        if len(X) == 0: continue

        A = np.vstack([X**0, X, X**2]).T
        beta = np.linalg.lstsq(A, Y, rcond=None)[0]
        continuation_value = np.dot(A, beta)
        
        V[t, in_the_money] = np.where(h[t, in_the_money] > continuation_value, h[t, in_the_money], Y)
        V[t, ~in_the_money] = V[t+1, ~in_the_money] * np.exp(-r*delta_t)
    
    return np.mean(V[1] * np.exp(-r*delta_t))

if __name__ == "__main__":
    price = LSM_american_option_price(Stock(1.0, 0.25, 0.0075, 0.2186), Option(306/365, 1.0, 'call'), 0.0529, 84)
    print("Option Price:", price)