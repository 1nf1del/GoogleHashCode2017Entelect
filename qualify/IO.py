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
        array = np.array(f.readline().split(' '), dtype=int)
        latency, connected = array
        for c in xrange(connected):
            np.array(f.readline().split(' '), dtype=int)

    requests = []
    for r in xrange(requestCount):
        arr = np.array(f.readline().split(' '), dtype=int)
        count, video, endpoint = arr
        pass


    
    return videoSizes, endpoints, requests, cachesCount, capacity