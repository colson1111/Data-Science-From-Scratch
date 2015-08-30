from __future__ import division
import numpy as np
from collections import Counter
import LinearAlgebraFunctions as alg
import math

num_friends = np.random.poisson(5, 1000)
num_friends = [20 * nf_i for nf_i in num_friends]

daily_minutes = np.random.poisson(10, 1000)
daily_minutes = [15 * dm_i for dm_i in daily_minutes]

# number of points
num_points = len(num_friends)

# largest value
largest_value = max(num_friends)
smallest_value = min(num_friends)

# specific positions
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


# MEASURES OF CENTRAL TENDENCY

# mean
def mean(x):
    return sum(x) / len(x)
    
# median
def median(v):
    """ finds the middle most value of v """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

# quantile
def quantile(x, p):
    """ returns the pth-percentile value in x """
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# mode
def mode(x):
    """ returns a list, might be more than one mode """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() 
        if count == max_count]
       
    
# MEASURES OF DISPERSION
# range
def data_range(x):
    return max(x) - min(x)

# variance
def de_mean(x):
    """ translate x by subtracting its mean (so the result has mean 0) """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
    
def variance(x):
    """ assumes x has at least two elements """
    n = len(x)
    deviations = de_mean(x)
    return alg.sum_of_squares(deviations) / (n - 1)

# standard deviation
def standard_deviation(x):
    return math.sqrt(variance(x))

# inter quartile range
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


# CORRELATION

def covariance(x, y):
    n = len(x)
    return alg.dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is 0


