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
        global classname, studentnames, students, filename, groupnums, numstudents
        ### need to setup way to choose different class lists
        filename = "Spanish 2.txt"
        groupnums = 2
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
        #t.geometry('500x500')
        t.wm_title("Draw")

        # groupnums / len(students) + 1 = # r
        # chane of groupnums = run startdraw again
        # but what if starts drawing again? okay




        #t.frame = tk.Frame(t, relief=RAISED, borderwidth=1).grid(sticky = N+W, row = 0, column = 0, columnspan = 4, rowspan = 4)
        t.names_draw = tk.Label(t, text = "John Joe Mary", width = 20).grid(sticky = N+W, row = 0, column = 0, columnspan = 8, rowspan = 4)

        #Names = tk.Label(t, text = "ME ME ME!", justify = CENTER).grid(sticky = N+E+S+W)
        #frame.pack(fill=BOTH, side = BOTTOM, expand=True)


        #l = tk.Label(t, text="IT WORKS!").grid(row = 0, column = 0)
        t.labelHeaderStudentList = tk.Label(t, text="#   Name", width = 20).grid(row=0,column=8, columnspan = 4)
        t.sep = Separator(t, orient="horizontal").grid(row = 1, column = 8, columnspan = 8, sticky = E+W)
        sty = Style(t)
        sty.configure("TSeperator", fg = "black")
        r = 1
        numstudents = len(students)
        random.shuffle(students)

        # FIXME: want every time press draw names to add one more line to the names list
        # FIXME: eventually want names being drawn to be shown where Joe John Mary is

        drawnames()


        drawnamesButton = tk.Button(t, text = "Draw Names", command = drawnames).grid(row = r+1, column = 0)



        def drawnames():
            try:
                for i in range(int(len(students)/groupnums)-1, -1, -1):
                    num = r
                    t.labelStudentList = tk.Label(t, text=str(num) + ".   " + students[r-1] + " & " + students[r], width = 20).grid(row=r,column=8, columnspan = 4)
                    numstudents = numstudents - 1

                    if students[i] == 0:
                        students.pop(i)
            except IndexError:
                print()
            print("Hello")




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)
    studentList.grid()
    studentList.config()
    root.mainloop()
