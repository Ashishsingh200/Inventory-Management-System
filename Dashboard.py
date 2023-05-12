from tkinter import*
from Employee import EmployeeClass
from Supplier import SupplierClass
from Category import CategoryClass
from Products import ProductClass
from Sales    import SalesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x830+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        self.root.title("Inventory Management System | Developed by Our Group")
       
        #----TITLE
        self.icon_title=PhotoImage(file="E:\Self Study\Major Project\images\logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Famtasy",35,"bold"),fg="white",bg="blue",anchor="w",padx=20).place(x=0,y=0,height=70,relwidth=1)

        #-----Logout button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15),cursor="hand2").place(x=1350,y=22,height=35)
        
        #----Making Date As well as time
        self.lbl_clock=Label(self.root,text="Welcome to our project inventory management system\t\tDate:DD-MM-YYYY\t\tTime: HH:MM:SS",font=("times new roman",15),bg="grey",fg="black")
        self.lbl_clock.place(x=0,y=70,height=30,relwidth=1)


        #---Left menu button
        self.menu_logo=PhotoImage(file="E:\Self Study\Major Project\images\menu_im.png")

        left_menu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_menu.place(x=0,y=150,height=600,width=200)

        #logo
        lbl_menu_logo=Label(left_menu,image=self.menu_logo)
        lbl_menu_logo.pack(side=TOP,fill=X)

        #side icon
        self.side_icon=PhotoImage(file="E:\Self Study\Major Project\images\side.png")


        #menu button
        lbl_menu=Label(left_menu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(left_menu,text="Employee",image=self.side_icon,padx=5,compound=LEFT,command=self.Employee,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(left_menu,text="Supplier",image=self.side_icon,padx=5,compound=LEFT,command=self.Supplier,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_categories=Button(left_menu,text="Categories",image=self.side_icon,padx=5,compound=LEFT,command=self.Category,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_products=Button(left_menu,text="Products",image=self.side_icon,padx=5,compound=LEFT,command=self.Product,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(left_menu,text="Sales",image=self.side_icon,padx=5,compound=LEFT,command=self.Sales,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_analysis=Button(left_menu,text="Analysis",image=self.side_icon,padx=5,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(left_menu,text="Exit",image=self.side_icon,padx=5,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=2,cursor="hand2").pack(side=TOP,fill=X)
#--contents
        self.lbl_employee=Label(self.root,text="Total Employee\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#33bbf9")
        self.lbl_employee.place(x=260,y=190,height=150,width=300)
        self.lbl_supplier=Label(self.root,text="Total Supplier\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#ff5722")
        self.lbl_supplier.place(x=660,y=190,height=150,width=300)
        self.lbl_categories=Label(self.root,text="Total Categories\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#009688")
        self.lbl_categories.place(x=1060,y=190,height=150,width=300)
        self.lbl_products=Label(self.root,text="Total Products\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#009688")
        self.lbl_products.place(x=260,y=390,height=150,width=300)
        self.lbl_sales=Label(self.root,text="Total Sales\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#607d8b")
        self.lbl_sales.place(x=660,y=390,height=150,width=300)
        self.lbl_analysis=Label(self.root,text="Analytics\n [0]",font=("times new roman",20),bd=5,relief=RIDGE,bg="#ffc107")
        self.lbl_analysis.place(x=1060,y=390,height=150,width=300)
    

#----Footer
        lbl_footer=Label(root,text="This is a dummy project made by Ashish , Kuntak , Shubhankar , Nikita",font=("times new roman",15),bg="grey",fg="black").pack(side=BOTTOM,fill=X)


#=========================================
    def Employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmployeeClass(self.new_win)

    def Supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)

    def Category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)
    
    def Product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)

    def Sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)

if __name__=="__main__":
    
    root=Tk()
    obj=IMS(root)

    root.mainloop()