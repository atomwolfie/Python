import math

import const
from deriv import deriv, logdiff, ln_deriv
from infl import find_infl_pnts
from maker import make_prod, make_const, make_pwr, make_plus, make_quot, make_const, make_e_expr, make_ln, make_pwr_expr
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from tof import tof



fex = make_prod(make_pwr("x", 1.0),
                    make_prod(make_plus(make_pwr("x", 1.0),
                                        make_const(1.0)),
                                        make_plus(make_pwr("x", 1.0),
                                        make_const(2.0))))
drv = logdiff(fex)
assert not drv is None
print(drv)
drvf = tof(drv)
print(drvf(2))

