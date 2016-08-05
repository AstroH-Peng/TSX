#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

from __future__ import absolute_import

import numpy as np
import scipy as sp

import PyKEP as pk

import config
from src import tensor_constructor

class Propagator:
    """ Virtual class devoting to the trajectory propation. 

    Attributes defined here:
    -tensor_constructor: provides the acceleration to be taken into account for
     trajectory propagation. 

    Methods define here:
    -rate_function(): gives the rate of the evaluated function respects to 
    the position and velocity vectors.

    """

    def __init__(self, tensor_constructor):
        """Constructor of class Propagator."""
        self.tensor_constructor = tensor_constructor 
    def rate_function(self, date, pos_vel):
        """Method providing the acceleration(s) undergone by the spacecraft
        from space bodies like Sun, planets, asteroids... and from dissipative
        forces like solar radiation pressure, magnetic field... to be integrated 
        in order to return new both position and velocity vectors.
        """
        pos = pos_vel[0:3]
        vel = pos_vel[3:6]
        acc = self.tensor_constructor.get_sum_accelerations(date*pk.SEC2DAY, pos)
        acc = np.array([acc[0][0], acc[1][1], acc[2][2]])
        acc = acc - pk.MU_SUN*pos/(np.linalg.norm(pos)**3)
        return np.append(vel, acc)
    def propagate_traj(self):
        """Virtual method."""
        pass

