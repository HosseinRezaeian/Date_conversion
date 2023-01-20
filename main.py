from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
import datetime
import jdatetime
import calendar
window=Tk()
window.geometry('350x400')
window.resizable(0,0)
window.title('Date Conversion')
List_Format=["%Y/%m/%d","%A ","%B %d",]

List_Format_Selection=["%Y %m %d","%Y-%m-%d","%Y/%m/%d","%A ","%B %d","%B"]

def gregorian(date):
    if len(date)>4:
        try:
            sgdate=''
            date=jdatetime.datetime.strptime(date, '%Y-%m-%d').date()
            leap_jalali=date.isleap()
            sgdate="{} is leap: {}\n".format(str(date.year),leap_jalali)
            gdate=jdatetime.date(year=date.year,month=date.month,day=date.day).togregorian()
            sgdate+="{} is leap: {}\n".format(str(gdate.year),calendar.isleap(int(gdate.year)))
            for item in List_Format:
                sgdate = '\n'.join([sgdate, gdate.strftime(item)])
            list_sel=[]
            for item in List_Format_Selection:
                list_sel.append(gdate.strftime(item))   
            copy_format(list_sel) 
            show_res.config(text=sgdate)
        except:
            show_res.config(text="Invalid Date")


def jalali(date):
    if len(date)>4:
        try:
            sjdate=''
            date=datetime.datetime.strptime(date, '%Y-%m-%d')
            sjdate="{} is leap: {}\n".format(str(date.year),calendar.isleap(int(date.year)))
            print(calendar.isleap(int(date.year)))
            jdate=jdatetime.date.fromgregorian(date=date)
            sjdate+="{} is leap: {}\n".format(str(jdate.year),jdate.isleap())
            for item in List_Format:
                sjdate = '\n'.join([sjdate, jdate.strftime(item)])
            
            list_sel=[]
            for item in List_Format_Selection:
                list_sel.append(jdate.strftime(item))   
            copy_format(list_sel) 
            
            show_res.config(text=sjdate)
        except:
            show_res.config(text="Invalid Date")
            


def Separation(date):
    date_list=[]
    if len(date)==4 and date.isdigit():
        if int(date)>=1000:
            return date
         
        
    elif 10>=len(date)>=8:
        
        r=re.compile('\d{4}[ /-]\d{2}[ /-]\d{2}')
        r2=re.compile('\d{4}[ /-]\d{1}[ /-]\d{1}')
        r3=re.compile('\d{4}[ /-]\d{2}[ /-]\d{1}')
        r4=re.compile('\d{4}[ /-]\d{1}[ /-]\d{2}')
        
        r1=re.compile('\d{8}')
        if bool(r.match(date)) or bool(r2.match(date)) or bool(r3.match(date)) or bool(r4.match(date)):
            if only_number(date):
                if '/' in date:
                    date_list=date.split('/')
                    
                elif '-' in date:
                    date_list=date.split('-')
                    
                elif ' ' in date:
                    date_list=date.split(' ')
                
        
        elif bool(r1.match(date)):
            date=int(date)
            date=str(date)
            if bool(r1.match(date)):
                date_list=[]
                date_list.append(date[0:4])
                date_list.append(date[4:6])
                date_list.append(date[6:8])
             
        
        if len(date_list)>0 :
            if 12>=int(date_list[1])>0 and 31>=int(date_list[2])>0:
                    return '{}-{}-{}'.format(date_list[0],date_list[1],date_list[2])
        else:
            None






def select_format(sel):
    if str(format_list.get(format_list.curselection()))!="":
        window.clipboard_clear()
        window.clipboard_append(str(format_list.get(format_list.curselection())))




def only_number(s):
    for c in s:
        if c.isdigit()==False:
            if c =='/' or c =='-' or c =='_' or c =='|' or c ==' ':
                continue
            else:
                return False
    return True
            
            


def copy_format(list_date):
    
    
    format_list.delete(0,END)
    format= list_date
  
    for each_item in range(len(format)):
        format_list.insert(END, format[each_item])
      
      
      
def get_date(event):
    date=Separation(str(get_datejorg.get()))
    if date != None:
        if 'jalali' in str(selectin.get()) :
            jalali(date)   
        elif 'gregorian' in str(selectin.get()) :
            gregorian(date) 
            
            
def get_date_butt():
    get_date('')           
            

window.bind('<Return>', get_date)



get_datejorg=Entry(window,width='30')
get_datejorg.place(x=55,y=20)
n = tk.StringVar()
selectin = ttk.Combobox(window,state="readonly", width = 12, textvariable = n)

# Adding combobox drop down list
selectin['values'] = (' to gregorian', 
                          ' to jalali',
                          )

selectin.place(x=120,y=55)
selectin.current(1)

show_res=Label(window,text='')
show_res.place(y=80,x=120)

format_list = Listbox(window,height=5,width=30, selectmode = "single")
format_list.place(x=55,y=220)
format_list.bind('<<ListboxSelect>>',select_format)

con=ttk.Button(text='canvert',command=get_date_butt)
con.place(x=130,y=360)




window.mainloop()