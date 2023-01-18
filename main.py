from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
import datetime
import jdatetime
window=Tk()
window.geometry('350x400')

def gregorian(date):
    if len(date)>4:
        try:
            date=jdatetime.datetime.strptime(date, '%Y-%m-%d').date()
            gdate=jdatetime.date(year=date.year,month=date.month,day=date.day).togregorian()
            show_res.config(text=gdate)
        except:
            print("Invalid Date")


def jalali(date):
    if len(date)>4:
        try:
            date=datetime.datetime.strptime(date, '%Y-%m-%d')
            jdate=jdatetime.date.fromgregorian(date=date)
            show_res.config(text=jdate)
        except:
            print("Invalid Date")



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
    print('tesss',format_list.get(format_list.curselection()))




def only_number(s):
    for c in s:
        if c.isdigit()==False:
            if c =='/' or c =='-' or c =='_' or c =='|' or c ==' ':
                continue
            else:
                return False
    return True
            
            



def copy_format():
    Separation(str(get_datejorg.get()))
    
    format_list.delete(0,END)
    format= ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby"]
  
    for each_item in range(len(format)):
        format_list.insert(END, format[each_item])
      
      
      
def get_date():
    date=Separation(str(get_datejorg.get()))
    if date != None:
        if 'jalali' in str(selectin.get()) :
            jalali(date)   
        elif 'gregorian' in str(selectin.get()) :
            gregorian(date) 
            
get_datejorg=Entry(window,width='30')
get_datejorg.pack()  
n = tk.StringVar()
selectin = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
selectin['values'] = (' to gregorian', 
                          ' to jalali',
                          )

selectin.pack()
selectin.current(1)



format_list = Listbox(window,height=2, selectmode = "single")
format_list.pack()
format_list.bind('<<ListboxSelect>>',select_format)
show_res=Label(window,text='')
show_res.pack()
con=ttk.Button(text='canvert',command=get_date)
con.pack()




window.mainloop()