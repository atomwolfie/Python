#!/usr/bin/python

#!/usr/bin/python

###########################################
# module: hw05.py
# YOUR NAME
# YOUR A#
###########################################

# place the imports necessary for your solution here



###################### Problem 1 ########################
import math

import numpy as np

from const import const
from deriv import deriv
from prod import prod
from pwr import pwr
from quot import quot
from tof import tof


def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)

    expr = pwr(math.e,quot(k2,k1))

    exprfunc = tof(expr)
    return exprfunc

def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)

    expr = prod(y0, pwr(math.e,(prod(k,pwr('t', y0)))))

    exprfunc = tof(expr)
    return exprfunc

############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)

    k = np.log(n/p0)/t

    growth_expr = prod(p0, pwr(math.e,prod(k,'t')))

    return growth_expr

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)

    decay_expr = prod(p0,pwr(math.e,prod(prod(lmbda, const(-1.0)),'t')))

    return decay_expr

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):

    decmal_percentage = c14_percent * 0.001

    age = np.log(decmal_percentage)/0.00012

    return age

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)

    demand_deriv = deriv(demand_eq)

    elasticity = (-1 * price.get_val() * demand_deriv) / demand_eq(price.get_val())
    return elasticity

def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)

    demand_deriv = deriv(demand_eq)

    elasticity = (-1 * price.get_val() * demand_deriv) / demand_eq(price.get_val())

    if(elasticity == price.get_val()):
        return True

    else:
        return False

def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or \
           price_direction.get_val() == -1

    demand_deriv = deriv(demand_eq)

    elasticity = (-1 * price.get_val() * demand_deriv) / demand_eq(price.get_val())

    elasticity_direction = (-1 * price_direction.get_val() * demand_deriv) / demand_eq(price_direction.get_val())

    if(price_direction.get_val() == -1.0):
        if(elasticity_direction < elasticity):
            return True
        else:
            return False

    if (price_direction.get_val() == 1.0):
        if (elasticity_direction > elasticity):
            return True
        else:
            return False



    
