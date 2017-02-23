"""
Created on Mon Feb 20 17:23:05 2017

@author: jp.strydom
"""

import numpy as np

def ReadFile(fileName):

    f = open(fileName, 'r')

    line = np.array(f.readline().split(' '), dtype=int)
    videoCount, endpointCount, requestCount, cachesCount, capacity = line
    
    videoSizes = np.array(f.readline().split(' '), dtype=int)

    endpoints = []
    for e in xrange(endpointCount):
        latency, connected = np.array(f.readline().split(' '), dtype=int)
        for c in xrange(connected):
            pass

    requests = []
    for r in xrange(requestCount):
        count, video, endpoint = np.array(f.readline().split(' '), dtype=int)
        pass


    
    return videoSizes, endpoints, requests, cachesCount, capacity