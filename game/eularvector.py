# Euler's Method
# Equation: dy/dx = 3*exp(-x) - 0.4y; initial conditions: y(0) = 5, X(0) = 0, h = 1.5
# exact solution y = 10*exp(-0.4x) - 5*exp(-x)
import numpy as np, math
from pylab import *

h = .1
x = .1
y =.1

t = 0

graft = 'y'

def calcx( x,y ,t):


    return(0.0051709 *math.exp(x) - x - 1)


def calcy(x,y, t):
    return (x+y )



table =  [(0,-1,-.5,0,0,0)]







# rs is the anount to round
rs=8
steps = 6 * int(1/h)

for i  in range(1 ,steps):
    slopex = (calcx(x,y, t))
    slopey = (calcy(x, y, t))

    table[-1] = (i-1,   t, x ,y, slopex, slopey)
    s, t, x,y, slopex , slopey = table[-1]
    x = x + slopex * h
    x = round(x,rs)
    y = y + slopey * h
    y = round(y, rs)
    t = t + h

    table+= [(i+1,t,x,y,0)]
print ("i           t           x           y     slopex    slopey")

for i in range(0, steps-1):
    print("% 4d" % (table[i][0]),end='')



    print( "% 12.6f" %   table[i][1], end=' ')
    print("% 12.6f" % table[i][2], end=' ')
    print("% 12.6f" % table[i][3], end=' ')
    print("% 12.6f" % table[i][4], end=' ')
    print("% 12.6f" % table[i][5], end=' ')

    print('')

y_value = []
x_value = []
t_value = []

for i in range(0, steps - 3):
    y_value.append(table[i][3])
    x_value.append(table[i][2])
    t_value.append(table[i][1])






plt.plot(t_value, y_value, label='y to t ')
plt.legend()
plt.show()

plt.plot(t_value, x_value, label='x to t ')
plt.legend()
plt.show()


plt.plot(x_value, y_value, label='x to y ')
plt.legend()
plt.show()

plt.plot(y_value, x_value, label='y to x ')
plt.legend()
plt.show()