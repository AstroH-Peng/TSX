#!usr/bin/env python
# -*- coding: utf-8 -*- 
#Modified date: 17/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk
 
class Acceleration:
    """Class defining the acceleration components of a body.

    Attributes defined here:
    -ax: defines the x component
    -ay: defines the y component
    -az: defines the z component
    -a_vec: represents an empty list of acceleration

    Methods defined here:
    -axayaz_array(): returns the (x, y, z) vector.

    """
    def __init__(self, ax = 0.0, ay = 0.0, az = 0.0, a_vec = []):
	"""Constructor of the class Acceleration."""
	self.ax = ax
	self.ay = ay
	self.az = az
	self.a_vec = a_vec
    def __repr__(self):
	"""Method displaying a customized message when an instance of the
	class Acceleration is called in the command line.
	"""
	return "Acceleration: ax({}), ay({}), az({})".format(self.ax, 
	self.ay, self.az)
    def axayaz_array(self):
	"""Method returning the (ax, ay, az) vector of a body."""
	a_vec = self.a_vec.append[ax, ay, az]
	a_vec = np.array(a_vec)
	return a_vec

class Date:
    """Class defining the date of an event from objects.

    Attributes defined here:
    -date: represents an epoch (a fixed point in time)
    
    Methods defined here:
    -vts(): return epoch as vts format with MJD type.

    """
    def __init__(self, date = 0.0):
	"""Constructor of the class Date."""
	self.date = date
    def __repr__(self):
	"""Method displaying a customized message when an instance of the 
	class Date is called in the command line.
	"""
	return "Date: this is the epoch ({})".format(self.date)
    def vts(self, time):
	"""Method converting an epoch to the vts format.
	it returns the integer part of the MJD and
	the fractional part (converted to seconds) of the MJD. 
	"""
	mjd_integer_part = int(pk.epoch(time).mdj // 1)
	mjd_decimal_part = (pk.epoch(time) % 1) * pk.DAY2SEC
	return mjd_integer_part, mjd_decimal_part

class Position:
    """Class defining the location of a body.

    Attributes defined here:
    -x: defines the x position 
    -y: defines the y position
    -z: defines the z position
    -pos_vec: represents an empty list of position
    -latitude: defines the latitude position
    -longitude: defines the longitude position
    -radius: defines the radius vector between the body with another.

    Methods defined here:
    -xyz_array(): returns the (x, y, z) vector
    -car2sph(): transforms cartesian coordinates to spherical coordinates
    -sph2car(): transforms spherical coordinates to cartesian coordinates.


    """
    def __init__(self, x = 0.0, y = 0.0, z = 0.0, pos_vec = [], 
	latitude = 0.0, longitude = 0.0, radius = 0.0):
	"""Constructor of the class Position."""
        self.x = x
        self.y = y
        self.z = z 
	self.pos_vec = pos_vec
	self.latitude = latitude
	self.longitude = longitude
	self.radius = radius
    def __repr__(self):
        """Method displaying a customized message when an instance of the 
	class Position is called in the command line.
	"""
        return "Position: x({}), y({}), z({}), latitude({}), longitude({}), radius({})".format(
	self.x, self.y, self.z, self.latitude, self.longitude, self.radius)
    def xyz_array(self):
	"""Method returning the (x, y, z) vector of a body."""
	self.pos_vec = [self.x, self.y, self.z]
	pos = np.array(self.pos_vec)
	return pos
    def car2sph(self, car_pos):
	"""Method transforming cartesian coordinates to spherical coordinates.
	return tuple: longitude, latitude, r. The units are respectively in
	degree, degree, m.
	"""
	r = np.linalg.norm(car_pos)
	latitude = np.arcsin(car_pos[2] / r) * 180. / np.pi
	longitude = np.arctan2(car_pos[1], car_pos[0]) * 180. / np.pi 
	return longitude, latitude, r
    def sph2car(self, longitude, latitude, r):
	"""Method transforming spherical coordinate to cartesian coordinates.
	return tuple: x, y, z. The units are respectively in m, m, m.
	"""
	x = r * np.cos(latitude) * np.cos(longitude)
	y = r * np.cos(latitude) * np.sin(longitude)
	z = r * np.sin(latitude)
	return x, y, z

class Velocity:
    """Class defining the velocity components of a body.

    Attributes defined here:
    -vx: defines the x component
    -vy: defines the y component
    -vz: defines the z component
    -vel_vec: represents an empty list of velocity

    Methods defined here:
    -vxvyvz_array(): returns the (vx, vy, vz) vector.

    """
    def __init__(self, vx = 0.0, vy = 0.0, vz = 0.0, vel_vec = []):
	"""Constructor of the class Velocity."""
	self.vx = vx
	self.vy = vy
	self.vz = vz
	self.vel_vec = vel_vec
    def __repr__(self):
	"""Method displaying a customized message when an instance of the
	class Velocity is called in the command line.
	"""
	return "Velocity: vx({}), vy({}), vz({})".format(
	self.vx, self.vy, self.vz)
    def vxvyvz_array(self):
	"""Method returning the (vx, vy, vz) vector of a body."""
	self.vel_vec = [self.vx, self.vy, self.vz]
	vel = np.array(self.vel_vec)
	return vel
