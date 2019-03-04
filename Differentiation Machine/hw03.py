#!/usr/bin/python

#######################################
# module: hw03.py
# YOUR NAME
# YOUR A#
#######################################

# place all necessary imports here.
#
# I placed the updated version of maker.py
# Use it as you see fit.
import math

import const
from deriv import deriv
from maker import make_prod, make_const, make_pwr
from tof import tof


def maximize_revenue(dmnd_eq, constraint=lambda x: x >= 0):

     idealx = 0
     rev = 0
     price = 0

     for i in range(0,constraint) :
      tempprice = 0
      tempprice = eval(dmnd_eq)
      if(tempprice > price):
          idealx = i
          price = tempprice

      rev = idealx * price
      return idealx,rev,price

def dydt_given_x_dxdt(yt, x, dxdt):

    ytderiv = deriv(yt)
    ytderivfunc = tof(ytderiv)

    #evaluate deriv at x
    temp = ytderiv(x)

    #multiply at dxdt
    ans = temp * dxdt

    return const(ans)

def oil_disk_test():
    yt = make_prod(make_const(0.02*math.pi),
                    make_pwr('r', 2.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                             make_const(20.0))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)

def arm_tumor_test():
    yt = make_prod(make_const(0.003 * math.pi),
                   make_pwr('r', 3.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(10.3),
                             make_const(-1.75))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)
    pass
    
