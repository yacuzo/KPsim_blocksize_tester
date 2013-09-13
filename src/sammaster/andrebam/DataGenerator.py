'''
Created on Sep 6, 2013

@author: andrebam
--bathymetry_no=6
--water_elevation_no=5
--nx=500
--ny=500
--dx=1
--dy=1
--total_time=2
'''
import commands #subprocess.call([path, arg, arg ...])
import csv
import subprocess
from sammaster.andrebam import CommandTimeout

class DataGenerator(object):
    kp_args = ["--bathymetry_no=6", "--water_elevation_no=5", "--nx=500", "--ny=500", "--dx=1", "--dy=1", "--total_time=2"]
    run_kp = None
    args = ""
    path = ""
    exe = ""
    timeout = 10
    max_dim = 16

    def __init__(self, _path, _exe):
        self.path = _path
        self.exe = _exe
        self.args = [self.path + self.exe] + self.kp_args
        self.run_kp = CommandTimeout.Command(self.args)

    def generate(self):
        print "Running kp with args: "+" ".join(self.args)
        for x in range(10, self.max_dim):
            for y in range(10, self.max_dim):
                #Change macros through cmake
                cmake_str = "cmake -DKPSIMULATOR_FLUX_BLOCK_WIDTH="+str(x)+" -DKPSIMULATOR_FLUX_BLOCK_HEIGHT="+str(y)
                print ("Running CMAKE..."),
                cmake_output = subprocess.check_output(cmake_str, shell=True, stderr=subprocess.STDOUT, cwd=self.path)                
                #Run exec and save results
                print("Running make..."),
                make_output = subprocess.check_output("make", shell=True, stderr=subprocess.STDOUT, cwd=self.path)
                print ("Running with block size: " + str(x) + "*" + str(y) +"..."),
                sub_process = self.run_kp.run(self.timeout)
                #status, output = commands.getstatusoutput(" ".join(self.args))
                if sub_process.returncode != 0:
                    print "Run timed out!"
                    self.writeData(-1, sub_process.ret_o, x, y)
                else:
                    print "Done!"
                    self.writeData(sub_process.returncode, sub_process.ret_o, x, y)
                
        
        print "Data generation done!"
    
    def writeData(self, status, output, x,  y):
        csvfile = open("test.csv", "ab")
        datawriter = csv.writer(csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL) 
        
        if status != -1:
            lines = output.split("\n")
            time_taken = lines[-4][14:22]
        else:
            time_taken = self.timeout
        
        datawriter.writerow([x, y, status, time_taken])
        csvfile.close()
        
        
        '''command = Command("echo 'Process started'; sleep 2; echo 'Process finished'")
command.run(timeout=3)
command.run(timeout=1)'''  