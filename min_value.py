#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 18th, 2023
# This program generates 10 random numbers
# then finds and displays the minimum of those numbers
import constants
import random


def find_min(some_list_of_int):
    # Initialize the minimum
    minimum = 100

    # Use for in to find the min
    for a_num in some_list_of_int:
        if a_num < minimum:
            minimum = a_num

    # Return the min number
    return minimum


def main():
    # Create empty list
    list_of_int = []

    # Use a for loop to generate all of the random numbers and populate the array
    for counter in range(0, constants.ARRAY_SIZE):
        list_of_int.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        print(
            "{} added to the list at position {}.".format(list_of_int[counter], counter)
        )

    # Function call
    minimum = find_min(list_of_int)

    # Display the min
    print("")
    print("The min number is {}.".format(minimum))


if __name__ == "__main__":
    main()
