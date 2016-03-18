#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 14/03/2016
#Nima
#

import config
import date
import position 
import velocity
import trajectory_parser 

if __name__ == '__main__':

    host_traj = trajectory_parser.TrajectoryParser()
    t = date.Date()
    pos = position.Position()
    vel = velocity.Velocity()
    with open(config.input_dir + config.host_trajectory_file) as input_file:
        #t, pos.position_vector, vel.velocity_vector = host_traj.parse_trajectory(input_file)
	t.dates, pos.x, pos.y, pos.z, vel.vx, vel.vy, vel.vz = host_traj.parse_trajectory(input_file)	

    print "z: ", pos.z
    print "vx: ", vel.vx
    print "v: ", vel.velocity_vector
    print "z: ", pos.position_vector

    
