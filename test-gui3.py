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
    zip = Column(String(6))
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
        vcmd = (parent.register(self.validate), '%S')

        # create top frame
        frame = Frame(parent)
        frame.pack(expand=YES, fill=BOTH, padx=5, pady=5)

        # create bottom frame
        btm_frame = Frame(parent, relief=SUNKEN, borderwidth=1)
        btm_frame.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=5, pady=5)

        # create datetime object
        d = datetime.today()
        date = d.strftime("%Y-%m-%d")
        

#------------------------Create Labels-------------------------------#
        

        # label to display date
        date_label = Label(btm_frame, text=date)
        date_label.pack(side=LEFT)

        # name label
        name_label = Label(frame, text="Enter Name:")
        name_label.grid(row=0, sticky=W)

        # age label
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
        

#----------------------Create Vars and Entry-------------------------#
        
            
        # name variable and entry
        self.name_var = StringVar()
        self.e1 = Entry(frame, textvariable=self.name_var)
        self.e1.grid(row=0, column=1)
         
        # age variable and entry
        self.age_var =  StringVar()     # IntVar()
        self.e2 = Entry(frame, textvariable=self.age_var,validate="key", validatecommand=vcmd)                                 
        self.e2.grid(row=1, column=1)

        # address variable and entry
        self.address_var = StringVar()
        self.e3 = Entry(frame, textvariable=self.address_var)
        self.e3.grid(row=2, column=1)

        # city variable and entry
        self.city_var = StringVar()
        self.e4 = Entry(frame, textvariable=self.city_var)
        self.e4.insert(0, "Roanoke")        # insert default value
        self.e4.grid(row=3, column=1)

        # state variable and entry
        self.state_var = StringVar()
        self.e5 = Entry(frame, textvariable=self.state_var)
        self.e5.insert(0, "VA")             # insert default value
        self.e5.grid(row=4, column=1)

        # zip code variable and entry
        self.zip_var = IntVar()
        self.e6 = Entry(frame, textvariable=self.zip_var)
        self.e6.grid(row=5, column=1)

        # s.s.n variable and entry
        self.ssn_var = StringVar()
        self.e7 = Entry(frame, textvariable=self.ssn_var)
        self.e7.grid(row=6, column=1)

        # phone variable and entry
        self.phone_var = StringVar()
        self.e8 = Entry(frame, textvariable=self.phone_var)
        self.e8.grid(row=7, column=1)

        # cell variable and entry
        self.cell_var = StringVar()
        self.e9 = Entry(frame, textvariable=self.cell_var)
        self.e9.grid(row=8, column=1)

        # quit, search, clear, add, delete buttons
        quit_button = Button(btm_frame, text="Quit", relief=RAISED, command=parent.destroy, fg="white", bg="gray66")
        quit_button.pack(side=RIGHT, padx=2, pady=2)        

        search_button = Button(btm_frame, text="Search", relief=RAISED, command=self.search, fg="white", bg="gray66")
        search_button.pack(side=RIGHT, padx=2, pady=2)

        clear_button = Button(btm_frame, text="Clear", relief=RAISED, command=self.clear_entries, fg="white", bg="gray66")
        clear_button.pack(side=RIGHT, padx=2, pady=2)        

        del_button = Button(btm_frame, text="Delete", relief=RAISED, command=self.del_employee, fg="white", bg="red")
        del_button.pack(side=RIGHT, padx=2, pady=2)

        add_button = Button(btm_frame, text="Add", relief=RAISED, command=self.add_data, fg="white", bg="gray66")
        add_button.pack(side=RIGHT, padx=2, pady=2)
        

    def add_data(self):        
        name = self.name_var.get()
        age = self.age_var.get()        
        addr = self.address_var.get()
        city = self.city_var.get()
        state = self.state_var.get()
        zip = self.zip_var.get()
        ssn = self.ssn_var.get()
        phone = self.phone_var.get()
        cell = self.cell_var.get()
        # create new Employee in .db
        new_person = Employee(name=name, age=age, address=addr, city=city, state=state, zip=zip, ssn=ssn, phone=phone, cell=cell)
        session.add(new_person)
        session.commit()
        session.close()
        self.callback()
        return

    def validate(self, S):
        try:
            v = int(S)
            return True
        except ValueError:
            showinfo("Age", "Please Enter A Number")
            return False        

    def callback(self):        
        showinfo("New Employee", "Data Added")
        self.clear_entries()
        return        

    def clear_entries(self):
        entries = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9]
        [e.delete(0,END) for e in entries]    # list comprehension (instead of for loop)
##        for entry in entries:
##            entry.delete(0, END)
        return            

    def search(self):
        search_win = Toplevel()
        search_win.title("Employee Search")

        # create labels for each employee attribute
        attr = ["Id","Name","Age","Address","City","State","Zip","SSN","Cell","Phone"]
        column = 0
        for a in attr:
                Label(search_win, text=a).grid(row=0,column=column,padx=2, pady=2)
                column += 1

        # search all employees, put each emp. in Entry Widget with For Loop
        res = session.query(Employee).all()
        row = 1
        column = 0
        for employee in res:
            txt = [employee.id, employee.name, employee.age, employee.address, employee.city, employee.state, employee.zip, employee.ssn, employee.phone, employee.cell]
            for t in txt:
                ent = Entry(search_win, relief=RIDGE, width=19)
                ent.grid(row=row, column=column, sticky=W, padx=1, pady=1)
                ent.insert(0, t)
                column += 1
            row += 1
            column = 0
        return

    def del_employee(self):
        del_win = Toplevel()
        del_win.title("Delete Employee")

        id_label = Label(del_win, text="Enter Employee Id:")
        id_label.grid(row=0, column=0, padx=5, pady=5)

        self.employee_id = IntVar()
        self.e10 = Entry(del_win, textvariable=self.employee_id)
        self.e10.grid(row=0, column=1, padx=5, pady=5)

        del_button = Button(del_win, text="Delete Employee", relief=GROOVE, command=self.erase)
        del_button.grid(row=0, column=2, padx=5, pady=5)
        return

    def erase(self):
        emp_id = self.employee_id.get()
        res = session.query(Employee).filter(Employee.id==emp_id).first()
        session.delete(res)
        session.commit()
        showinfo("Employee", "Data Deleted")
        return
        
        

if __name__ == '__main__':
    root = Tk()
    root.geometry("310x270")
    root.title("Employee Info")
    mygui = GUI(root)
    root.mainloop()

