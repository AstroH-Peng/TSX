#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 20/05/2016
#Nima 
#

from __future__ import absolute_import

import numpy as np
import scipy as sp

import PyKEP as pk

from src.model_tensor import base_model
from . import bodies

class SphericalBody(base_model.BaseModel):
    """Class giving the potential acceleration of body as a perfect sphere.

    This class inherits from class base_model.BaseModel.

    Attributes defined here:
    -body: instance of class PyKEPBody and / or class UnKnownBody. 

    Method defined here:
    -get_acceleration(): method inherits from Super-class.

    """

    pykep_bodies = [] 
    unkown_bodies = {}                              

    def __init__(self, name):
        """Constructor of the class SphericalBody."""
        base_model.BaseModel.__init__(self, name)
        
        if name in SphericalBody.pykep_bodies:
            self.body = bodies.PyKEPBody("%s" % name)
        else:
            self.body = bodies.UnKnownBody("%s" % name, SphericalBody.unkown_bodies[name]["mu"],\
                        SphericalBody.unkown_bodies[name]["radius"], \
                        SphericalBody.unkown_bodies[name]["traj_file"])

    def get_acceleration(self, date, satellite_position):
        """Method computing the potential acceleration of a given body as
        a perfect sphere. Returns a tensor 3*3.
        """
        r_p = self.body.relative_position(date, satellite_position)
        acc = -self.body._get_mu() * r_p / (np.linalg.norm(r_p)**3)
        return self.vec_to_tensor(acc)
