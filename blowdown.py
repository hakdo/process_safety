###############################################################
# blowdown.py
#
# Script to calculate orifice size of ideal gas relief problem.
# Usage: ./blowdown.py 25 900
# Simulates blowdown through a 25 mm diameter orifice for 900 seconds.
#
# Dependencies: see requirements.txt
# H. Olsen - 2021 @sjefersuper
# License: MIT
###############################################################
from math import pi, sqrt
from scipy.integrate import solve_ivp as solver
from numpy import array, exp
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fsolve
from sys import argv as args


# Physical constants and parameters
R = 8.314       # Universal gas constant in J/K mol
M = 25E-3       # molecular weight in kg/mol
k = 1.4         # Cp/Cv ratio of ideal gas
C = 0.72        # Orifice coefficient 
Z = 1.          # compressibility factor

# Operational factors
T0 = 400.0        # K, temperature
P0 = 2.01E7       # Pa, initial pressure
Q = 18000        # W, heat input
V = 20.0         # m3, volume
Cv = 27           # Specific heat at constant volume, J/K kg

initmass = P0*V*M/(R*T0)

def ystrength(T):
    # Function returns yield strength P_y (Pa) at temperature T (K)
    P_y = 3.0E7 - 50000.*(T-400.)
    return P_y

def cflow(P,T,D):
    # Function to give critical mass flow (kg/s)
    # D = diameter of orifice plate in mm
    A = 0.25*pi*(D/1000.0)**2
    m = C*A*P*sqrt((k*M/(Z*R*T))*(2/(k+1))**((k+1)/(k-1)))
    return m

def pressure(y):
    m = y[0]
    T=y[1]
    rho = m/V
    p = rho*R*T/M
    return p

def baleq(t, y, D):
    # State vector = [m, T]
    m = y[0]
    T=y[1]
    p = pressure(y)
    mb = cflow(p, T, D)
    dm = -mb
    dT = -mb*R*T/(m*Cv) + Q/(m*Cv)
    dy = array([dm,dT])
    return dy

def main():
    try:
        dia = float(args[1])
        tmax = int(args[2])
    except:
        print("You must supply 2 arguments: diameter in mm + maximum simulation time in seconds.")
        return None
    y0 = array([initmass,T0])
    eq10 = lambda t,y: baleq(t,y,dia)
    dy = eq10(0, y0)
    sol = solver(lambda t,y: baleq(t,y,dia), array([0,tmax]), y0, t_eval=range(0,tmax))

    plt.subplot(2,1,1)
    plt.plot(sol.t, pressure(sol.y)/100000, label="Pressure")
    plt.plot(sol.t, ystrength(sol.y[1])/100000, label="Yield strength")
    plt.xlabel('t/s')
    plt.ylabel('p/barg')
    plt.title('Pressure profile vs yield strength')
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(sol.t, sol.y[0])
    plt.xlabel('t/s')
    plt.ylabel('m/kg')
    plt.title('Mass in control volume')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
