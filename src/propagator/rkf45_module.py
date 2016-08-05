#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

import rk_module

class PropagatorRkf45(rk_module.Propagator):
    """Class devoting to the trajectory propation.

    This class inherits from class rk_module.Propagator.

    Attributes defined here:
    -h_min: step time minimum
    -h_max: step time maximum
    -tolerance: tolerance to be compared with estimating error
    -safty_factor: safty factor of the error evaluation.

    Methods define here:
    -propagate_traj(): computes the Runge-Kutta-felburg order 5 numerical integration method.

    """

    def __init__(self, tensor_constructor, h_min, h_max, tolerance, safty_factor):
        """Constructor of class PropagatorRkf45."""
        rk_module.Propagator.__init__(self, tensor_constructor)
        self.h_min = h_min * pk.DAY2SEC
        self.h_max = h_max * pk.DAY2SEC
        self.tolerance = tolerance
        self.safty_factor = safty_factor

    def propagate_traj(self, date, pos_vel, h):
        """Complete the Runge-Kutta-Fehlberg numerical integration method 
        by using an adaptive step time control during the computation.
        """ 
        n = len(pos_vel)

        k1 = self.rate_function(date, pos_vel)
        k2 = self.rate_function(date + h/4, pos_vel + k1/4)
        k3 = self.rate_function(date + 3/8*h, pos_vel + 3/32*k1 + 9/32*k2)
        k4 = self.rate_function(date + 12/13*h, pos_vel + 1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3)
        k5 = self.rate_function(date + h, pos_vel + 439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4)
        k6 = self.rate_function(date + 1/2*h, pos_vel - 8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5)

        next_pos_vel = pos_vel + (25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 1/5*k5)*h
        tild_pos_vel = pos_vel + (16/135*k1 + 6656/12.825*k3 + 28.561/56.430*k4 - 9/50*k5 + 2/55*k6)*h

        estimate_error = np.fabs(tild_pos_vel - next_pos_vel) 
        mean_estimate_error = np.sqrt(sum(estimate_error**2) / n)

        delta = self.safty_factor * ((self.tolerance * h) / mean_estimate_error)**(0.25)  

        # Following conditions should be reevaluated to validate the sampling.
        if h < self.h_min:
            h = self.h_min
        if h > self.h_max:
            h = self.h_max
        if delta < 0.75 and h > 2*self.h_min:
            pos_vel = np.append(next_pos_vel, k1[3:6])
            h = h/2
        elif delta > 1.50 and 2*h < self.h_max:
            pos_vel = np.append(next_pos_vel, k1[3:6])
            h = 2*h
        else:
            pos_vel = np.append(next_pos_vel, k1[3:6])
  
        return h, pos_vel
