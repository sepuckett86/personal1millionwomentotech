import copy
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

def make_continent(indices, pre_world):
    """
    Input: Starting land point indices in (i,j) format and world array in [[],[],[]] format
    Output: Continent indices list, world array with continent as 0s
    """
    # Next line necessary to not write over original world
    world = copy.deepcopy(pre_world)
    continent = []
    indices_to_check = set([(indices)])
    while len(indices_to_check) > 0:
        # Check each member of set
        indices_list = list(indices_to_check)
        for x in range(len(indices_list)):
            # Define x and y for this point
            i = indices_list[x][0]
            j = indices_list[x][1]
            # Add to continent list
            continent.append((i,j))
            # Set to 0 on world board
            world[i][j] = 0
            # Remove point from set to check
            indices_to_check.remove((i, j))
            # Check neighbors
            neighbors = [
                (i-1, j-1), (i-1, j+0), (i-1, j+1),
                (i+0, j-1), (i+0, j+0), (i+0, j+1),
                (i+1, j-1), (i+1, j+0), (i+1, j+1)]
            for y in range(len(neighbors)):
                 test_i = neighbors[y][0]
                 test_j = neighbors[y][1]
                 # Make sure indices not off edge of world
                 if test_i >= 0 and test_i < len(world):
                     if test_j >= 0 and test_j < len(world[0]):
                         water_or_land = world[test_i][test_j]
                         if water_or_land == 1:
                             # Add point to indices_to_check
                             indices_to_check.add((test_i, test_j))

    return (continent, world)

def find_land(pre_world):
    """
    Input: world array
    Output: continent dictionary, world array with unexplored continents
    (should be all zeros)
    """
    # Next line necessary to not write over original world
    world = copy.deepcopy(pre_world)
    continents = {}
    continent_number = 1
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == 1:
                continent, world = make_continent((i,j), world)
                continents[continent_number] = continent
                continent_number += 1
    return (continents, world)

def calculate_size(continent_dictionary):
    """
    Input: continent dictionary with points as values
    Output: continent dictionary with sizes as values
    """
    new_dict = {}
    for key, value in continent_dictionary.items():
        newvalue = len(value)
        new_dict[key] = newvalue
    return new_dict

def label_world(pre_world, continent_dictionary):
    """
    Input: original world array with ones and zeros
    Output: discovered world array with each continent labeled by number
    """
    # Next line necessary to not write over original world
    world = copy.deepcopy(pre_world)
    for key, value in continent_dictionary.items():
        for x in range(len(value)):
            i = value[x][0]
            j = value[x][1]
            world[i][j] = key
    return world

def tile_info(i, j, world):
    """
    Input: world[i][j] point and world
    Output: A bunch of info about the world and where you are
    """
    continents, new_world = find_land(a_world)
    sizes = calculate_size(continents)
    discovered_world = label_world(world, continents)

    if world[i][j] == 0:
        print(' ')
        print('Discovered World:')
        # Prints ordered world board
        print(*discovered_world, sep='\n')
        print(' ')
        print("Your tile info: (row ", i+1, ", column ", j+1, ")")
        print(' ')
        print("You are swimming in water.")
        print(' ')
        print("Your world contains ", len(continents), " continent(s).")
        print(' ')
        print("Here are their sizes:")
        for k,v in sorted(calculate_size(continents).items()):
            print(k, v, "units")
        print(' ')
    if discovered_world[i][j] != 0:
        print(' ')
        print('Discovered World:')
        # Prints ordered world board
        print(*discovered_world, sep='\n')
        print(' ')
        print("Your tile info: (row ", i+1, ", column ", j+1, ")")
        print(' ')
        print("You are on sturdy ground.")
        print(' ')
        print("You are in continent ", discovered_world[i][j], ".")
        print("Your world contains ", len(continents), " continent(s).")
        print(' ')
        print("Here are their sizes:")
        for k,v in sorted(calculate_size(continents).items()):
            print(k, v, "units")
        print(' ')

##### END FUNCTIONS #####


# Define size of world
rows = 9
columns = 9


# Makes a world board
a_world = generate_world(rows, columns)
print(' ')
print('Original World:')
print(*a_world, sep='\n')

# Generate random point
i = randint(0, rows-1)
j = randint(0, columns-1)

# Find out about random point
tile_info(i, j, a_world)



# print('World:')
# Prints ordered world board
# print(*a_world, sep='\n')

# continents, new_world = find_land(a_world)
# print(' ')
# print('Continent Dictionary:')
# for k,v in sorted(continents.items()):
#     print(k, v)

# print(' ')
# print('Size Dictionary:')
# for k,v in sorted(calculate_size(continents).items()):
#     print(k, v)

# print(' ')
# print('Discovered World:')
# Prints ordered world board
# print(*label_world(a_world, continents), sep='\n')

# print(' ')
