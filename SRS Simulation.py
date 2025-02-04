#%% Preamble
import numpy as np
import matplotlib as plt
from fractions import Fraction as frac


#%% Setup
sample_rate = 100000 #ensure time is sampled at 10x frequency
x = np.linspace(0,100,sample_rate)

freq_range = (1e2,1e5)

oct_ratio = frac(1,6)
oct_points = [freq_range[0]]

while oct_points[-1] < freq_range[1]/10:
    point = oct_points[-1]*(2**oct_ratio)
    if point < freq_range[1]:
        oct_points.append(point)
