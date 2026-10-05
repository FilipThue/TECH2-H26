import matplotlib.pyplot as plt
import numpy as np


def util(c, A, B, C):
    utility_of_c = -A*(c-B)**2+C
    return utility_of_c


def find_max_cons(candidates, A = float, B = float, C = float):
       """
       Find the consumption level that maximizes utility from a
       sequence of candidates.

       Parameters
       ----------
       candidates : list or array-like
           Sequence of candidate consumption levels to evaluate.
       A, B, C : float
           Parameters of the utility function.

       Returns
       -------
       u_max
           Maximized utility
       cons_max
           Consumption at which utility is maximized
       """
       u_max = -np.inf
       cons_max = None
       for c in candidates:
             u = util(c, A, B, C)
             if u > u_max:
                   u_max = u
                   cons_max = c
       return u_max, cons_max

cons = np.linspace(0, 4, 51)
A = 1
B = 2
C = 10

u_max, cons_max = find_max_cons(cons, A, B, C)

print("Maksimal nytte:", u_max)
print("Forbruk ved maksimal nytte:", cons_max)

#---------------------------

cons = np.array(cons)
utility_levels = -A*(cons-B)**2+C
u_max_index = np.argmax(utility_levels)

u_max_vectorized = utility_levels[u_max_index]
cons_max_vectorized = cons[u_max_index]
print("Maksimal nytte (vektorisert):", u_max_vectorized)
print("Forbruk ved maksimal nytte (vektorisert):", cons_max_vectorized)


c = np.linspace(0, 4, 50)
u = -1 * (c - 2) ** 2 + 10
plt.plot(c, u)
plt.xlabel('Consumption')
plt.ylabel('Utility')
plt.show()