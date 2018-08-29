import tkinter as tk
import random
from tkinter import messagebox
from random import shuffle
from tkinter import *
import io
from tkinter.ttk import Separator, Style


class StudentList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        global classname, studentnames, students, filename
        ### need to setup way to choose different class lists
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
        classname = filename[:len(filename) - 4]
        print(classname)



    def create_widgets(self):

        #global students, classname, studentnames, filename

        self.labelClassName = tk.Label(self, text = classname).grid(row = 0, column = 0, columnspan = 2)
        self.buttonAddClass = tk.Button(self, text = "Add Class").grid(row = 1, column = 0)
        self.buttonChooseClass = tk.Button(self, text = "Choose Class").grid(row = 1, column = 1)
        self.buttonDraw = tk.Button(self, text = "Draw", command = self.start_draw).grid(row = 2, column = 0, columnspan = 2, sticky = E+W)
        self.labelHeaderStudentList = tk.Label(self, text="#   Name").grid(row=3,column=0, columnspan = 2, sticky = W)
        sep = Separator(self, orient="horizontal").grid(row = 4, column = 0, columnspan = 2, sticky = E+W)
        sty = Style(self)
        sty.configure("TSeperator", fg = "black")
        r = 5
        numstudents = len(students)
        random.shuffle(students)
        for i in range(len(students)-1, -1, -1):
            num = r-4
            self.labelStudentList = tk.Label(self, text=str(num) + ".   " + students[r-5]).grid(row=r,column=0, columnspan = 2, sticky = W)
            numstudents = numstudents - 1
            r = r + 1
            if students[i] == 0:
                students.pop(i)
        self.buttonShuffle = tk.Button(self, text = "Shuffle", command = self.create_widgets).grid(row = r+1, column = 0, columnspan = 2, sticky = E+S+W)


    def start_draw(self):
        t = tk.Toplevel(self)
        t.resizable(True,True)
        t.grid()
        t.config()
        t.wm_title("Draw")
        l = tk.Label(t, text="IT WORKS!").grid(row = 0, column = 0)
        r = 3
        numstudents = len(students)
        random.shuffle(students)
        for i in range(len(students)-1, -1, -1):
            num = r-2
            labelStudentList2 = tk.Label(t, text=str(num) + ".   " + students[r-3]).grid(row=r,column=0, columnspan = 2, sticky = W)
            numstudents = numstudents - 1
            r = r + 1
            if students[i] == 0:
                students.pop(i)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)
    studentList.grid()
    studentList.config()
    root.mainloop()
