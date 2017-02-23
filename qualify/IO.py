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

    endpoints = np.zeros((2, endpointCount), dtype=object )

    for e in xrange(endpointCount):
        latency, connected = np.array(f.readline().split(' '), dtype=int)
        endpoints[0, e] = latency
        tempArray = np.zeros((2, connected))
        for c in xrange(connected):
            cacheID, cacheLatency = np.array(f.readline().split(' '), dtype=int)
            tempArray[0, c] = cacheID
            tempArray[1, c] = cacheLatency

        endpoints[1, e] = np.array(tempArray)
        #tempArray
        print endpoints


    requests = [ # video, endpoint, count
        np.array(f.readline().split(' '), dtype=int).tolist() for r in xrange(requestCount)
    ]

    #requests = requests[requests[:,2].argsort()]

    return videoSizes, endpoints, requests, cachesCount, capacity
