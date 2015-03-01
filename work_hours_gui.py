from datetime import datetime
from Tkinter import *
from tkMessageBox import *
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
    '''Main GUI (Tkinter) Class'''
    
    def __init__(self, parent):
        self.parent = parent

        # create top frame
        frame = Frame(parent)
        frame.pack(expand=YES, fill=BOTH, padx=5, pady=5)

        # create bottom frame
        btm_frame = Frame(parent, relief=SUNKEN, borderwidth=1)
        btm_frame.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=5, pady=5)

        # create datetime object
        d = datetime.today()
        date = d.strftime("%Y-%m-%d")

        # create label to display date
        date_label = Label(btm_frame, text=date)
        date_label.pack(side=LEFT)


        # creat name label
        name_label = Label(frame, text="Enter Name:")
        name_label.grid(row=0, sticky=W)


        # creat age label
        age_label = Label(frame, text="Enter Age:")
        age_label.grid(row=1, sticky=W)


        # create text label
        #txt_label = Label(btm_frame, fg="white",bg="blue")
        #txt_label.pack(side=LEFT)

            
        # creat name variable and entry
        self.name_var = StringVar()
        e1 = Entry(frame, textvariable=self.name_var)
        e1.grid(row=0, column=1)

         
        # creat age variable and entry
        self.age_var =  IntVar()
        e2 = Entry(frame, textvariable=self.age_var)
        e2.grid(row=1, column=1)
        

        quit_button = Button(btm_frame, text="Quit", command=parent.destroy)
        quit_button.pack(side=RIGHT)
##        quit_button.config(padx=5, pady=5)
        

        add_button = Button(btm_frame, text="Add", command=self.add_data)
        add_button.pack(side=RIGHT, padx=5, pady=5)
##        add_button.config(padx=5, pady=5)

        

    def add_data(self):
        name = self.name_var.get()
        age = self.age_var.get()
        new_person = Test(name=name, age=age)
        session.add(new_person)
        session.commit()
        session.close()
        self.callback()

    def callback(self):
        showinfo("Data", "Data Added")
            
        


root = Tk()
root.geometry("250x100")
root.title("Work-Hours-GUI")
mygui = GUI(root)
root.mainloop()
