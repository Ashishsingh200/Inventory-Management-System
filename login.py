from tkinter import*
from PIL import ImageTk
import time
import sqlite3
from tkinter import messagebox
import email_
import smtplib #pip install smtplib

import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x830+0+0")
        #self.root.resizable(False, False)
        self.root.config(bg="#fafafa")
        self.root.focus_force()
        self.otp=''


        self.root.title("Login System | Developed by Our Group")

        #----------images
        self.photo_image=ImageTk.PhotoImage(file="E:\Self Study\Major Project\images\phone.png")
        self.lbl_photo_img=Label(self.root,image=self.photo_image,bd=0).place(x=200,y=90)


        #---------variables
        self.employee_id=StringVar()
        self.password=StringVar()


#----------login frame
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=660,y=105,width=350,height=480)

        labl_login_system=Label(login_frame,text="Login System",font=("Elephant",26,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        
        labl_user_name=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_user_name=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        labl_user_password=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_user_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)


        btn_login=Button(login_frame,command=self.login_,text="Log In",font=("Arial Rounded MT Bold",15),fg="white",bg="#00B0F0",cursor="hand2",activebackground="#00B0F0",activeforeground="white").place(x=50,y=300,width=250,height=40)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=375,width=250,height=2)
        or_=Label(login_frame,text="OR",font=("times new roman",15,"bold"),bg="white",fg="lightgray").place(x=150,y=360)

        btn_forget=Button(login_frame,command=self.forget_window,text="Forget Password",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=100,y=400)

        #----frame 2
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        frame2.place(x=660,y=600,width=350,height=70)

        txt_label=Label(frame2,text="Major Project Demo",font=("times new roman",13),bg="white",justify=CENTER).place(x=0,y=25,relwidth=1)


        #------Animation
        self.im1=ImageTk.PhotoImage(file="E:\Self Study\Major Project\images\im1.png")
        self.im2=ImageTk.PhotoImage(file="E:\Self Study\Major Project\images\im2.png")
        self.im3=ImageTk.PhotoImage(file="E:\Self Study\Major Project\images\im3.png")

        self.lbl_change_img=Label(self.root,bg="white")
        self.lbl_change_img.place(x=367,y=192,width=240,height=428)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im

        self.lbl_change_img.config(image=self.im)
        self.lbl_change_img.after(2000,self.animate)




    def login_(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            cur.execute("select user_type from employee where emp_id=? and password=?",(
                self.employee_id.get(),
                self.password.get()
            ))
            user=cur.fetchone()
            if user==None:
                messagebox.showerror("Error","Invalid Employee ID | Password",parent=self.root)
            else:
                if user[0]=="Admin":
                    self.root.destroy()
                    os.system("py Dashboard.py")
                else:
                    self.root.destroy()
                    os.system("py billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def forget_window(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                    messagebox.showerror("Error","Employee ID required",parent=self.root)
            else:
                cur.execute("select email from employee where emp_id=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID , Try again",parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_cnf_pass=StringVar()

                    #call send email function
                    chk=self.send_email(email[0])
                    if chk !='s':
                        messagebox.showerror("Error","connection error,Try again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x450+1060+150')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="Reset Password",font=("times new roman",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)

                        reset_lbl=Label(self.forget_win,text="Enter OTP sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15,"bold"),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        
                        self.btn_reset=Button(self.forget_win,text="Submit",command=self.validate_otp,font=("times new roman",15,"bold"),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)


                        new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15,"bold")).place(x=45,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=45,y=190,width=250,height=30)

                        cnf_new_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15,"bold")).place(x=45,y=225)
                        txt_cnf_new_pass=Entry(self.forget_win,textvariable=self.var_cnf_pass,font=("times new roman",15),bg="lightyellow").place(x=45,y=255,width=250,height=30)


                        self.btn_update=Button(self.forget_win,command=self.update_pss,text="Update",font=("times new roman",15,"bold"),bg="lightblue",state=DISABLED)
                        self.btn_update.place(x=145,y=330,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
    
    def update_pss(self):
        if self.var_new_pass.get()=="" or self.var_cnf_pass.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get() != self.var_cnf_pass.get():
            messagebox.showerror("Error","Password must be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute("update employee set password=? where emp_id=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success",'Password updated successfully',parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}")

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP,try again",parent=self.forget_win)

    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        get_email=email_.email_
        get_pass=email_.pass_

        s.login(get_email,get_pass)
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir / Madam ,\n\nYour OTP to reset password is {str(self.otp)}.\n\nWith Regards,\nIMS Team'

        msg="Subject:{}\n\n{}".format(subj,msg)

        s.sendmail(get_email,to_,msg)
        chk=s.ehlo()

        if chk[0]==250:
            return "s" 
        else:
            return 'f'
        





if __name__=="__main__":
    
    root=Tk()
    obj=Login_System(root)

    root.mainloop()