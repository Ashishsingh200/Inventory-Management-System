from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x830+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        self.root.title("Inventory Management System | Developed by Our Group")
       
        #----TITLE
        self.icon_title=PhotoImage(file="E:\Self Study\Major Project\images\logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Famtasy",35,"bold"),fg="white",bg="blue",anchor="w",padx=20).place(x=0,y=0,height=70,relwidth=1)
        #----Footer
        lbl_footer=Label(root,text="This is a dummy project made by Ashish , Kuntak , Shubhankar , Nikita",font=("times new roman",15),bg="grey",fg="black").pack(side=BOTTOM,fill=X)

        #-----Logout button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15),cursor="hand2").place(x=1350,y=22,height=35)
        
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

        btn_search=Button(ProductFrame2,text="Search",bg="#2196f3",fg="white",cursor="hand2").place(x=350,y=45,width=80,height=25)
        btn_showAll=Button(ProductFrame2,text="Show All",bg="#083531",fg="white",cursor="hand2").place(x=350,y=15,width=80,height=25)


        #---making triview
        product_frame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        product_frame3.place(x=2,y=133,height=520,width=438)

        scroly=Scrollbar(product_frame3,orient=VERTICAL)
        scrolx=Scrollbar(product_frame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.productTable.xview)
        scroly.config(command=self.productTable.yview)


        self.productTable.heading("pid",text="PID")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=70)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=75)
        self.productTable.column("qty",width=70)
        self.productTable.column("status",width=100)
        
        self.productTable.pack(fill=BOTH,expand=1)

        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the caart'",font=("times new roman",14),fg="red",bg="white").pack(side=BOTTOM,fill=X)
        

        #self.productTable.bind("<ButtonRelease-1>",self.get_data)
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

        cartTitle=Label(Cart_frame,text="Cart \t Toatal Products: [0]",font=("times new roman",15),bg="lightgray").pack(side=TOP,fill=X)


        scroly=Scrollbar(Cart_frame,orient=VERTICAL)
        scrolx=Scrollbar(Cart_frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scroly.set,xscrollcommand=scrolx.set)
        
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)

        scrolx.config(command=self.CartTable.xview)
        scroly.config(command=self.CartTable.yview)


        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Qty")
        self.CartTable.heading("status",text="Status")
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=85)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90)
        
        self.CartTable.pack(fill=BOTH,expand=1)
        

        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        #self.show()

        #----Add cart buttons
#making variable
        self.var_p_name=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_status=StringVar()

        Cart_button_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cart_button_frame.place(x=460,y=684,height=115,width=570)

        #widgets addng
        lbl_p_name=Label(Cart_button_frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Cart_button_frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Cart_button_frame,text="Price Per Quantity",font=("times new roman",15),bg="white").place(x=210,y=5)
        txt_p_price=Entry(Cart_button_frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=210,y=35,width=150,height=22)

        lbl_p_qty=Label(Cart_button_frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Cart_button_frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=150,height=22)

        self.lbl_instock=Label(Cart_button_frame,text="In Stock []",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)


        #Adding buttons

        btn_clear_cart=Button(Cart_button_frame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=200,y=68,width=150,height=35)
        btn_clear_cart=Button(Cart_button_frame,text="Add | Update cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=365,y=68,width=180,height=35)


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



        btn_print=Button(bill_menu_frame,text="Print",font=("times new roman",15,"bold"),fg="white",bg="lightgreen",cursor="hand2")
        btn_print.place(x=2,y=83,width=140,height=62)

        btn_clear_all=Button(bill_menu_frame,text="Clear All",font=("times new roman",15,"bold"),fg="white",bg="gray",cursor="hand2")
        btn_clear_all.place(x=145,y=83,width=140,height=62)

        btn_generate_bill=Button(bill_menu_frame,text="Generate/Save Bill",font=("times new roman",15,"bold"),fg="white",bg="#009688",cursor="hand2")
        btn_generate_bill.place(x=289,y=83,width=190,height=62)



    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))







if __name__=="__main__":
    
    root=Tk()
    obj=BillClass(root)

    root.mainloop()