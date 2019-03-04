#!/usr/bin/python

############################################
# module: poly12.py
# Aaron Adams
# #A02026009
############################################
from maker import make_quot, make_const
from prod import prod
from const import const
from pwr import pwr
from plus import plus
from quot import quot
from var import var
from deriv import deriv
from tof import tof
import math

def find_poly_1_zeros(expr):
    firstpart = expr.get_elt1()
    a = firstpart.get_mult1()
    b = expr.get_elt2()

    fex1 = prod(mult1=b, mult2=-1)
    fex2 = make_quot(1, a)


    return const(val=prod(mult1=fex1, mult2=fex2))

def find_poly_2_zeros(expr):
    firstpart = expr.get_elt1()
    firstpart_1 = firstpart.get_elt1()
    secondpart = firstpart.get_elt2()

    aconst = firstpart_1.get_mult1()
    bconst = secondpart.get_mult1()
    cconst = expr.get_elt2()

    a = aconst.get_val()
    b = bconst.get_val()
    c = cconst.get_val()



    #quadratic formula to get zeroes

    part1 = (b**2) - (4 * a * c)
    part2 = math.sqrt(part1)


    negb = b * -1

    option1 = negb + part2
    option2 = negb - part2

    result1 = option1/(2*a)
    result2 = option2/(2*a)

    return const(result1), const(result2)

    
    
    
            
    




