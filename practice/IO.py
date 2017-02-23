"""
Created on Mon Feb 20 17:23:05 2017

@author: jp.strydom
"""

import numpy as np

def ReadFile(fileName):

    f = open(fileName, 'r')
    
    line = np.array(f.readline().split(' '), dtype=int)
    height, width, ingredientMin, ingredientMax = line 
    
    array = np.zeros([height, width], dtype=int)
    
    for h, line in enumerate(f):
        for w, element in enumerate(line):
            if element != "\n":
                array[h, w] = (element == 'T')*2 - 1
    
    return array, ingredientMin, ingredientMax