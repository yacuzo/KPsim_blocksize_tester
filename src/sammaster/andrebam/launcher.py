'''
Created on Sep 6, 2013

@author: andrebam
'''

'''
Program flow:
Take argument, path to KPSImulator
Start DataGenerator (which runs kp with different blocksizes)
run GraphGenerator to produce 3d plot of block.x block.y and time taken to run.
'''
#from sammaster.andrebam import *
from sammaster.andrebam import DataGenerator
import os.path

if __name__ == '__main__':
    
    from optparse import OptionParser
    usage = "usage: %prog [var=value]"
    p = OptionParser(usage)
    p.add_option("--dirPath", type="string", help="path to program dir - '/home/user/SW-GPU/'")
    p.add_option("--exePath", type="string", help="subpath of dirPath to executable - 'bin/kp'")
    (opts, args) = p.parse_args()

    if opts.dirPath == None:
        print "Missing --dirPath argument"
        exit()
    if opts.exePath == None:
        print "Missing --exePath argument"
        exit()
    
    print "checking paths"
    
    if os.path.isdir(opts.dirPath):
        print "dir found"
    else:
        print "Path "+opts.dirPath+" not found or not a dir!"
        exit()
        
    if os.path.isfile(opts.dirPath + opts.exePath):
        print "executable found"
    else:
        print "Executable "+opts.dirPath + opts.exePath+" not found!"
        exit()
    
    gen = DataGenerator.DataGenerator(opts.dirPath, opts.exePath)
    gen.generate()
    