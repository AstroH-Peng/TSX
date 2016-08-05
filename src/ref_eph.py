#!usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 16/06/2016
#Nima 
#

import datetime as dtm
import numpy as np
import scipy as sp

import PyKEP as pk

from tools import motion
from model_tensor.gravitational import bodies

class EphOutput:
    """Class exporting ephemerides of bodies to a file in vts format

    """

    def __init__(self, foreground_objects, output_dir, vts_headers = [], vts_headers_next = []):
        """Constructor of class EphOutput."""
        self.foreground_objects = foreground_objects
        self.vts_headers = vts_headers
        self.vts_headers_next = vts_headers_next
        self.output_dir = output_dir

    def tab_write(self, *args):
        """Method writting to file."""
        for val in args:
            self.file.write('%s\t' % val)
    def export_eph(self, trajectory):
        """Exporting ephemerides of forward celestial bodies to specified file
        with respect to the spacecraft trajectory."""
        dt = motion.Date()
        ps = motion.Position()
        for body in self.foreground_objects:
            bd = bodies.PyKEPBody(body)
            with open(self.output_dir + "%s_" % body + "eph_%s.traj" % dtm.datetime.now(), 'w') as self.file:
                self.file.writelines(self.vts_headers)
                if (self.vts_headers or self.vts_headers_next) != []:
                    self.file.write("TARGET_NAME  = %s\n" % body.upper())
                    self.file.write("TARGET_ID    = OBJECT-%s\n" % body)
                self.file.writelines(self.vts_headers_next)
                for values in trajectory:
                    time = values[0]
                    pos = values[1:4]
                    lat, lon, r = ps.car_to_sph(bd.relative_position(time, pos))
                    mjd_integer_part, mjd_decimal_part = dt.mjd_vts(time)
                    self.tab_write(mjd_integer_part, mjd_decimal_part, lat, lon, r)
                    self.file.write('\n')
