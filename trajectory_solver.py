#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 18/05/2016
#Nima 
#

import numpy as np
import scipy as sp

import PyKEP as pk

import config
from src import instances
from src import ref_traj
from src import ref_eph

if __name__ == '__main__':
 
    trj = instances.builder.compute_traj()
    print ("Succes for computing traj !")
    instances.ref_traj.export_traj(trj)
    print ("Success for creating the trajectory")
    instances.ref_eph.export_eph(trj)
    print ("Success for creating ephemerides") 
