"""
unfinished
"""

import QuantLib as ql

def QuantLib_American_Binomial_Price(T, S, K, r, sigma, q, dividend_dates, n, option_type):
    calculation_date = ql.Date(1, 1, 2020)
    ql.Settings.instance().evaluationDate = calculation_date
    maturity = calculation_date + int(T*365.25)
    
    payoff_type = ql.Option.Call if option_type == 'call' else ql.Option.Put
    payoff = ql.PlainVanillaPayoff(payoff_type, K)
    exercise = ql.AmericanExercise(calculation_date, maturity)
    
    ql_dividend_dates = [calculation_date + date for date in dividend_dates]
    div_values = [S * q for _ in dividend_dates]
    
    dividend_option = ql.DividendVanillaOption(payoff, exercise, ql_dividend_dates, div_values)
    
    spot_handle = ql.QuoteHandle(ql.SimpleQuote(S))
    flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, r, ql.Actual365Fixed()))
    dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, q, ql.Actual365Fixed()))
    flat_vol = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(sigma)), ql.Actual365Fixed()))
    
    bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol)
    
    binomial_engine = ql.MCAmericanEngine(bsm_process, "pseudorandom", n)
    dividend_option.setPricingEngine(binomial_engine)
        
    return dividend_option.NPV()

price = QuantLib_American_Binomial_Price(306/365, 1.0, 1.0, 0.0529, 0.2186, 0.0075/4, [24,49,74], 84, option_type='call')
print("Option Price:", price)