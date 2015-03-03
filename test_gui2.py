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


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    address = Column(String(250))
    city = Column(String(10))
    state = Column(String(2))
    zip = Column(Integer)
    ssn = Column(String(12))
    phone = Column(String(12))
    cell = Column(String(12))

# create engine for Session connection
engine = create_engine('sqlite:///employee.db')

# create all tables in engine ('CREATE TABLE' in raw SQL)
Base.metadata.create_all(engine)

# create configured 'Session' class
Session = sessionmaker(bind=engine)

# create session
session = Session()


class GUI:
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
        

#------------------------Create Labels-----------------------------#
        

        # create label to display date
        date_label = Label(btm_frame, text=date)
        date_label.pack(side=LEFT)

        # create name label
        name_label = Label(frame, text="Enter Name:")
        name_label.grid(row=0, sticky=W)

        # creat age label
        age_label = Label(frame, text="Enter Age:")
        age_label.grid(row=1, sticky=W)

        # address label
        addr_label = Label(frame, text="Enter Address:")
        addr_label.grid(row=2, sticky=W)

        # city label
        city_label = Label(frame, text="Enter City:")
        city_label.grid(row=3, sticky=W)

        # state label
        state_label = Label(frame, text="Enter State:")
        state_label.grid(row=4, sticky=W)

        # zip code label
        zip_label = Label(frame, text="Enter Zip Code:")
        zip_label.grid(row=5, sticky=W)

        # ssn label
        ssn_label = Label(frame, text="Enter Social Security #:")
        ssn_label.grid(row=6, sticky=W)

        # phone label
        phone_label = Label(frame, text="Enter Phone #:")
        phone_label.grid(row=7, sticky=W)

        # cell label
        cell_label = Label(frame, text="Enter Cell #:")
        cell_label.grid(row=8, sticky=W)
        

#---------------------Create Vars and Entry-----------------------#
        
            
        # create name variable and entry
        self.name_var = StringVar()
        e1 = Entry(frame, textvariable=self.name_var)
        e1.grid(row=0, column=1)
         
        # creat age variable and entry
        self.age_var =  IntVar()
        e2 = Entry(frame, textvariable=self.age_var)
        e2.grid(row=1, column=1)

        # create address variable and entry
        self.address_var = StringVar()
        e3 = Entry(frame, textvariable=self.address_var)
        e3.grid(row=2, column=1)

        # create city variable and entry
        self.city_var = StringVar()
        e4 = Entry(frame, textvariable=self.city_var)
        e4.grid(row=3, column=1)

        # create state variable and entry
        self.state_var = StringVar()
        e5 = Entry(frame, textvariable=self.state_var)
        e5.grid(row=4, column=1)

        #create zip code variable and entry
        self.zip_var = IntVar()
        e6 = Entry(frame, textvariable=self.zip_var)
        e6.grid(row=5, column=1)

        # create s.s.n variable and entry
        self.ssn_var = StringVar()
        e4 = Entry(frame, textvariable=self.ssn_var)
        e4.grid(row=6, column=1)

        # create phone variable and entry
        self.phone_var = StringVar()
        e5 = Entry(frame, textvariable=self.phone_var)
        e5.grid(row=7, column=1)

        # create cell variable and entry
        self.cell_var = StringVar()
        e6 = Entry(frame, textvariable=self.cell_var)
        e6.grid(row=8, column=1)

        # create quit and add buttons
        quit_button = Button(btm_frame, text="Quit", relief=GROOVE, command=parent.destroy)
        quit_button.pack(side=RIGHT)        

        add_button = Button(btm_frame, text="Add", relief=GROOVE, command=self.add_data)
        add_button.pack(side=RIGHT, padx=5, pady=5)

        

    def add_data(self):
        '''add Employee info to .db'''
        
        name = self.name_var.get()
        age = self.age_var.get()
        addr = self.address_var.get()
        city = self.city_var.get()
        state = self.state_var.get()
        zip = self.zip_var.get()
        ssn = self.ssn_var.get()
        phone = self.phone_var.get()
        cell = self.cell_var.get()
        new_person = Employee(name=name, age=age, address=addr, city=city, state=state, zip=zip, ssn=ssn, phone=phone, cell=cell)
        session.add(new_person)
        session.commit()
        session.close()
        self.callback()    
        

    def callback(self):        
        showinfo("Work_Hours_GUI", "Data Added")            
        

if __name__ == '__main__':
    root = Tk()
    root.geometry("310x270")
    root.title("Work-Hours-GUI")
    mygui = GUI(root)
    root.mainloop()


##def clear_data(self):
##        for field in fields:
##            field.delete(0, END)

##    def match(self, filter):
##        return filter in self.memo or filter in self.tags
        

##    def search(self, filter):
##        return [person for person in self.people if note.match(filter)]


##    def search_notes(self):
##        filter = input("Search for: ")
##        notes = self.notebook.search(filter)
##        self.show_notes(notes)
