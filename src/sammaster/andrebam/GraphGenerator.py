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
    data = []
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
    
    def surfgraph(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        max_x = max(self.x)
        min_x = min(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        xi = np.linspace(min_x, max_x, max_x - min_x + 1)
        yi = np.linspace(min_y, max_y, max_y - min_y + 1)
        xy, yx = np.meshgrid(xi, yi)
        zi = griddata((self.x, self.y), self.times, (xy, yx), method='linear')
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
        d2_times = np.transpose(np.reshape(np.array(self.times), (max_x - min_x +1, -1)))
        print d2_times
        im = plt.imshow(d2_times, interpolation='nearest', cmap=cm.hot, origin="lower", aspect='auto')
        plt.xlabel('x')
        plt.ylabel('y')
        im.set_extent([min_x - 0.5,max_x + 0.5,min_y-0.5,max_y+0.5])
        plt.colorbar(im,orientation='vertical', shrink=0.8)
        plt.show()
        
    
        
gen = GraphGenerator("test.csv")
gen.readfile()
gen.simplegraph()