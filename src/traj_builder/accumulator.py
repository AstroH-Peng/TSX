#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 14/06/2016
#Nima 
#

from __future__ import absolute_import

import numpy as np
import scipy as sp

import PyKEP as pk

from src.propagator import rk4_module
from src.propagator import rkf45_module

class Coordinate:
    """Class accumulating the trajectory.

    Method defined here:
    -accumulate_traj(): accumulates trajectories.

    """

    def accumulate_traj(self, propagator, t, values, time_step, step_number):
        """Method accumulating spacecraft trajectories."""
        for i in xrange(step_number):
            time = t + time_step * i
            if isinstance(propagator, rk4_module.PropagatorRk4):
                cmp_pos_vel = propagator.propagate_traj(time, values[i][1:7], time_step)
                values.append(np.append(time*pk.SEC2DAY, cmp_pos_vel))
            if isinstance(propagator, rkf45_module.PropagatorRkf45):
                h, cmp_pos_vel = propagator.propagate_traj(time, values[i][1:7], time_step)
                values.append(np.append(time*pk.SEC2DAY, cmp_pos_vel))
                time_step = h
        return values
