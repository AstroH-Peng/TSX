#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

class BaseModel:
    """Class defining the acceleration's format for numerical integration.

    Attributed defined here:
    -name: the name of the object.

    Method defined here:
    -vec_to_tensor(): provides the acceleration of a given object as tensor.

    """
    def __init__(self, name):
        """Constructor of the class BaseModel."""
        self._name = name
    def _get_name(self):
        """Method called when trying to read the attribute 'name'."""
        return self._name
    def _set_name(self, new_name):
        """Method called when trying to modify the attribute 'name'."""
        self._name = new_name

    name = property(_get_name, _set_name)

    def __repr__(self):
        """Method displaying a customized message when an instance of the 
        class BaseModel is called in the command line.
        """
        return "BaseModel: name = '{}'".format(self.name)
    def get_acceleration(self):
        """Virtual method."""
        pass
    def vec_to_tensor(self, acc):
        """Transforms a given acceleration vector into a matrix tensor 3*3.
        """
        a11 = float (acc[0])
        a22 = float (acc[1])
        a33 = float (acc[2])

        matrix_tensor = np.array([[a11, 0, 0],
				  [0, a22, 0],
				  [0, 0, a33]])
        return matrix_tensor
