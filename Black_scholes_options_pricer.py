import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import streamlit as st

# build a black scholes option pricer

def black_scholes_call(S, K, T, r, sigma,):
  d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)
  C = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
  return C



def black_scholes_put(S, K, T, r, sigma,):
  d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)
  P = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
  return P


# Streamlit UI

st.title("Black–Scholes Call and Put Option Pricer")

st.sidebar.header("Options Parameters")

K = st.sidebar.slider("Strike Price (K)", 10.0, 300.0, 100.0)
T = st.sidebar.slider("Time to Maturity (Years)", 0.1, 5.0, 1.0)
r = st.sidebar.slider("Risk-Free Rate (r)", 0.0, 0.15, 0.05)
sigma = st.sidebar.slider("Volatility (σ)", 0.01, 1.0, 0.2)

# define a range of stock prices around the strike price

S = np.linspace(0.5*K, 1.5*K, 200)

# Calculate option prices
C = black_scholes_call(S, K, T, r, sigma)
P = black_scholes_put(S, K, T, r, sigma)

# plot call option price vs stock price

plt.plot(S, C)
plt.xlabel("Stock Price (S)")
plt.ylabel("Call Option Price")
plt.title("Call Price vs Stock Price")
st.pyplot(plt)

# plot put option price vs stock price
plt.figure()  # Create a new figure for the put option plot
plt.plot(S, P)
plt.xlabel("Stock Price (S)")
plt.ylabel("Put Option Price")
plt.title("Put Price vs Stock Price")
st.pyplot(plt)

