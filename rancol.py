from __future__ import print_function

import fixpath

from colorama import init, Fore, Back, Style

import math

import random

init()

print("")

width = int(input("How many squares do you want across the page? "))

print("")

lines = int(input("How many squares do you want down the page? "))

print("")

# print(Back.GREEN + 'G', end=' ')
# print(Back.RESET + "")


# I would like to have a master list of colours, which can be chosen from.
# Then, I would like to have a current chosen list.

master_colour_list = ["Red",
                      "Green",
                      "Blue",
                      "Black",
                      "Yellow",
                      "Magenta",
                      "Cyan",
                      "White"]
# Range of colours

colour_list = []
# Temporarily filling this list, but it should be empty,
# and added to according to user input.


# Something not working here.

print("The next set of questions determines the colours you want.")

print("")

print("Write y or n to each colour choice.")

print("")

allyesorno = input("Would you like all 8 colours, Red, Green, Blue, Black, Yellow, Magenta, Cyan, White? (y/n) ")

print("")

if allyesorno == "y" or allyesorno == "Y":

    colour_list = master_colour_list

else: 

    for colour in master_colour_list:

        yesorno = input("Would you like " + colour + "? (y/n) ")

        if yesorno == "y" or yesorno == "Y":

            colour_list.append(colour)

print("")

size = len(colour_list)

print(colour_list)

print("")

weighting = int(input("What weighting would you like to use ? (1-10) "))

print("")

random_colour_sequence_lists = []
# This keeps all of the lines of data

# I would also like to look at other variations of how it creates the pattern.
# At this point, it starts top left, moves to the right, then down a row.
# So each time, it can only look left or above for colours that effect the 
# weighted randomisation.
# Possible variations might include:
# - Starting from any of the corners, then giving the order of directions.
# - Starting from the centre.
# - Working in a spiral fashion, from centre, or from a corner.

for m in range(lines):
    
    random_colour_sequence = []
    # This keeps all of the data for one line.

    for n in range(width):

        if m == 0 and n == 0:

            random_colour = random.choice(colour_list)

            random_colour_sequence.append(random_colour)

        elif m == 0:

            current_colour_list = colour_list

            # current_colour_list.append(random_colour_sequence[n - 1])

            current_colour_list += weighting * [random_colour_sequence[n - 1]]

            # print(current_colour_list)

            random_colour = random.choice(current_colour_list)

            random_colour_sequence.append(random_colour)

            for n in range(weighting):

                current_colour_list.pop(size)

            # print(current_colour_list)

        elif n == 0:

            current_colour_list = colour_list

            current_colour_list += weighting * [random_colour_sequence_lists[m - 1][n]]

            # print(current_colour_list)

            random_colour = random.choice(current_colour_list)

            random_colour_sequence.append(random_colour)

            for n in range(weighting):

                current_colour_list.pop(size)

            # print(current_colour_list)

        else:

            current_colour_list = colour_list

            current_colour_list += weighting * [random_colour_sequence[n - 1]]

            current_colour_list += weighting * [random_colour_sequence_lists[m - 1][n]]

            # print(current_colour_list)

            random_colour = random.choice(current_colour_list)

            random_colour_sequence.append(random_colour)

            for n in range(weighting):

                current_colour_list.pop(size)

            # print(current_colour_list)

            for n in range(weighting):

                current_colour_list.pop(size)

            # print(current_colour_list)

    random_colour_sequence_lists.append(random_colour_sequence)


for colour_line in range(len(random_colour_sequence_lists)):

    for colour in range(len(random_colour_sequence_lists[colour_line])):

        if random_colour_sequence_lists[colour_line][colour] == "Red":

            print(Back.RED + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "Green":

            print(Back.GREEN + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "Blue":

            print(Back.BLUE + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "Black":

            print(Back.BLACK + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "Yellow":

            print(Back.YELLOW + ' ', end=' ')
            
        elif random_colour_sequence_lists[colour_line][colour] == "Magenta":

            print(Back.MAGENTA + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "Cyan":

            print(Back.CYAN + ' ', end=' ')

        elif random_colour_sequence_lists[colour_line][colour] == "White":

            print(Back.WHITE + ' ', end=' ')
            
        # print(random_colour_sequence_lists[colour_line][colour], end=" ")

    print(Back.RESET + "")

print("")

