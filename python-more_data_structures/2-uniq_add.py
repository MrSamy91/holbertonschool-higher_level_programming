#!/usr/bin/python3

# maj

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Add each element of the list to the set (duplicates will be ignored)
    for element in my_list:
        unique_integers.add(element)

    # Sum all unique integers and return the result
    return sum(unique_integers)
