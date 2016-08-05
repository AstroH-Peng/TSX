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

class TrajOutput:
    """Class exporting the spacecraft trajectory to a file in vts format

    """

    def __init__(self, output_dir, traj_vts_headers = []):
        """Constructor of the class TrajOutput."""
        self.output_dir = output_dir
        self.vts_headers = traj_vts_headers

    def tab_write(self, *args):
        """Method writting to file."""
        for val in args:
            self.file.write('%s\t' % val)
    def export_traj(self, trajectory):
        """Exporting the trajectory of the spacecraft to specified file."""
        dt = motion.Date()
        with open(self.output_dir + "ref_traj_%s.xyzv" % dtm.datetime.now(), 'w') as self.file:  
            self.file.writelines(self.vts_headers)
            for values in trajectory:
                time = values[0]
                mjd_integer_part, mjd_decimal_part = dt.mjd_vts(time)
                self.tab_write(mjd_integer_part, mjd_decimal_part, \
                values[1]/1000., values[2]/1000., values[3]/1000., \
                values[4], values[5], values[6], values[7], values[8], \
                values[9], np.linalg.norm(values[1:4])/1000.)
                self.file.write('\n')


