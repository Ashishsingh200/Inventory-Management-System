from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class EmployeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.focus_force()
        #-------All Variables
        self.var_searchby=StringVar()
        self.var_search_txt=StringVar()
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_password=StringVar()
        self.var_emp_user_type=StringVar()
        self.var_emp_address=StringVar()
        self.var_emp_salary=StringVar()

        #====SEARCH BAR
        search_frame=LabelFrame(self.root,text="Search Employee",bg="White",font=("times new roman",12,"bold"))
        search_frame.place(x=300,y=20,width=700,height=70)

        #====options
        self.search=ttk.Combobox(search_frame,values=("Select","Email","Name","Contact"),textvariable=self.var_searchby,state="readonly",justify="center")
        self.search.place(x=10,y=10,width=130)
        self.search.current(0)

        #text field
        self.txt_search=Entry(search_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_search_txt).place(x=200,y=8)
        #button in the search field
        self.search_bttn=Button(search_frame,text="Search",command=self.search_data,font=("times new roman",15),bg="lightgreen",fg="black",cursor="hand2").place(x=425,y=6,width=150,height=30)

        #---title
        title=Label(self.root,text="Employee Details",fg="white",bg="#0f4d7d",font=("times new roman",15)).place(x=100,y=100,width=1080)

        #----content
        #------row 1
        lbl_emp_id=Label(self.root,text="Emp ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=400,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=800,y=150)

        txt_emp_id=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),bg="lightyellow").place(x=150,y=150,width=180)
        #lbl_gender=Entry(self.root,textvariable=self.var_emp_gender,font=("times new roman",15),bg="white").place(x=450,y=150,width=180)
        self.gender=ttk.Combobox(self.root,values=("Select","Male","Female","Other"),font=(15),textvariable=self.var_emp_gender,state="readonly",justify="center")
        self.gender.place(x=500,y=150,width=180,height=28)
        self.gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_emp_contact,font=("times new roman",15),bg="lightyellow").place(x=900,y=150,width=180)

        #----row 2

        lbl_emp_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=200)
        lbl_dob=Label(self.root,text="D.O.B",font=("times new roman",15),bg="white").place(x=400,y=200)
        lbl_doj=Label(self.root,text="D.O.J",font=("times new roman",15),bg="white").place(x=800,y=200)

        txt_emp_name=Entry(self.root,textvariable=self.var_emp_name,font=("times new roman",15),bg="lightyellow").place(x=150,y=200,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_emp_dob,font=("times new roman",15),bg="lightyellow").place(x=500,y=200,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_emp_doj,font=("times new roman",15),bg="lightyellow").place(x=900,y=200,width=180)

        #----row 3
        lbl_emp_email=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=250)
        lbl_password=Label(self.root,text="Password",font=("times new roman",15),bg="white").place(x=400,y=250)
        lbl_usertype=Label(self.root,text="User Type",font=("times new roman",15),bg="white").place(x=800,y=250)

        txt_emp_email=Entry(self.root,textvariable=self.var_emp_email,font=("times new roman",15),bg="lightyellow").place(x=150,y=250,width=180)
        txt_password=Entry(self.root,textvariable=self.var_emp_password,font=("times new roman",15),bg="lightyellow").place(x=500,y=250,width=180)
        self.usertype=ttk.Combobox(self.root,values=("Admin","Employee"),font=(15),textvariable=self.var_emp_user_type,state="readonly",justify="center")
        self.usertype.place(x=900,y=250,width=180,height=28)
        self.usertype.current(0)

        #-----row 4
        lbl_emp_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=300)
        lbl_salary=Label(self.root,text="Salary",font=("times new roman",15),bg="white").place(x=550,y=300)

        self.txt_emp_address=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_emp_address.place(x=150,y=300,width=300,height=80)
        txt_password=Entry(self.root,textvariable=self.var_emp_salary,font=("times new roman",15),bg="lightyellow").place(x=650,y=300,width=180)
        
        #-----row 5 buttons
        self.add_bttn=Button(self.root,text="Add",command=self.add_data,font=("times new roman",15),bg="#2196f3",fg="black",cursor="hand2").place(x=500,y=350,width=110,height=30)
        self.update_bttn=Button(self.root,text="Update",command=self.update_data,font=("times new roman",15),bg="#4caf50",fg="black",cursor="hand2").place(x=650,y=350,width=110,height=30)
        self.delete_bttn=Button(self.root,text="Delete",command=self.delete_data,font=("times new roman",15),bg="#f44336",fg="black",cursor="hand2").place(x=800,y=350,width=110,height=30)
        self.clear_bttn=Button(self.root,text="Clear",command=self.clear_data,font=("times new roman",15),bg="#607d8b",fg="black",cursor="hand2").place(x=950,y=350,width=110,height=30)

        #---making triview
        #Employee details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=390,relwidth=1,height=259)

        scroly=Scrollbar(emp_frame,orient=VERTICAL)
        scrolx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("emp_id","name","email","gender","contact","dob","doj","password","user_type","address","salary"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.EmployeeTable.xview)
        scroly.config(command=self.EmployeeTable.yview)


        self.EmployeeTable.heading("emp_id",text="Emp_ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("password",text="Password")        
        self.EmployeeTable.heading("user_type",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("emp_id",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("user_type",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
        

        self.show()

        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

#----------------------------------------------------------------------------------------------------------------
    def add_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_emp_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from employee where emp_id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Employee ID is already assigned")
                else:
                    cur.execute("INSERT INTO employee(emp_id,name,email,gender,contact,dob,doj,password,user_type,address,salary) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(

                                    self.var_emp_id.get(),
                                    self.var_emp_name.get(),
                                    self.var_emp_email.get(),
                                    self.var_emp_gender.get(),
                                    self.var_emp_contact.get(),
                                    self.var_emp_dob.get(),
                                    self.var_emp_doj.get(),
                                    self.var_emp_password.get(),
                                    self.var_emp_user_type.get(),
                                    self.txt_emp_address.get('1.0',END),
                                    self.var_emp_salary.get()

                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Employee data added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for rows in rows:
                self.EmployeeTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']

        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_emp_email.set(row[2]),
        self.var_emp_gender.set(row[3]),
        self.var_emp_contact.set(row[4]),
        self.var_emp_dob.set(row[5]),
        self.var_emp_doj.set(row[6]),
        self.var_emp_password.set(row[7]),
        self.var_emp_user_type.set(row[8]),
        self.txt_emp_address.delete('1.0',END),
        self.txt_emp_address.insert(END,row[9]),
        self.var_emp_salary.set(row[10])


#-------------UPDATING DATA
    def update_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_emp_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from employee where emp_id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Employee ID")
                else:
                    cur.execute("UPDATE employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,user_type=?,address=?,salary=? where emp_id=?",(

                                    
                                    self.var_emp_name.get(),
                                    self.var_emp_email.get(),
                                    self.var_emp_gender.get(),
                                    self.var_emp_contact.get(),
                                    self.var_emp_dob.get(),
                                    self.var_emp_doj.get(),
                                    self.var_emp_password.get(),
                                    self.var_emp_user_type.get(),
                                    self.txt_emp_address.get('1.0',END),
                                    self.var_emp_salary.get(),
                                    self.var_emp_id.get()

                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Employee data updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
#-------------Deleting the data
    def delete_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_emp_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from employee where emp_id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Employee ID")
                else:
                    op=messagebox.askyesno("Confirm","Do you Want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where emp_id=?",(self.var_emp_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Success","Employee ID Deleted Successfully",parent=self.root)
                        self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

#-------------clear
    def clear_data(self):
        self.var_emp_id.set(""),
        self.var_emp_name.set(""),
        self.var_emp_email.set(""),
        self.var_emp_gender.set("Select"),
        self.var_emp_contact.set(""),
        self.var_emp_dob.set(""),
        self.var_emp_doj.set(""),
        self.var_emp_password.set(""),
        self.var_emp_user_type.set("Admin"),
        self.txt_emp_address.delete('1.0',END),
        self.var_emp_salary.set("")
        self.var_search_txt.set("")
        self.var_searchby.set("Select")
        self.show()


#-------searching
    def search_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_search_txt.get()=="":
                messagebox.showerror("Error","Search input required",parent=self.root)
            else:
                cur.execute("SELECT * FROM employee where " +self.var_searchby.get()+" LIKE '%"+self.var_search_txt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for rows in rows:
                        self.EmployeeTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")




if __name__=="__main__":
    
    root=Tk()
    obj=EmployeeClass(root)
    root.mainloop()