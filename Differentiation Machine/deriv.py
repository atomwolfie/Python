#!/usr/bin/python

####################################
# Aaron Adams
# A#02026009
####################################
from absv import absv
from ln import ln
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from maker import make_const, make_pwr, make_pwr_expr, make_quot, make_ln
import math

def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, quot):
        return quot_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    elif isinstance(expr, ln):
        return ln_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))



def ln_deriv(expr):
    assert isinstance(expr,ln)
    lnexpression = expr.get_expr()
    if isinstance(lnexpression,const):
        return const(0)
    elif isinstance(lnexpression,absv):
        return quot(const(1),lnexpression.get_expr())
    else:
        return prod(quot(const(1), lnexpression), deriv(lnexpression))




#converting the quotient to a prod and calling deriv on it
def quot_deriv(q):
    num = q.get_num()
    denom = q.get_denom()
    newexpr = prod(mult1=num,mult2=pwr(base=denom,deg=make_const(-1.0)))
    return deriv(newexpr)

# the derivative of a constant is 0.
def const_deriv(c):
    assert isinstance(c, const)
    return const(val=0.0)

def plus_deriv(s):
    assert isinstance(s,plus)
    element1=  s.get_elt1()
    element2 = s.get_elt2()
    element1deriv = deriv(element1)
    element2deriv = deriv(element2)
    plusderiv = plus(element1deriv,element2deriv)
    return plusderiv

def pwr_deriv(p):
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()

    #this assumes ever contact that comes in is e
    if isinstance(b,const):
        if b.get_val() == math.e:
            return prod(mult1=p,mult2=deriv(d))
        else:
         return d

    if isinstance(b, var):
        if isinstance(d, const):
            if d.get_val() - 1.0 == 0:
                return const(1)
            else:
                return pwr(prod(d,b), const(d.get_val() - 1.0))
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    if isinstance(b, pwr):
        if isinstance(d, const):
           basederiv = deriv(b)
           return prod(basederiv, pwr(prod(b,d), const(d.get_val() - 1)))
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))

    elif isinstance(b, plus):
        if isinstance(d, const):
           basederiv = deriv(b)
           return prod(basederiv, pwr(prod(b,d), const(d.get_val()- 1.0)))
        else:
            raise Exception('pwr_deriv: case 3: ' + str(p))

    elif isinstance(b, prod):
        if isinstance(d, const):
            basederiv = deriv(b)
            return prod(basederiv,pwr(prod(b,d), const(d.get_val() - 1)))
        else:
            raise Exception('pwr_deriv: case 4: ' + str(p))

    elif isinstance(b, ln):
        if isinstance(d, const):
            temp = d.get_val()
            return prod(mult1=prod(mult1=d,mult2=pwr(base=b,deg=const(temp - 1))),
                        mult2=prod(mult1=(quot(num=1.0,denom=b.get_expr())),mult2=deriv(b.get_expr())))
    else:
        raise Exception('pwr_deriv: case 5: ' + str(p))

def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()
    m2 = p.get_mult2()
    if isinstance(m1, const):
        if isinstance(m2, const):
            return const(val=0.0)
        elif isinstance(m2, pwr):
            return prod(mult1= m1, mult2= deriv(m2))
        elif isinstance(m2, plus):
            return prod(mult1=m1, mult2=deriv(m2))
        elif isinstance(m2, prod):
            return prod(mult1=m1, mult2=deriv(m2))
        else:
            raise Exception('prod_deriv: case 0' + str(p))

    elif isinstance(m1, plus):
        if isinstance(m2, const):
            return prod(mult1=plus_deriv(m1), mult2=m2)
        if isinstance(m2, plus):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, pwr):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, prod):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, quot):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        else:
             raise Exception('plus issue: case 2:' + str(p))
    elif isinstance(m1, pwr):
        if isinstance(m2, const):
            return prod(mult1=deriv(m1), mult2=m2)
        if isinstance(m2, ln):
            return plus(elt1=deriv(m1), elt2=m2)
        if isinstance(m2, plus):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, pwr):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, prod):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, quot):
            return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
        elif isinstance(m2, ln):
            return plus(elt1=m2, elt2 =deriv(m1))
        else:
             raise Exception('pwr issue: case 2:' + str(p))
    elif isinstance(m1, prod):
            if isinstance(m2, const):
                return prod(mult1=deriv(m1), mult2=m2)
            if isinstance(m2, plus):
                return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
            elif isinstance(m2, pwr):
                return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
            elif isinstance(m2, prod):
                return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
            elif isinstance(m2, quot):
                return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
            else:
                raise Exception('prod issue: case 2:' + str(p))
    elif isinstance(m1, quot):
             if isinstance(m2, plus):
                 return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
             elif isinstance(m2, pwr):
                 return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
             elif isinstance(m2, prod):
                 return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
             elif isinstance(m2, quot):
                 return plus(elt1=prod(deriv(m1), m2), elt2=prod(m1, deriv(m2)))
             else:
                 raise Exception('quot issue: case 2:' + str(p))
    else:
       raise Exception('prod_deriv: case 4:' + str(p))


def logdiff(expr):
    newln = make_ln(expr)
    return prod(expr, deriv(newln))


