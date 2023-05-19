from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.resizable(False, False)
        self.root.focus_force()
        #-------All Variables
        self.var_searchby=StringVar()
        self.var_search_txt=StringVar()


        self.var_supp_invoice=StringVar()
        self.var_sup_name=StringVar()
        self.var_sup_contact=StringVar()

        #====SEARCH BAR
        #====options
        lbl_search=Label(self.root,text="Search by Invoice ID",bg="white",font=("times new roman",12))
        lbl_search.place(x=640,y=75,width=130)


        #text field
        self.txt_search=Entry(self.root,font=("times new roman",15),bg="lightyellow",textvariable=self.var_search_txt).place(x=790,y=75)
        #button in the search field
        self.search_bttn=Button(self.root,text="Search",command=self.search_data,font=("times new roman",15),bg="lightgreen",fg="black",cursor="hand2").place(x=1040,y=75,width=150,height=30)

        #---title
        title=Label(self.root,text="Supplier Details",fg="white",bg="#0f4d7d",font=("times new roman",20,"bold")).place(x=100,y=10,height=40,width=1080)

        #----content
        #------row 1
        lbl_sup_invoice=Label(self.root,text="Invoice ID",font=("times new roman",15),bg="white").place(x=100,y=80)
        txt_sup_invoice=Entry(self.root,textvariable=self.var_supp_invoice,font=("times new roman",15),bg="lightyellow").place(x=220,y=80,width=180)
        #----row 2

        lbl_sup_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=100,y=130)
        
        txt_sup_name=Entry(self.root,textvariable=self.var_sup_name,font=("times new roman",15),bg="lightyellow").place(x=220,y=130,width=180)
        
        #----row 3
        lbl_sup_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=100,y=180)

        txt_sup_contact=Entry(self.root,textvariable=self.var_sup_contact,font=("times new roman",15),bg="lightyellow").place(x=220,y=180,width=180)

        #-----row 4
        lbl_sup_desc=Label(self.root,text="Description",font=("times new roman",15),bg="white").place(x=100,y=230)

        self.txt_desc=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_desc.place(x=220,y=230,width=340,height=120)
        
        #-----row 5 buttons
        self.add_bttn=Button(self.root,text="Add",command=self.add_data,font=("times new roman",15),bg="#2196f3",fg="black",cursor="hand2").place(x=120,y=440,width=110,height=30)
        self.update_bttn=Button(self.root,text="Update",command=self.update_data,font=("times new roman",15),bg="#4caf50",fg="black",cursor="hand2").place(x=240,y=440,width=110,height=30)
        self.delete_bttn=Button(self.root,text="Delete",command=self.delete_data,font=("times new roman",15),bg="#f44336",fg="black",cursor="hand2").place(x=360,y=440,width=110,height=30)
        self.clear_bttn=Button(self.root,text="Clear",command=self.clear_data,font=("times new roman",15),bg="#607d8b",fg="black",cursor="hand2").place(x=480,y=440,width=110,height=30)

        #---making triview
        #Supplier details
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=600,y=130,height=480,width=650)

        scroly=Scrollbar(sup_frame,orient=VERTICAL)
        scrolx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("invoice_id","name","contact","desc"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.SupplierTable.xview)
        scroly.config(command=self.SupplierTable.yview)


        self.SupplierTable.heading("invoice_id",text="Invoice_ID")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        
        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice_id",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
        
        self.SupplierTable.pack(fill=BOTH,expand=1)
        

        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#----------------------------------------------------------------------------------------------------------------
    def add_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_supp_invoice.get()=="" or self.var_sup_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice_id=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Invoice ID is already assigned")
                else:
                    cur.execute("INSERT INTO supplier(invoice_id,name,contact,desc) VALUES(?,?,?,?)",(

                                    self.var_supp_invoice.get(),
                                    self.var_sup_name.get(),
                                    self.var_sup_contact.get(),
                                    self.txt_desc.get('1.0',END),

                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Supplier data added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for rows in rows:
                self.SupplierTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']

        self.var_supp_invoice.set(row[0]),
        self.var_sup_name.set(row[1]),
        self.var_sup_contact.set(row[2]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),


#-------------UPDATING DATA
    def update_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_supp_invoice.get()=="" or self.var_sup_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice_id=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice ID")
                else:
                    cur.execute("UPDATE supplier set name=?,contact=?,desc=? where invoice_id=?",(

                                    
                                    self.var_sup_name.get(),
                                    self.var_sup_contact.get(),
                                    self.txt_desc.get('1.0',END),
                                    self.var_supp_invoice.get()

                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Supplier data updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
#-------------Deleting the data
    def delete_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_supp_invoice.get()=="" or self.var_sup_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice_id=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice ID")
                else:
                    op=messagebox.askyesno("Confirm","Do you Want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice_id=?",(self.var_supp_invoice.get(),))
                        conn.commit()
                        messagebox.showinfo("Success","Supplier ID Deleted Successfully",parent=self.root)
                        self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

#-------------clear
    def clear_data(self):
        self.var_supp_invoice.set(""),
        self.var_sup_name.set(""),
        self.var_sup_contact.set(""),
        self.txt_desc.delete('1.0',END),
        self.var_search_txt.set("")
        self.var_searchby.set("Select")
        self.show()


#-------searching
    def search_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            #if self.var_searchby.get()=="Select":
                #messagebox.showerror("Error","Select search by option",parent=self.root)
            if self.var_search_txt.get()=="":
                messagebox.showerror("Error","Search input required",parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier where invoice_id=? ",(self.var_search_txt.get(),))
                rows=cur.fetchone()
                if rows != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for rows in rows:
                        self.SupplierTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")




if __name__=="__main__":
    
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()