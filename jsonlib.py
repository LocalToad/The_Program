
import json as j
import os

def read_file(filename):
    #opens filename given and returns what is in the file
    with open(filename, 'r') as f:
        return j.load(f)


def write_file_list(filename, data):
    #only works with files that hold 1 list

    #if the file had anything in it
    if not is_json_file_empty_by_size(filename):
        # retreives the list on the file
        list = read_file(filename)
        #if the data given doesnt exist in the list on the file
        if data not in list:
            #add the data to the list
            list.append(data)
    #if the file doesnt have anything on it
    elif is_json_file_empty_by_size(filename):
        #make a list and make the only thing in it the data
        list = [data]
    else:
        print('is_json_file_empty_by_size has returned something other than a boolean to write_file_list')
    #save the list var to the file given
    with open(filename, 'w') as f:
        j.dump(list, f)

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