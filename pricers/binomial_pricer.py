from core.models import Stock, Option
from math import exp, sqrt

def calculate_p(gain, up, down):
    return (exp(gain) - down)/(up - down)

def binomial_option_price(stock, option, r, n):
    T = option.expiry
    K = option.strike_price
    S = stock.price
    sigma = stock.volatility
    q = stock.dividend_yield_per_payout()
    dividend_timesteps = stock.get_dividend_timesteps(T, n)
    
    delta_t = T / n
    up = exp(sigma * sqrt(delta_t))
    down = exp(-sigma * sqrt(delta_t))
    
    tree = [[0 for _ in range(j+1)] for j in range(n+1)]
    
    # leaf values
    for i in range(n+1):
        if option.type == 'call':
            tree[n][i] = max(S * up**(2*i - n) - K, 0)
        elif option.type == 'put':
            tree[n][i] = max(K - S * up**(2*i - n), 0)
    
    # backward induction
    for j in range(n-1, -1, -1):
        for i in range(j+1):
            if j in dividend_timesteps:
                gain = r * delta_t - q
            else:
                gain = r * delta_t
            p = calculate_p(gain, up, down) # p will be negative when dividend, but this is fine (?)
            tree[j][i] = p * tree[j+1][i+1] + (1-p) * tree[j+1][i]
            tree[j][i] *= exp(-r * delta_t)

            if option.type == 'call':
                exercise = S * up**(2*i-j) - K
            elif option.type == 'put':
                exercise = K - S * up**(2*i-j)
            
            if exercise > tree[j][i]:
                # print(j, i, exercise, tree[j][i])
                tree[j][i] = exercise
    

    return tree[0][0]

if __name__ == "__main__":
    price = binomial_option_price(Stock(1.0, 0.25, 0.0075, 0.2186), Option(306/365, 1.0, 'call'), 0.0529, 84)
    print("Option Price:", price)