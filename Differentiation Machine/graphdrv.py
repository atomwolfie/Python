#!/usr/bin/python

###########################################
# module: graph_drv.py
# Aaron Adams
# A#02026009
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt
import math

def graph_drv(fexpr, xlim, ylim):

    #derivatives
    deriv1 = deriv(fexpr)
    deriv2 = deriv(deriv1)

    #converting them to functions
    f1 = tof(deriv1)
    f2 = tof(deriv2)

    xvals = np.linspace(-2, 2, 10000)
    yvals1 = np.array([f1 for x in xvals])
    yvals2 = np.array([f2 for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle("Aaron's Graph")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim([0, ylim])
    plt.xlim([0, xlim])
    plt.grid()
    plt.plot(xvals, yvals1, label="first line")
    plt.plot(xvals, yvals2, label="second line")
    plt.legend(loc="best")
    plt.show()

