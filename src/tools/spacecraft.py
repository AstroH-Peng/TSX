#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 13/06/2016
#Nima 
#

import numpy as np
import scipy as sp

import config

class Spacecraft():
    """Class defining a spacecraft features.

    Attributes defined here:
    -mass: the mass of the spacecraft
    -area_exposed_to_sun: the exposed area to the Sun
    -reflectivity: the coefficient indicating how the spacecraft reacts to
    the interaction with photons. 

    """
    _mass = 0.0
    _area_exposed_to_sun = 0.0
    _reflectivity = 0.0
        
    def get_mass(self):
        """Method called when trying to read the attribute 'mass'."""
        return Spacecraft._mass
   
    def get_area_exposed_to_sun(self):
        """Method called when trying to read the attribute 'area_exposed_to_sun'."""
        return Spacecraft._area_exposed_to_sun
    
    def get_reflectivity(self):
        """Method called when trying to read the attribute 'reflectivity'."""
        return Spacecraft._reflectivity
   
   


