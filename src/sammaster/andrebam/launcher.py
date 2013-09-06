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
from sammaster.andrebam import *

if __name__ == '__main__':
    
    from optparse import OptionParser
    usage = "usage: %prog [var=value]"
    p = OptionParser(usage)
    p.add_option("--kpPath", type="string", help="path to kp executable with '' - '~/SW-GPU/bin/kp'")
    (opts, args) = p.parse_args()
    if opts.kpPath == None:
        print "Missing --kpPath argument"
        exit()
    else:
        kpPath = opts.kpPath
    
    gen = DataGenerator(kpPath)
    gen.callLoop()
    