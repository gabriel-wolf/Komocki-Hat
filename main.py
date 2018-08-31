import tkinter as tk
import random
from tkinter import messagebox
from random import shuffle
from tkinter import *
import io
from tkinter.ttk import Separator, Style

# TODO: have music with draw
# TODO: make draw name or something show up in top left box with joe john marry
# FIXME: make names stop just putting themselves on top of the previous ones
# TODO: have changeable groupnums

class StudentList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        global classname, studentnames, students, filename, groupnums, numstudents, content, classNameVar
        filename = "Example Class.txt"
        groupnums = 2
        classlist = open(filename, mode='r+')
        classname = filename[:len(filename) - 4]
        print(classname)
        space_students = classlist.readlines()
        students = []
        for i in space_students:
            students.append(i.strip())

        # print out list of students
        i = 0

        try:
            while i >= 0:
                num = int(i) + 1
                print(str(num) + ". " + students[i])
                i = i + 1
        except IndexError:
            print()

        classNameVar = StringVar()
        classNameVar.set(classname)

        self.create_widgets()

        classname = filename[:len(filename) - 4]
        classNameVar.set(classname)
        print(classname)



    def create_widgets(self):
        self.labelClassName = tk.Label(self, textvariable = classNameVar).grid(row = 0, column = 0, columnspan = 2)
        self.buttonAddClass = tk.Button(self, text = "Add Class", command = self.add_class_func).grid(row = 1, column = 0)
        self.buttonChooseClass = tk.Button(self, text = "Choose Class").grid(row = 1, column = 1)
        self.buttonDraw = tk.Button(self, text = "Draw", command = self.start_draw).grid(row = 2, column = 0, columnspan = 2, sticky = E+W)
        self.labelHeaderStudentList = tk.Label(self, text="#   Name").grid(row=3,column=0, columnspan = 2, sticky = W)
        sep = Separator(self, orient="horizontal").grid(row = 4, column = 0, columnspan = 2, sticky = E+W)
        sty = Style(self)
        sty.configure("TSeperator", fg = "black")

        r = 5
        random.shuffle(students)
        i = len(students)
        while i > 0:
            num = r -4
            self.labelStudentList = tk.Label(self, text=str(num) + ".   " + students[r-5])
            self.labelStudentList.grid(row=r,column=0, columnspan = 2, sticky = W)
            r = r + 1
            i = i - 1

        self.buttonShuffle = tk.Button(self, text = "Shuffle", command = self.create_widgets).grid(row = len(students)+5, column = 0, columnspan = 2, sticky = E+S+W)



    def add_class_func(self):
        def grabText(event):
            i = 0
            input = StudentsEntryBox.get("1.0",'end-1c')
            filename = str(ClassEntryBox.get())
            classname = filename
            classNameVar.set(classname)
            # # FIXME: make class name become text file name
            # # FIXME: have it create text file
            full_file_name = filename + ".txt"
            classlist = open(full_file_name, mode='w+')
            #classname = filename[:len(filename) - 4]
            classlist.write(input)
            classlist = open(full_file_name, mode="r+")
            space_students = classlist.readlines()
            oldstudents = []
            print(space_students[0])
            for j in space_students:
                oldstudents.append(j.strip())

            del students[:]
            try:
                while i >= 0:
                    students.append(oldstudents[i])
                    i = i + 1
            except IndexError:
                print()


            i = 0

            try:
                while i >= 0:
                    num = int(i) + 1
                    print(str(num) + ". " + students[i])
                    i = i + 1
            except IndexError:
                print()

            add_class.destroy()
            self.create_widgets()
            classname = filename
            classNameVar.set(classname)
            print(classname)


        add_class = tk.Toplevel()
        add_class.resizable(True,True)
        add_class.grid()
        add_class.config()
        #t.geometry('500x500')
        add_class.wm_title("Draw")
        label = tk.Label(add_class, text = "Class Name", justify = CENTER).grid(row = 0, column = 0, columnspan = 5, sticky = E+W)
        ClassEntryBox = Entry(add_class)
        ClassEntryBox.grid(row = 1, column = 0, columnspan = 5)
        StudentsEntryBox = Text(add_class, width = 20, height = 10)
        StudentsEntryBox.grid(row = 3, column = 0, columnspan = 5, rowspan = 7, sticky = N+E+S+W, padx = 1, pady = 5)
        grabBtn = Button(add_class, text = "Add Class")
        grabBtn.grid(row = 12, column = 1, columnspan = 3, sticky = E+W, padx = 1, pady = 1, ipadx = 1, ipady = 1)
        grabBtn.bind('<Button-1>', grabText)


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
        t.names_draw = tk.Label(t, text = "John Joe Mary", width = 25).grid(sticky = N+W, row = 0, column = 0, columnspan = 10, rowspan = 4)

        #Names = tk.Label(t, text = "ME ME ME!", justify = CENTER).grid(sticky = N+E+S+W)
        #frame.pack(fill=BOTH, side = BOTTOM, expand=True)


        #l = tk.Label(t, text="IT WORKS!").grid(row = 0, column = 0)
        t.labelHeaderStudentList = tk.Label(t, text="#   Name", width = 20).grid(row=0,column=9, columnspan = 4, sticky=W)
        t.sep = Separator(t, orient="horizontal").grid(row = 1, column = 9, columnspan = 8, sticky = E+W)
        t.sep2 = Separator(t, orient="vertical").grid(row = 0, column = 9, rowspan = 8, sticky = N+S)
        sty = Style(t)
        sty.configure("TSeperator", fg = "black")
        r = 1
        numstudents = len(students)
        random.shuffle(students)

        # FIXME: want every time press draw names to add one more line to the names list
        # FIXME: eventually want names being drawn to be shown where Joe John Mary is

        #drawnames()


        # def drawnames():
        try:
            num = r
            for i in range(int(len(students)/groupnums)-1, -1, -1):

                # FIXME: have align left for all
                t.labelStudentList = tk.Label(t, text=str(num) + ".   " + students[r-1] + " & " + students[r], width = 20).grid(row=r+1,column=10, columnspan = 4, sticky=W)
                # t.labelStudentList2 = tk.Label(t, text=" & ").grid(row=r,column=10)
                # t.labelStudentList3 = tk.Label(t, text=students[r]).grid(row=r,column=11)

                num = num + 1
                numstudents = numstudents - 1
                r = r + 2
                if students[i] == 0:
                    students.pop(i)
        except IndexError:
            print()

        t.sep3 = Separator(t, orient="horizontal").grid(row = r+2, column = 0, columnspan = 20, sticky = E+W)

        drawnamesButton = tk.Button(t, text = "Draw Names").grid(row = r+3, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)
    studentList.grid()
    studentList.config()
    root.mainloop()
