#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_01.py
# Aaron Adams
# A#02026009
##############################################################

## add all your imports here

# ************* Problem 1 (1 point) **********************
import math

import numpy as np

from const import const
from deriv import deriv
from hw03 import dydt_given_x_dxdt
from infl import find_infl_pnts
from plus import plus
from poly12 import find_poly_2_zeros
from prod import prod
from pwr import pwr
from quot import quot
from tof import tof


def test_deriv(fexpr, gt, lwr, uppr, err):
    assert isinstance(lwr, const)
    assert isinstance(uppr, const)
    assert isinstance(err, const)

    derivfexpr = deriv(fexpr)
    derivfexprfunc = tof(derivfexpr)

    gtfunc = tof(gt)

    for i in range(lwr, uppr):
        print(derivfexprfunc(i), gtfunc(i))
        assert abs(derivfexprfunc(i) - gtfunc(i)) <= err





# ************* Problem 2 (2 points) **********************

def max_profit(cost_fun, rev_fun):

    profit = plus(cost_fun, prod(rev_fun,-1))
    profit_deriv = deriv(profit)

    zeroes = find_poly_2_zeros(profit_deriv)

    return max(zeroes)

# ************* Problem 3 (2 points) **********************

def fastest_growth_time(pm, tl, tu):
    assert isinstance(tl, const)
    assert isinstance(tu, const)

    p = tof(pm)

    C = p(0)
    t = tu.get_val()

    k = np.log(p(tu.get_val())/C)/t

    fastestGrowth = 0

    for i in range(tl.get_val(),tu.get_val()):

        if(k * p(i)> fastestGrowth):
            fastestGrowth = k * p(i)

    return   fastestGrowth


# ************* Problem 4 (2 points) **********************

def max_norman_window_area(p):
    assert isinstance(p, const)


    hexpr = quot(plus(plus(p,prod(const(-2.0),'r')), prod(prod(np.pi,'r'), const(-1.0)))/const(2.0))


    area = plus(prod(const(0.5), prod(np.pi, pwr('r', const(2.0)))), prod(prod(const(2.0),'r'), hexpr))

    area_deriv = deriv(area)

    zeroes = find_poly_2_zeros(area_deriv)
    ans = area(zeroes)

    return max(ans)

# ************* Problem 5 (2 points) **********************

def tumor_volume_change(m, c, k):
    assert isinstance(m, const)
    assert isinstance(c, const)
    assert isinstance(k, const)

    yt = prod(const(k.get_val() * math.pi), pwr('r', 3.0))

    dydt = dydt_given_x_dxdt(yt, m, const(-1 * c.get_val()))

    return dydt

# ************* Problem 6 (1 point) **********************

def penicillin_amount(p0, lmbda, t):
    assert isinstance(p0, const)
    assert isinstance(lmbda, const)
    assert isinstance(t, const)

    return p0.get_val() * math.e **(-1 * lmbda * t.get_val())

def penicillin_half_life(lmbda):
    assert isinstance(lmbda, const)

    return np.log(0.5)/lmbda.get_val()
    


    
