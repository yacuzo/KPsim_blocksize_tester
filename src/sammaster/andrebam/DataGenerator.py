'''
Created on Sep 6, 2013

@author: andrebam
--bathymetry_no=6
--water_elevation_no=5
--nx=100
--ny=100
--dx=1
--dy=1
--total_time=5
'''
import subprocess #subprocess.call([path, arg, arg ...])

class DataGenerator(object):
    kp_args = ["--bathymetry_no=6", "--water_elevation_no=5", "--nx=500", "--ny=500", "--dx=1", "--dy=1, --total_time=2"]
    path = ""

    def __init__(self, _path):
        self.path = _path
        
    def callLoop(self):
        print [self.path].append(self.kp_args)