#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 09/06/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

from model_tensor.gravitational import sphr
from model_tensor.non_gravitational import srp

class AccelConstructor():
    """Class computing the sum of accelerations to be integrated numerically.

    Attributes defined here:
    -list_models: list of models to be take into account by the propagator.
    -list_perturbations: list of perturbations that can interact with 
     spacecraft.

    Method defined here:
    -get_sum_accelerations(): gives the sum of accelerations.

    """

    def __init__(self, list_models, list_perturbations):
        """Constructor of the class AccelConstructor."""
        self.list_models = list_models
        self.list_perturbations = list_perturbations

    def get_sum_accelerations(self, date, satellite_position):
        """Computes the sum of the different accelerations to be integrated
        numerically. Returns a tensor 3*3.
        """
        list_acc = []
        for model in self.list_models:
            if model in self.list_perturbations:
                if model.lower() == "srp":
                    non_g = srp.RadiationPressure(model)
                    acc = non_g.get_acceleration(date, satellite_position) 
            else:
                g = sphr.SphericalBody(model.lower())
                acc = g.get_acceleration(date, satellite_position) 
            list_acc.append(acc)
        sum_acc = sum(acceleration for acceleration in list_acc)
        return sum_acc
		
