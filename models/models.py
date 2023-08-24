class Stock:
    def __init__(self, price, dividend_spacing, annual_dividend_payout, volatility):
        self.price = price
        self.dividend_spacing = dividend_spacing
        self.annual_dividend_payout = annual_dividend_payout
        self.volatility = volatility
    
    def dividend_yield_per_payout(self):
        return self.annual_dividend_payout * self.dividend_spacing
    
    def get_dividend_timesteps(self, end_date, n):
        dividend_timestep = 0
        dividend_timesteps = []
        # can replace this with while True; the break condition is sufficient, but keep this for clarity
        while dividend_timestep < n:
            dividend_timestep += n / end_date * self.dividend_spacing
            if dividend_timestep >= n: break
            dividend_timesteps.append(int(dividend_timestep)-1)
        return dividend_timesteps

class Option:
    def __init__(self, expiry, strike_price, type):
        if type not in ['call', 'put']:
            raise ValueError("Option type must be either 'call' or 'put'.")
        self.expiry = expiry
        self.strike_price = strike_price
        self.type = type