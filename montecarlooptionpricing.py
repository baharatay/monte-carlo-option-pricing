
import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100    # Initial stock price
K = 110     # Strike price
T = 1       # Time to maturity (1 year)
r = 0.05    # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)
num_simulations = 10000  # Number of Monte Carlo simulations
num_steps = 252          # Number of time steps in a year
dt = T / num_steps       # Time increment

np.random.seed(42)  # Ensures results are reproducible
stock_paths = np.zeros((num_steps, num_simulations))  # Matrix to store stock prices
stock_paths[0] = S0  # First row (day 0) is the initial stock price

for t in range(1, num_steps):  # Loop through time steps
    Z = np.random.standard_normal(num_simulations)  # Generate random normal values
    stock_paths[t] = stock_paths[t-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

plt.figure(figsize=(10,5))
plt.plot(stock_paths[:, :100], lw=1, alpha=0.6)  # Plot 100 paths
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.title("Monte Carlo Simulated Stock Prices")
plt.show()

# Final stock prices at maturity
final_prices = stock_paths[-1]

# Compute call option payoff: max(S_T - K, 0)
payoffs = np.maximum(final_prices - K, 0)

# Discount payoffs to present value
option_price = np.exp(-r * T) * np.mean(payoffs)
print(f"Estimated European Call Option Price: ${option_price:.2f}")

