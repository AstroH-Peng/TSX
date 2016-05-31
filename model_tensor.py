#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

class BaseModel:
    """Class defining models of relative position and accelerations.

    Attributed defined here:
    -name: the name of the body
    -mu: the gravitational parameter of the body

    Method defined here:
    -accel_instensity(): gives the acceleration intensity of the body
    -accel_tensor(): provides the acceleration of the body as tensor.
    -relative_position(): defines position of the spacecraft with respect 
	to a body.
    -sph_acc(): provides the potential acceleration of a given body as a 
	perfect sphere.

    """
    def __init__(self, name):
	"""Constructor of the class BaseModel."""
	self.name = name
    def __repr__(self):
	"""Method displaying a customized message when an instance of the 
	class BaseModel is called in the command line.
	"""
	return "BaseModel: name = '{}'".format(self.name)
    def accel_intensity(self, date, satellite_position):
	"""Computes the acceleration intensity undergone by spacecraft."""
	rp = self.relative_position(date, satellite_position)
	acc_intens = self.mu_self / (rp**2)
	return acc_intens
    def accel_tensor(self, acc):
	"""Transforms a given acceleration vector into a matrix tensor 3*3.
	"""
	a11 = float (acc[0])
	a22 = float (acc[1])
	a33 = float (acc[2])

	matrix_tensor = np.array([[a11, 0, 0],
				  [0, a22, 0],
				  [0, 0, a33]])
	return matrix_tensor
    def relative_position(self, date, satellite_position):
	"""Gives the relative position of the spacecraft with respect to 
	a body. Returns a vector position.
	"""
	body_position, _ = np.array(self.eph(date))
	r_p = satellite_position - body_position
	return r_p
    def sph_acc(self, date, satellite_position):
	"""Method computing the potential acceleration of a given body as
	a perfect sphere. It returns a tensor 3*3.
	"""
	rel_pos = self.relative_position(date, satellite_position)
	acc = -self.mu * rel_pos / (np.linalg.norm(rel_pos)**3)
	acc_to_tensor = self.accel_tensor(acc)
	return acc_to_tensor
