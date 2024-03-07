
# Name		    :	Muhammad Tuheed Ahmed
# Roll Number	 :	36820
# Email		    :	tuheedahmed55@gmail.com
# Project		 :	Currency Converter App




#  import library
from currency_converter import CurrencyConverter
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *


# currency list
currency = ["USD","EUR","CAD","INR","GBP","JPY","BRL","CHF","BGN","NZD","AUD","CNY","CZK","DKK","HKD","HUF","ISK","IDR","KRW","MYR","MXN",]


# import color
clr0 = "#FFFFFF"    #white
clr1 = "#333333"    #black
clr2 = "#1E90FF"    #blue
clr3 = "#E85051"    #red


# define variable
c = CurrencyConverter()


# create  window
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")
window.config(bg=clr0)
window.resizable(height=FALSE, width=FALSE)


# main frame
main = Frame(window,relief="solid",width=300,height=260,bg=clr0)
main.grid(row=1,column=0)


# define function
def clicked():
     try:
        amount = float(value.get())
        currency1 = str(combo1.get())
        currency2 = str(combo2.get())
        data = c.convert(amount,currency1,currency2)


# display result
        result_text = f"{round(data , 2)}  {currency2}"
        label5 = tk.Label(main,text=result_text, font = "Times 18 bold",relief="solid",anchor=CENTER,width=16,height=2,bg=clr0)
        label5.place(x=40, y=20)


# display error
     except ValueError:
        messagebox.showerror("Error", "invalid currency/currency not supported. Please enter a valid currency.")
     except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
     except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {e}")


# top frame
top = Frame(window,width=500,height=60,bg=clr2)
top.grid(row=0,column=0)


# create title
l1 = tk.Label(window,text="Currency Converter", font="Times 26 bold",bg=clr2,fg=clr0,anchor=CENTER)
l1.place(x = 100, y = 10,)


# create entry box
value = Entry(window,width=22,relief="solid",justify=CENTER,font="Ivy 12 bold",bg=clr0,fg=clr1,)
value.place(x = 150, y = 240)


# create from label
from_label = Label(window,text="From",width=8,height=1,relief="flat",anchor=NW,font="Ivy 10 bold",bg=clr0,fg=clr1,)
from_label.place(x = 125, y = 150)


#create combobox 1
combo1 = ttk.Combobox(window,width=12,justify=CENTER,font="Ivy 10 ")
combo1["values"] = (currency)


# create to label
to_label = Label(window,text="To",width=8,height=1,relief="flat",anchor=NW,font="Ivy 10 bold",bg=clr0,fg=clr1,)
to_label.place(x = 260, y = 150)


# create combobox 2
combo2 = ttk.Combobox(window,width=12,justify=CENTER,font="Ivy 10")
combo2["values"] = (currency)


# create button
b1 = tk.Button(window,text="Enter",font="Ivy 18 bold",width=12,bg=clr2,fg=clr0, command= clicked,)
b1.place(x = 155, y = 280)


# combobox entry place
combo1.place(x = 130, y = 180)
combo2.place(x = 270, y = 180)


window.mainloop()
