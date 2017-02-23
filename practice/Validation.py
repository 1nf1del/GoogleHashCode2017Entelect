"""
Created on Mon Feb 20 19:09:04 2017

@author: jp.strydom
"""

import numpy as np

def checkArray(alist, minVal ,maxVal):
    if((minVal*2) <= alist.size <= (maxVal*2)):
        return (0 <= sum(sum(alist)) <= maxVal - minVal)
    else: 
        return False