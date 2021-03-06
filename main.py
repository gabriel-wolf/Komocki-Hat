import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import count, cycle
from tkinter import PhotoImage
from random import shuffle
from tkinter import *
from AnimatedGif import AnimatedGif
import base64
import io
from tkinter.ttk import Separator, Style


class StudentList(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        global classname, studentnames, students, filename, groupnums, content, classNameVar, classlists, allClassesList, entryb1
        # settings
        global gif_on
        global defaultClassName
        gif_on = True

        self.happened = 1
        groupnums = 2
        readDefaultClass = open("defaultClass.txt", mode='r+')
        space_filename = readDefaultClass.readlines()
        list_filename = []
        for k in space_filename:
            list_filename.append(k.strip())
        classname = str(list_filename[0])
        filename = classname + ".txt"
        ReadAllClasses = open("allclasses.txt", mode='r+')
        spaceAllClasses = ReadAllClasses.readlines()
        allClassesList = []
        for q in spaceAllClasses:
            allClassesList.append(q.strip())
        classlist = open(filename, mode='r+')

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

        # variables
        self.variable = tk.StringVar()
        self.variable.set(classname)
        classNameVar = StringVar()
        classNameVar.set(classname)

        # start main widgets creation
        self.create_widgets()



    def create_widgets(self):

        print(students[0])
        for widget in self.winfo_children():
            widget.destroy()

        print(students[0])

        self.labelClassName = tk.Label(self, textvariable = classNameVar).grid(row = 0, column = 0, columnspan = 2)
        self.buttonAddClass = tk.Button(self, text = "Add Class", command = self.add_class_func).grid(row = 1, column = 0)

        self.dropdownChooseClass = tk.OptionMenu(self, self.variable, *allClassesList, command = self.func)
        self.dropdownChooseClass.grid(row = 1, column = 1)

        self.buttonDraw = tk.Button(self, text = "Draw", command = self.start_draw).grid(row = 2, column = 0, columnspan = 2, sticky = E+W)
        self.labelHeaderStudentList = tk.Label(self, text="#   Name").grid(row=3,column=0, columnspan = 2, sticky = W)
        Separator(self, orient="horizontal").grid(row = 4, column = 0, columnspan = 2, sticky = E+W)
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


    def func(self,value):
        i = 0
        classname = value
        classNameVar.set(classname)
        filename = classname + ".txt"
        classlist = open(filename, mode='r+')
        print(classname)
        space_students = classlist.readlines()
        students_not = []
        for cocopuffs in space_students:
            students_not.append(cocopuffs.strip())

        del students[:]
        try:
            while i >= 0:
                students.append(students_not[i])
                i = i + 1
        except IndexError:
            print()

        ReadAllClasses = open("allclasses.txt", mode='r+')
        spaceAllClasses = ReadAllClasses.readlines()
        allClassesList = []
        for q in spaceAllClasses:
            allClassesList.append(q.strip())

        self.happened = 1
        self.create_widgets()


    def add_class_func(self):
        def grabText(event):
            i = 0
            input = StudentsEntryBox.get("1.0",'end-1c')
            filename = str(ClassEntryBox.get())
            classname = filename
            classNameVar.set(classname)
            full_file_name = filename + ".txt"

            with open("allclasses.txt", mode='r+') as classesFile:
                for line in classesFile:
                    if classname in line:
                        break
                    else:
                        classesFile.write(classname)

            classlist = open(full_file_name, mode='w+')
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
        add_class.wm_title("Draw")
        tk.Label(add_class, text = "Class Name", justify = CENTER).grid(row = 0, column = 0, columnspan = 5, sticky = E+W)
        ClassEntryBox = Entry(add_class)
        ClassEntryBox.grid(row = 1, column = 0, columnspan = 5)
        StudentsEntryBox = Text(add_class, width = 20, height = 10)
        StudentsEntryBox.grid(row = 3, column = 0, columnspan = 5, rowspan = 7, sticky = N+E+S+W, padx = 1, pady = 5)
        grabBtn = Button(add_class, text = "Add Class")
        grabBtn.grid(row = 12, column = 1, columnspan = 3, sticky = E+W, padx = 1, pady = 1, ipadx = 1, ipady = 1)
        grabBtn.bind('<Button-1>', grabText)



    def start_draw(self):
        def getgrounumsfunc(en):
            global groupnums
            content = groupnumsentry.get()
            print(content)
            groupnums = int(content)
            for widget in t.winfo_children():
                widget.destroy()

        global groupnums, entryb1
        print("groupnums: " + str(groupnums))


        entryb1 = StringVar
        if self.happened == 1 :
            print("starting initial draw")
            global t
            t = tk.Toplevel()
            t.resizable(True,True)
            t.grid()
            t.config()
            t.wm_title("Draw")
            self.happened = 0
        else:
            print()
            try:
                lbl_with_my_gif.stop()
            except UnboundLocalError:
                print("UnboundLocalError")



        tk.Label(t, text="#   Name").grid(row=0,column=5, columnspan = 4, sticky=W)
        Separator(t, orient="horizontal").grid(row = 1, column = 4, columnspan = 8, sticky = E+W)
        Separator(t, orient="vertical").grid(row = 0, column = 4, rowspan = 40, sticky = N+S)
        sty = Style(t)
        sty.configure("TSeperator", fg = "black")
        r = 3
        random.shuffle(students)
        studentlabelstringvar1 = StringVar()
        groupsub2 = groupnums - 1
        def chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i+n]
        print(list(chunks(students, groupnums)))
        numgrounps = len(list(chunks(students, groupnums)))
        groupsub3 = numgrounps - 1
        range(0,numgrounps+1)

        num = 1
        options = []

        for i in range(numgrounps):
            # for i in range(groupnums+1):
            new_label_value = str(num) + ". "
            print(str(num) + ". ", end = '', flush = True)
            for i in range(groupnums):
                try:
                    new_label_value = new_label_value + list(chunks(students, groupnums))[groupsub3][groupsub2]
                    print(list(chunks(students, groupnums))[groupsub3][groupsub2], end='', flush = True)
                    if groupsub2 != 0:
                        new_label_value = new_label_value + " & "
                        print(" & ", end = '', flush = True)
                    else:
                        options.append(new_label_value)
                        studentlabelstringvar1.set(new_label_value)
                        print("options: " + options[0])
                        print(new_label_value)
                        print(studentlabelstringvar1)
                        tk.Label(t, text=new_label_value).grid(row=r+1,column=5, columnspan = 4, sticky=W)

                except IndexError:
                    print('', end = '', flush = True)
                groupsub2 = groupsub2 - 1
                r = r + groupnums
            num = num + 1
            groupsub3 = groupsub3 - 1
            groupsub2 = groupnums - 1


        if gif_on == True:
            lbl_with_my_gif = AnimatedGif(t, 'danceStick.gif', 0.05)
            lbl_with_my_gif.grid(row=0,column=0,rowspan = r+1)
            lbl_with_my_gif.start_thread()
        else:
            print("Gif is not activated.")

        Separator(t, orient="horizontal").grid(row = r + 2, column = 0, columnspan = 20, sticky = E+W)
        Label(t, text = "Students per group: ").grid(row = r + 3, column = 8, sticky = E)
        groupnumsentry = Entry(t, text = groupnums, width = 5)
        groupnumsentry.grid(row = r+3, column = 9, sticky = W, padx = 10)
        tk.Button(t, text = "Draw Groups", command=lambda:[getgrounumsfunc(0),self.start_draw()]).grid(row = r+3, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)




if __name__ == '__main__':
    root = tk.Tk()

    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)
    studentList.grid()
    studentList.config()
    root.mainloop()
