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
import commands #subprocess.call([path, arg, arg ...])
import fileinput

class DataGenerator(object):
    kp_args = ["--bathymetry_no=6", "--water_elevation_no=5", "--nx=500", "--ny=500", "--dx=1", "--dy=1", "--total_time=2"]
    path = ""
    max_dim = 5

    def __init__(self, _path):
        self.path = _path
        self.args = [self.path] + self.kp_args
        
    def callLoop(self):
        for x in range(self.max_dim):
            print "Running kp with args: "+" ".join(self.args)
            status, output = commands.getstatusoutput(" ".join(self.args))
            self.writeData(status, output)
            for line in fileinput.input("../../../configure (copy).h", inplace=True):
                if line.find("define KPSIMULATOR_FLUX_BLOCK_WIDTH") >= 0:
                    print "#define KPSIMULATOR_FLUX_BLOCK_WIDTH "+str(x)+"\n" ,
                else:
                    print line,
        
    
    def writeData(self, status, output):
        lines = output.split("\n")
        time_taken = lines[-3][14:22]
        print "Status: "+str(status)+" Time taken: "+time_taken
        