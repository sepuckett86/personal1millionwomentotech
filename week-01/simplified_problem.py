# Take a list of ones and zeros. Determine the number of consecutive ones starting
# on the first index that has a one.
#

my_list = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0]


def make_continent(index, my_list):
    continent = []
    while my_list[index] != 0:
        # Add index to continent
        continent.append(index)
        # Change to 0 in my_list
        my_list[index] = 0
        # Deal with end of list
        if index < len(my_list) - 1:
            index += 1
    return (continent, my_list)

def all_continents(my_list):
    continents = {}
    continent_number = 1
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continent, my_list = make_continent(i, my_list)
            print(my_list)
            continents[continent_number] = continent
            continent_number += 1
    return continents

print(all_continents(my_list))
