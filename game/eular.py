# Euler's Method
# Equation: dy/dx = 3*exp(-x) - 0.4y; initial conditions: y(0) = 5, X(0) = 0, h = 1.5
# exact solution y = 10*exp(-0.4x) - 5*exp(-x)
import numpy as np, math, matplotlib
from pylab import *

h = .25



y = 10

t = 0

def calc1( y ,t):


    return(.5*1/y** .5)


table = np.array = [(0,-1,-.5,0)]
steps = 30
for i  in range(1 ,steps):
    slope = (calc1(y, t))

    table[-1] = (i-1,   t, y, slope)
    s, t, y, slope = table[-1]
    y = y + slope * h
    t = t + h

    table+= [(i+1,t,y,0)]
print ("i           t           y     slope")

for i in range(0, steps):
    print("% 4d" % (table[i][0]),end='')



    print( "% 12.6f" %   table[i][1], end=' ')
    print("% 12.6f" % table[i][2], end=' ')
    print("% 12.6f" % table[i][3], end=' ')

    print('')