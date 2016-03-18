#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 11032016
#Nima
#

import numpy as np
import scipy as sp

class Velocity:
    """Class defining the velocity of a body.

    Attributes defined here:
    -vx: defines the x velocity
    -vy: defines the y velocity
    -vz: defines the z velocity.

    Methods defines here:
    -vxvyvz(): returns the (vx, vy, vz) vector.

    """
    def __init__(self):
	"""Constructor of the class Velocity."""
	self.vx = []
	self.vy = []
	self.vz = []
	self.velocity_vector = []
    def __repr__(self):
	"""Method displaying a customized message when an instance of the class Velocity is 
	called in the command line.
	"""
	return "Velocity: vx({}), vx({}), vx({})".format(self.vx, self.vy, self.vz)
    def vxvyvz(self):
	"""Function returning the (vx, vy, vz) vector of a body."""
	self.velocity_vector.append([self.vx, self.vy, self.vz])
	self.velocity_vector = np.array(self.velocity_vector)
	return self.velocity_vector
