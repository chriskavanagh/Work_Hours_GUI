from datetime import datetime
from Tkinter import *
import sqlite3, sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# map classes to tables through Base Class
Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    

# create engine for Session connection
engine = create_engine('sqlite:///database_sqlalchemy.db')

# create all tables in engine ('CREATE TABLE' in raw SQL)
Base.metadata.create_all(engine)

# create configured 'Session' class
Session = sessionmaker(bind=engine)

# create session
session = Session()


class GUI:
    def __init__(self, parent):
        self.parent = parent
        frame = Frame(parent)
        frame.pack(expand=YES, fill=BOTH)

        name_label = Label(frame, text="Enter Name:")
        name_label.grid(row=0, sticky=W)

        age_label = Label(frame, text="Enter Age:")
        age_label.grid(row=1, sticky=W)
        
        
        name_var = StringVar()
        e1 = Entry(frame, textvariable=name_var)
        e1.grid(row=0, column=1)

        #name_var.set("Enter Name Please?") # use Label instead
        #s = name_var.get()

        age_var = StringVar()
        e2 = Entry(frame, textvariable=age_var)
        e2.grid(row=1, column=1)

        #age_var.set("Enter Age Please?")   # use Label instead
        #s2 = age_var.get()

        add_button = Button(frame, text="Add")
        add_button.grid(row=2, column=2)

        quit_button = Button(frame, text="Quit")
        quit_button.grid(row=2, column=3)
        


root = Tk()
#root.geometry("350x400")
root.title("Work-Hours-GUI")
mygui = GUI(root)
root.mainloop()


##
##from datetime import datetime
##from tkinter import *
##
##root = Tk()
##
### create master frame with title
##master = Frame(root, width=768, height=576)
##root.title("Work Hours GUI")
##master.pack()
##
##
### create date string
##d = datetime.today()
##date = d.strftime("%Y-%m-%d")
##
##
### create labels and entries
##label_add = Label(master, text="Add Hours? ")
##label_add.grid(row=0)
##entry_add = Entry(master)
##entry_add.grid(row=0, column=1)
##
##label_sub = Label(master, text="Subtract Hours? ")
##label_sub.grid(row=1)
##entry_sub = Entry(master)
##entry_sub = entry_sub.grid(row=1, column=1)
##
##label_notes = Label(master, text="Add Notes? ")
##label_notes.grid(row=2)
##entry_notes = Entry(master)
##entry_notes.grid(row=2, column=1)
##
##label_show_hours = Label(master, text="Total Hours: ")
##label_show_hours = label_show_hours.grid(row=3)
##entry_show_hours = Entry(master)        #this needs to be changed to Text()
##entry_show_hours.grid(row=3, column=1)  #this needs to be changed to Text()
##
### text.delete(0.0, END)
### text.insert(0.0, message)
##
##
##
##
##master.mainloop()
