#Script to open txt file and build list of lines in that file

def parseFile(curr_list):
    """Open text file of currencies and compile into list object""" 
    with open(curr_list) as f:
        currencies = f.read().splitlines()
    return currencies