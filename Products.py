from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class ProductClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.focus_force()

#-------variables
        self.var_prod_id=StringVar()
        self.var_cat=StringVar()
        self.var_supplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        self.var_searchby=StringVar()
        self.var_search_txt=StringVar()

        self.cat_list=[]
        self.supp_list=[]

        self.fetch_cat_sup()
#-----------Frame
        product_frame=Frame(self.root,bd=1.5,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=475,height=638)
#---title
        title=Label(product_frame,text="Manage Product Details",fg="white",bg="#0f4d7d",font=("times new roman",19)).pack(side=TOP,fill=X)

#----------column 1
        lbl_category=Label(product_frame,text="Category",bg="white",font=("times new roman",19)).place(x=25,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",bg="white",font=("times new roman",19)).place(x=25,y=110)
        lbl_name=Label(product_frame,text="Name",bg="white",font=("times new roman",19)).place(x=25,y=160)
        lbl_price=Label(product_frame,text="Price",bg="white",font=("times new roman",19)).place(x=25,y=210)
        lbl_quantity=Label(product_frame,text="Quantity",bg="white",font=("times new roman",19)).place(x=25,y=260)
        lbl_status=Label(product_frame,text="Status",bg="white",font=("times new roman",19)).place(x=25,y=310)
        
#----column 2
        cmb_cat=ttk.Combobox(product_frame,values=self.cat_list,textvariable=self.var_cat,state="readonly",justify="center")
        cmb_cat.place(x=170,y=69,width=200)
        cmb_cat.current(0)


        cmb_supplier=ttk.Combobox(product_frame,values=self.supp_list,textvariable=self.var_supplier,state="readonly",justify="center")
        cmb_supplier.place(x=170,y=119,width=200)
        cmb_supplier.current(0)


        txt_name=Entry(product_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_name).place(x=170,y=169,width=200)
        txt_price=Entry(product_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_price).place(x=170,y=219,width=200)
        txt_quantity=Entry(product_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_quantity).place(x=170,y=269,width=200)
        
        cmb_status=ttk.Combobox(product_frame,values=("Active","Inactive"),textvariable=self.var_status,state="readonly",justify="center")
        cmb_status.place(x=170,y=319,width=200)
        cmb_status.current(0)


        self.add_bttn=Button(product_frame,text="Add",command=self.add_data,font=("times new roman",15),bg="#2196f3",fg="black",cursor="hand2").place(x=4,y=400,width=100,height=35)
        self.update_bttn=Button(product_frame,text="Update",command=self.update_data,font=("times new roman",15),bg="#4caf50",fg="black",cursor="hand2").place(x=124,y=400,width=100,height=35)
        self.delete_bttn=Button(product_frame,text="Delete",command=self.delete_data,font=("times new roman",15),bg="#f44336",fg="black",cursor="hand2").place(x=244,y=400,width=100,height=35)
        self.clear_bttn=Button(product_frame,text="Clear",command=self.clear_data,font=("times new roman",15),bg="#607d8b",fg="black",cursor="hand2").place(x=364,y=400,width=100,height=35)




        #--------searchbar

        search_frame=LabelFrame(self.root,text="Search Employee",bg="White",font=("times new roman",12,"bold"))
        search_frame.place(x=550,y=10,width=700,height=80)

        #====options
        self.search=ttk.Combobox(search_frame,values=("Select","Category","Supplier","Name"),textvariable=self.var_searchby,state="readonly",justify="center")
        self.search.place(x=10,y=10,width=170)
        self.search.current(0)

        #text field
        self.txt_search=Entry(search_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_search_txt).place(x=250,y=8)
        #button in the search field
        self.search_bttn=Button(search_frame,text="Search",command=self.search_data,font=("times new roman",15),bg="lightgreen",fg="black",cursor="hand2").place(x=490,y=6,width=150,height=30)


        #---making triview
        #Product details
        prod_frame=Frame(self.root,bd=3,relief=RIDGE)
        prod_frame.place(x=500,y=110,width=800,height=543)

        scroly=Scrollbar(prod_frame,orient=VERTICAL)
        scrolx=Scrollbar(prod_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(prod_frame,columns=("prod_id","Category","Supplier","name","price","qty","status"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.ProductTable.xview)
        scroly.config(command=self.ProductTable.yview)


        self.ProductTable.heading("prod_id",text="Prod_ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")

        self.ProductTable["show"]="headings"

        self.ProductTable.column("prod_id",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        
        self.ProductTable.pack(fill=BOTH,expand=1)
        
        

        self.show()

        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

#----------------------------------------------------------------------------------------------------------------
    def fetch_cat_sup(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:

            cur.execute("select name from categories")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")

                for i in cat:
                    self.cat_list.append(i[0])


            cur.execute("select name from supplier")
            supp=cur.fetchall()
            self.supp_list.append("Empty")
            if len(supp)>0:
                del self.supp_list[:]
                self.supp_list.append("Select")

                for i in supp:
                    self.supp_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    
    
    def add_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_supplier.get()=="Select" or self.var_supplier.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Product is already assigned try different product")
                else:
                    cur.execute("INSERT INTO product(Category,Supplier,name,price,qty,status) VALUES(?,?,?,?,?,?)",(

                                    self.var_cat.get(),
                                    self.var_supplier.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_quantity.get(),
                                    self.var_status.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Product added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for rows in rows:
                self.ProductTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']

        self.var_prod_id.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6]),

        


#-------------UPDATING DATA
    def update_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_prod_id.get()=="":
                messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                cur.execute("select * from product where prod_id=?",(self.var_prod_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product")
                else:
                    cur.execute("UPDATE product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where prod_id=?",(
                        self.var_cat.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_prod_id.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Product data updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
#-------------Deleting the data
    def delete_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_prod_id.get()=="":
                messagebox.showerror("Error","Select product from list",parent=self.root)
            else:
                cur.execute("select * from product where prod_id=?",(self.var_prod_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you Want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where prod_id=?",(self.var_prod_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Success","Product Deleted Successfully",parent=self.root)
                        self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

#-------------clear
    def clear_data(self):
        self.var_prod_id.set("")
        self.var_cat.set("Select"),
        self.var_supplier.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_quantity.set(""),
        self.var_status.set("Active"),
        
        
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
                cur.execute("SELECT * FROM product where " +self.var_searchby.get()+" LIKE '%"+self.var_search_txt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for rows in rows:
                        self.ProductTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")



        

if __name__=="__main__":
    
    root=Tk()
    obj=ProductClass(root)



    root.mainloop()