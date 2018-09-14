import numpy as np
import scipy as sp
from astro import time
import matplotlib.pyplot as plt

def pendulum_eoms(y, t):
    """Equations of motion for a pendulum
    """
    b =1
    c =1

    x1 = y[0]
    x2 = y[1]

    x1_dot = x2
    x2_dot = -b * x2 - c * x1

    return np.array([x1_dot, x2_dot])

initial_state = np.array([np.pi - 0.1, 0])
t = np.linspace(0, 10, 100)

sol = sp.integrate.odeint(pendulum_eoms, initial_state, t)

theta = sol[:, 0]
theta_dot = sol[:, 1]

plt.figure()
plt.plot(t, theta)
plt.plot(t, theta_dot)
plt.show()
