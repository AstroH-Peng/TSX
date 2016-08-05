#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 14/06/2016
#Nima 
#

from __future__ import absolute_import

import numpy as np
import scipy as sp

import PyKEP as pk

from . import accumulator
from src import trajectory_parser
from src.propagator import rk4_module
from src.propagator import rkf45_module

class Builder:
    """Class computing the trajectory propagation of a given Spacecraft

    Attributes defined here:
    -time_step: time step between two propagation
    -step_number: number of propagation points to get

    Methods defined here:
    -compute_traj(): computes the trajectory propagation.

    """
    def __init__(self, propagator, step_number, time_step, input_trajectory_file):
        """Constructor of the class Builder."""
        self.propagator = propagator
        self.step_number = step_number
        self.time_step = time_step * pk.DAY2SEC
        self.input_trajectory_file = input_trajectory_file

    def __repr__(self):
        """Method displaying a customized message when an instance of the 
        class BaseModel is called in the command line.
        """
        return "Builder: time_step = '{}', step_number = '{}'".format(
        self.time_step, self.step_number)
    def compute_traj(self):
        """Computes the trajectory propagation of the spacecraft for a 
        given step_number. 
        Returns a tuple: epoch, position vector, velocity vector.
        """
        host_traj = trajectory_parser.TrajParser()
        cd = accumulator.Coordinate()

        with open(self.input_trajectory_file) as input_file:
            t, p, v = host_traj.parse_traj(input_file)

        a = np.array([0.0, 0.0, 0.0]) 
        pos_vel = np.append(p, v)
        pos_vel_acc = np.append(pos_vel, a) 
        values = [np.append(t.mjd2000, pos_vel_acc)]
        t = t.mjd2000 * pk.DAY2SEC
        
        return cd.accumulate_traj(self.propagator, t, values, self.time_step, self.step_number)
