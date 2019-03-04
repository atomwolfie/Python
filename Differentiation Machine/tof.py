#!/usr/bin/python


###########################################
# module: tof.py
# Aaron Adams
# Your A#02026009
###########################################
import numpy as np

from ln import ln
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from maker import make_pwr_expr, make_pwr, make_const

import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    elif isinstance(expr, quot):
        return quot_tof(expr)
    elif isinstance(expr, ln):
        return ln_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))



def ln_tof(l):
    assert isinstance(l, ln)
    temp = l.get_expr()
    newexpr = tof(temp)
    def f(x):
        return np.log(newexpr(x))
    return f



## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):
        def f(x):
            return expb.get_val()**x
        return f
    elif isinstance(expb, var):
        if isinstance(d, const):
            def f(x):
                return x ** d.get_val()
            return f
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus):
        if isinstance(d, const):
            def f(x):
                sunfunc = tof(expb)
                return sunfunc(x) ** d.get_val()
            return f
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    elif isinstance(expb, pwr):
        if isinstance(d, const):
            def f(x):
                pwrfunc = tof(expb)
                return pwrfunc(x) ** d.get_val()
            return f
        else:
            raise Exception('pw_tof: case 3:' + str(expr))
    elif isinstance(expb, prod):
        if isinstance(d, const):
            def f(x):
                prodfunc = tof(expb)
                return prodfunc(x) ** d.get_val()
            return f
    elif isinstance(expb, quot):
        if isinstance(d, const):
            def f(x):
                quotfunc = tof(expb)
                return quotfunc(x) ** d.get_val()
            return f

    elif isinstance(expb, ln):
        if isinstance(d, const):
            def f(x):
                lnfunc = tof(expb)
                temp = lnfunc(x)
                return temp ** d.get_val()
            return f
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    else:
        raise Exception('pw_tof: case 5:' + str(expr))

def prod_tof(expr):
    def f(x):
        func1 = tof(expr.get_mult1())
        func2 = tof(expr.get_mult2())
        return func1(x) * func2(x)
    return f

def plus_tof(expr):
    def f(x):
          func1 = tof(expr.get_elt1())
          func2 = tof(expr.get_elt2())
          return func1(x) + func2(x)
    return f

def quot_tof(expr):
    def f(x):
          func1 = tof(expr.get_num())
          func2 = tof(expr.get_denom())
          return func1(x) / func2(x)
    return f