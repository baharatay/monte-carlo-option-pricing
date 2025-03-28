# Monte Carlo Simulation for European Call Option Pricing

This project implements a **Monte Carlo simulation** to estimate the price of a European call option under the **Black-Scholes framework**. The model generates thousands of simulated stock price paths using geometric Brownian motion and calculates the expected payoff under the risk-neutral measure. The output is benchmarked against the analytical Black-Scholes formula.

---

## Key Concepts

- **Geometric Brownian Motion** to model stock prices  
- **Risk-Neutral Valuation** to estimate the option's expected payoff  
- **Monte Carlo Simulation** with 10,000 simulated paths  
- **Analytical Benchmark** using the Black-Scholes closed-form solution

---

## Model Parameters

| Parameter     | Value     |
|---------------|-----------|
| Stock Price (S₀) | $100      |
| Strike Price (K) | $110      |
| Time to Maturity (T) | 1 year   |
| Risk-Free Rate (r) | 5%        |
| Volatility (σ) | 20%       |
| Simulations   | 10,000    |
| Time Steps    | 252 (daily) |

---

## Sample Output

Estimated European Call Option Price: $5.93
Black-Scholes Analytical Price: $6.04



The Monte Carlo price converges closely to the analytical solution, validating the correctness of the simulation.

---

## Visualization

The figure attached shows 100 of the 10,000 simulated stock price paths over one year.
*Monte Carlo simulated stock prices using geometric Brownian motion.*

---

## Dependencies

- `numpy`  
- `matplotlib`  
- `scipy`

Install using:

```bash
pip install numpy matplotlib scipy
