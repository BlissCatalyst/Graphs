# Write a function that takes a D binary array and returns the number of 1 islands
# An island consists of 1s that are connected to the north, south, east or west.
# For example:

# islands =
# [[0, 1, 0, 1, 0],
# [1, 1, 0, 1, 1],
# [0, 0, 1, 0, 0],
# [1, 0, 1, 0, 0],
# [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# Vocab map:
# ls - nodes/vertexes
# NSEW neighbors - edges
# binary array - this is the graph
# groups/connected/islands - connected components

# One sentence plan
# if we think of the matrix as a graph
# we can loop through it
# and do a breadth first search on each 1
# and mark all of the ones we've found
# and skip the ones we've already visited
# and count how many times we do this
# the result will be the number of connected components
# or islands

# ** NOT PART OF ASSIGNMENT **
