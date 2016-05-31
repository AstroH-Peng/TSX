#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

class Propagator:
    """Class devoting to the trajectory propation.

    Attributes defined here:
    -none

    Methods define here:
    -rate_function(): gives the rate of the evaluated function respects to 
    the position and velocity vectors
    -rk4(): computes the Runge-Kutta order 4 numerical integration method.

    """
    def rate_function(self, date, pos_vel):
	"""Method providing the acceleration undergone by the spacecraft
	from space bodies like Sun, planets, asteroids... to be integrated 
	in order to return new both position and velocity vectors.
	"""
	pass
    def rk4(self, rate_function, date, pos_vel, step_time):
	"""Method computing the Runge-Kutta order 4 numerical integration 
	method to estimate new position of spacecraft trajectory.
	"""
	half_step_time = step_time / 2

	k1 = rate_function(date, pos_vel)
	k2 = rate_function(date + half_step_time, pos_vel + k1*half_step_time)
	k3 = rate_function(date + half_step_time, pos_vel + k2*half_step_time)
	k4 = rate_function(date + step_time, pos_vel + k3*step_time)

	next_pos_vel = pos_vel + 1./6*(k1 + 2*k2 + 2*k3 + k4)*step_time

	return next_pos_vel 


