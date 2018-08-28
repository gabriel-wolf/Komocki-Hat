import tkinter as tk
from tkinter import *
import io


def main(filename):
    global classname, studentnames
    classlist = open(filename, mode='r+')
    classname = filename[:len(filename) - 4]
    print(classname)
    students = classlist.readlines()


    # print out list of students
    i = 0

    try:
        while i >= 0:
            num = int(i) + 1
            print(str(num) + ". " + students[i])
            i = i + 1
    except IndexError:
        print()





main("Spanish 2.txt")
