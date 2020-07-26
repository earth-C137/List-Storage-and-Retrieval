"""
A small module I made to save lists to files for future use.
There are two classes and multiple methods.
"""

# The pickle module can only be used in python.
import pickle
# So you can use the more universal json format.
import json


class StoreList():
# This class requires one argument, a list, on creation.
    def __init__(self, list):
        self.list = list

# Now you can send it to any file in any method as many times as you want.
# Just use a file path as file name.
# The file_name must be entered as a string.
# file_name example: '/home/user/Desktop/example_list.txt'

#***Single line, aka iterator loop.
    def simplesend(self, file_name):
        with open('{}'.format(file_name), 'a+') as filehandle:
            for listitem in self.list:
                filehandle.write('%s\n' % listitem)

#***Multi line
    def multisend(self, file_name):
        with open('{}'.format(file_name), 'a+') as filehandle:
            filehandle.writelines("%s\n" % place for place in self.list)

#***Python only pickle module.
# Typically use a .pickle extension.
    def pklsend(self, file_name):
        with open('{}'.format(file_name), 'wb') as filehandle:
            # Store the data as binary data stream.
            pickle.dump(self.list, filehandle)

#***JSON format, very universal.
    def jsend(self, file_name):
        with open('{}'.format(file_name), 'w') as filehandle:
            json.dump(self.list, filehandle)

# Seperated store and retrieve
# because it would use the same list and cause problems.
# Now you can retrieve anyway as a one liner right to a list or print.
class GetList():

#***Single line
    def simpleretrieve(file_name):
        list = []
        # Open file and read the content in a list.
        with open('{}'.format(file_name), 'r') as filehandle:
            for line in filehandle:
                # Remove linebreak which is the last character of the string.
                currentPlace = line[:-1]
                # Add item to the list.
                list.append(currentPlace)
        return(list)

#***Multi line
    def multiretrieve(file_name):
        # Define empty list.
        list = []
        # Open file and read the content in a list.
        with open('{}'.format(file_name), 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                # Remove linebreak which is the last character of the string.
                current_place = line[:-1]
                # Add item to the list.
                list.append(current_place)
        return(list)

#***Pythonic aka one liner.
    def pythonicmultiretrive(file_name):
        list = []
        # Open file and read the content in a list.
        with open('{}'.format(file_name), 'r') as filehandle:
            list = [
                current_place.rstrip()
                for current_place in filehandle.readlines()
                ]
        return(list)

#***Python only pickle module
# Typically use .pickle extension.
    def pklretrieve(file_name):
        list = []
        with open('{}'.format(file_name), 'rb') as filehandle:
            # Read the data as binary data stream.
            list = pickle.load(filehandle)
        return(list)

#***JSON format, very universal.
    def jretrieve(file_name):
        list = []
        # Open output file for reading.
        with open('{}'.format(file_name), 'r') as filehandle:
            list = json.load(filehandle)
        return(list)
