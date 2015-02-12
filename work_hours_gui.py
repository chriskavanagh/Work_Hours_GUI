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
        
        
        self.name_var = StringVar()
        e1 = Entry(frame, textvariable=self.name_var)
        e1.grid(row=0, column=1)
        

        self.age_var =  IntVar()
        e2 = Entry(frame, textvariable=self.age_var)
        e2.grid(row=1, column=1)
        

        add_button = Button(frame, text="Add", command=self.add_data)
        add_button.config(padx=5, pady=5)
        add_button.grid(row=2, column=2)

        quit_button = Button(frame, text="Quit", command=parent.destroy)
        quit_button.config(padx=5, pady=5)
        quit_button.grid(row=2, column=3)

    def add_data(self):
        name = self.name_var.get()
        age = self.age_var.get()
        new_person = Test(name=name, age=age)
        session.add(new_person)
        session.commit()
        session.close()
            
        


root = Tk()
#root.geometry("350x400")
root.title("Work-Hours-GUI")
mygui = GUI(root)
root.mainloop()
