# work_hours_gui.py

from datetime import datetime
from tkinter import *

root = Tk()

# create master frame with title
master = Frame(root, width=768, height=576)
root.title("Work Hours GUI")
master.pack()


# create date string
d = datetime.today()
date = d.strftime("%Y-%m-%d")


# create labels and entries
label_add = Label(master, text="Add Hours? ")
label_add.grid(row=0)
entry_add = Entry(master)
entry_add.grid(row=0, column=1)

label_sub = Label(master, text="Subtract Hours? ")
label_sub.grid(row=1)
entry_sub = Entry(master)
entry_sub = entry_sub.grid(row=1, column=1)

label_notes = Label(master, text="Add Notes? ")
label_notes.grid(row=2)
entry_notes = Entry(master)
entry_notes.grid(row=2, column=1)

label_show_hours = Label(master, text="Total Hours: ")
label_show_hours = label_show_hours.grid(row=3)
entry_show_hours = Entry(master)        #this needs to be changed to Text()
entry_show_hours.grid(row=3, column=1)  #this needs to be changed to Text()

# text.delete(0.0, END)
# text.insert(0.0, message)




master.mainloop()
