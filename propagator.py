#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 15/03/2016
#Nima
#

class Propagator:
    """Class devoting to the trajectory propation.

    Attributes defined here:
    -time: correspond to a specified epoch
    -position_velocity: represents both position and velocity vectors
    -step_time: interval time during which the estimations of new position are done.

    Methods define here:
    -rate_function(): gives the rate of the evaluated function respects to 
	the position and velocity vectors
    -rk4(): computes the Runge-Kutta order 4 numerical integration method.

    """
    def __init__(self, time, position_velocity, step_time):
	"""Constructor of the class Propagator."""
	self.time = time
	self.position_velocity = position_velocity
	self.step_time = step_time
    def rate_function(self):
	"""Method defining the acceleration to be integrated in order 
	to return new both position and velocity vector.
	"""
	pass
    def rk4(self, rate_function):
	"""Method computing the Runge-Kutta order 4 numerical integration 
	method to estimate new position of the trajectory.
	"""
	semi_interval = self.step_time / 2

	k1 = rate_function(self.time, self.position_velocity)
        k2 = rate_function(self.time+semi_interval, values + k1*semi_interval)
        k3 = rate_function(self.time+semi_interval, values + k2*semi_interval)
        k4 = rate_function(self.time+time_interval, values + k3*time_interval)

	next_position_velocity = position_velocity + 1./6*(k1 + 2*k2 + 2*k3 + k4)*self.step_time
	return next_position_velocity
