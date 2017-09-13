"""Simualtion of two body inertial motion

This solves Problem 4 from Homework 1 from MAE3145

"""

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

from astro.eoms import eomTBI

m1 = 2
m2 = 1
G = 1
# define initial conditions
r10 = [0, 0, 0]
r20 = [1, 0, 0]
v10 = [0, 0, 0]
v20 = [1, 1, 0]

initial_state = np.hstack(( r10, v10, r20, v20 ))

t = np.linspace(0, 10, 1000)

# simulate
sol = scipy.integrate.odeint(eomTBI, initial_state, t, args=(m1, m2, G))

# plot
r1 = sol[:, 0:3]
v1 = sol[:, 3:6]
r2 = sol[:, 6:9]
v2 = sol[:, 9:12]

rcom = (m1 * r1 + m2 * r2) / (m1 + m2)
r = r2 - r1

traj_fig, traj_ax = plt.subplots()
traj_ax.plot(r1[:, 0], r1[:, 1], label=r'$r_1$')
traj_ax.plot(r2[:, 0], r2[:, 1], label=r'$r_2$')
traj_ax.plot(rcom[:,0],rcom[:,1], label=r'$r_c$')
traj_ax.grid()
traj_ax.set_title('Inertial Frame')
traj_ax.set_xlabel('X axis')
traj_ax.set_ylabel('Y Axis')
plt.legend()

rel_fig, rel_ax = plt.subplots()
rel_ax.plot(r[:, 0], r[:, 1])
rel_ax.plot([0], [0], 'bo', markersize=20)
rel_ax.set_title('Relative motion of $m_2$ wrt $m_1$')
rel_ax.set_xlabel('X Axis')
rel_ax.set_ylabel('Y Axis')
rel_ax.grid()
plt.show()

