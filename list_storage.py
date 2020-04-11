"""
A small module I made to save lists to files for future use.
There are two classes and multiple methods.
"""

#The pickle module can only be used in python.
import pickle
#So you can use the more universal json format.
import json


class StoreList():
#This class requires one argument, a list, on creation.
    def __init__(self, list):

        self.list = list

#Now you can send it to any file in any method as many times as you want.
#Just use a file path as file name.  The extension is already added.
#The file_name must be entered as a string.
#file_name example: '/home/user/Desktop/example_list'

    #***single line
    def simplesend(self, file_name):
        with open('{}.txt'.format(file_name), 'w') as filehandle:
            for listitem in self.list:
                filehandle.write('%s\n' % listitem)

    #***multi line
    def multisend(self, file_name):
        with open('{}.txt'.format(file_name), 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in self.list)

    #***python only pickle module
    def pklsend(self, file_name):
        with open('{}.data'.format(file_name), 'wb') as filehandle:
            # store the data as binary data stream
            pickle.dump(self.list, filehandle)

    #***json format, very universal
    def jsend(self, file_name):
        # open output file for writing
        with open('{}.txt'.format(file_name), 'w') as filehandle:
            json.dump(self.list, filehandle)

            
#Store and retrieve are seperate because it would use the same list and cause problems.
#Now you can retrieve anyway as a one liner right to a list or print.
class GetList():
    #Same deal with file name, pass in as a string file path, extension added automatically.
    #***single line
    def simpleretrieve(file_name):
        list = []
        # open file and read the content in a list
        with open('{}.txt'.format(file_name), 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentPlace = line[:-1]
                # add item to the list
                list.append(currentPlace)
        return(list)
    #***multi line
    def multiretrieve(file_name):
        # define empty list
        list = []
        # open file and read the content in a list
        with open('{}.txt'.format(file_name), 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                # remove linebreak which is the last character of the string
                current_place = line[:-1]
                # add item to the list
                list.append(current_place)
        return(list)
    #pythonic aka one liner
    def pythonicmultiretrive(file_name):
        list = []
        # open file and read the content in a list
        with open('{}.txt'.format(file_name), 'r') as filehandle:
            list = [current_place.rstrip() for current_place in filehandle.readlines()]
        return(list)
    #***python only pickle module
    def pklretrieve(file_name):
        list = []
        with open('{}.data'.format(file_name), 'rb') as filehandle:
            # read the data as binary data stream
            list = pickle.load(filehandle)
        return(list)
    #***json format, very universal
    def jretrieve(file_name):
        list = []
        # open output file for reading
        with open('{}.txt'.format(file_name), 'r') as filehandle:
            list = json.load(filehandle)
        return(list)
