#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os


def main():
    print "Splitting file contents program"
    output_file_contents()

def output_file_contents():
    """Function to split file lines and make an output"""
    file_path = "f1.txt"

    is_file_exists(file_path)

    # Open file and read each line it has
    for line in open(file_path, 'r').readlines():
        # Making iteratable object and split lines using requested separator
        for line_num, whole_line in enumerate(line.split('– ')):
            for substring_num, after_dash in enumerate(whole_line.split(', ')):
                print str(after_dash)

def is_file_exists(path):
    """Function to verify whether file exists or not
               :param path - path to file to open
               :raise OSError
    """

    if os.path.isfile(path):
          print "Current file exists: {0} . You can work with it".format(path)

    else:
        raise OSError(
            "Your file does not exist, please, create one or make sure path to file is correct: {0}".format(path))

if __name__=="__main__":
    main()
