#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    a_dictionary.pop(key, None)
    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}

    # Test case 1
    new_dict = simple_delete(a_dictionary, 'track')
    print("--")

    # Test case 2
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
