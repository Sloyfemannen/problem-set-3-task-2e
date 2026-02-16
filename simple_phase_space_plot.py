# Simple 1D pendulum example of phase space plot

import numpy as np
import matplotlib.pyplot as plt

m = 1; g = 10; l = 1; w = 1; b = 2 # mass, gravitational acceleration & length of pendulum


# Determining Hamilton's equations
def Hamiltons_Equations(qp):
    q, p = qp
    q_dot = p / m
    p_dot = -m * w**2 * q - b / m * p
    return np.array([q_dot, p_dot])


# Defining linspaces for generalised coordinate& momentum values
r = np.linspace(0, 10, 1000)
p = np.linspace(0, 10, 1000)


# Creating a meshgrid of the coordinate & momentum values
X, Y = np.meshgrid(r, p)


# Computing derivatives
u, v = Hamiltons_Equations(np.array([X, Y]))


# Making a stream plot of the Hamiltonian
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, u, v, linewidth=1, cmap='viridis')
plt.xlabel(r'$q$', fontsize=10)
plt.ylabel(r'$p$', fontsize=10)
plt.title(r'Simple 1D pendulum', fontsize=15)
plt.tight_layout()
fig.savefig(f'ham_phasespace.pdf')
plt.close()
