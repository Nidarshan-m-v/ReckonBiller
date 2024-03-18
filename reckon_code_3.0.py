import csv
from tkinter import *
import pymysql
from PIL import ImageTk
from tkinter import messagebox
import math, random
from twilio.rest import Client
import mysql.connector as mc


class biller:
    def my_sql_func():
        tables=[]
        data_base=[]
        flag=0
        try:
            conxn=mc.connect(host='localhost',user='root',password='ADMIN',database='test')
            cursr=conxn.cursor()
            cursr.execute('SHOW DATABASES')
            for a in cursr:
                if a not in data_base:
                    data_base.append(a)
            print(data_base)

            for i in data_base:
                if i[0]=='reckon':
                    print("reckon exist")
                    flag=1

            if flag==0:
                print("reckon not there")
                cursr.execute('CREATE DATABASE reckon')
                try:
                    cursr.execute('USE RECKON')
                    cursr.execute('SHOW TABLES')
                    for a in cursr:
                        if a not in data_base:
                            tables.append(a)
                    print(tables)
                    if tables==[]:
                        cursr.execute('CREATE TABLE log_details(name varchar(20),mobileno int,password varchar(50),Confirmpassword varchar(50))')
                        print("table created successfuly")
                    else:
                        print("table exist already")

                except:
                    print("a error is there while connecting reckon")

        except Exception as es:
            print("error")
            print("error",f"Error due to:{str(es)}")
    
    def __init__(self,root):
        self.root=root
        self.root.title("Reckon Biller")
        self.root.geometry("1300x700+100+50")
        self.root.resizable(False,False)
        self.my_sql_func
        self.login_page()


    
    def login_page(self):
        login_wind=Frame(self.root,bg="green")
        login_wind.place(x=0,y=0,height=700,width=1300)
          

        self.img=ImageTk.PhotoImage(file="bg1.jpeg")
        img=Label(login_wind,image=self.img).place(x=0,y=0,width=1300,height=700)

        
        windowbox1=Frame(self.root,bg='light cyan',borderwidth=10,relief=RIDGE)
        windowbox1.place(x=270,y=140,height=430,width=750)

        text1=Label(windowbox1,text="Login To Reckon",font=('Segoe UI',28,'bold'), fg="gold",bg='light cyan',bd=10)
        text1.place(x=215,y=15)


        text2=Label(windowbox1,text="Username",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        text2.place(x=50,y=95)


        self.name=Entry(windowbox1,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.name.place(x=50,y=145,width=270,height=35)


        text3=Label(windowbox1,text="Password",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        text3.place(x=420,y=95)
          

        self.password=Entry(windowbox1,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.password.place(x=420,y=145,width=270,height=35)

        text4=Label(windowbox1,text="Welcome To Reckon System",font=("Comic Sans MS",20,"bold"),fg='red',bg='light cyan')
        text4.place(x=185,y=220)

        but1=Button(windowbox1,text="forgot password?",command=self.forget_pass,cursor='hand1',font=('calibri',10),bg='light cyan',fg='black',bd=0)
        but1.place(x=310,y=275)


        but2=Button(windowbox1,text="Login",command=self.login_func,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but2.place(x=250,y=305)
       

        but3=Button(windowbox1,command=self.registeration,text="Not Registered?register",cursor="hand1",font=("calibri",10),bg='light cyan',fg="black",bd=0)
        but3.place(x=300,y=370)

        self.my_sql_func

    
    
    def login_func(self):
        if self.name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conxn=pymysql.connect(host='localhost',user='root',password='ADMIN', database='reckon')
                cursr=conxn.cursor()
                cursr.execute('select * from log_details where name=%s and password=%s' ,(self.name.get(),self.password.get()))
                detail=cursr.fetchone()
                if detail==None:
                    messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
                    self.logentryclear()
                else:
                    self.menu()
                    conxn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
        
    
    def registeration(self):
        register_wind=Frame(self.root,bg="light cyan")
        register_wind.place(x=0,y=0,height=700,width=1300)
        
        
        self.img=ImageTk.PhotoImage(file="bg2.jpeg")
        img=Label(register_wind,image=self.img).place(x=0,y=0,width=1300,height=720)
        
        
        windowbox2=Frame(self.root,bg='light cyan',borderwidth=10,relief=RIDGE)
        windowbox2.place(x=250,y=50,height=600,width=800)
        
        
        text1=Label(windowbox2,text="Register To Reckon",font=('Segoe UI',32,'bold'),fg="gold",bg='light cyan')
        text1.place(x=180,y=13)
        
        
        uname=Label(windowbox2,text="Username",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        uname.place(x=40,y=95)
        self.entry=Entry(windowbox2,font=("Segoe Print",15,"bold"), bg='ivory2',bd=4)
        self.entry.place(x=40,y=145,width=270,height=35)
        
        
        mob_no=Label(windowbox2,text="Mobile Number",font=("Comic Sans MS",20,"bold"), fg='medium spring green',bg='light cyan')
        mob_no.place(x=40,y=195)
        self.entry3=Entry(windowbox2,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.entry3.place(x=40,y=245,width=270,height=35)
        

        
        pas=Label(windowbox2,text="Password",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        pas.place(x=40,y=295)
        self.entry2=Entry(windowbox2,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.entry2.place(x=40,y=345,width=270,height=35)
        text2=Label(windowbox2,text="your password must contain at least 8 character",font=('Segoe UI',12,'bold'),fg="red",bg='light cyan')
        text2.place(x=320,y=348)


        conf_pas=Label(windowbox2,text="Confirm Password",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        conf_pas.place(x=40,y=395)
        self.entry4=Entry(windowbox2,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.entry4.place(x=40,y=445,width=270,height=35)
        
        btn2=Button(windowbox2,command=self.otp_page,text="Register",cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        btn2.place(x=270,y=490)
        
        btn3=Button(windowbox2,command=self.login_page,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='light cyan',fg="black",bd=0)
        btn3.place(x=320,y=560)
                  
    
    def registeration_func(self):
        if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
        elif len(self.entry3.get())<10 or len(self.entry3.get())>10:
            messagebox.showerror("Error","Enter a valid mobile number",parent=self.root)
        elif len(self.entry2.get())<8:
            messagebox.showerror('Error','your password must contain at least 8 character',parent=self.root)
            self.pasclear()
        else:
            try:
                conxn=pymysql.connect(host="localhost",user="root",password="ADMIN", database="reckon")
                cursr=conxn.cursor()
                cursr.execute("select * from log_details where mobileno=%s",self.entry3.get())
                detail=cursr.fetchone()
                
                if detail!=None:   
                    messagebox.showerror("Error","User already Exist,Please try with another Mobile Number",parent=self.root)
                    self.clearentry()
                    self.entry.focus()
                
                else:
                    cursr.execute("insert into log_details values(%s,%s,%s,%s)" ,(self.entry.get(),self.entry3.get(), self.entry2.get(),self.entry4.get()))
                    conxn.commit()
                    conxn.close()
                    messagebox.showinfo("Success","Register Succesfull",parent=self.root)
                    self.clearentry()
            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


    def forget_pass(self):
        forget_pwrd=Frame(self.root,bg="green")
        forget_pwrd.place(x=0,y=0,height=700,width=1300)

        self.img=ImageTk.PhotoImage(file="bg1.jpeg")
        img=Label(forget_pwrd,image=self.img).place(x=0,y=0,width=1300,height=700)

        windowbox3=Frame(self.root,bg='light cyan',borderwidth=10,relief=RIDGE)
        windowbox3.place(x=450,y=140,height=470,width=350)

        text001=Label(windowbox3,text="OTP verification",font=('Segoe UI',28,'bold'), fg="gold",bg='light cyan')
        text001.place(x=25,y=15)

        text002=Label(windowbox3,text="Enter your mobile number",font=("Comic Sans MS",16,"bold"),fg='medium spring green',bg='light cyan')
        text002.place(x=30,y=95)
        self.mob_no_box=Entry(windowbox3,font=("Segoe Print",15,"bold"),bg='lightpink',bd=4)
        self.mob_no_box.place(x=30,y=145,width=270,height=35)


        text003=Label(windowbox3,text="Enter your OTP",font=("Comic Sans MS",16,"bold"),fg='medium spring green',bg='light cyan')
        text003.place(x=30,y=255)
        self.forg_otp_box=Entry(windowbox3,font=("Segoe Print",15,"bold"),bg='lightpink',bd=4)
        self.forg_otp_box.place(x=30,y=305,width=270,height=35)


        but2=Button(windowbox3,text="Send otp",command=self.send_forg_otp,cursor="hand2",font=("Segoe Script",12),fg="white",bg="brown",bd=5,width=13,height=0)
        but2.place(x=85,y=200)


        but1=Button(windowbox3,text="resend otp",command=self.send_forg_otp,cursor='hand2',font=('calibri',10),bg='light cyan',fg='black',bd=0)
        but1.place(x=130,y=345)


        but2=Button(windowbox3,text="Verify",command=self.check_forg_OTP,cursor="hand2",font=("Segoe Script",12),fg="white",bg="brown",bd=5,width=13,height=0)
        but2.place(x=85,y=375)

        but1=Button(windowbox3,text="Login page",command=self.login_page,cursor='hand2',font=('calibri',10),bg='light cyan',fg='black',bd=0)
        but1.place(x=130,y=425)


    def send_forg_otp(self):
        if self.mob_no_box.get() == "" or len(self.mob_no_box.get())<10 :
            messagebox.showerror("Error!", "Enter a valid mobile number")
        else:
            self.number2 = random.randint(100000,999999)
            self.client=Client("ACf925bfd07de292fffeb65689865f59ff","0a72400cbe2a2f9b3e3e1995d74b687e")
            self.client.messages.create(to = ["+91" + self.mob_no_box.get()],from_="+15165189355",body=self.number2)


    def check_forg_OTP(self):
        try:
            if self.number2 == int(self.forg_otp_box.get()):
                self.forget_pass_func()
                self.number2="done"
            elif self.forg_otp_box=="":
                messagebox.showerror("Error!", "OTP box Should not empty")
            elif self.number2=="done":
                messagebox.showerror("Error!", "already Entered the OTP")
            else:
                messagebox.showerror("Error!", "wrong OTP")
        except:
            messagebox.showerror("Error!", "INVALID OTP")


    def forget_pass_func(self):
        forg_wind=Frame(self.root,bg="green")
        forg_wind.place(x=0,y=0,height=700,width=1300)
          

        self.img=ImageTk.PhotoImage(file="bg1.jpeg")
        img=Label(forg_wind,image=self.img).place(x=0,y=0,width=1300,height=700)

        
        windowbox4=Frame(self.root,bg='light cyan',borderwidth=10,relief=RIDGE)
        windowbox4.place(x=270,y=140,height=430,width=750)

        text_1=Label(windowbox4,text="Change Password",font=('Segoe UI',28,'bold'), fg="gold",bg='light cyan',bd=10)
        text_1.place(x=215,y=15)


        text_2=Label(windowbox4,text="Username",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        text_2.place(x=50,y=95)


        self.name2=Entry(windowbox4,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.name2.place(x=50,y=145,width=270,height=35)


        text_3=Label(windowbox4,text="New Password",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='light cyan')
        text_3.place(x=420,y=95)
          

        self.new_password=Entry(windowbox4,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.new_password.place(x=420,y=145,width=270,height=35)

        text_4=Label(windowbox4,text="Enter a New Password",font=("Comic Sans MS",20,"bold"),fg='red',bg='light cyan')
        text_4.place(x=185,y=220)

        but_2=Button(windowbox4,text="Change Password",command=self.change_pass,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but_2.place(x=250,y=305)


    def change_pass(self):
        if self.name2.get()=="" or self.new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conxn=pymysql.connect(host='localhost',user='root',password='ADMIN', database='reckon')
                cursr=conxn.cursor()
                cursr.execute('select * from log_details where name=%s and mobileno=%s',(self.name2.get(),self.mob_no_box.get()))
                detail=cursr.fetchone()

               	if detail==None:
                    messagebox.showerror('Error','Invalid Username or Mobile Number',parent=self.root)
                    self.logentryclear()
                else:
                	conxn2=pymysql.connect(host='localhost',user='root',password='ADMIN', database='reckon')
                	cursr2=conxn2.cursor()
                	cursr2.execute('update log_details set password=%s where mobileno=%s',(self.new_password.get(),(self.mob_no_box.get())))
                	messagebox.showinfo('Done','Password changes Succesfullyu ',parent=self.root)
                	self.login_page()
                	conxn.close()
                	conxn2.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

    def otp_page(self):
    	if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
    	elif self.entry2.get()!=self.entry4.get():
    		messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
    	elif len(self.entry3.get())<10 or len(self.entry3.get())>10:
    		messagebox.showerror("Error","Enter a valid mobile number",parent=self.root)
    	elif len(self.entry2.get())<8:
    		messagebox.showerror('Error','your password must contain at least 8 character',parent=self.root)
    		self.pasclear()
    	else:
    		page_otp=Frame(self.root,bg="green")
    		page_otp.place(x=0,y=0,height=700,width=1300)
    		
    		self.img=ImageTk.PhotoImage(file="bg1.jpeg")
    		img=Label(page_otp,image=self.img).place(x=0,y=0,width=1300,height=700)
    		
    		windowbox5=Frame(self.root,bg='light cyan',borderwidth=10,relief=RIDGE)
    		windowbox5.place(x=460,y=220,height=450,width=350)
    		
    		text1=Label(windowbox5,text="OTP verification",font=('Segoe UI',28,'bold'), fg="gold",bg='light cyan')
    		text1.place(x=25,y=15)
    		
    		text2=Label(windowbox5,text="Enter your OTP",font=("Comic Sans MS",16,"bold"),fg='medium spring green',bg='light cyan')
    		text2.place(x=30,y=95)
    		
    		self.otpbox=Entry(windowbox5,font=("Segoe Print",15,"bold"),bg='lightpink',bd=4)
    		self.otpbox.place(x=30,y=145,width=270,height=35)
    		
    		but1=Button(windowbox5,text="resend otp",command=self.resendOTP,cursor='hand2',font=('calibri',10),bg='light cyan',fg='black',bd=0)
    		but1.place(x=125,y=255)
    		
    		but1=Button(windowbox5,text="Enter another number",cursor='hand2',font=('calibri',10),bg='light cyan',fg='black',bd=0)
    		but1.place(x=120,y=285)
    		
    		but2=Button(windowbox5,text="Verify",command=self.checkOTP,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
    		but2.place(x=60,y=360)
    		
    		self.number1 = random.randint(100000,999999)
    		self.client=Client("ACf925bfd07de292fffeb65689865f59ff","0a72400cbe2a2f9b3e3e1995d74b687e")
    		self.client.messages.create(to = ["+91" + self.entry3.get()],from_="+15165189355",body=self.number1)

    def checkOTP(self):
        try:
            if self.number1 == int(self.otpbox.get()):
                self.registeration_func()
                self.login_page()
                self.number1="done"
            elif self.number1=="done":
                messagebox.showerror("Error!", "already Entered the OTP")
            else:
                messagebox.showerror("Error!", "wrong OTP")
        except:
            messagebox.showerror("Error!", "INVALID OTP")
    
    def resendOTP(self):
        self.number1=random.randint(100000, 999999)
        self.client=Client("ACf925bfd07de292fffeb65689865f59ff","0a72400cbe2a2f9b3e3e1995d74b687e")
        self.client.messages.create(to = ["+91" + self.entry3.get()],from_="+15165189355",body=self.number1)
    
    def close_app(self):
       	messagebox.showinfo("exiting","Closing App",parent=self.root)
       	self.menu()

    def create(self):
        
        create_wind=Frame(self.root,bg="light gray")
        create_wind.place(x=0,y=0,height=700,width=1300)
                  
        windowbox6=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox6.place(x=270,y=140,height=400,width=750)

        text01=Label(windowbox6,text="Create Product List",font=('Segoe UI',28,'bold'),fg="gold",bg='red')
        text01.place(x=180,y=13)


        text02=Label(windowbox6,text="Product Name",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text02.place(x=50,y=95)


        self.prod_name=Entry(windowbox6,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name.place(x=50,y=145,width=270,height=35)


        text03=Label(windowbox6,text="Price",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text03.place(x=420,y=95)
          

        self.price=Entry(windowbox6,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.price.place(x=420,y=145,width=270,height=35)


        text04=Label(windowbox6,text="Quantity",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text04.place(x=290,y=185)
          
        self.qty=Entry(windowbox6,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty.place(x=290,y=235,width=170,height=35)


        but1=Button(windowbox6,text="Enter data",command=self.biller_display,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but1.place(x=170,y=305)

        but2=Button(windowbox6,text="Main Menu",command=self.menu,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but2.place(x=370,y=305)


    def edit_price_page(self):
        
        edit_wind=Frame(self.root,bg="light gray")
        edit_wind.place(x=0,y=0,height=700,width=1300)
                  
        windowbox7=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox7.place(x=270,y=140,height=400,width=750)

        text01=Label(windowbox7,text="Change price of the Product",font=('Segoe UI',28,'bold'),fg="gold",bg='red')
        text01.place(x=160,y=13)


        text02=Label(windowbox7,text="Product Name",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text02.place(x=50,y=95)


        self.edit_prod_name=Entry(windowbox7,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.edit_prod_name.place(x=50,y=145,width=270,height=35)


        text03=Label(windowbox7,text="New Price",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text03.place(x=420,y=95)
          

        self.new_price=Entry(windowbox7,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.new_price.place(x=420,y=145,width=270,height=35)

        text4=Label(windowbox7,text="Enter the name and price of the product",font=("Comic Sans MS",18,"bold"),fg='red',bg='red')
        text4.place(x=185,y=220)


        but1=Button(windowbox7,text="Change",command=self.edit_price_func,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but1.place(x=170,y=305)

        but2=Button(windowbox7,text="Main Menu",command=self.menu,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but2.place(x=370,y=305)


    def edit_qty_page(self):
        
        edit_wind=Frame(self.root,bg="light gray")
        edit_wind.place(x=0,y=0,height=700,width=1300)
                  
        windowbox8=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox8.place(x=270,y=140,height=400,width=750)

        text01=Label(windowbox8,text="Change Product Quantity ",font=('Segoe UI',28,'bold'),fg="gold",bg='red')
        text01.place(x=160,y=13)


        text02=Label(windowbox8,text="Product Name",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text02.place(x=50,y=95)


        self.edit_qty_prod_name=Entry(windowbox8,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.edit_qty_prod_name.place(x=50,y=145,width=270,height=35)


        text03=Label(windowbox8,text="New Quantity",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text03.place(x=420,y=95)
          

        self.new_qty=Entry(windowbox8,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.new_qty.place(x=420,y=145,width=270,height=35)


        but1=Button(windowbox8,text="Change",command=self.edit_qty_func,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but1.place(x=170,y=305)

        but2=Button(windowbox8,text="Main Menu",command=self.menu,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but2.place(x=370,y=305)


    def add_data(self):
        
        add_wind=Frame(self.root,bg="light gray")
        add_wind.place(x=0,y=0,height=700,width=1300)
                  
        windowbox9=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox9.place(x=270,y=140,height=400,width=750)

        text01=Label(windowbox9,text="Add New Products",font=('Segoe UI',28,'bold'),fg="gold",bg='red')
        text01.place(x=180,y=13)


        text02=Label(windowbox9,text="Product Name",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text02.place(x=50,y=95)


        self.prod_name=Entry(windowbox9,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name.place(x=50,y=145,width=270,height=35)


        text03=Label(windowbox9,text="Price",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text03.place(x=420,y=95)
          

        self.price=Entry(windowbox9,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.price.place(x=420,y=145,width=270,height=35)

        text4=Label(windowbox9,text="Enter the name and price of the product",font=("Comic Sans MS",18,"bold"),fg='red',bg='red')
        text4.place(x=185,y=220)

        text5=Label(windowbox9,text="Quantity",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text5.place(x=290,y=185)
          

        self.qty=Entry(windowbox9,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty.place(x=290,y=235,width=170,height=35)


        but1=Button(windowbox9,text="Enter data",command=self.biller_display,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but1.place(x=170,y=305)

        but2=Button(windowbox9,text="Main Menu",command=self.menu,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but2.place(x=370,y=305)


    def delete_page(self):
        delete_wind=Frame(self.root,bg="light gray")
        delete_wind.place(x=0,y=0,height=700,width=1300)
                  
        windowbox10=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox10.place(x=270,y=140,height=400,width=750)

        text0_1=Label(windowbox10,text="Enter the product Name to Delete",font=('Segoe UI',28,'bold'),fg="gold",bg='red')
        text0_1.place(x=80,y=13)


        text0_2=Label(windowbox10,text="Product Name",font=("Comic Sans MS",20,"bold"),fg='medium spring green',bg='red')
        text0_2.place(x=150,y=95)


        self.delete_prod_name=Entry(windowbox10,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.delete_prod_name.place(x=150,y=145,width=270,height=35)


        but1=Button(windowbox10,text="Delete data",command=self.delete_data_func,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but1.place(x=170,y=305)

        but2=Button(windowbox10,text="Main Menu",command=self.menu,cursor="hand2",font=("Segoe Script",15),fg="white",bg="blue",bd=5,width=13,height=0)
        but2.place(x=370,y=305)


 
    def biller_display(self):
        if self.prod_name.get()=="" or self.price.get()=="" or self.qty.get()=="":
            messagebox.showerror("Error!", "Both fields Should be Filled")
        else:
            file_pointer=open("productlist.csv","a",newline="")
            writer_obj=csv.writer(file_pointer)
            if self.qty.get().isalpha()==True:
            	messagebox.showerror("Error!", "For quantity enter only digits")
            	self.qty.delete(0,END)
            elif self.price.get().isalpha()==True:
            	messagebox.showerror("Error!", "For price enter only digits")
            	self.price.delete(0,END)
            elif self.qty.get().isdigit()==True:
            	writer_obj.writerow([self.prod_name.get(),self.price.get(),self.qty.get()])
            	file_pointer.close()
            	messagebox.showinfo("Done","Data Entry is Success",parent=self.root)
            	self.create_entry_clear()


    def edit_price_func(self):
        if self.edit_prod_name.get()=="" or self.new_price.get()=="":
            messagebox.showerror("Error!", "Both fields Should be Filled")
        else:
            file=open('productlist.csv', 'r')
            Reader=csv.reader(file)
            data=[]
            Found=False
            for row in Reader:
                if row[0] == self.edit_prod_name.get():
                    Found=True
                    row [1] = self.new_price.get()
                data.append(row)
            file.close()
            
            if Found==False:
            	messagebox.showerror("Error!", "product Not Found")
            else:
                file=open('productlist.csv','w+', newline='')
                Writer=csv.writer(file)
                Writer.writerows(data)
                messagebox.showinfo("Done","Quantity changed Succesfully")
                self.edit_prod_name.delete(0,END)
                self.new_price.delete(0,END)
                file.close()
            

    def edit_qty_func(self):
        if self.edit_qty_prod_name.get()=="" or self.new_qty.get()=="":
            messagebox.showerror("Error!", "Both fields Should be Filled")
        else:
            file=open('productlist.csv', 'r')
            Reader=csv.reader(file)
            data=[]
            Found=False
            for row in Reader:
                if row[0] == self.edit_qty_prod_name.get():
                    Found=True
                    row [2] = self.new_qty.get()
                data.append(row)
            file.close()
            
            if Found==False:
            	messagebox.showerror("Error!", "product Not Found")
            else:
                file=open('productlist.csv','w+', newline='')
                Writer=csv.writer(file)
                Writer.writerows(data)
                messagebox.showinfo("Done","Quantity changed Succesfully")
                self.edit_qty_prod_name.delete(0,END)
                self.new_qty.delete(0,END)
                file.close()


    def delete_data_func(self):
        if self.delete_prod_name.get()=="":
            messagebox.showerror("Error!", "Both fields Should be Filled")
        else:
            file=open('productlist.csv', 'r')
            Reader=csv.reader(file)
            data=[]
            Found=False
            for row in Reader:
                if row[0] == self.delete_prod_name.get():
                    Found=True
                else:
                    data.append(row)
            file.close()
            
            if Found==False:
            	messagebox.showerror("Error!", "product Not Found")
            else:
                file=open('productlist.csv','w+', newline='')
                Writer=csv.writer(file)
                Writer.writerows(data)
                messagebox.showinfo("Done","product Removed Succesfully")
                self.delete_prod_name.delete(0,END)
                file.close()       


    def bill_calculate(self):
        file_pointer=open('productlist.csv','r')
        Reader=csv.reader(file_pointer)
        data=[]
        self.dict_data={}
        for row in Reader:
        	self.dict_data[row[0]]=row[1]
        	data.append(row)


        calc_wind=Frame(self.root,bg="light gray")
        calc_wind.place(x=0,y=0,height=700,width=1300)

        windowbox11=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        windowbox11.place(x=3,y=5,height=80,width=1290)

        but01=Button(windowbox11,text="Menu",command=self.menu,cursor="hand2",font=("Bauhaus 93",12),fg="black",bg="yellow",bd=3,width=5,height=1)
        but01.place(x=1200,y=10)

        letter1=Label(windowbox11,text="RECKON BILLER",font=("Bauhaus 93",28,'bold'),fg="yellow",bg='red')
        letter1.place(x=480,y=10)

        self.windowbox12=Frame(self.root,bg='red',borderwidth=10,relief=RIDGE)
        self.windowbox12.place(x=3,y=89,height=610,width=1290)

        text02=Label(self.windowbox12,text="Product Name",font=("Comic Sans MS",24,"bold"),fg='DodgerBlue4',bg='red')
        text02.place(x=20,y=30)

        text03=Label(self.windowbox12,text="Price",font=("Comic Sans MS",24,"bold"),fg='DodgerBlue4',bg='red')
        text03.place(x=430,y=30)

        text04=Label(self.windowbox12,text="Quantity",font=("Comic Sans MS",24,"bold"),fg='DodgerBlue4',bg='red')
        text04.place(x=560,y=30)

        text05=Label(self.windowbox12,text="Total",font=("Comic Sans MS",24,"bold"),fg='DodgerBlue4',bg='red')
        text05.place(x=770,y=30)

        self.prod_name_1=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_1.place(x=20,y=125,width=270,height=35)

        self.prod_name_2=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_2.place(x=20,y=225,width=270,height=35)

        self.prod_name_3=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_3.place(x=20,y=325,width=270,height=35)

        self.prod_name_4=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_4.place(x=20,y=425,width=270,height=35)

        self.prod_name_5=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_5.place(x=20,y=525,width=270,height=35)

        self.prod_name_6=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.prod_name_6.place(x=20,y=625,width=270,height=35)

        but1=Button(self.windowbox12,text="Enter",command=self.biller_display1,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but1.place(x=300,y=120)

        but2=Button(self.windowbox12,text="Enter",command=self.biller_display2,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but2.place(x=300,y=220)

        but3=Button(self.windowbox12,text="Enter",command=self.biller_display3,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but3.place(x=300,y=320)

        but4=Button(self.windowbox12,text="Enter",command=self.biller_display4,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but4.place(x=300,y=420)

        but5=Button(self.windowbox12,text="Enter",command=self.biller_display5,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but5.place(x=300,y=520)

        but6=Button(self.windowbox12,text="Enter",command=self.biller_display6,cursor="hand2",font=("Segoe Script",15),fg="black",bg="light green",bd=5,width=5,height=0)
        but6.place(x=300,y=620)

        self.qty_1=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_1.place(x=560,y=125,width=145,height=35)

        self.qty_2=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_2.place(x=560,y=225,width=145,height=35)

        self.qty_3=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_3.place(x=560,y=325,width=145,height=35)

        self.qty_4=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_4.place(x=560,y=425,width=145,height=35)

        self.qty_5=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_5.place(x=560,y=525,width=145,height=35)

        self.qty_6=Entry(self.windowbox12,font=("Segoe Print",15,"bold"),bg='ivory2',bd=4)
        self.qty_6.place(x=560,y=625,width=145,height=35)

        but7=Button(self.windowbox12,text="Calculate bill",command=self.calculate_bill_func,cursor="hand2",font=("Bauhaus 93",14),fg="black",bg="yellow",bd=5,width=13,height=1)
        but7.place(x=915,y=530)

        but8=Button(self.windowbox12,text="Clear bill",command=self.bill_calculate,cursor="hand2",font=("Bauhaus 93",14),fg="black",bg="yellow",bd=5,width=13,height=1)
        but8.place(x=1070,y=530)

        self.windowbox13=Frame(self.root,bg='white',borderwidth=10,relief=RIDGE)
        self.windowbox13.place(x=920,y=180,height=420,width=350)

        print_word1=Label(self.windowbox13,text="welcome to our shop",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word1.place(x=70,y=5)

        print_word2=Label(self.windowbox13,text="********************************",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word2.place(x=0,y=40)

        print_word3=Label(self.windowbox13,text="Total price:",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word3.place(x=120,y=260)

        print_word4=Label(self.windowbox13,text="Tax:       12% ",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word4.place(x=180,y=290)

        print_word5=Label(self.windowbox13,text="********************************",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word5.place(x=0,y=320)

        print_word6=Label(self.windowbox13,text="Final price:",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word6.place(x=120,y=350)

        print_word7=Label(self.windowbox13,text="Product Name",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word7.place(x=10,y=60)

        print_word8=Label(self.windowbox13,text="Qty",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word8.place(x=170,y=60)

        print_word9=Label(self.windowbox13,text="Price",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word9.place(x=255,y=60)

        print_word10=Label(self.windowbox13,text="-----------------------------------------",font=("Comic Sans MS",14),fg='black',bg='white')
        print_word10.place(x=0,y=90)


    def biller_display1(self):
        
        if self.prod_name_1.get() in self.dict_data:
        	letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_1.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
        	letter1.place(x=460,y=125)
        elif self.prod_name_1.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")

    def biller_display2(self):
        
        if self.prod_name_2.get() in self.dict_data:
            letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_2.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
            letter1.place(x=460,y=225)

        elif self.prod_name_2.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")

    def biller_display3(self):
        
        if self.prod_name_3.get() in self.dict_data:
            letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_3.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
            letter1.place(x=460,y=325)

        elif self.prod_name_3.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")

    def biller_display4(self):
        
        if self.prod_name_4.get() in self.dict_data:
            letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_4.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
            letter1.place(x=460,y=425)

        elif self.prod_name_4.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")

    def biller_display5(self):  
        
        if self.prod_name_5.get() in self.dict_data:
            letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_5.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
            letter1.place(x=460,y=525)

        elif self.prod_name_5.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")

    def biller_display6(self):
        
        if self.prod_name_6.get() in self.dict_data:
            letter1=Label(self.windowbox12,text=self.dict_data[self.prod_name_6.get()],font=("Comic Sans",15,'bold'),fg="white",bg='red')
            letter1.place(x=460,y=625)

        elif self.prod_name_6.get()=="":
            messagebox.showerror("Error!", "product box is empty\nEnter any product name")

        else:
            messagebox.showerror("Invalid name!", "product Not Found")


    def calculate_bill_func(self):
        
        def total_price1():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_1.get()!="" and self.prod_name_1.get()!="":
                    self.total_1=int(self.dict_data[self.prod_name_1.get()])*int(self.qty_1.get())
                    letter1=Label(self.windowbox12,text=str(self.total_1),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=125)
                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")

        def total_price2():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_2.get()!="" and self.prod_name_2.get()!="":
                    self.total_2=int(self.dict_data[self.prod_name_2.get()])*int(self.qty_2.get())
                    letter1=Label(self.windowbox12,text=str(self.total_2),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=225)

                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        def total_price3():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_3.get()!="" and self.prod_name_3.get()!="":
                    self.total_3=int(self.dict_data[self.prod_name_3.get()])*int(self.qty_3.get())
                    letter1=Label(self.windowbox12,text=str(self.total_3),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=325)
                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")

        def total_price4():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_4.get()!="" and self.prod_name_4.get()!="":
                    self.total_4=int(self.dict_data[self.prod_name_4.get()])*int(self.qty_4.get())
                    letter1=Label(self.windowbox12,text=str(self.total_4),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=425)
                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")

        def total_price5():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_5.get()!="" and self.prod_name_5.get()!="":
                    self.total_5=int(self.dict_data[self.prod_name_5.get()])*int(self.qty_5.get())
                    letter1=Label(self.windowbox12,text=str(self.total_5),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=525)
                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")

        def total_price6():
            if self.qty_1.get()!="" or self.qty_2.get()!="" or self.qty_3.get()!="" or self.qty_4.get()!="" or self.qty_5.get()!="" or self.qty_6.get()!="":
                if self.qty_6.get()!="" and self.prod_name_6.get()!="":
                    self.total_6=int(self.dict_data[self.prod_name_6.get()])*int(self.qty_6.get())
                    letter1=Label(self.windowbox12,text=str(self.total_6),font=("Comic Sans",15,'bold'),fg="white",bg='red')
                    letter1.place(x=785,y=625)
                elif (self.qty_1.get()=="" and self.prod_name_5.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()==""):
                    pass
                else:
                    messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")

        total_price1()
        total_price2()
        total_price3()
        total_price4()
        total_price5()
        total_price6()

        if self.qty_1.get()!="" and self.prod_name_1.get()!="":
            self.update_qty1_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_1.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=110)
            print_word2=Label(self.windowbox13,text=str(self.qty_1.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=110)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_1.get()])*int(self.qty_1.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=110)
        elif (self.qty_1.get()!="" and self.prod_name_1.get()=="") or (self.qty_1.get()=="" and self.prod_name_1.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_1=0
        
        
        if self.qty_2.get()!="" and self.prod_name_2.get()!="":
            self.update_qty2_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_2.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=140)
            print_word2=Label(self.windowbox13,text=str(self.qty_2.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=140)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_2.get()])*int(self.qty_2.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=140)
        elif (self.qty_2.get()!="" and self.prod_name_2.get()=="") or (self.qty_2.get()=="" and self.prod_name_2.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_2=0
        
        
        if self.qty_3.get()!="" and self.prod_name_3.get()!="":
            self.update_qty3_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_3.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=170)
            print_word2=Label(self.windowbox13,text=str(self.qty_3.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=170)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_3.get()])*int(self.qty_3.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=170)
        elif (self.qty_3.get()!="" and self.prod_name_3.get()=="") or (self.qty_3.get()=="" and self.prod_name_3.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_3=0
        
        if self.qty_4.get()!="" and self.prod_name_4.get()!="":
            self.update_qty4_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_4.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=200)
            print_word2=Label(self.windowbox13,text=str(self.qty_4.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=200)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_4.get()])*int(self.qty_4.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=200)
        elif (self.qty_4.get()!="" and self.prod_name_4.get()=="") or (self.qty_4.get()=="" and self.prod_name_4.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_4=0
        
        if self.qty_5.get()!="" and self.prod_name_5.get()!="":
            self.update_qty5_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_5.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=230)
            print_word2=Label(self.windowbox13,text=str(self.qty_5.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=230)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_5.get()])*int(self.qty_5.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=230)
        elif (self.qty_5.get()!="" and self.prod_name_5.get()=="") or (self.qty_5.get()=="" and self.prod_name_5.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_5=0
        
        if self.qty_6.get()!="" and self.prod_name_6.get()!="":
            self.update_qty6_func()
            print_word1=Label(self.windowbox13,text=self.prod_name_6.get(),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word1.place(x=10,y=260)
            print_word2=Label(self.windowbox13,text=str(self.qty_6.get()),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word2.place(x=180,y=260)
            print_word3=Label(self.windowbox13,text=str(int(self.dict_data[self.prod_name_6.get()])*int(self.qty_6.get())),font=("Comic Sans MS",14),fg='black',bg='white')
            print_word3.place(x=265,y=260)
        elif (self.qty_6.get()!="" and self.prod_name_6.get()=="") or (self.qty_6.get()=="" and self.prod_name_6.get()!=""):
            messagebox.showerror("Empty box!", "Make sure both\nproduct name and quantity is entered ")
        else:
            self.total_6=0

        self.full_total=self.total_1+self.total_2+self.total_3+self.total_4+self.total_5+self.total_6
        self.tax_price=(self.full_total*0.12)+self.full_total

        print_word6=Label(self.windowbox13,text=str(self.tax_price),font=("Comic Sans MS",14),fg='black',bg='white')
        print_word6.place(x=230,y=350)

        letter2=Label(self.windowbox13,text=str(self.full_total),font=("Comic Sans MS",14),fg='black',bg='white')
        letter2.place(x=265,y=260)


    def update_qty1_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_1.get():
                Found=True
                row [2] =str(int(row[2])-int(self.qty_1.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()


    def update_qty2_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_2.get():
                Found=True
                row [2] = str(int(row[2])-int(self.qty_2.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()


    def update_qty3_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_3.get():
                Found=True
                row [2] = str(int(row[2])-int(self.qty_3.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()

    def update_qty4_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_4.get():
                Found=True
                row [2] = str(int(row[2])-int(self.qty_4.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()

    def update_qty5_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_5.get():
                Found=True
                row [2] = str(int(row[2])-int(self.qty_5.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()

    def update_qty6_func(self):
        file=open('productlist.csv', 'r')
        Reader=csv.reader(file)
        data=[]
        Found=False
        for row in Reader:
            if row[0] == self.prod_name_6.get():
                Found=True
                row [2] = str(int(row[2])-int(self.qty_6.get()))
            data.append(row)
        file.close()
        
        if Found==False:
            messagebox.showerror("Error!", "product Not Found")
        else:
            file=open('productlist.csv','w+', newline='')
            Writer=csv.writer(file)
            Writer.writerows(data)
            file.seek (0)
            file.close()


    def modify(self):
        modify_wind=Frame(self.root,bg="PeachPuff2")
        modify_wind.place(x=0,y=0,height=1080,width=1920)

        letter1=Label(modify_wind,text="What You Want To Modify",font=('times new roman',32,'bold'),fg="black",bg='PeachPuff2')
        letter1.place(x=320,y=100)

        self.img=ImageTk.PhotoImage(file="bg3.jpeg")
        img=Label(modify_wind,image=self.img).place(x=0,y=0,width=1280,height=700)

        
        btn1=Button(modify_wind,text="CHANGE PRICE",command=self.edit_price_page,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=19,height=1)
        btn1.place(x=500,y=255)

        btn2=Button(modify_wind,text="CHANGE QUANTITY",command=self.edit_qty_page,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=19,height=1)
        btn2.place(x=500,y=325)


        btn3=Button(modify_wind,text="REMOVE DATA",command=self.delete_page,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=19,height=1)
        btn3.place(x=500,y=390)


        btn4=Button(modify_wind,text="MAIN MENU",cursor="hand2",command=self.menu,font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=19,height=1)
        btn4.place(x=500,y=455)


    def menu(self):
        menu_wind=Frame(self.root,bg="PeachPuff2",borderwidth=10,relief=RIDGE)
        menu_wind.place(x=0,y=0,height=1080,width=1920)

        self.img=ImageTk.PhotoImage(file="bg3.jpeg")
        img=Label(menu_wind,image=self.img).place(x=0,y=0,width=1280,height=700)

        letter2=Label(menu_wind,text="Hi! Welcome To Reckon Biller",font=('times new roman',32,'bold'),fg="black",bg='PeachPuff2')
        letter2.place(x=320,y=100)

        but1=Button(menu_wind,text="CREATE",command=self.create,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but1.place(x=500,y=200)


        but2=Button(menu_wind,text="ADD DATA",command=self.add_data,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but2.place(x=500,y=265)


        but3=Button(menu_wind,text="MODIFY",command=self.modify,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but3.place(x=500,y=330)


        but4=Button(menu_wind,text="CALCULATE BILL",command=self.bill_calculate,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but4.place(x=500,y=395)

        but5=Button(menu_wind,text="LOGOUT",command=self.login_page,cursor="hand2",font=("Segoe Script",15),fg="white",bg="brown",bd=5,width=15,height=1)
        but5.place(x=500,y=460)


    def clearentry(self):
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.entry4.delete(0,END)
        self.entry3.delete(0,END)

   
    def clearentry1(self):
        self.entry0.delete(0,END)


    def logentryclear(self):
        self.name.delete(0,END)
        self.password.delete(0,END)


    def pasclear(self):
        self.entry2.delete(0,END)
        self.entry2.delete(0,END)


    def nameclear(self):
        self.entry.delete(0,END)


    def create_entry_clear(self):
        self.prod_name.delete(0,END)
        self.price.delete(0,END)
        self.qty.delete(0,END)


    def edit_entry_clear(self):
        self.edit_prod_name.delete(0,END)
        self.new_price.delete(0,END)


root=Tk()

ob=biller(root)

root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     



