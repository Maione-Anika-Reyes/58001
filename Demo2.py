from tkinter import *
win = Tk()
win.geometry("400x100")
win.title("Grid Manager")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=0,column=0)
txt1.insert(0,"row 0 " "column 0")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=0,column=1)
txt1.insert(0,"row 0 " "column 1")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=0,column=2)
txt1.insert(0,"row 0 " "column 2")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=1,column=0)
txt1.insert(0,"row 1 " "column 0")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=1,column=1)
txt1.insert(0,"row 1 " "column 1")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=1,column=2)
txt1.insert(0,"row 1 " "column 2")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=2,column=0)
txt1.insert(0,"row 2 " "column 0")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=2,column=1)
txt1.insert(0,"row 2 " "column 1")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=2,column=2)
txt1.insert(0,"row 2 " "column 2")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=3,column=0)
txt1.insert(0,"row 3 " "column 0")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=3,column=1)
txt1.insert(0,"row 3 " "column 1")

txt1 = Entry(win, bd=2,justify="center")
txt1.grid(row=3,column=2)
txt1.insert(0,"row 3 " "column 2")

win.mainloop()