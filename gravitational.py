#!/usr/bin/env python
# -*- coding: utf-8 -*-
#N

import numpy as np
import scipy as sp

import PyKEP as pk

import config
import trajectory_parser

class SphericalBody(pk.planet.jpl_lp):
    """Class defining the gravitational model of bodies.

    Attributes defined here:
    -mass: the mass of the body

    Methods defined here:
    -tensor(): provides the acceleration of SphericalBody as a tensor matrix 3*3

    """
    def __init__(self, *args, **kwargs):
        """Constructor of the class SphericalBody."""
        super(SphericalBody, self).__init__(*args, **kwargs)
	self._mass = self.mu_self
    def _get_mass(self):
	"""Method called when trying to read the attribute 'mass'."""
	return self._mass
    def _set_mass(self, new_mass):
	"""Method called when trying to modify the attribute 'mass'."""
	self._mass = new_mass

    mass = property(_get_mass, _set_mass)

    def __repr__(self):
	"""Method displaying a customized message when an instance of the class Position is 
	called in the command line.
	"""
	return "SphericalBody: name({}), mass({})".format(self.name, self.mu_self)
    def relative_position(self, sat_pos, epoch):
	"""Gives the relative position of the spacecraft with respect to a body."""
	body_position, _ = np.array(self.eph(epoch))
	r_p = sat_pos - body_position
	return r_p
    def acceleration_intensity(self, sat_pos, epoch):
	"""Computes the acceleration intensity undergone by spacecraft."""
	rp = relative_position(sat_pos, epoch)
	acc_intens = self.mu_self / (rp**2)
	return acc_intens
    def tensor(self, sat_position, date):
	"""Provides the acceleration of the main potential of body.

	Method converts the CubeSat's position (Ecliptic) into the distance 
	on center of the SphericalBody, computes the acceleration intensity and return 
	a matrix tensor 3*3 of the acceleration.
	"""
	#body_position, _ = np.array(self.eph(date))
	rel_pos = relative_position(sat_position, date)
	acc_intensity = acceleration_intensity(sat_position, date)
	acc = -self.mu_self * rel_pos / (np.linalg.norm(rel_pos)**3)

	a11 = float (acc[0])
	a22 = float (acc[1])
	a33 = float (acc[2])

	matrix_tensor = np.array([[a11, 0, 0],
				  [0, a22, 0],
				  [0, 0, a33]])
	return matrix_tensor #a1, a2, a3 #matrix_tensor

class SphericalHarmonic(pk.planet.jpl_lp):
    """Class defining the perturbations due to the aspherical shape of bodies.
    
    Attributes defined here:
    -mass: the mass of the body
    -equa_radius: the equatorial radius of the body

    Methods defined here:
    -j2_tensor(): provides the acceleration due to the j2 terms as a tensor matrix 3*3
    
    """
    def __init__(self, *args, **kwargs):
        """Constructor of the class SphericalHarmonic."""
        super(SphericalHarmonic, self).__init__(*args, **kwargs)
	self._mass = self.mu_self
	self._equa_radius = self.radius
    def _get_mass(self):
	"""Method called when trying to read the attribute 'mass'."""
	return self._mass
    def _set_mass(self, new_mass):
	"""Method called when trying to modify the attribute 'mass'."""
	self._mass = new_mass
    def _get_equa_radius(self):
	"""Method called when trying to read the attribute 'equa_radius'."""
	return self._equa_radius
    def _set_equa_radius(self, new_equa_radius):
	"""Method called when trying to modify the attribute 'equa_radius'."""
	self._equa_radius = new_equa_radius

    mass = property(_get_mass, _set_mass)
    equa_radius = property(_get_equa_radius, _set_equa_radius)

    def j2_tensor(self, radius_vector):
        """Provides the acceleration due to the j2 terms of the aspherical shape of body.
	Returns a matrix tensor 3*3.
	"""
	pass

class UnknownBody:
    """Class defining the gravitational model of unknown bodies from librairies.

    Attributes defined here:
    -mass: the mass of the body
    -traj: name of trajectory file of an undefined body in PyKEP library

    Methods defined here:
    -u_eph(): provides the body position and velocity at a given epoch
    -u_tensor(): provides the acceleration of SphericalBody as a tensor matrix 3*3

    """
    def __init__(self, mass, traj):
	"""Constructor of the class UnknowedBody."""
	self.mass = mass
	self.traj = traj
    def u_eph(self, date):
	"""Method providing the unknown body position and velocity at a given epoch.
	Returns a tuple r, v.
	"""
	#file_name = self.traj
	prs = trajectory_parser.TrajectoryParser()
	with open(config.input_dir + config.da) as input_file:
	    t, r, v = prs.parse_trajectory(input_file)
	print t
	print r
	print v
	pos_vel = [(r, v) for i,date in enumerate(t) if t[i] == date]
	pos, vel = pos_vel 
	print pos_vel
	print date
	return pos, vel
    def u_tensor(self, sat_position, date):
	"""Provides the acceleration of the main potential of unknown body.

	Method converts the CubeSat's position (Ecliptic) into the distance 
	on center of the UnknownBody, computes the acceleration intensity and return 
	a matrix tensor 3*3 of the acceleration.
	"""
	u_body_position, _ = np.array(u_eph(date))
	rel_pos = sat_position - u_body_position
	acc_intensity = -self.mass / (rel_pos**2)
	acc = -self.mass * rel_pos / (np.linalg.norm(rel_pos)**3)

	a11 = float (acc[0])
	a22 = float (acc[1])
	a33 = float (acc[2])

	matr_tensor = np.array([[a11, 0, 0],
				[0, a22, 0],
				[0, 0, a33]])
	return matr_tensor
    
