#!/usr/bin/env python3
"""
ecosystem_simulation.py

Predator-Prey Ecosystem Simulation using the Lotka-Volterra Model

This simulation models the dynamics between prey and predators over time
using the Lotka-Volterra equations:
    dx/dt = alpha * x - beta * x * y
    dy/dt = delta * x * y - gamma * y

The populations are animated using matplotlib.

Usage:
    python ecosystem_simulation.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Model Parameters
alpha = 1.0    # Prey growth rate
beta = 0.1     # Predation rate coefficient
delta = 0.075  # Predator reproduction rate per prey eaten
gamma = 1.5    # Predator death rate

# Initial conditions: [prey, predator]
X0 = [40, 9]
t = np.linspace(0, 50, 500)

# Solve the differential equations
solution = odeint(lotka_volterra, X0, t, args=(alpha, beta, delta, gamma))
prey, predators = solution.T

# Create the figure and set up the axis.
fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, max(max(prey), max(predators)) * 1.1)
ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.set_title("Predator-Prey Dynamics")

def update(frame):
    ax.clear()
    ax.plot(t[:frame], prey[:frame], lw=2, color='blue', label='Prey')
    ax.plot(t[:frame], predators[:frame], lw=2, color='red', label='Predator')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, max(max(prey), max(predators)) * 1.1)
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    ax.legend()
    ax.set_title("Predator-Prey Dynamics")
    return ax

# Create animation that updates the plot for each time frame.
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=False, repeat=True)

plt.show()
