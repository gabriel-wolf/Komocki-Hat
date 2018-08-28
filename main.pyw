import tkinter as tk
import random
from random import shuffle
from tkinter import *
import io


class StudentList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        global classname, studentnames, students, filename
        filename = "Spanish 2.txt"
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



        self.create_widgets()


    def create_widgets(self):
        global students, classname, studentnames, filename
        self.buttonAddClass = tk.Button(self, text = "Add Class").grid(row = 0, column = 0)
        self.buttonChooseClass = tk.Button(self, text = "Choose Class").grid(row = 0, column = 1)
        self.labelClassName = tk.Label(self, textvariable = classname).grid(row = 1, column = 0, columnspan = 2)
        x = [[students] for students in range(len(students))]
        shuffle(x)
        r = 3
        for c in students:
            num = r-2
            # self.labelStudentList = tk.Label(text=).grid(row=r,column=0, sticky = W)
            self.labelStudentList = tk.Label(text=str(num) + ".   " + c).grid(row=r,column=0, columnspan = 2, sticky = W)
            r = r + 1
        self.buttonShuffle = tk.Button(self, text = "Shuffle").grid(row = len(students)+1, column = 0)
        self.buttonDraw = tk.Button(self, text = "Draw").grid(row = len(students)+1, column = 1)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)
    studentList.grid()
    studentList.config()
    root.mainloop()
