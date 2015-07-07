"""closestPair.py - A script to find the two closest points in metric space
by Giovanni Prinzivalli"""

def closest_pair(coordinates):
    """Takes a list of tuples of identical size as input.
       Returns the two tuples that are closest."""
    try:
        if len(coordinates) < 2:
            raise ValueError("Must have at least two sets of coordinates to find the closest pair.")

        for vals in coordinates:
            if len(vals) != len(coordinates[0]):
                raise ValueError("All coordinate pairs must be of the same size.")

        #Find n-dimensional Pythagorean value for each pair of coordinates. We'll cap it at 3 dimensions for sanity's sake.
        #Log the smallest pair.
        pass
    except TypeError:
        print "Non-number coordinates can't be calculated.

if __name__ == "__main__":
    pass
