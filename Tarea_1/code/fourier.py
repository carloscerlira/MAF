import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def square(x):
    return np.sin(np.pi*x)/x

N = 10000; dx = 1/N; integral = 0;
partition = np.linspace(0.0001,1,N)

for x in partition:
    integral += square(x)*dx

print((1/2*integral-np.pi/4)*2/np.pi)

