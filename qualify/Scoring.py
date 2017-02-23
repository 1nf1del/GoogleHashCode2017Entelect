# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:48:02 2017

@author: michael.nunes
"""

import numpy as np

def output(aArray):
    f = open('output.out', 'w')
    length = len(aArray)
    f.write(str(length)+"\n")
    for i in xrange(length):
        f.write(str(i) + " "  + " ".join(map(str,aArray[i][1]))+'\n')
        
        print str(i) + " " + " ".join(map(str,aArray[i][1]))+'\n'
    f.close()