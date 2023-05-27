from tkinter import*
from tkinter import ttk,messagebox
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from PIL import Image,ImageTk
from idlelib.tooltip import Hovertip
class AnalysisClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650+205+150")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.title("Inventory Management System | Developed by Our Group")
        self.root.focus_force()

        #title
        #self.icon_title=PhotoImage(file="E:\Self Study\Major Project\images\cat.jpg")
        title=Label(self.root,text="Analysis Of Product Data",justify=CENTER,font=("Famtasy",26,"bold"),fg="black",bg="lightblue",padx=20).place(x=0,y=0,height=60,relwidth=1)


#setting images
        self.im1=Image.open("E:\Self Study\Major Project\images\pie.jpg")
        self.im1=self.im1.resize((300,270))
        self.im1=ImageTk.PhotoImage(self.im1)
        self.im1_lbl=Label(self.root,image=self.im1)
        self.im1_lbl.place(x=20,y=64)


        self.im2=Image.open("E:\Self Study\Major Project\images\ibar.jpg")
        self.im2=self.im2.resize((300,270))
        self.im2=ImageTk.PhotoImage(self.im2)
        self.im2_lbl=Label(self.root,image=self.im2)
        self.im2_lbl.place(x=20,y=350)

        self.im3=Image.open("E:\Self Study\Major Project\images\iarea_chart.png")
        self.im3=self.im3.resize((300,270))
        self.im3=ImageTk.PhotoImage(self.im3)
        self.im3_lbl=Label(self.root,image=self.im3)
        self.im3_lbl.place(x=460,y=164)


        self.im5=Image.open("E:\Self Study\Major Project\images\icount.png")
        self.im5=self.im5.resize((300,270))
        self.im5=ImageTk.PhotoImage(self.im5)
        self.im5_lbl=Label(self.root,image=self.im5)
        self.im5_lbl.place(x=900,y=64)

        self.im6=Image.open("E:\Self Study\Major Project\images\line.jpg")
        self.im6=self.im6.resize((300,270))
        self.im6=ImageTk.PhotoImage(self.im6)
        self.im6_lbl=Label(self.root,image=self.im6)
        self.im6_lbl.place(x=900,y=350)
        #bar_button=Button(text="Bar-Graph")

#---------Lebeling images
        self.im1_label=Button(self.root,text="Pie Chart",command=self.plot_pie,font=("times new roman",15,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2")
        self.im1_label.place(x=25,y=300)

        myBtn = Button(self.root,text='?',bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        myBtn.place(x=299,y=70)
        myTip = Hovertip(myBtn,'A pie chart is a circular graphical representation of data where the size of each slice corresponds to the proportion or percentage it represents.')

        self.im2_label=Button(self.root,text="Bar Chart",command=self.plot_bar,font=("times new roman",15,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2")
        self.im2_label.place(x=25,y=583)

        myBtn2 = Button(self.root,text='?',bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        myBtn2.place(x=299,y=355)
        myTip2 = Hovertip(myBtn2,'A bar chart is a graphical representation of data using rectangular bars, where the length of each bar corresponds to the value it represents.')

        self.im3_label=Button(self.root,text="Area Chart",command=self.plot_area,font=("times new roman",15,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2")
        self.im3_label.place(x=470,y=168)

        myBtn3 = Button(self.root,text='?',bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        myBtn3.place(x=740,y=168)
        myTip3 = Hovertip(myBtn3,'An area chart is a graphical representation of data that uses a series of filled areas to display the cumulative magnitude or value of multiple data points over time or categories.')

        self.im4_label=Button(self.root,text="Count Chart",command=self.plot_scatter,font=("times new roman",15,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2")
        self.im4_label.place(x=905,y=73)

        myBtn4 = Button(self.root,text='?',bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        myBtn4.place(x=1175,y=70)
        myTip4 = Hovertip(myBtn4,'A count chart is a graphical representation of data that displays the frequency or count of different categories or data points using bars or columns.')

        self.im5_label=Button(self.root,text="Line Chart",command=self.plot_line,font=("times new roman",15,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2")
        self.im5_label.place(x=905,y=585)

        myBtn5 = Button(self.root,text='?',bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E")
        myBtn5.place(x=1175,y=355)
        myTip5 = Hovertip(myBtn5,'A line chart is a graphical representation of data that uses connected data points with straight lines to show the trend or change in values over time or any other continuous variable.')



    def plot_bar(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        cur.execute("select Category,Supplier,name,price,qty,status from product")
        result=cur.fetchall()
        Category=[]
        Supplier=[]
        name=[]
        price=[]
        qty=[]
        status=[]
        try:
            for row in result:
                Category.append(row[0])
                Supplier.append(row[1])
                name.append(row[2])
                price.append(int(row[3]))
                qty.append(row[4])
                status.append(row[5])
            #print(Category) print(Supplier)print(name)print(price)print(qty)print(status)
            sns.barplot(x=name,y=price)

            #plt.bar(name,price)
            #plt.ylim(0, 5)
            plt.xlabel("Name of product")
            plt.ylabel("Price of product")
            
            plt.show()
            plt.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def plot_pie(self):

        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        cur.execute("select Category,Supplier,name,price,qty,status from product")
        result=cur.fetchall()
        Category=[]
        Supplier=[]
        name=[]
        price=[]
        qty=[]
        status=[]
        try:
            for row in result:
                Category.append(row[0])
                Supplier.append(row[1])
                name.append(row[2])
                price.append(row[3])
                qty.append(row[4])
                status.append(row[5])
            #print(Category) print(Supplier)print(name)print(price)print(qty)print(status)

            plt.pie(qty,labels=name, autopct='%.1f%%')
            #plt.legend(title='Product Names',loc="upper left")
            
            plt.title("Quantity Pie Chart")
            
            plt.show()
            plt.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    
    def plot_area(self):

        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        cur.execute("select Category,Supplier,name,price,qty,status from product")
        result=cur.fetchall()
        Category=[]
        Supplier=[]
        name=[]
        price=[]
        qty=[]
        status=[]
        try:
            for row in result:
                Category.append(row[0])
                Supplier.append(row[1])
                name.append(row[2])
                price.append(row[3])
                qty.append(int(row[4]))
                status.append(row[5])
            #print(Category) print(Supplier)print(name)print(price)print(qty)print(status)

            plt.fill_between(name,qty)
            #plt.ylim(0,5)

            plt.title("Name Vs Price")
            plt.xlabel("Name of product")
            plt.ylabel("Quantity of product")
            
            plt.show()
            plt.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def plot_scatter(self):

        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        cur.execute("select Category,Supplier,name,price,qty,status from product")
        result=cur.fetchall()
        Category=[]
        Supplier=[]
        name=[]
        price=[]
        qty=[]
        status=[]
        try:
            for row in result:
                Category.append(row[0])
                Supplier.append(row[1])
                name.append(row[2])
                price.append(row[3])
                qty.append(row[4])
                status.append(row[5])
            #print(Category) print(Supplier)print(name)print(price)print(qty)print(status)

            sns.countplot(x=status)
            plt.title("Count of Active And Inactive Data")
            
            
            plt.show()
            plt.close()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def plot_line(self):

        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        cur.execute("select Category,Supplier,name,price,qty,status from product")
        result=cur.fetchall()
        Category=[]
        Supplier=[]
        name=[]
        price=[]
        qty=[]
        status=[]
        try:
            for row in result:
                Category.append(row[0])
                Supplier.append(row[1])
                name.append(row[2])
                price.append(row[3])
                qty.append(int(row[4]))
                status.append(row[5])
            #print(Category) print(Supplier)print(name)print(price)print(qty)print(status)

            plt.plot(Supplier,qty)
            #plt.ylim(0, 5)
            plt.xlabel("Name of product")
            plt.ylabel("Price of product")
            
            plt.show()
            plt.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")


            





if __name__=="__main__":
    
    root=Tk()
    obj=AnalysisClass(root)
    root.mainloop()