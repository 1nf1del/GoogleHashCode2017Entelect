"""
Created on Mon Feb 20 19:25:07 2017

@author: jp.strydom
"""

import Validation as V
import IO as IO
from operator import itemgetter
import random

import numpy as np
import Scoring as Sc

test_in = "trending_today.in"
videoSizes, endpoints, requests, cachesCount, capacity = IO.ReadFile(test_in)

def sorter(r):
    count = r[2]
    endp = endpoints[r[1]]
    ld = endp[0]
    serverLatencies = sorted(endp[1], key=itemgetter(1))
    return count * (ld - serverLatencies[0][1])
requests = sorted(requests, key=sorter, reverse=True)


def getMaxCapacity(l):
    return max(zip(*l)[0])


caches = [[100, []] for _ in xrange(cachesCount)]

while True:
    if len(requests) <= 0:
        break  # Storage space left
    req = requests.pop(0)
    videoId = req[0]
    videoSize = videoSizes[videoId]

    endpId = req[1]
    endp = endpoints[endpId]
    serverLatencies = sorted(endp[1], key=itemgetter(1))  # cacheId, cacheLatency
    if len(serverLatencies) == 0:
        continue
    serverDetails = [caches[s[0]] for s in serverLatencies]

    if videoSize > getMaxCapacity(serverDetails):
        continue

    found = False
    for s in serverLatencies:
        if videoId in caches[s[0]][1]:
            found = True
            break
    if found:
        continue

    ids = random.shuffle(range(0, len(serverLatencies)))

    for i in ids:
        s = serverLatencies[i]
        sid = s[0]
        cacheObj = caches[sid]
        if cacheObj[0] > videoSize:
            cacheObj[0] = cacheObj[0] - videoSize
            cacheObj[1].append(videoId)
            break

Sc.output(caches)

print "Done"
