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

        print("INIT")
        global classname, studentnames, students, filename, groupnums, numstudents, content, classNameVar, defaultClassName, classlists, allClassesList
        self.happened = 1
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

        groupnums = 2
        classlist = open(filename, mode='r+')
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

        self.variable = tk.StringVar()
        self.variable.set(classname)

        classNameVar = StringVar()
        classNameVar.set(classname)

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


        names_draw = tk.Label(t, text = "John Joe Mary", width = 25).grid(sticky = N+W, row = 0, column = 0, columnspan = 10, rowspan = 4)

        labelHeaderStudentList = tk.Label(t, text="#   Name", width = 20).grid(row=0,column=9, columnspan = 4, sticky=W)
        sep = Separator(t, orient="horizontal").grid(row = 1, column = 9, columnspan = 8, sticky = E+W)
        sep2 = Separator(t, orient="vertical").grid(row = 0, column = 9, rowspan = 8, sticky = N+S)
        sty = Style(t)
        sty.configure("TSeperator", fg = "black")
        r = 3
        grouplabelsrepeat = groupnums - 1
        numstudents = len(students)
        random.shuffle(students)

        studentlabelstringvar1 = StringVar()
        groupsub = groupnums - 1
        groupsub2 = groupnums - 1
        def chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i+n]
        print(list(chunks(students, groupnums)))
        numgrounps = len(list(chunks(students, groupnums)))
        groupsub3 = numgrounps - 1
        labelendlist = range(0,numgrounps+1)

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
                        tk.Label(t, text=new_label_value, width = 30).grid(row=r+1,column=10, columnspan = 4, sticky=W)

                except IndexError:
                    print('', end = '', flush = True)
                groupsub2 = groupsub2 - 1
                r = r + groupnums
            num = num + 1
            groupsub3 = groupsub3 - 1
            groupsub2 = groupnums - 1


        sep3 = Separator(t, orient="horizontal").grid(row = r+2, column = 0, columnspan = 20, sticky = E+W)

        drawnamesButton = tk.Button(t, text = "Draw Groups", command = self.start_draw).grid(row = r+3, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Komocki Hat")
    root.resizable(True,True)
    studentList = StudentList(root)

    studentList.grid()
    studentList.config()
    root.mainloop()
