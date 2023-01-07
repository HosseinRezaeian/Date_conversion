from tkinter import *
import tkinter as tk
from tkinter import ttk
window=Tk()
window.geometry('270x400')



get_date=Entry(window,width='30')
get_date.pack()

def select_format(sel):
    print(format_list.get(format_list.curselection()))




def get_date():
    print(selectin.get())
    format_list.delete(0,END)
    format= ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby"]
  
    for each_item in range(len(format)):
      
        format_list.insert(END, format[each_item])
      
   

    
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

sub=ttk.Button(text='submit',command=get_date)
sub.pack()




window.mainloop()