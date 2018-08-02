#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random


def main():
    print "Searching for minimum number . . ."
    get_minimum_number()

def get_minimum_number():
    """Function to get a minimum number from randomly generated list of numbers"""
    list_of_nums = random.sample(range(1000), 500)
    print "Minimum number in the list of 500 randomly generated numbers is: {0}".format(min(list_of_nums))


if __name__=="__main__":
    main()
