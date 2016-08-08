# -*- coding: utf-8 -*-
# Modified date: 01/08/2016
# Nima

# Trajectory Solver configuration file for propagating trajectories.
# This file is devoted to be the lonely interface that user can declare or
# create variables and to choose input and/or ouptut directories of files.

import time  as tm

# Directories inputs and outputs (in absolute paths) 
input_dir = "/home/birdy/Software/TSX/host-trajectories/"
unknown_bodies_input_dir = "/home/birdy/Software/TSX/bodies-trajectories/"
output_dir = "/home/birdy/Software/TSX/output-trajectories/"

# Directories inputs and outputs (in relative paths)
input_dir = "./host-trajectories/"
output_dir = "./output-trajectories/"

# [default input]
input_trajectory_file = "host_traj.xyzv"

# List of models to be taken into account by the propagator
# Example: if Earth, Jupiter and Venus are the desired planets to choose, 
# 'tototata' as the unknown body and solar radiation as the perturbation, 
# one has list_models = ["earth", "jupiter", "saturn", "tototata", "srp"]
list_models = ["earth", "mars", "srp"]

# List of foreground celestial bodies to be taken into account by system
# to get ephemerides with respect to Spacecraft position
list_foreground_objects = ["jupiter", "saturn", "uranus"]

# List of bodies to be considered, if selected in the models, from PyKEP 
# library
pykep_bodies = ["mercury", "venus", "earth", 
		"mars", "jupiter", "saturn", 
		"uranus", "neptune", "pluto"]

# Unknown bodies attributes
# Gravitational parameter, mu, of unknown bodies in (m³/s²)
# Equatorial radius of unknown bodies in (m)
# Unknown bodies ephemerides files in (string)
# Example: if "tototata" is the unknown body's name, then one must have:
# "tototata":{"mu":'value', "radius":'value', "traj_file":"string"}

unknown_bodies = {"didymos": {"mu":35.351,
                              "radius":1500.0,
                              "traj_file":"da_traj.xyzv"}
                 }

# List of non-gravitational perturbations undergone by the spacecraft
# srp = solar radiation pressure 
# (in the future, following models could be added in list_perturbations: 
# "magnetic_field", "aerodynamic_drag", "plasma_radiation")
list_perturbations = ["srp"]

# Propagator type
# Choose between classical Runge-Kutta4 or Runge-Kutta-felburg with time
# step sampling method (eg: propagator_type = "rkf45_module")
# "rk4_module" = classical Runge-Kutta4
# "rkf45_module" = Runge-Kutta-felburg with sampling
propagator_type = "rk4_module"

# Propagator attributes:
# step_number (no unit), time_step (in day), time_step_min (in day),
# time_step_max (in day), tolerance (no unit) 
# and 0.8 <= safty_factor <= 0.9
propagator_attributes = {"step_number":60,
                         "time_step":1./4,
                         "time_step_min":0.25 / 64,
                         "time_step_max":0.25 * 64,
                         "tolerance":1.0E-6,
                         "safty_factor":0.8408}

# Spacecraft features
# mass (in kg), area (in m²) and 0 <= refl <= 2 (refl = reflectivity)
spacecraft = {"mass":4.0,
              "area":1200E-4,
              "refl":1.5}

# Solar Radiation Pressure parameters
# solar_pression (in N/m²) and solar_flux (in W/m²)
solar = {"pression":4.57E-6,
         "flux":1367.0}

# VTS format headers for the reference trajectory output files
traj_vts_headers = [
    "CIC_OEM_VERS = 2.0\n", 
    "ORIGINATOR   = C²ERES\n",
    "Date         = ", tm.strftime("%d-%B-%Y %H:%M:%S\n"),  
    "\n",
    "OBJECT_NAME  = BIRDY\n", 
    "OBJECT_ID    = CORPS\n", 
    "\n",
    "CENTER_NAME  = SUN\n", 
    "REF_FRAME    = ECLIPTICJ2000\n"
    "TIME_SYSTEM  = UTC\n", 
    "\n", 
    "META_START\n", 
    "\n",
    "COLUMN #01   : Day of the date in (MJD)\n",
    "COLUMN #02   : Fractional seconds in the day (in seconds)\n",
    "COLUMN #03   : X  axis of the Spacecraft (in km)\n",
    "COLUMN #04   : Y  axis of the Spacecraft (in km)\n",
    "COLUMN #05   : Z  axis of the Spacecraft (in km)\n",
    "COLUMN #06   : Vx axis of the Spacecraft (in m/s)\n",
    "COLUMN #07   : Vy axis of the Spacecraft (in m/s)\n",
    "COLUMN #08   : Vz axis of the Spacecraft (in m/s)\n",
    "COLUMN #09   : Ax axis of the Spacecraft (in m/s²)\n",
    "COLUMN #10   : Ay axis of the Spacecraft (in m/s²)\n",
    "COLUMN #11   : Az axis of the Spacecraft (in m/s²)\n",
    "COLUMN #12   : The radii of the Spacecraft from the Sun (in km)\n",
    "\n", 
    "META_STOP\n", 
    "\n" ]

# VTS format headers for the reference ephemerides output files
eph_vts_headers = [
    "CIC_OEM_VERS = 2.0\n", 
    "ORIGINATOR   = C²ERES\n",
    "Date         = ", tm.strftime("%d-%B-%Y %H:%M:%S\n"),  
    "\n" ]
eph_vts_headers_next = [
    "\n",
    "CENTER_NAME  = SUN\n",
    "REF_FRAME    = ECLIPTICJ2000\n",
    "TIME_SYSTEM  = UTC\n",
    "\n",
    "META_START\n",
    "\n",
    "COLUMN #01   : Day of the date in (MJD)\n",
    "COLUMN #02   : Fractional seconds in the day (in seconds)\n",
    "COLUMN #03   : Latitude  of the target body (in degree)\n",
    "COLUMN #04   : Longitude of the target body (in degree)\n",
    "COLUMN #05   : The radii of the target body (in km)\n",
    "\n",
    "META_STOP\n",
    "\n" ]

