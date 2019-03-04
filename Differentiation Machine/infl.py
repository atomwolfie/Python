#!/usr/bin/python

#######################################
# module: infl.py
# Aaron Adams
# YOUR A#02026009
#######################################

from const import const
from deriv import deriv
from poly12 import find_poly_1_zeros
from tof import tof
from point2d import point2d

def find_infl_pnts(expr):

    deriv1 = deriv(expr)
    deriv2 = deriv(deriv1)

    zero = find_poly_1_zeros(deriv2)

    func = tof(expr)

    answers = abs(func(zero.get_val()) - 0.0)


    # add answers to iflection points
    inflpoints = [answers]


    return inflpoints
    
    
            

    
