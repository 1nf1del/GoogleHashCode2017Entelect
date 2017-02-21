"""
Created on Mon Feb 20 19:25:07 2017

@author: jp.strydom
"""

import Validation as V
import IO as IO

array, ingredientMin, ingredientMax = IO.ReadFile("small.in")
print array, ingredientMin, ingredientMax, "\n"

print array[1:3, 4:6], "\n"

print V.checkArray(array[1:3, 4:6], ingredientMin, ingredientMax)