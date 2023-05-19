from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
class SalesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.focus_force()

        #------Variables
        self.billing_list=[]
        self.var_invoice=StringVar()
        


        #--------title
        lbl_title=Label(self.root,text="View Customer Bills",font=("times new roman",25,"bold"),fg="white",bg="#196666",justify=CENTER).place(x=10,y=10,width=1280,height=50)

        lbl_invoice=Label(self.root,text="Invoice ID",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)


        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=110,height=28)

        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=490,y=100,width=110,height=28)

        #---------sales list

        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=40,y=135,height=499,width=220)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("times new roman",15),bg="white",yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

        #-----billing area
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=270,y=135,height=499,width=500)
        
        
        lbl_title2=Label(bill_frame,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="orange",justify=CENTER).pack(side=TOP,fill=X)


        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_list=Listbox(bill_frame,bg="lightyellow",yscrollcommand=scrolly2)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_list.yview)
        self.bill_list.pack(fill=BOTH,expand=1)

        #---images
        self.bill_img=Image.open("E:\Self Study\Major Project\images\ill.png")
        self.bill_img=self.bill_img.resize((480,520),Image.ANTIALIAS)
        self.bill_img=ImageTk.PhotoImage(self.bill_img)

        lbl_image=Label(self.root,image=self.bill_img,bd=0)
        lbl_image.place(x=800,y=120)
        self.show()

        #-----------------
    def show(self):
        del self.billing_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('E:\Self Study\Major Project\Bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.billing_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)

        self.bill_list.delete('0',END)

        fp=open(f'Bill/{file_name}','r')
        for i in fp:
            self.bill_list.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice ID requires",parent=self.root)
        else:
            if self.var_invoice.get() in self.billing_list:
                fp=open(f'Bill/{self.var_invoice.get()}.txt','r')
                self.bill_list.delete(0,END)
                for i in fp:
                    self.bill_list.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid invoice number",parent=self.root)

    def clear(self):
        self.show()
        self.bill_list.delete('0',END)







if __name__=="__main__":
    
    root=Tk()
    obj=SalesClass(root)
    root.mainloop()