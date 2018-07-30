# How to determine the number and sizes of continents?
# How to input a location and determine size of continent?
#
# Example board:
# [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1]
# [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
# [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
# [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0]
# [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
# [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
# [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
# [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
# [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
# [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
#
# If a tile is on the edge, the edges count as water.
# Diagonal land tiles are connected.

# Start simple
#
# 3x3 board
# 2 continents, size 3 and 1
# [1, 1, 1]
# [0, 0, 0]
# [0, 1, 0]
#
# Systematic way to go through it
#
# Start at row 1, column 1 (location 0, 0).
# If 0, skip to (0, 1).
# If 1, check neighbors in row, store locations.
#
# Goal:
# Array with continents numbered
# [1, 1, 1]
# [0, 0, 0]
# [0, 2, 0]
#
# Use array to calculate size list:
# [5, 3, 1]
#
# Function to search array with row and column index and return size
