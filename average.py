#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on November 2020
# This program finds the average of a list


def list_average(marks):
    # This function finds the average of a list

    average = sum(marks) / len(marks)

    return average


def main():
    # This function receives input

    marks = []
    temp_mark = 0

    print("Please enter 1 mark at a time. Enter -1 to end.")
    print(" ")

    # Input
    temp_mark = int(input("What is your mark?: "))
    marks.append(temp_mark)
    while temp_mark != -1:
        temp_mark = int(input("What is your mark?: "))
        marks.append(temp_mark)

    marks.pop()  # Remove the "-1" that was added
    print(" ")

    # Call Functions
    average = list_average(marks)

    print("The average is {0:.0f}".format(average))


if __name__ == "__main__":
    main()
