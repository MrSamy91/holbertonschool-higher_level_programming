#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    
    # Test case 1
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print("--")
    
    # Test case 2
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
