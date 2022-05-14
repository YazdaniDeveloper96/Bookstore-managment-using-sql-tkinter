import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/13_farvardin")
#----------------------------------------------------------------------------------######## requirments #######
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from khayyam import JalaliDatetime
#----------------------------------------------------------------------------------##### optional module ######
import os
os.system('cls')
#----------------------------------------------------------------------------------
from DAL.product import Book
from DAL.database_manager import DataBase_manager_book
#----------------------------------------------------------------------------------

class Form:
    #-----------------------------------------------------------------------------############ get time function
    @staticmethod
    def get_time():
        time1=str(JalaliDatetime.now().strftime("%Y %m %A  "))
        time2=str(JalaliDatetime.now().strftime("%H:%M"))
        return time1,time2
    #-----------------------------------------------------------------------------############ set form size function
    def __set_size(self,body,width,height):
        w=width
        h=height
        x=self.main_form.winfo_screenwidth()
        y=self.main_form.winfo_screenheight()
        xs=(x/2)-(w/2)
        ys=(y/2)-(h/2)
        body.geometry("%dx%d+%d+%d"%(w,h,xs,ys))
    #-----------------------------------------------------------------------------############ creating main form
    def __init__(self,book) -> None:
        self.book=book
        self.main_form=Tk()
        self.main_form.title('Library')
        self.__set_size(self.main_form,787,300)

        self.welcome_label=Label(self.main_form,text="سیستم مدیریت کتابخانه کوشا",font=('tahoma',18,BOLD))
        self.date_label1=Label(self.main_form,text=f'{Form.get_time()[0]}',font=('tahoma',12),borderwidth=2,relief="ridge",padx=5)
        self.date_label2=Label(self.main_form,text=f'{Form.get_time()[1]}',font=('tahoma',12),borderwidth=2,relief="ridge",padx=5)
        
        self.show_button=Button(self.main_form,text="نمایش لیست کتاب ها",width=18,font=('tahoma',12,BOLD))
        self.search_button=Button(self.main_form,text="جست و جوی کتاب",width=18,font=('tahoma',12,BOLD),fg="#0000ff")
        self.add_button=Button(self.main_form,text="اضافه کردن کتاب جدید",width=18,font=('tahoma',12,BOLD),fg="#00ff00")
        self.delete_button=Button(self.main_form,text="حذف کتاب",width=18,font=('tahoma',12,BOLD),fg="#ff0000")

        self.welcome_label.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.date_label1.grid(row=1,column=1,columnspan=3,padx=10,pady=(0,5))
        self.date_label2.grid(row=2,column=1,columnspan=3,padx=10,pady=(0,104))
        self.show_button.grid(row=3,column=0,padx=10,pady=(3))
        self.search_button.grid(row=4,column=0,padx=10,pady=3)
        self.add_button.grid(row=3,column=4,padx=10,pady=3)
        self.delete_button.grid(row=4,column=4,padx=10,pady=3)

        self.show_button.bind("<Enter>",lambda event : self.__enter(event,'show'))
        self.show_button.bind("<Leave>",lambda event : self.__leave(event,'show'))
        self.add_button.bind("<Enter>",lambda event : self.__enter(event,'add'))
        self.add_button.bind("<Leave>",lambda event : self.__leave(event,'add'))
        self.search_button.bind("<Enter>",lambda event : self.__enter(event,'search'))
        self.search_button.bind("<Leave>",lambda event : self.__leave(event,'search'))
        self.delete_button.bind("<Enter>",lambda event : self.__enter(event,'delete'))
        self.delete_button.bind("<Leave>",lambda event : self.__leave(event,'delete'))

        self.show_button.bind("<Button-1>",lambda event : self.__show_database(event))
        self.add_button.bind("<Button-1>",lambda event : self.__add_book(event))
        self.search_button.bind("<Button-1>",lambda event : self.__search_book(event))
        self.delete_button.bind("<Button-1>",lambda event : self.__delete_book(event))
        self.main_form.mainloop()
    #----------------------------------------------------------------------------------------
    def __enter(self,event,enter):
        if enter=='show':
            self.show_button.config(bg="#f9a602",fg="#000000")
        elif enter=='add':
            self.add_button.config(bg="#f9a602",fg="#000000")
        elif enter=='search':
            self.search_button.config(bg="#f9a602",fg="#000000")
        else:
            self.delete_button.config(bg="#f9a602",fg="#000000")
    def __leave(self,event,enter):
        if enter=='show':
            self.show_button.config(bg="#f0f0f0")
        elif enter=='add':
            self.add_button.config(bg="#f0f0f0",fg="#00ff00")
        elif enter=='search':
            self.search_button.config(bg="#f0f0f0",fg="#0000ff")
        else:
            self.delete_button.config(bg="#f0f0f0",fg="#ff0000")
    #----------------------------------------------------------------------------------------
    def __show_database(self,event):      #ok
        #-------create new window-------
        book_window=Toplevel(self.main_form)
        book_window.title("نمایش تمامی محصولات")
        self.__set_size(book_window,900,300)
        #-------create table for showing products--------
        tree=ttk.Treeview(book_window,column=('Record','help_number','Title','Author','Publishing_Specifications'),show='headings',height=12)
        tree.grid(row=1,columnspan=1,padx=10,pady=20)
        tree.column('# 1',anchor=CENTER,width=100)
        tree.heading('# 1',text='رکورد')
        tree.column('# 2',anchor=CENTER,width=150)
        tree.heading('# 2',text='شماره راهنما')
        tree.column('# 3',anchor=CENTER,width=300)
        tree.heading('# 3',text='عنوان')
        tree.column('# 4',anchor=CENTER,width=200)
        tree.heading('# 4',text='پدید آور')
        tree.column('# 5',anchor=CENTER,width=125)
        tree.heading('# 5',text='مشخصات ناشر')
        #------get all products---------
        n=1
        for item in self.book:
            tree.insert('','end',text=str(n),values=(item[0],item[1],item[2],item[3],item[4]))
            n+=1
    def __add_book(self,event):           #ok      
        #-------create new window-------
        add_window=Toplevel(self.main_form)
        add_window.title("ثبت کتاب جدید در کتابخانه")
        self.__set_size(add_window,810,300)
        #-------create table for showing products--------
        record_label=Label(add_window,text='شماره رکورد')
        record_entry=Entry(add_window,width=100)
        help_number_label=Label(add_window,text='شماره راهنما')
        help_number_entry=Entry(add_window,width=100)
        title_label=Label(add_window,text='عنوان')
        title_entry=Entry(add_window,width=100)
        author_label=Label(add_window,text='پدید آور')
        author_entry=Entry(add_window,width=100)
        Publishing_Specifications_label=Label(add_window,text='مشخصات ناشر')
        Publishing_Specifications_entry=Entry(add_window,width=100)
        #------------------------------------
        submit_button1=Button(add_window,text="ثبت کتاب در کتابخانه",font=('tahoma',12,BOLD))
        submit_button2=Button(add_window,text="پاک کردن فیلد ها",font=('tahoma',12,BOLD))
        #------------------------------------
        record_label.grid(row=0,column=0,padx=10,pady=10)
        record_entry.grid(row=0,column=1,columnspan=6)
        ############
        help_number_label.grid(row=1,column=0,padx=10,pady=10)
        help_number_entry.grid(row=1,column=1,columnspan=6)
        ############
        title_label.grid(row=2,column=0,padx=10,pady=10)
        title_entry.grid(row=2,column=1,columnspan=6)
        ############
        author_label.grid(row=3,column=0,padx=10,pady=10)
        author_entry.grid(row=3,column=1,columnspan=6)
        ############
        Publishing_Specifications_label.grid(row=4,column=0,padx=10,pady=10)
        Publishing_Specifications_entry.grid(row=4,column=1,columnspan=6)
        ############
        submit_button1.grid(row=5,column=0,padx=10,pady=(50,0))
        submit_button2.grid(row=5,column=1,padx=10,pady=(50,0))
        ##############################################################################################
        def adding(event):
            record=record_entry.get()
            help_number=help_number_entry.get()
            title=title_entry.get()
            author=author_entry.get()
            Publishing_Specifications=Publishing_Specifications_entry.get()
            try:
                if int(record):
                    p1=Book(int(record),help_number,title,author,Publishing_Specifications)
                    adding=DataBase_manager_book()
                    adding.insert_into_type1(p1)
                    messagebox.showinfo(add_window,message="کتاب شما با موفقیت در کتابخانه ثبت گردید\nدر صورت عدم ثبت کتاب , یکبار برنامه بسته و سپس باز کنید")

            except Exception  as error:
                messagebox.showinfo(add_window,message="لطفا شماره رکورد را وارد کنید")

        def deleting(event):
            record_entry.delete(0,END)
            help_number_entry.delete(0,END)
            title_entry.delete(0,END)
            author_entry.delete(0,END)
            Publishing_Specifications_entry.delete(0,END)
        ##############################################################################################
        def change_color_of_button(event,type):
            if type=="enter1":
                submit_button1.config(bg="#f9a602",fg="#000000")
            elif type=="enter2":
                submit_button2.config(bg="#f9a602",fg="#000000")
            elif type=="leave1":
                submit_button1.config(bg="#f0f0f0")
            else:
                submit_button2.config(bg="#f0f0f0")
        ##############################################################################################
        submit_button1.bind("<Button-1>",lambda event :adding(event))
        submit_button1.bind("<Enter>",lambda event:change_color_of_button(event,'enter1'))
        submit_button1.bind("<Leave>",lambda event:change_color_of_button(event,'leave1'))
        submit_button2.bind("<Button-1>",lambda event :deleting(event))
        submit_button2.bind("<Enter>",lambda event:change_color_of_button(event,'enter2'))
        submit_button2.bind("<Leave>",lambda event:change_color_of_button(event,'leave2'))
    def __search_book(self,event):        #ok
        search_window=Toplevel(self.main_form)
        search_window.title("جست و جوی  کتاب  در کتابخانه")
        self.__set_size(search_window,900,260)
        #-------create table for showing products--------
        frame_1=Frame(search_window)
        frame_2=Frame(search_window)
        frame_3=Frame(search_window)
        record_label=Label(frame_1,text='شماره رکورد')
        record_entry=Entry(frame_1,width=133)
        record_entry.insert(END,'شماره رکورد را وارد کنید')
        search_button=Button(frame_3,text="جست و جو",font=('tahoma',12,BOLD))
        # delete_button=Button(search_window,text="پاک کردن فیلد",font=('tahoma',12,BOLD))
        #--------------------------------------------------------------------------------------
        tree=ttk.Treeview(frame_2,column=('Record','help_number','Title','Author','Publishing_Specifications'),show='headings',height=3)
        tree.column('# 1',anchor=CENTER,width=100)
        tree.heading('# 1',text='رکورد')
        tree.column('# 2',anchor=CENTER,width=150)
        tree.heading('# 2',text='شماره راهنما')
        tree.column('# 3',anchor=CENTER,width=300)
        tree.heading('# 3',text='عنوان')
        tree.column('# 4',anchor=CENTER,width=200)
        tree.heading('# 4',text='پدید آور')
        tree.column('# 5',anchor=CENTER,width=125)
        tree.heading('# 5',text='مشخصات ناشر')
        def search(event):
            for record in tree.get_children():
                tree.delete(record)
            record=record_entry.get()
            try:
                if int(record):
                    search=DataBase_manager_book()
                    result=search.search_into_type1(record)
                    if result:
                        n=1
                        for item in result:
                            tree.insert('','end',text=str(n),values=(item[0],item[1],item[2],item[3],item[4]))
                            record_entry.delete(0,END)
                            record_entry.insert(END,"شماره رکورد را وارد کنید")
                    else:
                        for record in tree.get_children():
                            tree.delete(record)
                        messagebox.showwarning(search_window,message="رکورد مورد نظر یافت نشد")
                        record_entry.delete(0,END)
                        record_entry.insert(END,"شماره رکورد را وارد کنید")
            except Exception as error:
                messagebox.showwarning(search_window,message="لطفا شماره رکورد را درست وارد کنید")
                record_entry.delete(0,END)
                record_entry.insert(END,"شماره رکورد را وارد کنید")
        #----------------------------------------------------------------------------------------------------
        def change_color_of_button(event,type):
            if type=="enter":
                search_button.config(bg="#f9a602",fg="#000000")
            else:
                search_button.config(bg="#f0f0f0")
        #----------------------------------------------------------------------------------------------------
        search_button.bind("<Enter>",lambda event :change_color_of_button(event,'enter'))
        search_button.bind("<Leave>",lambda event :change_color_of_button(event,'leave'))
        #----------------------------------------------------------------------------------------------------
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        record_label.pack(side=LEFT,padx=5,pady=(30,40))
        record_entry.pack(side=LEFT,pady=(30,40),fill=BOTH)
        tree.pack()
        search_button.pack(pady=(30,0))
        #----------------------------------------------------------------------------------------------------
        search_button.bind("<Button-1>",lambda event : search(event))
    def __delete_book(self,event):        #ok
        #-------create new window-------
        delete_window=Toplevel(self.main_form)
        delete_window.title("حذف کتاب  از کتابخانه")
        self.__set_size(delete_window,730,150)
        #-------create table for showing products--------
        record_label=Label(delete_window,text='شماره رکورد')
        record_entry=Entry(delete_window,width=100)
        record_entry.insert(END,"شماره رکورد را وارد کنید")
        #------------------------------------
        submit_button=Button(delete_window,text="حذف کتاب",font=('tahoma',12,BOLD))
        #------------------------------------
        record_label.grid(row=0,column=0,padx=10,pady=10)
        record_entry.grid(row=0,column=1,padx=(1,10),columnspan=6)
        ############
        submit_button.grid(row=5,column=0,padx=10,pady=(50,0))
        #--------------------------------------------------------------------------------------------------
        def delete_book(event):
            record=record_entry.get()
            try:
                if int(record):
                    #----------------------------------------------------------------------------------------------
                    search=DataBase_manager_book()
                    result=search.search_into_type1(record)
                    #----------------------------------------------------------------------------------------------
                    if result:
                        db=DataBase_manager_book()
                        db.delete_1_record(record)
                        messagebox.showwarning(delete_window,message="کتاب مورد نظر با موفقیت حذف شد")
                        ###############
                        record_entry.delete(0,END)
                        record_entry.insert(END,"شماره رکورد را وارد کنید")
                    else:
                        messagebox.showwarning(delete_window,message="کتاب مورد نظر در دیتابیس موجود نیست")
                        record_entry.delete(0,END)
                        record_entry.insert(END,"شماره رکورد را وارد کنید")
            except Exception as error:
                messagebox.showwarning(delete_window,message="لطفا شماره رکورد را درست وارد کنید")
                record_entry.delete(0,END)
                record_entry.insert(END,"شماره رکورد را وارد کنید")
        #--------------------------------------------------------------------------------------------------
        def change_color_of_button(event,type):
            if type=="enter":
                submit_button.config(bg="#f9a602",fg="#000000")
            else:
                submit_button.config(bg="#f0f0f0")
        #--------------------------------------------------------------------------------------------------
        submit_button.bind("<Button-1>",lambda event :delete_book(event))
        submit_button.bind("<Enter>",lambda event :change_color_of_button(event,'enter'))
        submit_button.bind("<Leave>",lambda event :change_color_of_button(event,'leave'))
