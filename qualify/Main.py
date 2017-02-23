"""
Created on Mon Feb 20 19:25:07 2017

@author: jp.strydom
"""

import Validation as V
import IO as IO
from operator import itemgetter

import numpy as np

test_in = "test.in"
videoSizes, endpoints, requests, cachesCount, capacity = IO.ReadFile(test_in)

requests = sorted(requests, key=itemgetter(2), reverse=True)

caches = [(100, [])]*cachesCount

def getMaxCapacity(caches):
    return max(zip(*caches)[0])


while True:
    if len(requests) <= 0:
        break # Storage space left
    req = requests.pop(0)
    videoId = req[0]
    videoSize = videoSizes[videoId]

    endpId = req[1]
    endp = endpoints[endpId]
    serverLatencies = sorted(endp[1], key=itemgetter(1)) # cacheId, cacheLatency
    serverDetails = [caches[s[0]] for s in serverLatencies]

    if videoSize > getMaxCapacity(serverDetails):
        continue

    found = False
    for s in serverLatencies:
        if videoId in caches[s][1]:
            found = True
            break
    if found:
        continue

    for s in serverLatencies:
        sid = s[0]
        cacheObj = caches[sid]
        if cacheObj[0] > videoSize:
            cacheObj[0] -= videoSizes
            cacheObj[1].append(videoId)
            break















print "Done"
