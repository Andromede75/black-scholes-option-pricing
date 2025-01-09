# Black-Scholes Option Pricing Model

# Import necessary libraries
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Function to calculate the Black-Scholes price for a European call option
def black_scholes_call(S, K, T, r, sigma):
    """
    Parameters:
    S : float : current stock price
    K : float : strike price
    T : float : time to maturity (in years)
    r : float : risk-free interest rate (annualized)
    sigma : float : volatility of the underlying stock (annualized)

    Returns:
    float : price of the call option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Function to calculate the Black-Scholes price for a European put option
def black_scholes_put(S, K, T, r, sigma):
    """
    Parameters:
    S : float : current stock price
    K : float : strike price
    T : float : time to maturity (in years)
    r : float : risk-free interest rate (annualized)
    sigma : float : volatility of the underlying stock (annualized)

    Returns:
    float : price of the put option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# Example usage
if __name__ == "__main__":
    # Parameters
    S = 100  # Current stock price
    K = 100  # Strike price
    T = 1    # Time to maturity in years
    r = 0.05 # Risk-free interest rate (5%)
    sigma = 0.2 # Volatility (20%)

    # Calculate call and put option prices
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print(f"Black-Scholes Call Option Price: {call_price:.2f}")
    print(f"Black-Scholes Put Option Price: {put_price:.2f}")

    # Plot the call and put option prices as a function of stock price
    stock_prices = np.linspace(50, 150, 100)
    call_prices = [black_scholes_call(S, K, T, r, sigma) for S in stock_prices]
    put_prices = [black_scholes_put(S, K, T, r, sigma) for S in stock_prices]

    plt.figure(figsize=(12, 6))
    plt.plot(stock_prices, call_prices, label='Call Option Price')
    plt.plot(stock_prices, put_prices, label='Put Option Price')
    plt.axvline(x=K, color='gray', linestyle='--', label='Strike Price')
    plt.title('Black-Scholes Option Pricing')
    plt.xlabel('Stock Price')
    plt.ylabel('Option Price')
    plt.legend()
    plt.grid(True)
    plt.show()
