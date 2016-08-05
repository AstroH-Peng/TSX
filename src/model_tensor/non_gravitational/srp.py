#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 13/06/2016
#Nima 
#

from __future__ import absolute_import

import numpy as np
import scipy as sp

import PyKEP as pk

from src.model_tensor import base_model
from src.tools import spacecraft

class RadiationPressure(base_model.BaseModel):
    """Class giving the solar radiation pressure undergone by the spacecraft.

    This class inherits from class base_model.BaseModel.

    Attributes defined here:
    -solar_pression: the pression due to the interaction of photons
    -solar_flux: conventional flux got in Earth from Sun.

    Methods defined here:
    -get_acceleration(): computes the srp acceleration.

    """

    _pression = 0.0
    _flux = 0.0

    def __init__(self, name):
        """Constructor of the class RadiationPressure."""
        base_model.BaseModel.__init__(self, name)
        self.sat = spacecraft.Spacecraft()
    
    def get_pression(self):
        """Method called when trying to read the attribute 'pression'."""
        return RadiationPressure._pression
    def get_flux(self):
        """Method called when trying to read the attribute 'flux'."""
        return RadiationPressure._flux
    def __repr__(self):
        """Method displaying a customized message when an instance of the 
        class BaseModel is called in the command line.
        """
        return "SRP: name = '{}', pression = '{}', solar flux = '{}'".format(
        self.name, RadiationPressure._pression, RadiationPressure._flux)
    def get_acceleration(self, date, satellite_position):
        """Method computing the solar radiation pressure (srp) undergone
        by the spacecraft. returns a tensor 3*3.
        """
        acc = ((-RadiationPressure._pression * self.sat.get_reflectivity() \
		* self.sat.get_area_exposed_to_sun()) / self.sat.get_mass()) \
		* (satellite_position / (np.linalg.norm(satellite_position)))
        return self.vec_to_tensor(acc)
