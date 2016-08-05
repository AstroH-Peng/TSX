#usr/bin/env python
# -*- coding:utf-8 -*-
#Modified date: 01/08/2016
# Nima

# Trajectory Solver instances file for propagating trajectories.
# All variables (ojbects or any parameters) declared or created in the configuration
# file must be passed in this file. Thus, global variables in the configuration file
# should not be present anywhere.

import config
import ref_eph
import ref_traj
import tensor_constructor
from model_tensor.gravitational import bodies
from model_tensor.gravitational import sphr
from model_tensor.non_gravitational import srp
from propagator import rk4_module
from propagator import rkf45_module
from traj_builder import builder
from tools import spacecraft

# Instance of class AccelConstructor
tensor_constructor = tensor_constructor.AccelConstructor(config.list_models, \
                     config.list_perturbations)

# Instance of the propagators
if "rk4_module" == config.propagator_type:
    # Instance of class PropagatorRk4
    propagator = rk4_module.PropagatorRk4(tensor_constructor)
if "rkf45_module" == config.propagator_type:
    # Instance of class PropagatorRkf45
    propagator = rkf45_module.PropagatorRkf45(tensor_constructor, \
                 config.propagator_attributes["time_step_min"], \
                 config.propagator_attributes["time_step_max"], \
                 config.propagator_attributes["tolerance"], \
                 config.propagator_attributes["safty_factor"])

# Instance of class Builder
builder = builder.Builder(propagator, config.propagator_attributes["step_number"], \
          config.propagator_attributes["time_step"], \
          config.input_dir + config.input_trajectory_file)

# Class attributes for the class SphericalBody
sphr.SphericalBody.pykep_bodies = config.pykep_bodies
sphr.SphericalBody.unknown_bodies = config.unknown_bodies

# Class attributes for the class UnKnownBody
bodies.UnKnownBody.input_dir = config.unknown_bodies_input_dir

# Class attributes for the class RadiationPressure
srp.RadiationPressure._pression = config.solar["pression"]
srp.RadiationPressure._flux = config.solar["flux"]

# Class attributes for the class Spacecraft
spacecraft.Spacecraft._mass = config.spacecraft["mass"]
spacecraft.Spacecraft._area_exposed_to_sun = config.spacecraft["area"]
spacecraft.Spacecraft._reflectivity = config.spacecraft["refl"]

# Instance of class TrajOutput
ref_traj = ref_traj.TrajOutput(config.output_dir, config.traj_vts_headers)

# Instance of class EphOutput
ref_eph = ref_eph.EphOutput(config.list_foreground_objects, config.output_dir, \
          config.eph_vts_headers, config.eph_vts_headers_next)
