#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 11032016
#Nima 
#

import numpy as np
import scipy as sp

class Position:
    """Class defining the location of a body.

    Attributes defined here:
    -x: defines the x position 
    -y: defines the y position
    -z: defines the z position
    -position_vector: represents the (x, y, z) vector
    -latitude: defines the latitude position
    -longitude: defines the longitude position
    -latitude_longitude: represents the couple (latitude, longitude)
    -radius: defines the radius vector between the body with another.

    Methods defines here:
    -xyz(): returns the (x, y, z) vector.
    -latitude_longitude(): returns the couple (latitude, longitude).

    """
    def __init__(self):
        """Constructor of the class Position."""
        self.x = []
        self.y = []
        self.z = [] 
	self.position_vector = []
	self.latitude = []
	self.longitude = []
	self.latitude_longitude = []
	self.radius = []
    def __repr__(self):
        """Method displaying a customized message when an instance of the class Position is 
	called in the command line.
	"""
        return "Position: x({}), y({}), z({}), latitude({}), longitude({}), radius({}))".format(
	self.x, self.y, self.z, self.latitude, self.longitude, self.radius)
    def xyz(self):
        """Function returning the (x, y, z) vector of a body."""
	self.position_vector.append([self.x, self.y, self.z])
	self.position_vector = np.array(self.position_vector) 
	return self.position_vector
    def latitude_longitude(self):
	"""Function returning the couple (latitude, longitude)."""
	self.latitude_longitude.append([self.latitude, self.longitude])
	self.latitude_longitude = np.array(self.latitude_longitude)
	return self.latitude_longitude







