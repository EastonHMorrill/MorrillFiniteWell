import numpy as np
import matplotlib.pyplot as plt
import Bisection

# Consatants

V_0 = 8E-15 #Joules
a = 1E-10 #meters
h_bar = 1.054E-34 #J*s
m_e = 9.109E-31 #Kg

# Equations

z_0 = (a/h_bar)*np.sqrt(2*m_e*V_0)

# Calculation

z = np.linspace(0, z_0, 1000)

def z_1(z):
    if (z == 0):
        return 1
    else:
        return np.sqrt((z_0/z)**2 - 1) - np.tan(z)

def z_2(z):
    if (z == 0):
        return 1
    else:
        return np.sqrt((z_0/z)**2 - 1) + 1/np.tan(z)

pairs = Bisection.find_sign_changes(z_1, 0.1, 0, 15)
zeros = Bisection.bisection(z_1, pairs, 1E-10, 100)

pairs_2 = Bisection.find_sign_changes(z_2, 0.1, 0, 15)
zeros_2 = Bisection.bisection(z_2, pairs_2, 1E-10, 1000)

E = []
n = 0

for z in zeros:
    E.append(h_bar**2/(2*m_e*a**2)*z**2 - V_0)

for z in zeros_2:
    E.append(h_bar**2/(2*m_e*a**2)*z**2 - V_0)

#print(E)

def Infinite(n):
    return (n*np.pi*h_bar)**2/(8*m_e*a**2) - V_0

#print("infinite", Infinite(1), Infinite(2), Infinite(3), Infinite(4), Infinite(5), Infinite(6), Infinite(7))

x = np.linspace(-15,15,5)
plt.plot(x, E)
plt.plot(x, (Infinite(1), Infinite(2), Infinite(3), Infinite(4), Infinite(5)))
plt.plot(x, x)
plt.ylim(-8.3E-15, -7.6E-15)
plt.show()