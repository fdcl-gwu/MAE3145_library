import numpy as np
import matplotlib.pyplot as plt

# define orbit
p = 10000
ecc = 1.2

# plot the orbit in the perifocal reference frame
true_anomaly = np.linspace(-np.deg2rad(135), np.deg2rad(135), 1000)
radius = p / (1 + ecc * np.cos(true_anomaly))

# transform lvlh to perifocal
r_pqw = np.array([radius * np.cos(true_anomaly), 
                  radius * np.sin(true_anomaly),
                  0])

# transform pqw to eci

# look up how to plot 3D in matplotlib
fig, ax = plt.subplots()
ax.plot(r_pqw[0], r_pqw[1])
# ax.plot(np.linalg.norm(r) * np.cos(nu * np.pi/180), np.linalg.norm(r) * np.sin(nu * np.pi/180), 'bo', markersize=10)
ax.plot(0, 0, 'bo', markersize=20)
ax.set_xlabel('$\hat p$')
ax.set_ylabel('$\hat q$')
plt.grid()
plt.axis('equal')
plt.show()
