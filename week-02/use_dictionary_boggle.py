# Load
my_dict = np.load('my_dictionary.npy').item()

board = [['a', 'c', 'e', 'z'],
         ['s', 'n', 'r', 'o'],
         ['p', 'e', 'e', 't'],
         ['p', 'a', 'h', 's']]

def check_neighbors():
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
