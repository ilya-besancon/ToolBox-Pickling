"""
@ilya-besancon
A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import pickle
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    if (exists(file_name) is False) or reset is True:
        # initializes counter
        counter = 1
        # if file doesn't exist, creates new file with name: file_name
        fileObject = open(file_name, 'wb')
        # stores counter with value 1 in file
        pickle.dump(counter, fileObject)
    else:
        # allows for both reading and writing of file
        fileObject = open(file_name, 'rb+')
        # adds one to counter value
        counter = pickle.load(fileObject) + 1
        # returns to beginning of file:
        fileObject.seek(0, 0)
        # updates counter to new value
        pickle.dump(counter, fileObject)
    return counter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
