#Program 3 Python Code for Cutlier Detection and Removal using Standard Deviation

#Import the libraries

import numpy as np

from matplotlib

import

pyplot as plt

defata=[10, 386, 479,627,20,523,482,483, 542,699,535, 637, 331617, 577, 471,615, 583, 441, 562,63, 527, 453,530, 579,433, 541,585, 615,704, 
443, 569, 430,, 511, 552,496, 484, 566,554,72, 335, 440,341, 545,548, 604, 439, 556,442, 461,624,611,444, 578, 405,487,90, 496, 398,
 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414, 665,63, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 
 492, 476, 437, 483, 12 363, 711, 543]

print("original List \n", data)

elements= np.array(data)

mean- np.mean (elements)

std=np.std (elements)

np.array(elements)

#For plotting a Histogram

plt.hist (a, bins = [0, 100, 200, 300, 400, 500, 600, 700, 800])

plt.title("histogram")

plt.show()

#Identify outliers

cut_off_std * 3

Lower, upper =mean-cut_off, mean + cut_off

outliers= [x for x in a if x < lower or x> upper] 
print ("No of Identified outliers: %d len (outliers))

Creating a Dataset without outliers

Sinal list = [x for x in data if (x> lower) and (x < upper)]

== np.array(final list)

For plotting a Histogram

blt.hist (a, bins [0, 100, 200, 300, 400, 500, 600, 700, 8001)

olt.title("histogram")

plt.show()

Activate Windows

Go