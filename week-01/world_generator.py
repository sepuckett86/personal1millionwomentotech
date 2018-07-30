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
world = generate_world(3, 5)

# Prints ordered world board
print(*world, sep='\n')
print(' ')
print (world[0][1])
