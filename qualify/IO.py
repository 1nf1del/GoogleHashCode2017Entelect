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

    endpoints = np.zeros((endpointCount, 2), dtype=object )

    for e in xrange(endpointCount):
        latency, connected = np.array(f.readline().split(' '), dtype=int)
        endpoints[e, 0] = latency
        tempArray = np.zeros((connected, 2 ), dtype=int)
        for c in xrange(connected):
            cacheID, cacheLatency = np.array(f.readline().split(' '), dtype=int)
            tempArray[c, 0] = cacheID
            tempArray[c, 1] = cacheLatency

        endpoints[e, 1] = tempArray


    requests =  [# video, endpoint, count
        np.array(f.readline().split(' '), dtype=int) for _ in xrange(requestCount)
    ]

    return videoSizes, endpoints, requests, cachesCount, capacity
