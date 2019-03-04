#!/usr/bin/python

#########################################
# module: derivtest.py
# Aaron Adams
# A#02026009
#########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from deriv import deriv
from poly12 import find_poly_1_zeros
from poly12 import find_poly_2_zeros
from tof import tof
from point2d import point2d


def loc_xtrm_1st_drv_test(expr):



    #step 1 take derivative
    myderiv = deriv(expr)


       #step2 solve for x
    zeros = find_poly_2_zeros(myderiv)

    # for c in zeros:
    #     print c

    pf = tof(expr)

    extremas = []

    for c in zeros:
        yval = abs(pf(c.get_val()) - 0.0)


        if (pf(c.get_val()) - 1 > 0 & pf(c.get_val()) + 1 < 0):
            extremas.append("min", point2d(c.get_val(), yval))

        else:
            extremas.append("max", point2d(c.get_val(), yval))

    return extremas

def loc_xtrm_2nd_drv_test(expr):

    firstDeriv = deriv(expr)
    secondDeriv = deriv(firstDeriv)

    finalyval = secondDeriv.get_elt2()

    zeros =  find_poly_1_zeros(secondDeriv)

    pf = tof(secondDeriv)
    extremas = []

    for c in zeros:
        if(pf(c.get_val()) > 0):
            extremas.append(tuple("min", point2d(c.get_val(), finalyval)))

        else:
            extremas.append("max", tuple("max", point2d(c.get_val(), finalyval)))
    return extremas

