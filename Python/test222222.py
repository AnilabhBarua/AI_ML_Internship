import numpy as np
from matplotlib import pyplot as plt

data = [10, 386, 479, 627, 20, 523, 482, 483, 542, 699, 535, 637, 331, 617, 577, 471, 615, 583, 441, 562, 63, 527, 453, 530, 579, 433, 541, 585, 615, 704, 443, 569, 430, 511, 552, 496, 484, 566, 554, 72, 335, 440, 341, 545, 548, 604, 439, 556, 442, 461, 624, 611, 444, 578, 405, 487, 90, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414, 665, 63, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 123, 363, 711, 543]

print("Original List:\n", data)

elements = np.array(data)

mean = np.mean(elements)
std = np.std(elements)

print("Mean:", mean)
print("Standard Deviation:", std)

#for Plotting a Histogram
plt.hist(elements, bins=[0, 100, 200, 300, 400, 500, 600, 700, 800])
plt.title("Histogram")
plt.show()

# Identify outliers
cut_off = std * 3
lower, upper = mean - cut_off, mean + cut_off

outliers = [x for x in elements if x < lower or x > upper]
print("Number of identified outliers:", len(outliers))

# Creating a Dataset without outliers
final_list = [x for x in data if lower <= x <= upper]
final_array = np.array(final_list)

# Plotting a Histogram without outliers
plt.hist(final_array, bins=[0, 100, 200, 300, 400, 500, 600, 700, 800])
plt.title("Histogram")
plt.show()
