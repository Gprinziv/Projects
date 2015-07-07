"""closestPair.py - A script to find the two closest points in metric space
   by Giovanni Prinzivalli"""

from itertools import combinations
from math import sqrt

def closest_pair(coordinates):
    """Takes a list of tuples of identical size as input.
       Returns the two tuples that are closest."""
    try:
        if len(coordinates) < 2:
            raise ValueError("Must have at least two sets of coordinates to find the closest pair.")

        shortest = (coordinates[0], coordinates[1])
        shdist = find_dist(shortest)
        for pair in combinations(coordinates, 2):
            if len(pair[0]) != len(pair[1]):
                raise ValueError("All coordinate pairs must be of the same size.")

            distance = find_dist(pair)
            if distance < shdist:
                shortest = pair
                shdist = distance

        return shortest

    except TypeError:
        print "Non-number coordinates can't be calculated."

def find_dist(pair):
    """Subfunction to find the distance between two tuples of coordinates.
       Assumes a and b have the same size"""
    a = pair[0]
    b = pair[1]
    dist = 0.00
    for i in range(0, len(a)):
        dist += pow(a[i] - b[i], 2)

    return sqrt(dist)

if __name__ == "__main__":
    print "closestPair.py testing. I got lazy on actually trying this."
    point_a = (0, 0)
    point_b = (4, 4)
    point_c = (3, 4)
    point_d = (2, 2)

    print closest_pair([point_a, point_b, point_c, point_d])
