#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

import rk_module

class PropagatorRk4(rk_module.Propagator):
    """Class devoting to the trajectory propation.

    This class inherits from class rk_module.Propagator.

    Methods define here:
    -propagate_traj(): computes the Runge-Kutta order 4 numerical integration method.

    """
    def __init__(self, tensor_constructor):
        """Constructor of class PropagatorRk4."""
        rk_module.Propagator.__init__(self, tensor_constructor)

    def propagate_traj(self, date, pos_vel, h):
        """Method computing the Runge-Kutta order 4 numerical integration 
        method to estimate new position of spacecraft trajectory.
        Returns a tuple:(r, v, a) respectively position vectors, velocity 
        vectors and acceleration vectors.
        """

        k1 = self.rate_function(date, pos_vel)
        k2 = self.rate_function(date + h/2, pos_vel + k1/2)
        k3 = self.rate_function(date + h/2, pos_vel + k2/2)
        k4 = self.rate_function(date + h, pos_vel + k3)

        next_pos_vel = pos_vel + 1./6*(k1 + 2*k2 + 2*k3 + k4)*h
        return np.append(next_pos_vel, k1[3:6])
