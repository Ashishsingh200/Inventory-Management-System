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


        #product frame

        #----variables under product frame
        self.var_search=StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,height=690,width=450)

        pTitle=Label(ProductFrame1,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)


        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=40,height=90,width=438)

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


        #--------Customer Frame

        #-----variables
        self.var_name=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=460,y=110,height=70,width=530)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("times new roman",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_name,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=170)

        lbl_contact=Label(CustomerFrame,text="Contact",font=("times new roman",15),bg="white").place(x=265,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=345,y=35,width=170)



if __name__=="__main__":
    
    root=Tk()
    obj=BillClass(root)

    root.mainloop()