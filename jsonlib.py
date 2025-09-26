
import json as j
import os

def read_file(filename):
    #opens filename given and returns what is in the file
    with open(filename, 'r') as f:
         return j.load(f)


def write_file_dict(filename, key, value=None):
    if value is None:
        value = key

    #only works with files that hold 1 dict
    #if the file had anything in it
    if not is_json_file_empty_by_size(filename):
        # retreives the dict on the file
        dict = read_file(filename)
        #if the key given doesnt exist in the dict on the file
        if key not in list.key():
            #add the data to the list
            dict[key] = {"username":value}
    #if the file doesnt have anything on it
    elif is_json_file_empty_by_size(filename):
        #make a dict and make the only thing in it the key:value
        dict = {key: {"username":value}}
    else:
        print('is_json_file_empty_by_size has returned something other than a boolean to write_file_list')
        return TypeError
    #save the list var to the file given
    with open(filename, 'w') as f:
        j.dump(dict, f)
        return True

def is_json_file_empty_by_size(filepath):
    """Checks if a file is empty by its size."""
    try:
        if os.path.getsize(filepath) == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return True

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        j.dump(data, f)