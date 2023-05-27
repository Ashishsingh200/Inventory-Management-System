from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x830+0+0")
        self.root.config(bg="white")
        #self.root.resizable(False, False)
        self.root.focus_force()

        self.root.title("Inventory Management System | Developed by Our Group")

        self.cart_list=[]

        self.chk_print=0
       
        #----TITLE
        self.icon_title=PhotoImage(file="E:\Self Study\Major Project\images\logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Famtasy",35,"bold"),fg="white",bg="blue",anchor="w",padx=20).place(x=0,y=0,height=70,relwidth=1)
        #----Footer
        lbl_footer=Label(root,text="This is a dummy project made by Ashish , Kuntak , Shubhankar , Nikita",font=("times new roman",15),bg="grey",fg="black").pack(side=BOTTOM,fill=X)

        #-----Logout button
        btn_logout=Button(self.root,command=self.logout,text="Logout",font=("times new roman",15),cursor="hand2").place(x=1350,y=22,height=35)
        
        #----Making Date As well as time
        self.lbl_clock=Label(self.root,text="Welcome to our project inventory management system\t\tDate:DD-MM-YYYY\t\tTime: HH:MM:SS",font=("times new roman",15),bg="grey",fg="black")
        self.lbl_clock.place(x=0,y=70,height=30,relwidth=1)

#--------Column1 no.1 Frame----------------

        #product frame

        #----variables under product frame
        self.var_search=StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,height=690,width=450)

        pTitle=Label(ProductFrame1,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)


        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=40,height=90,width=438)

        #product search frame

        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="White").place(x=5,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,height=22)

        btn_search=Button(ProductFrame2,command=self.search_data,text="Search",bg="#2196f3",fg="white",cursor="hand2").place(x=350,y=45,width=80,height=25)
        btn_showAll=Button(ProductFrame2,command=self.show,text="Show All",bg="#083531",fg="white",cursor="hand2").place(x=350,y=15,width=80,height=25)


        #---making triview
        product_frame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        product_frame3.place(x=2,y=133,height=520,width=438)

        scroly=Scrollbar(product_frame3,orient=VERTICAL)
        scrolx=Scrollbar(product_frame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame3,columns=("prod_id","name","price","qty","status"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.productTable.xview)
        scroly.config(command=self.productTable.yview)


        self.productTable.heading("prod_id",text="PID")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"

        self.productTable.column("prod_id",width=70)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=75)
        self.productTable.column("qty",width=70)
        self.productTable.column("status",width=100)
        
        self.productTable.pack(fill=BOTH,expand=1)

        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the caart'",font=("times new roman",14),fg="red",bg="white").pack(side=BOTTOM,fill=X)
        

        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        #self.show()

#--------------Column 2 ------------------
        #--------Customer Frame

        #-----variables
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=460,y=110,height=70,width=570)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("times new roman",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=170)

        lbl_contact=Label(CustomerFrame,text="Contact",font=("times new roman",15),bg="white").place(x=265,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=345,y=35,width=170)

        #----cal cart frame

        Cal_Cart_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_frame.place(x=460,y=185,height=500,width=570)

        #---calculator frame
#making variables under calculator frame

        self.var_cal_input=StringVar()

        Cal_frame=Frame(Cal_Cart_frame,bd=9,relief=RIDGE,bg="white")
        Cal_frame.place(x=5,y=5,height=485,width=268)

        text_cal_input=Entry(Cal_frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,border=8,relief=GROOVE,justify=RIGHT).grid(row=0,columnspan=4)

        btn_7=Button(Cal_frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=30,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=30,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=30,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=30,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=30,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=30,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=30,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input("-"),bd=5,width=4,pady=30,cursor="hand2").grid(row=2,column=3)


        btn_1=Button(Cal_frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=30,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=30,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=30,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=30,cursor="hand2").grid(row=3,column=3)


        btn_c=Button(Cal_frame,text="C",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=30,cursor="hand2").grid(row=4,column=0)
        btn_0=Button(Cal_frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=30,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=30,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=30,cursor="hand2").grid(row=4,column=3)

        #---making triview

        #-------cart frame
        Cart_frame=Frame(Cal_Cart_frame,bd=3,relief=RIDGE)
        Cart_frame.place(x=280,y=5,height=485,width=282)

        self.cartTitle=Label(Cart_frame,text="Cart \t Toatal Products: [0]",font=("times new roman",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)


        scroly=Scrollbar(Cart_frame,orient=VERTICAL)
        scrolx=Scrollbar(Cart_frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.CartTable.xview)
        scroly.config(command=self.CartTable.yview)


        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Qty")
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=38)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=80)
        self.CartTable.column("qty",width=38)
        
        self.CartTable.pack(fill=BOTH,expand=1)
        

        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        

        #----Add cart buttons
#making variable
        self.var_prod_id=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Cart_button_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cart_button_frame.place(x=460,y=684,height=115,width=570)

        #widgets addng
        lbl_p_name=Label(Cart_button_frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Cart_button_frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Cart_button_frame,text="Price Per Quantity",font=("times new roman",15),bg="white").place(x=210,y=5)
        txt_p_price=Entry(Cart_button_frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=210,y=35,width=150,height=22)

        lbl_p_qty=Label(Cart_button_frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Cart_button_frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=150,height=22)

        self.lbl_instock=Label(Cart_button_frame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)


        #Adding buttons

        btn_clear_cart=Button(Cart_button_frame,command=self.clear_cart,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=200,y=68,width=150,height=35)
        btn_add_update_cart=Button(Cart_button_frame,command=self.add_update_cart,text="Add | Update cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=365,y=68,width=180,height=35)


#---------COLUMN 3
        #------BILLING AREA

        bill_frame=Frame(self.root,relief=RIDGE,bd=4,bg="white")
        bill_frame.place(x=1035,y=110,width=490,height=540)

        BTitle=Label(bill_frame,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="#942821",fg="white").pack(side=TOP,fill=X)
        scroly=Scrollbar(bill_frame,orient=VERTICAL)
        scroly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(bill_frame,yscrollcommand=scroly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scroly.config(command=self.txt_bill_area.yview)

#-----------billing buttons
        bill_menu_frame=Frame(self.root,relief=RIDGE,bd=4,bg="white")
        bill_menu_frame.place(x=1035,y=645,width=490,height=154)

        self.lbl_amount=Label(bill_menu_frame,text="Bill Amount \n [0]",font=("times new roman",15,"bold"),fg="white",bg="#1f2e2e")
        self.lbl_amount.place(x=2,y=5,width=160,height=70)

        self.lbl_discount=Label(bill_menu_frame,text="Discount \n [5%]",font=("times new roman",15,"bold"),fg="white",bg="#00e6b8")
        self.lbl_discount.place(x=163,y=5,width=160,height=70)

        self.lbl_net_pay=Label(bill_menu_frame,text="Net Pay \n [0]",font=("times new roman",15,"bold"),fg="white",bg="#008080")
        self.lbl_net_pay.place(x=324,y=5,width=155,height=70)



        btn_print=Button(bill_menu_frame,command=self.print_bill,text="Print",font=("times new roman",15,"bold"),fg="white",bg="lightgreen",cursor="hand2")
        btn_print.place(x=2,y=83,width=140,height=62)

        btn_clear_all=Button(bill_menu_frame,command=self.clear_all,text="Clear All",font=("times new roman",15,"bold"),fg="white",bg="gray",cursor="hand2")
        btn_clear_all.place(x=145,y=83,width=140,height=62)

        btn_generate_bill=Button(bill_menu_frame,command=self.generate_bill,text="Generate/Save Bill",font=("times new roman",15,"bold"),fg="white",bg="#009688",cursor="hand2")
        btn_generate_bill.place(x=289,y=83,width=190,height=62)

#Showing product data in column 1 
        self.show()
        self.add_date_time()
        #self.bill_top()




    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))


    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("SELECT prod_id,name,price,qty,status FROM product where status='Active'")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for rows in rows:
                self.productTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


#-------searching
    def search_data(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Select search by Name",parent=self.root)
            else:
                cur.execute("SELECT prod_id,name,price,qty,status FROM product where name LIKE '%"+self.var_search.get()+"%' AND status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for rows in rows:
                        self.productTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']

        self.var_prod_id.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")

        self.var_stock.set(row[3])

        self.var_qty.set('1')

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']

        self.var_prod_id.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")

        self.var_stock.set(row[4])

    def add_update_cart(self):
        if self.var_prod_id.get()=="":
            messagebox.showerror('Error',"Please select product from the list")
        elif self.var_qty.get()=="":
            messagebox.showerror('Error',"Please Enter Product Quantity",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            cart_data=[self.var_prod_id.get(),self.var_pname.get(),self.var_price.get(),self.var_qty.get(),self.var_stock.get()]
            
            #update cart
            present=0
            index_=0
            for row in self.cart_list:
                if self.var_prod_id.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product is already present Do you want to update | remove  from the cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()



    def bill_update(self):
        self.bill_amt=0
        self.net_amt=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))


        #discount 
        self.discount=(self.bill_amt*5)/100
        self.net_amt=self.bill_amt-((self.bill_amt*5)/100)   #discount
        self.lbl_amount.config(text=f"Bill Amount(Rs.) \n {str(self.bill_amt)}")
        self.lbl_net_pay.config(text=f"Net Amount(Rs.) \n {str(self.net_amt)}")
        self.cartTitle.config(text=f"Cart \t Toatal Products: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for rows in self.cart_list:
                self.CartTable.insert('',END,values=rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error",f"Customer Details Required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Please Add Product for billing")
        else:
            #=====bill top
            self.bill_top()
            #=====bill middle
            self.middle()
            #=====bill bottom
            self.bill_bottom()
            #pass
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated/Saved in backend",parent=self.root)
            self.chk_print=1
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        bill_top_temp=f""" 
\t\t\tABS - PVT LTD
\t Phone No. 8328897003 , Bihar-855106
{str("="*57)}
   Customer Name:{self.var_cname.get()}
   ph no. {self.var_contact.get()}
   Bill No. {str(self.invoice)}\t\t\tDate:{str(time.strftime("%d/%m/%y"))}\tTime:{str(time.strftime("%H:%M"))}
{str("="*57)}
 Product Name\t\t\tQTY\t\tPrice
{str("="*57)}
        """
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f"""
{str("="*57)}
Bill Amount\t\t\t\tRs.{self.bill_amt}
Discount\t\t\t\tRs.{self.discount}
Net PAy\t\t\t\tRs.{self.net_amt}\n
{str("="*57)}\n

        """
        self.txt_bill_area.insert(END,bill_bottom_temp)


    def middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:

            for row in self.cart_list:
                
                prod_id=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3]) ==int(row[4]):
                    status='Inactive'
                if int(row[3]) !=int(row[4]):
                    status='Active'

                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"\t\tRs."+price)
                #=====Update quantity in product table
                cur.execute("update product set qty=?,status=? where prod_id=?",(
                    qty,
                    status,
                    prod_id
                ))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


    def clear_cart(self):
        self.var_prod_id.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.lbl_instock.config(text=f"In Stock")

        self.var_stock.set("")

        self.var_qty.set('')
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete('1.0',END)
        self.clear_cart()
        self.show()
        self.show_cart()
        self.var_search.set('')
        self.cartTitle.config(text=f"Cart \t Toatal Products: [0]")
        self.lbl_net_pay.config(text=f"Net Amount(Rs.) \n[0]")
        self.lbl_amount.config(text=f"Bill Amount(Rs.) \n[0]")
    
    def add_date_time(self):
        Time=time.strftime("%I:%M:%S")
        date=time.strftime("%d:%m:%Y")
        self.lbl_clock.config(text=f"Welcome to our project inventory management system\t\tDate: {str(date)}\t\tTime: {str(Time)}")
        self.lbl_clock.after(100,self.add_date_time)

    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("print","Please Generate bill to get the receipt")

    def logout(self):
        self.root.destroy()
        os.system("python login.py")
            





if __name__=="__main__":
    
    root=Tk()
    obj=BillClass(root)

    root.mainloop()