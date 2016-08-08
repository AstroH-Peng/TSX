#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 17/05/2016
#Method first wrote by Jim
#Nima 
#


import numpy as np
import scipy as sp

import PyKEP as pk

from tools import motion

class TrajParser:
    """Class giving the location of the spacecraft at a certain eppoch.

    This class reads the contents of a file of trajectory and returns 
    data from the last line. The file should have as format a list of 
    data without containing any string. The class TrajParser uses following
    classes: Date, Position and Velocity.
    Recovered data are:
    -d: represents an epoch (a fixed point in time)
    -p: the position vector of the spacecraft
    -v: the velocity vector of the spacecraft.

    """

    def parse_traj(self, trajectory_file):
        """Method reading the contents of a specified trajectory file and 
        returning the data from last line of file as a tuple of an epoch, 
        an array of position vector and an array of velocity vector.
        Returns date (string format), position (m), velocity (km).
        """
        d = motion.Date()
        p = motion.Position()
        v = motion.Velocity()
        for line in trajectory_file.read().splitlines():
            values = [float(element) for element in line.split(' ')]
            d.date = pk.epoch(values[0], 'jd')
            p.x = values[1]
            p.y = values[2]
            p.z = values[3]
            v.vx = values[4]
            v.vy = values[5]
            v.vz = values[6]
	
        return d.date, p.xyz_array() * 1000, v.vxvyvz_array() * 1000
