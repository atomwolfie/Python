#!/usr/bin/python

#############################################
# module: hw06_s19.py
# YOUR NAME
# YOUR A#
#############################################

# These are the imports I used to implement my 
# solutions. Modify them as you see fit but
# make sure all your imports are zipped in your
# submission.

import math
import numpy as np
import matplotlib.pyplot as plt

from const import const
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from plus import plus
from tof import tof
from deriv import deriv
from poly12 import find_poly_2_zeros
from prod import prod
from pwr import pwr
from quot import quot
from tof import tof
from var import var

## ************* Problem 1 ******************

def percent_retention_model(lmbda, a):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)

    expr = plus(prod(plus(100, prod(a,const(-1.0))),pwr(math.e, prod(lmbda,prod(const(-1.0),var("t"))))), a)

    return expr

def plot_retention(lmbda, a, t0, t1):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    assert isinstance(t0, const)
    assert isinstance(t1, const)

    expr = percent_retention_model(lmbda, a)
    retention = tof(expr)

    expr_deriv =  deriv(expr)
    retention_deriv  =  tof(expr_deriv)

    min = t0.get_val()
    max = t1.get_val()

    xvals = np.linspace(min, max, 10000)
    yvals1 = np.array([retention(x) for x in xvals])
    yvals2 = np.array([retention_deriv(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle("Ebbinghaus Modael of Forgetting")
    plt.xlabel('t')
    plt.ylabel('prf and dprf')
    ymax = max(np.max(yvals1), np.max(yvals2))
    ymin = min(np.min(yvals1), np.min(yvals2))
    plt.ylim([ymin, ymax])
    plt.xlim([min, max])
    plt.grid()
    plt.plot(xvals,yvals1, label = 'prf', c = 'r')
    plt.plot(xvals, yvals2, label='dprf', c='b')
    plt.legend(loc = 'best')
    plt.show()

    if __name__ == '__main__':
        print("test 1: ")
        fex = percent_retention_model(make_const(1.0), make_const(1.0))





## ************* Problem 2 ******************

def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)

    expr = spread_of_disease_model(p, t0, p0, t1, p1)

    disease = tof(expr)
    disease_derive = tof(deriv(expr))

    min = tl.get_val()
    max = tu.get_val()

    xvals = np.linspace(min, max, 10000)
    yvals1 = np.array([disease(x) for x in xvals])
    yvals2 = np.array([disease_derive(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle("Spread of Disease")
    plt.xlabel('t')
    plt.ylabel('sdf and dsdf')
    ymax = max(np.max(yvals1), np.max(yvals2))
    ymin = min(np.min(yvals1), np.min(yvals2))
    plt.ylim([ymin, ymax])
    plt.xlim([min, max])
    plt.grid()
    plt.plot(xvals, yvals1, label='sdf', c='r')
    plt.plot(xvals, yvals2, label='dsdf', c='b')
    plt.legend(loc='best')
    plt.show()



def spread_of_disease_model(p, t0, p0, t1, p1):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)

    B = p.get_val() / (1 + p0.get_val())

    B_const = make_const(B)

    c = prod(const(-1.0), quot(plus(quot(p, p1), prod(const(1.0), const(-1.0)), B_const), t1))
    c_const = make_const(c)

    expr = quot(p, plus(const(1.0), prod(B_const, pwr(math.e, pwr(prod(const(-1.0), prod(c_const, var("t"))))))))

    return expr
    
## ************* Problem 3 ******************

def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(t2, const)
    assert isinstance(x2, const) and isinstance(tl, const)
    assert isinstance(tu, const)

    expr = plant_growth_model(m, t1, x1, t2, x2)
    growth = tof(expr)
    growth_deriv =  tof(deriv(expr))

    min = tl.get_val()
    max = tu.get_val()

    xvals = np.linspace(min, max, 10000)
    yvals1 = np.array([growth(x) for x in xvals])
    yvals2 = np.array([growth_deriv(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle("Plant Growth")
    plt.xlabel('t')
    plt.ylabel('pgf and dgdf')
    ymax = max(np.max(yvals1), np.max(yvals2))
    ymin = min(np.min(yvals1), np.min(yvals2))
    plt.ylim([ymin, ymax])
    plt.xlim([min, max])
    plt.grid()
    plt.plot(xvals, yvals1, label='pgf', c='r')
    plt.plot(xvals, yvals2, label='dgdf', c='b')
    plt.legend(loc='best')
    plt.show()

def plant_growth_model(m, t1, x1, t2, x2):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(x2, const)
    assert isinstance(x2, const)

    b = (m.get_val() / x1.get_val()) - 1
    k = (np.log(((m.get_val() / x2.get_val()) - 1.0) / b)) / (-1 * m.get_val() * t2.get_val())

    expr = quot(m, plus(const(1.0), prod(const(b),
                       make_e_expr(prod(const(m.get_val() * -1), prod(const(k), pwr(var("t"),const(1.0))))))))
    return expr
                                      
## ************* Problem 4 ******************

def spread_of_news_model(p, k):
    assert isinstance(p, const) and isinstance(k, const)

    expr = prod(p, plus(make_const(-1.0), pwr(math.e, prod(make_const(-1.73), var("t")))))

    return expr

def plot_spread_of_news(p, k, tl, tu):
    assert isinstance(p, const) and isinstance(k, const)
    assert isinstance(tl, const) and isinstance(tu, const)

    expr = spread_of_news_model(p,k)
    news = tof(expr)

    expr_deriv = deriv(expr)
    news_deriv = tof(expr_deriv)

    min = tl.get_val()
    max = tu.get_val()

    xvals = np.linspace(min, max, 10000)
    yvals1 = np.array([news(x) for x in xvals])
    yvals2 = np.array([news_deriv(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle("Spread of News")
    plt.xlabel('t')
    plt.ylabel('snf and dsnf')
    ymax = max(np.max(yvals1), np.max(yvals2))
    ymin = min(np.min(yvals1), np.min(yvals2))
    plt.ylim([ymin, ymax])
    plt.xlim([min, max])
    plt.grid()
    plt.plot(xvals, yvals1, label='snf', c='r')
    plt.plot(xvals, yvals2, label='dnsf', c='b')
    plt.legend(loc='best')
    plt.show()



    if __name__ == '__main__':
        print("test 1: ")
        fex = percent_retention_model(make_const(1.0), make_const(1.0))




 
