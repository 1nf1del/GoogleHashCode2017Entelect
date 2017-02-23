"""
Created on Mon Feb 20 19:25:07 2017

@author: jp.strydom
"""

import Validation as V
import IO as IO

test_in = "test.in"
videoSizes, endpoints, requests, cachesCount, capacity = IO.ReadFile(test_in)

from operator import itemgetter
print requests
requests = sorted(requests,key=itemgetter(2), reverse=true)
print requests

print "Done"
