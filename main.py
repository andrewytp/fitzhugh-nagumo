#!/usr/bin/env python

from scipy.integrate import ode

# define const
a = 0.7
b = 0.8
c = 3.0
I_ext = 0.0;

# initial condition
y0 = [1.0 , 0.0]   # v, w
t0 = 0

# define dv, dw
def f(t, y):
    v, w = y
    dy = [0.0 , 0.0]

    dy[0] = c * (v - v*v*v/3. + w + I_ext)  #dv
    dy[1] = -(v - a + b*w) / c              #dw

    return dy

# define integrator
r = ode(f).set_integrator("vode")
r.set_initial_value(y0, t0)
t1 = 10
dt = 1

while r.successful() and r.t < t1:
    r.integrate(r.t+dt)
    print(r.y)

