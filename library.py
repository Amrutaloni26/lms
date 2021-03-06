from tkinter import*
import tkinter as tk

from tkinter import ttk 
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
import logging


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")    
        self.root.geometry("1550x800+0+0") 
        loggers=logging.getLogger()
        
        
        
        
       # ==================================== variable ===========================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateretnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()
        self.search_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=16,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=90,width=1279,height=350)

#=================================================DATA FRAME LEFT=================================================
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",10,"bold"))
        DataFrameLeft.place(x=0,y=6,width=750,height=320)

        lblmemebr=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",9,"bold"),padx=2,pady=6)
        lblmemebr.grid(row=0,column=0,sticky=W)


        

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",10,"bold"),width=27,state="readonly")
        comMember['value']=("Admin Staff","Student","Lecturer ")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,font=("arial",10,"bold"),text="PRN NO:",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        

        



        lblTitle=Label(DataFrameLeft,font=("arial",10,"bold"),text="ID NO",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)


        lblFirstName=Label(DataFrameLeft,font=("arial",10,"bold"), text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)


        lblLastName=Label(DataFrameLeft,font=("arial",10,"bold"),text="Surname",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,font=("arial",10,"bold"),text="Address1:",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)


        lblAddress2=Label(DataFrameLeft,font=("arial",10,"bold"),text="Address2:",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

      
        lblPostCode=Label(DataFrameLeft,font=("arial",10,"bold"),text=" Post Code:",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
      


        lblMobile=Label(DataFrameLeft,font=("arial",10,"bold"),text="Mobile Number",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)



        lblBookId=Label(DataFrameLeft,font=("arial",10,"bold"),text="Book id",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        txtBookId.config(state=DISABLED)




        lblBookTitle=Label(DataFrameLeft,font=("arial",10,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        txtBookTitle.config(state=DISABLED)


        lblAuthor=Label(DataFrameLeft,font=("arial",10,"bold"),text="Author Name:",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        txtAuthor.config(state=DISABLED)




        lblDateBorrowed=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)



   
        lblDateDue=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)



        lblDaysOnBook=Label(DataFrameLeft,font=("arial",10,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)



        lblLateReturnFine=Label(DataFrameLeft,font=("arial",10,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.lateretnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

      


        lblDateOverdate=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDate.grid(row=7,column=3)





        lblActualPrice=Label(DataFrameLeft,font=("arial",10,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.finallprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

#=============================================DATA FRAME RIGHT=======================================================


        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",font=("arial",11,"bold"),text="Book Details")
        DataFrameRight.place(x=750,y=5,width=450,height=318)

        lblPRN_NO=Label(DataFrameRight,font=("arial",8,"bold"),text="PRN NO:",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=0,column=2,sticky=W)
        txtPRN_NO=Entry(DataFrameRight,font=("arial",8,"bold"),textvariable=self.search_var,width=20)
        txtPRN_NO.grid(row=0,column=3)
        
        btnAddData=Button(DataFrameRight,command=self.search,text="Search", font=("arial",7,"bold"),width=12,bg="grey",fg="white")
        btnAddData.grid(row=0,column=4)



        listScrollbar=Scrollbar(DataFrameRight) 
        listScrollbar.grid(row=0,column=1,sticky="ns") 
        conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT B.BookID,B.BookTitle,B.AuthorID,A.AuthorName,B.PubID,P.PublisherName FROM  library.BOOK B,library.publisher P,library.author A   WHERE B.AuthorID=A.AuthorID AND B.PubID=P.PubID")
        rows=my_cursor.fetchall()
        

        
        def SelectBook(event=""):
                value=str(listBox.get(listBox.curselection()))
                x=value
                for row in rows:
                  if(x==row[1]):
                        self.bookid_var.set(row[0])
                        self.booktitle_var.set(row[1])
                        self.author_var.set(row[3]) 
                        
                        
                        d1=datetime.date.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.daysonbook_var.set(15)
                        self.lateretnfine_var.set("Rs.50")
                        self.dateoverdue_var.set("NO")
                        self.finallprice_var.set("Rs.788")
                
                                                                                                                  
                        
                        
        listBox=Listbox(DataFrameRight,font=("arial",11,"bold"),width=15,height=14)
        for item in rows:
             listBox.insert(END,item[1])
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)    

        listScrollbar.config(command=listBox.yview)

            

#=====================================================BUTTONS FRAME==================================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=425,width=1279,height=50)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)


        btnAddData=Button(Framebutton,command=self.update,text="Update", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)


        btnAddData=Button(Framebutton,command=self.delete,text="Delete", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)


        btnAddData=Button(Framebutton,command=self.reset,text="Reset", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)


        btnAddData=Button(Framebutton,command=self.iExit,text="Exit", font=("arial",10,"bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
#==================================================Information Frame============================================ 

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=475,width=1280,height=167)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=5,width=1220,height=130)
        
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        
        
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","MemID","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","latereturnfine","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        







        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN   NO.")
        self.library_table.heading("MemID",text="MemID")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of borrowed")
        self.library_table.heading("datedue",text="Date Due")

        #self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        #self.library_table.heading("dateoverdue",text="DateOverDue")            
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        
        
        self.library_table.column("membertype",width=100)             
        self.library_table.column("prnno",width=100)
        self.library_table.column("MemID",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table. column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)

        self.library_table.column("datedue",width=100)
       # self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)

       # self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
       # self.loggers.info("Inside add data ")  
       
     if(not self.validate()):      
        conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT COUNT(1) FROM member WHERE PRN_NO=%s",(self.prn_var.get(),))
        if my_cursor.fetchone()[0]:
         my_cursor.execute("SELECT COUNT(1) FROM borrowdetail WHERE PRN_NO=%s AND BookID=%s",(self.prn_var.get(),self.bookid_var.get()))
         data=my_cursor.fetchone()[0]
         if data>0:
          messagebox.showerror("Error","The Book is allready borrowed!!")
          return
         else:
           my_cursor.execute("insert into borrowdetail values (%s,%s,%s,%s,%s,%s)",(self.dateborrowed_var.get(),self.lateretnfine_var.get(),self.finallprice_var.get(),self.datedue_var.get(),self.prn_var.get(),self.bookid_var.get()))                             
          
        else:
         my_cursor.execute("insert into member values (%s,%s,%s,%s,%s)",( self.prn_var.get(),self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get()))                            
         my_cursor.execute("insert into address values (%s,%s,%s,%s,%s)",(self.address1_var.get(),self.address2_var.get(),self.mobile_var.get(),self.postcode_var.get(),self.prn_var.get()))                             
         my_cursor.execute("insert into borrowdetail values (%s,%s,%s,%s,%s,%s)",(self.dateborrowed_var.get(),self.lateretnfine_var.get(),self.finallprice_var.get(),self.datedue_var.get(),self.prn_var.get(),self.bookid_var.get()))                             
        conn.commit()
        conn.close()  
        self.fatch_data()
    
        messagebox.showinfo("Success","Insertion has been done successfully!")
        
        
        
    def update(self):
      if(not self.validate()):      
        conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("update member set MemberType=%s,MemID=%s,F_name=%s,L_name=%s where  PRN_NO=%s",(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.prn_var.get()))
        my_cursor.execute("update address set Address1=%s,Address2=%s,Postcode=%s,MobNO=%s where  PRN_NO=%s",(self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.prn_var.get()))
        my_cursor.execute("update borrowdetail set BorrowedDate=%s,DueDate=%s,LateReturnFine=%s,FinalPrice=%s  where  BookID=%s and PRN_NO=%s",(self.dateborrowed_var.get(),self.datedue_var.get(),self.lateretnfine_var.get(),self.finallprice_var.get(),self.bookid_var.get(),self.prn_var.get()))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member Has Been Updated")
                
                
                
                
    def  fatch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT M.MemberType,M.PRN_NO,M.MemID,M.F_name,M.L_name,AD.address1,AD.ADDRESS2,AD.POSTCODE,AD.MOBNO,B.BOOKID,B.BOOKTITLE,A.AuthorName,BD.BorrowedDate,BD.DueDate,BD.LateReturnFine,BD.FinalPrice FROM  library.MEMBER M,library.BOOK B,library.publisher P,library.author A,library.ADDRESS AD,library.borrowdetail BD  WHERE M.PRN_NO=AD.PRN_NO AND M.PRN_NO=BD.PRN_NO AND BD.BOOKID=B.BOOKID AND B.PUBID=P.PubID AND B.AUTHORID=A.AuthorID ")
            rows=my_cursor.fetchall()

            self.library_table.delete(*self.library_table.get_children())
            if len(rows)!=0:
                    for i in rows:
                        self.library_table.insert("",END,values=i)
                    conn.commit()
            conn.close()                
                                  
    def get_cursor(self,event=""):

            cursor_row=self.library_table.focus()
            content=self.library_table.item(cursor_row)
            row=content['values']

            self.member_var.set(row[0]),  
            self.prn_var.set(row[1]),
            self.id_var.set(row[2]),
            self.firstname_var.set(row[3]),
            self.lastname_var.set(row[4]),
            self.address1_var.set(row[5]),
            self.address2_var.set(row[6]),
            self.postcode_var.set(row[7]),
            self.mobile_var.set(row[8]),
            self.bookid_var.set(row[9]),
            self.booktitle_var.set(row[10]),
            self.author_var.set(row[11]),
            self.dateborrowed_var.set(row[12]),
            self.datedue_var.set(row[13]),
            self.daysonbook_var.set(15),
            self.lateretnfine_var.set(row[14]),
            self.dateoverdue_var.set("NO"),
            self.finallprice_var.set(row[15])
            
    def showData(self):
            
            self.popup_bonus()

            
            
            
            
            
    def popup_bonus(self):
            
        win = tk.Toplevel()
        win.wm_title("Show Book Details")
        win.geometry('400x300')
        txtBox=Text(win, font=("arial",11,"bold"),width=50,height=14,padx=2,pady=6)
        txtBox.grid(row=0,column=0)
        txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")    
        txtBox.insert(END,"PRN NO:\t\t"+self.prn_var.get()+"\n")    
        txtBox.insert(END,"ID NO:\t\t"+self.id_var.get()+"\n")    
        txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")    
        txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")    
        txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")    
        txtBox.insert(END,"Address:\t\t"+self.address2_var.get()+"\n")    
        txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")    
        txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")    
        txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")    
        txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")    
        txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")    
        txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+"\n")    
        txtBox.insert(END,"DateDue:\t\t"+self.datedue_var.get()+"\n")    
        txtBox.insert(END,"DaysOnBook:\t\t"+self.daysonbook_var.get()+"\n")    
        txtBox.insert(END,"LateRetnFine:\t\t"+self.lateretnfine_var.get()+"\n")    
        txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue_var.get()+"\n")    
        txtBox.insert(END,"Finallprice:\t\t"+self.finallprice_var.get()+"\n")   


        b=ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0) 
        
    def search(self):
            
        win = tk.Toplevel()
        win.wm_title("Show Book Details")
        win.geometry("1000x1000")
     
        FrameDetails=Frame(win,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=0,width=1280,height=167)
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=5,width=1220,height=130)
        
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        
        
        
        library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","MemID","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","latereturnfine","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        
        xscroll.config(command=library_table.xview)
        yscroll.config(command=library_table.yview)

        







        library_table.heading("membertype",text="Member Type")
        library_table.heading("prnno",text="PRN   NO.")
        library_table.heading("MemID",text="MemID")
        library_table.heading("firstname",text="First Name")
        library_table.heading("lastname",text="Last Name")
        library_table.heading("adress1",text="Address1")
        library_table.heading("adress2",text="Address2")
        library_table.heading("postid",text="Post ID")
        library_table.heading("mobile",text="Mobile Number")
        library_table.heading("bookid",text="Book ID")
        library_table.heading("booktitle",text="Book Title")
        library_table.heading("author",text="Author")
        library_table.heading("dateborrowed",text="Date Of borrowed")
        library_table.heading("datedue",text="Date Due")

        #self.library_table.heading("days",text="DaysOnBook")
        library_table.heading("latereturnfine",text="LateReturnFine")
        #self.library_table.heading("dateoverdue",text="DateOverDue")            
        library_table.heading("finalprice",text="Final Price")
        
        library_table["show"]="headings"
        library_table.pack(fill=BOTH,expand=1)
        
        
        
        library_table.column("membertype",width=100)             
        library_table.column("prnno",width=100)
        library_table.column("MemID",width=100)
        library_table.column("firstname",width=100)
        library_table.column("lastname",width=100)
        library_table.column("adress1",width=100)
        library_table.column("adress2",width=100)
        library_table. column("postid",width=100)
        library_table.column("mobile",width=100)
        library_table.column("bookid",width=100)
        library_table.column("booktitle",width=100)
        library_table.column("author",width=100)
        library_table.column("dateborrowed",width=100)

        library_table.column("datedue",width=100)
       # self.library_table.column("days",width=100)
        library_table.column("latereturnfine",width=100)

       # self.library_table.column("dateoverdue",width=100)
        library_table.column("finalprice",width=100)


        # b=ttk.Button(win, text="Okay", command=win.destroy)
        # b.grid(row=10, column=2) 
        
        conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT M.MemberType,M.PRN_NO,M.MemID,M.F_name,M.L_name,AD.address1,AD.ADDRESS2,AD.POSTCODE,AD.MOBNO,B.BOOKID,B.BOOKTITLE,A.AuthorName,BD.BorrowedDate,BD.DueDate,BD.LateReturnFine,BD.FinalPrice FROM  library.MEMBER M,library.BOOK B,library.publisher P,library.author A,library.ADDRESS AD,library.borrowdetail BD  WHERE   M.PRN_NO=AD.PRN_NO AND M.PRN_NO=BD.PRN_NO AND BD.BOOKID=B.BOOKID AND B.PUBID=P.PubID AND B.AUTHORID=A.AuthorID AND  M.PRN_NO=%s",(self.search_var.get(),))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                    self.library_table.delete(*library_table.get_children())
                    for i in rows:
                        library_table.insert("",END,values=i)
                    conn.commit()
        conn.close()        
           

    def validate(self):
            message=""
            if(self.member_var.get()==""):
                    message="Member type is required"
                    messagebox.showerror(message)
                    return True

            if(self.prn_var.get()==""):
                    message="PRN NO is required"
                    messagebox.showerror(message)
                    return True
                    
            if(self.id_var.get()==""):
                    message="ID NO is required"
                    messagebox.showerror(message)
                    return True
                          
            elif(self.id_var.get().isdigit()==False):
                    message="ID NO onlys takes  integer value"
                    messagebox.showerror(message)
                    return True 
            
            if(self.firstname_var.get()==""):
                    message="Firstname is required"
                    messagebox.showerror(message)
                    return True
            
            if(self.lastname_var.get()==""):
                    message="Lastname is required"
                    messagebox.showerror(message)
                    return True  
                      
            if(self.address1_var.get()==""):
                    message="Address1 is required"
                    messagebox.showerror(message)
                    return True
            
            if(self.address2_var.get()==""):
                    message="Address2 is required"
                    messagebox.showerror(message)
                    return True
                
            if(self.postcode_var.get()==""):
                    message="Post code is required"
                    messagebox.showerror(message)
                    return True        
            elif(self.postcode_var.get().isdigit()==False):
                    message="Post code onlys takes  integer value"
                    messagebox.showerror(message)
            elif(len(self.postcode_var.get())!=6):
                    message="Please enter valid post code"
                    messagebox.showerror(message)
                    return True
            if(self.mobile_var.get()==""):
                    message="Mobile number is required"
                    messagebox.showerror(message)
                    return True        
            elif(self.mobile_var.get().isdigit()==False):
                    message="Mobile number onlys takes  integer value"
                    messagebox.showerror(message)
            elif(len(self.mobile_var.get())!=10):
                    message="Please enter valid mobile number"
                    messagebox.showerror(message)
            if(self.bookid_var.get()==""):
                    message="Book Id is required"
                    messagebox.showerror(message)
                    return True         

            if(self.booktitle_var.get()==""):
                    message="Book title is required"
                    messagebox.showerror(message)
                    return True 
            if(self.author_var.get()==""):
                    message="Author is required"
                    messagebox.showerror(message)
                    return True
            if(self.dateborrowed_var.get()==""):
                    message="Date borrowed is required"
                    messagebox.showerror(message)
                    return True 
            if(self.datedue_var.get()==""):
                    message="Due Date is required"
                    messagebox.showerror(message)
                    return True
            
            if(self.daysonbook_var.get()==""):
                    message="days on book is required"
                    messagebox.showerror(message)
                    return True
            if(self.lateretnfine_var.get()==""):
                    message="late return fine is required"
                    messagebox.showerror(message)
                    return True 
            if(self.dateoverdue_var.get()==""):
                    message="Date overdue is required"
                    messagebox.showerror(message)
                    return True
            if(self.finallprice_var.get()==""):
                    message="Final price is required"
                    messagebox.showerror(message)
                    return True
            
            return False   
             
            
                    
    def reset(self):
            self.member_var.set(""),    
            self.prn_var.set(""),    
            self.id_var.set(""),    
            self.firstname_var.set(""),    
            self.lastname_var.set(""),    
            self.address1_var.set(""),    
            self.address2_var.set(""),    
            self.postcode_var.set(""),    
            self.mobile_var.set(""),    
            self.bookid_var.set(""),    
            self.booktitle_var.set(""),    
            self.author_var.set(""),    
            self.dateborrowed_var.set(""),    
            self.datedue_var.set(""),    
            self.daysonbook_var.set(""),    
            self.lateretnfine_var.set(""),    
            self.dateoverdue_var.set(""),    
            self.finallprice_var.set(""),    
            
            
            
    def iExit(self):
            iExit=tkinter.messagebox.askyesno("Library Management System","Do You Want To Exit?")
            if iExit>0:
                    self.root.destroy()
                    return
            
    def delete(self):
            if self.prn_var.get()=="" or self.id_var.get()=="":
                    messagebox.showerror("Error","First Select The Member")
            else: 
                    conn=mysql.connector.connect(host="localhost",username="root",password="amu26",database="library")
                    my_cursor=conn.cursor() 
                   # query="delete from member where PRN_NO=%s"
                    value=(self.prn_var.get(),)
                     
                    my_cursor.execute("delete from borrowdetail where PRN_NO=%s AND BOOKID=%s",(self.prn_var.get(),self.bookid_var.get())) 
                    my_cursor.execute("SELECT COUNT(1) FROM borrowdetail WHERE PRN_NO=%s",(self.prn_var.get(),))
                    data=my_cursor.fetchone()[0]
                    print(data)
                    if (data==0):
                      my_cursor.execute("delete from member where PRN_NO=%s",value) 
                      my_cursor.execute("delete from address where PRN_NO=%s",value)  
                    
                    
                    conn.commit()
                    self.fatch_data()
                    self.reset()
                    conn.close()
                        
                    messagebox.showinfo("Success","Member Has Been Deleted")                               
                                        
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root) 
    root.mainloop()   
