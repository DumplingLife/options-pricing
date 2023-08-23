# Financial Options Pricing Engine

A Python-based solution for pricing financial options using both Binomial and Monte Carlo methods.

## Overview

This project provides tools to price options in the financial markets. The main techniques implemented include:

1. Binomial Pricing Model
2. Least-Squares Monte Carlo Method (LSM) for American options

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/DumplingLife/options-pricing
   ```

2. Navigate to the project directory:
   ```
   cd path-to-directory
   ```

3. Install required libraries:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Binomial Pricing Engine**:
   ```python
   from core.models import Stock, Option
   from pricers.binomial_pricer import binomial_option_price

   stock = Stock(1.0, 0.25, 0.0075, 0.2186)
   option = Option(306/365, 1.0, 'call')
   r = 0.0529
   n = 84
   price = binomial_option_price(stock, option, r, n)
   print("Option Price:", price)
   ```

2. **Least-Squares Monte Carlo Method**:
   ```python
   from core.models import Stock, Option
   from pricers.mc_pricer import LSM_american_option_price

   stock = Stock(1.0, 0.25, 0.0075, 0.2186)
   option = Option(306/365, 1.0, 'call')
   r = 0.0529
   n = 84
   price = LSM_american_option_price(stock, option, r, n)
   print("Option Price:", price)
   ```

## Experiments

1. **Binomial Pricing Engine Experiment**: To see how the binomial pricing engine's predictions change with the number of timesteps.

2. **Monte Carlo Convergence Test**: To see how the Monte Carlo engine's predictions change with the number of timesteps.

3. **Monte Carlo Variance Test**: To compute the variance of the Monte Carlo method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.