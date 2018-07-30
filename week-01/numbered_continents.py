def look_up(row, col, array):
    """
    Outputs value in array location (row,col)
    """
    result = array[row, col]
    return result

def numbered_continents(world):
    """
    Input: water and land array 'world' containing water (0) and land (1)
    Output: same array, but now continents are numbered

    Example:
    [1, 1, 1]
    [0, 0, 0]
    [0, 1, 0]

    Becomes:
    [1, 1, 1]
    [0, 0, 0]
    [0, 2, 0]
    """
    row_check = 0
    col_check = 0
    continent_number = 1
    numbered_array = []
    for i in range(len(world[0])):
        new_row = []
        if world[row_check][col_check] == 0:
            col_check++
            new_row.append(0)
        if world[row_check][col_check] == 1:
            new_row.append(continent_number)


    return numbered_array

# Idea: make array the size of original world with all values null.
# Systematically check all values in array.
# If null, check if 0 or 1 in original array.
# If not null, skip it.

def continent_dictonary(world):
    """
    Input: continent world array
    Output: dictionary with continent as key and array positions as values
    """
    # Make empty array of world size
    test_array = [[None]*len(world[0])]*len(world)

    # Make dictionary
    continent_dictionary = {}

    # Assign starting continent number
    continent_number = 1

    # Cycle through each member of test_array
    # Cycle through rows (up/down)
    for i in range(len(world)):
        # Cycle through columns (left/right)
        for j in range(len(world[0])):
            while test_array[i][j] != 0:
                # Possibilities:
                # 1) We haven't checked spot before
                if test_array[i][j] == None:
                    if world[i][j] == 0:
                        test_array[i][j] = 0
                    else if world[i][j] == 1:
                        test_array[i][j] = 1
                # 2) We checked it and it's land
                if test_array[i][j] == 1:
                    # Add to continent dictionary
                    continent_dictionary[continent_number] = [(i, j)]
                    # Check all surrounding tiles
                    # surrounding_indices =
                    #     [[(i-1, j+1), (i+0, j+1), (i+1, j+1)],
                    #      [(i-1, j+0), (i+0 ,j+0), (i+1, j+0)],
                    #      [(i-1, j-1), (i+0, j-1), (i+1, j-1)]]
                    surrounding_indices_list =
                        [(i-1, j+1), (i+0, j+1), (i+1, j+1),
                         (i-1, j+0), (i+0 ,j+0), (i+1, j+0),
                         (i-1, j-1), (i+0, j-1), (i+1, j-1)]
                    for x in range(len(surrounding_indices_list)):
                        test_i = surrounding_indices_list[x][0]
                        test_j = surrounding_indices_list[x][1]
                        if test_i >= 0 and test_i < len(test_array):
                            if test_j >= 0 and test_j < len(test_array[0]):
                                check = world[test_i][test_j]
                                # If it's land
                                if check == 1:
                                    # Add to continent dictionary
                                    continent_dictionary[continent_number] = continent_dictionary[continent_number].append((test_i, test_j))



# from world_generator.py
from random import randint
def generate_world(row, col):
     """
     Create a random world board of 'row' and 'col' integers.
     Each tile has water (0) or land (1)
     """
     board = []
     for x in range(row):
         new_row = []
         for y in range(col):
             zero_or_one = randint(0, 1)
             new_row.append(zero_or_one)
         board.append(new_row)

     return board

# Makes a world board
world = generate_world(4, 4)

# Prints ordered world board
print(*world, sep='\n')
#
