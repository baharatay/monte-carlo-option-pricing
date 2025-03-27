# Monte Carlo Simulation for European Call Option Pricing

This project implements a **Monte Carlo simulation** to estimate the price of a European call option under the **Black-Scholes framework**. It simulates thousands of stock price paths using **geometric Brownian motion** and discounts the expected payoff to present value.

---

## Key Concepts

- **Geometric Brownian Motion** for stock price modeling  
- **Risk-neutral valuation** to estimate expected payoffs  
- **Monte Carlo simulation** with 10,000 scenarios  
- **Discounting** of future payoffs to calculate present value  

---

## Model Parameters

- Initial Stock Price: \$100  
- Strike Price: \$110  
- Time to Maturity: 1 year  
- Risk-Free Rate: 5%  
- Volatility: 20%  
- Simulations: 10,000  
- Time Steps: 252 (daily)

---

## Visualization

Simulated stock price paths (first 100) to illustrate volatility and the range of outcomes.

![Simulated Stock Paths](simulated_paths.png)  
*Monte Carlo simulated stock prices over 252 time steps (1 year).*

---

## Output

- Estimated European Call Option Price
- (Optional) Comparison with Black-Scholes analytical price

---

## Dependencies

- `numpy`  
- `matplotlib`  

Install via:

```bash
pip install numpy matplotlib
