# Return the (slope, y_intercept) of a line which passes through
# the most 2D points. Input is an unordered collection of 2D points.
# Points are just tuples. You can simply return a tuple of (slope, y_int)
# representing the line equation of interest.
#
# Time complexity: O(N^2) == N choose 2 where N = # of coordinate points
# Space complexity: O(N^2) => Each pair of points form a unique line equation, so
# counter object stores N^2 tuples of (slope, y_int)

from collections import Counter
from itertools import permutations


def max_intercepting_points(points):
	pairs = permutations(points, 2)
	line_equations = Counter()

	for pair in pairs:
		# Compute slope and y_intercept, then store in Counter
		slope_num = pair[0][1] - pair[1][1]
		slope_denom = pair[1][0] - pair[1][0]

		slope = slope_num / slope_denom

		# y = mx + b => b = -mx / y

		y_int = (-slope * pair[0][0]) / pair[0][1]

		line_equations[(slope, y_int)] += 1

	return line_equations.most_common(1)[0]
