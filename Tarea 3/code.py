import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')
from scipy.special import factorial2
from scipy.integrate import quad

N = 100
X = np.linspace(0.01,5,1000)
Y1 = []
Y2 = []

def func(x):
    return np.exp(x**2)

for x in X:
    y1 = np.exp(-x**2)*quad(func, 0, x)[0]
    Y1.append(y1) 
    y2 = 1/(2*x)
    # for n in range(0, N):
    #      y2 += ((-1)**n*2**n*x**(2*n+1))/factorial2(2*n+1)
    Y2.append(y2)

plt.plot(X,Y1, color='royalblue', label='$F(x)$')
plt.plot(X,Y2, color='crimson', label='$\\frac{1}{2x}$')
plt.ylim(0,2)
plt.legend()
plt.show()
