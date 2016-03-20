#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 17/03/2016
#Nima
#

import numpy as np
import scipy as sp

import PyKEP as pk

class Date:
    """Class defining the date of events from objects.

    Attributes defined here:
    -dates: represents an epoch (a fixed point in time)
    -time_integer_part: integer part of mjd time
    -time_decimal_part: decimal part of mjd time in seconds

    Methods defined here:
    -vts(): return epoch as vts format with MJD type.

    """
    def __init__(self):
	"""Constructor of the class Date."""
	self.dates = [] 	# pas compris l'interet
	# ces 2 proprietés pourrait etre ecrites plus courtes?
	# self.dayvts & slef.secvts (pour "day" et "seconds" au format VTS)
	self.time_integer_part = 0
	self.time_decimal_part = 0 # ceci est-il bien un reel?
    def __repr__(self):
	"""Method displaying a customized message when an instance of 
	the class Date is called in the command line.
	"""
	return "Date: this is the epoch ({})".format(self.dates)
    def vts(self, dates):
	# pas compris, si un objet est de type "Date", sa méthode t.vts(...) utilise quoi et retourne quoi?
	"""Method converting an epoch to the vts format.
	it returns the integer part of the MJD and
	the fractional part (converted to seconds) of the MJD. 
	"""
	self.time_integer_part = int(pk.epoch(dates).mjd // 1)
	self.time_decimal_part = (pk.epoch(dates).mjd % 1) * pk.DAY2SEC
	return self.time_integer_part, self.time_decimal_part

