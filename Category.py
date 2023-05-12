from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class CategoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.focus_force()
        #--------variables
        self.var_cat_id=StringVar()
        self.var_cat_name=StringVar()

        #========Title
        lbl_title=Label(self.root,text="Manage Products Categories",font=("times new roman",25,"bold"),fg="white",bg="#196666",justify=CENTER).place(x=10,y=10,width=1280,height=50)

        #----label
        lbl_cat_name=Label(self.root,text="Enter Category Name",font=("times new roman",22),bg="white").place(x=50,y=100)
        
        
        lbl_name_entry=Entry(self.root,textvariable=self.var_cat_name,font=("times new roman",18),bg="lightyellow").place(x=50,y=170,width=300)

#--------bttn
        btn_add=Button(self.root,text="ADD",command=self.add_data,font=("times new roman",15),fg="white",bg="#4caf50",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete_data,font=("times new roman",15),fg="white",bg="#ff0000",cursor="hand2").place(x=520,y=170,width=150,height=30)


#Adding tree view
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=90,height=530,width=590)

        scroly=Scrollbar(cat_frame,orient=VERTICAL)
        scrolx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("cat_id","name"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.CategoryTable.xview)
        scroly.config(command=self.CategoryTable.yview)


        self.CategoryTable.heading("cat_id",text="Category_ID")
        self.CategoryTable.heading("name",text="Name")
        
        self.CategoryTable["show"]="headings"

        self.CategoryTable.column("cat_id",width=90)
        self.CategoryTable.column("name",width=100)
        
        self.CategoryTable.pack(fill=BOTH,expand=1)
        

        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    

    #-----images
        self.im1=Image.open("E:\Self Study\Major Project\images\cat2.jpg")
        self.im1=self.im1.resize((670,410),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.im1_lbl=Label(self.root,image=self.im1)
        self.im1_lbl.place(x=20,y=230)

    #-------functions
    def add_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if  self.var_cat_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from categories where name=?",(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Category is already assigned")
                else:
                    cur.execute("INSERT INTO categories(name) VALUES(?)",(

                        self.var_cat_name.get(),

                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Categories added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM categories")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for rows in rows:
                self.CategoryTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']

        self.var_cat_id.set(row[0]),
        self.var_cat_name.set(row[1]),

    def delete_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please Select or Enter Category name",parent=self.root)
            else:
                cur.execute("select * from categories where cat_id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Category ID")
                else:
                    op=messagebox.askyesno("Confirm","Do you Want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from categories where cat_id=?",(self.var_cat_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Success","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_cat_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
        
if __name__=="__main__":
    
    root=Tk()
    obj=CategoryClass(root)


    root.mainloop()