'''
Created on Sep 6, 2013

@author: andrebam
'''
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.interpolate import griddata

class GraphGenerator(object):
    '''
    classdocs
    '''
    data = np.array()
    file = None
    x = []
    y = []
    status = []
    times = []

    def __init__(self, csvfile):
        '''
        Constructor
        '''
        self.file = csvfile
    
    def readfile(self):
        with open(self.file, "r") as f:
            reader = csv.reader(f, delimiter=",", quotechar="'")
            for row in reader:
                self.data.append(row)
                self.x.append(int(row[0]))
                self.y.append(int(row[1]))
                self.status.append(int(row[2]))
                self.times.append(float(row[3]))
    
    def makegraph(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xi = np.linspace(min(self.x), max(self.x))
        yi = np.linspace(min(self.y), max(self.y))
        xy, yx = np.meshgrid(xi, yi)
        zi = griddata((self.x, self.y), self.times, (xy, yx), method='cubic')
        surf = ax.plot_surface(xy, yx, zi, rstride=1, cstride=1, cmap=cm.copper,
        linewidth=0, antialiased=False)
        
        plt.show()
       
    def simplegraph(self):
        plt.figure(1)
        plt.clf()
        max_x = max(self.x)
        min_x = min(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        print "max_x: " + str(max_x)
        print np.reshape(np.array(self.times), (max_x - min_x +1, -1))
        im = plt.imshow(np.reshape(self.times, (max_x - min_x +1, -1)), interpolation='bilinear', origin='lower', cmap=cm.gray, extent=(min_x,max_x,min_y,max_y))
        plt.show()
        
gen = GraphGenerator("test.csv")
gen.readfile()
gen.makegraph()