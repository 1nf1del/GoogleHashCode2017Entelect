"""
Created on Mon Feb 20 17:23:05 2017

@author: jp.strydom
"""

import numpy as np

def ReadFile(fileName):

    f = open(fileName, 'r')

    line = np.array(f.readline().split(' '), dtype=int)
    videos, endpoints, requests, caches, capacity = line
    
    videoSizes = np.array(f.readline().split(' '), dtype=int)

    for e in xrange(endpoints):
        latency, connected = np.array(f.readline().split(' '), dtype=int)
        for c in xrange(connected):
            pass

    for r in xrange(requests):
        count, video, endpoint = np.array(f.readline().split(' '), dtype=int)
        pass
    
    return array, ingredientMin, ingredientMax