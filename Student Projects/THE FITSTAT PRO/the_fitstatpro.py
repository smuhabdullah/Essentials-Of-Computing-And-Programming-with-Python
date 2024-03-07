#_____FitstatPro-A BMI calculator______

#objective-To create a program which will take weight (kg) and height (m) as user input and calculate Body mass index.

#import tkinter

from tkinter import *

import customtkinter 

from tkinter import messagebox

from PIL import Image 

# appearance mode
customtkinter.set_appearance_mode('light')

#For main window 

app_main_win = customtkinter.CTk(fg_color="violet")
app_main_win.title("Fitstatpro")
app_main_win.geometry("600x400")
app_main_win.maxsize(650,500)
app_main_win.configure(bg_color="dark-blue")


#Fonts 
font_1=('times new roman',28, 'bold')
font_2=('times new roman',18, 'bold')
font_3=('times new roman',25, 'bold')
font_4=('times new roman', 18)

def calculate_bmi():
    try:
        weight=float(weight_entry.get())
        height=float(height_entry.get())
        bmi=weight/(height*height)
        result_label.configure(text="Your BMI is: {:.2f} kg/m²".format(bmi))
    except ValueError:
        messagebox.showerror("Error", "Enter a Valid Number")
    except ZeroDivisionError: 
        messagebox.showerror("Error", 'Height cannot be at Zero')

# app logo

logo_image=customtkinter.CTkImage(light_image=Image.open("fitpro.jpg"), dark_image=Image.open("fitpro.jpg"), size=(50,25))
image_label=customtkinter.CTkLabel(app_main_win, text="", image=logo_image)
image_label.place(x=5, y=10)

logo_image2=customtkinter.CTkImage(light_image=Image.open("download_1.jpeg"), dark_image=Image.open("download_1.jpeg"), size=(50,50))
image_label2=customtkinter.CTkLabel(app_main_win, text="", image=logo_image2)
image_label2.place(x=5, y=30)

#creating title, weight and height label

title_label= customtkinter.CTkLabel(app_main_win,font=font_1, text='A BMI Calculator', text_color='white',bg_color='midnightblue')
title_label.place(x=170, y=20)

weight_label=customtkinter.CTkLabel(app_main_win,font=font_2, text='weight (kg)', text_color='white', bg_color='midnightblue')
weight_label.place(x=170, y=80)

height_label=customtkinter.CTkLabel(app_main_win, font=font_2,text='height (m)', text_color='white', bg_color='midnightblue')
height_label.place(x=170, y=150)

#Create weight and height entry box

weight_entry= customtkinter.CTkEntry(app_main_win,font=font_4, text_color='midnightblue',placeholder_text="Enter the number here", placeholder_text_color="violet", fg_color='pink', border_color='pink', width=250)
weight_entry.place(x=170,y=110)

height_entry= customtkinter.CTkEntry(app_main_win, font=font_4, text_color='midnightblue', placeholder_text= "Enter the number here",placeholder_text_color="violet", fg_color='pink', border_color='pink', width=250)
height_entry.place(x=170,y=180)

#Creating Calculate Button 

Calculate_btn= customtkinter.CTkButton(app_main_win, command=calculate_bmi,font=font_2, text_color='midnight blue', text='Calculate',fg_color='pink', hover_color='lightblue',bg_color='pink',cursor='fleur', corner_radius=5, width=200)
Calculate_btn.place(x=170, y=230)

# for closing main window
def close ():
        app_main_win.forget(app_main_win)
        app_main_win.update()

# Exit Button

exit_the_program = customtkinter.CTkButton(app_main_win, command=close,font=font_2, text="Exit the Calculator", text_color="midnightblue", fg_color="pink", bg_color="pink", hover_color="lightblue", cursor="fleur", corner_radius=5, width=200)
exit_the_program.place(x=170, y=360)


#Result-label

result_label= customtkinter.CTkLabel(app_main_win,text="",font=font_4, text_color='midnightblue',bg_color='violet')
result_label.place(x=170, y=280)

clickhere= customtkinter.CTkLabel(app_main_win, text="Click to know your class \u2192",font=font_2, text_color='midnightblue', fg_color="violet")
clickhere.place(x=40, y=320)

# new window 


def bmi_chart_screen():
    new_chart_window= customtkinter.CTkToplevel(app_main_win,fg_color="violet")
    new_chart_window.title("Classification of BMI")
    new_chart_window.geometry("700x400")
    new_chart_window.maxsize(900,600)

    # title label
    title_label_2=customtkinter.CTkLabel(new_chart_window, font=font_1, text= "Classification of BMI", text_color="white",bg_color="midnightblue")
    title_label_2.place(x=150,y=20)

# creating a BMI chart
# heading labels for chart
    
    headinglabel1=customtkinter.CTkLabel(new_chart_window, text="Classes", font=font_3, text_color="midnightblue", bg_color="violet")
    headinglabel1.place(x=50, y=90)

    headinglabel2=customtkinter.CTkLabel(new_chart_window, text="Ranges", font=font_3,text_color="midnightblue", bg_color="violet")
    headinglabel2.place(x=200, y=90)

    headinglabel3=customtkinter.CTkLabel(new_chart_window, text="Risk of Comorbidities", font=font_3,text_color="midnightblue", bg_color="violet")
    headinglabel3.place(x=350, y=90)


# Classes for chart
    
    class1=customtkinter.CTkLabel(new_chart_window, text="underweight", text_color="midnightblue",font=font_4,bg_color="violet")
    class1.place(x=50, y=130)

    class2=customtkinter.CTkLabel(new_chart_window, text='Normal weight', text_color='midnightblue',font=font_4,bg_color='violet')
    class2.place(x=50, y=160)

    class3=customtkinter.CTkLabel(new_chart_window, text="Overweight", text_color="midnightblue",font=font_4, bg_color="violet")
    class3.place(x=50, y=190)

    class4=customtkinter.CTkLabel(new_chart_window, text="Obese Class I", font=font_4, text_color="midnightblue", bg_color="violet")
    class4.place(x=50, y=220)

    class5=customtkinter.CTkLabel(new_chart_window,text="Obese Class II", font=font_4, text_color="midnightblue", bg_color="violet")
    class5.place(x=50, y=250)

    class6=customtkinter.CTkLabel(new_chart_window, text="Obese Class III", text_color="midnightblue", font=font_4, bg_color="violet")
    class6.place(x=50, y=280)

    # ranges for the chart
    
    range1=customtkinter.CTkLabel(new_chart_window, text="<18.5", font=font_4, text_color="midnightblue", bg_color="violet")
    range1.place(x=200, y=130)

    range2=customtkinter.CTkLabel(new_chart_window, text="18.5-24.9", font=font_4, text_color="midnightblue", bg_color="violet")
    range2.place(x=200, y=160)

    range3=customtkinter.CTkLabel(new_chart_window, text="25.0-29.9", font=font_4, text_color="midnightblue", bg_color="violet")
    range3.place(x=200, y=190)

    range4=customtkinter.CTkLabel(new_chart_window, text="30.0-34.9", font=font_4, text_color="midnightblue", bg_color="violet")
    range4.place(x=200, y=220)

    range5=customtkinter.CTkLabel(new_chart_window, text="35.0-39.9", font=font_4, text_color="midnightblue", bg_color="violet")
    range5.place(x=200, y=250)

    range6=customtkinter.CTkLabel(new_chart_window, text="\u2265 40", font=font_4, text_color="midnightblue", bg_color="violet")
    range6.place(x=200, y=280)

    # risk of commorbities

    risk_for_class1=customtkinter.CTkLabel(new_chart_window, text="Low", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class1.place(x=350, y=130)
    
    risk_for_class2=customtkinter.CTkLabel(new_chart_window, text="---", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class2.place(x=350, y=160)

    risk_for_class3=customtkinter.CTkLabel(new_chart_window, text="Increased", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class3.place(x=350, y=190)

    risk_for_class4=customtkinter.CTkLabel(new_chart_window, text="High", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class4.place(x=350, y=220)

    risk_for_class5=customtkinter.CTkLabel(new_chart_window, text="severe", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class5.place(x=350, y=250)

    risk_for_class6=customtkinter.CTkLabel(new_chart_window, text="very severe", font=font_4, text_color="midnightblue", bg_color="violet")
    risk_for_class6.place(x=350, y=280)

    # scale image

    scale_image=customtkinter.CTkImage(light_image=Image.open("picture2.jpeg"), dark_image=Image.open("picture2.jpeg"), size=(100,175))
    image_label3=customtkinter.CTkLabel(new_chart_window, text="", image=scale_image)
    image_label3.place(x=450, y=130)

    

    def close ():
        new_chart_window.forget(new_chart_window)
        new_chart_window.update()

     #  for closing the window
    back_to_bmi_calc = customtkinter.CTkButton(new_chart_window, command=close,font=font_2, text="Back to calculator", text_color="midnightblue", fg_color="pink", bg_color="pink", hover_color="lightblue", cursor="fleur", corner_radius=5, width=200)
    back_to_bmi_calc.place(x=150, y=320)


#Weight-Range Chart button

range_chart_button=customtkinter.CTkButton(app_main_win,command=bmi_chart_screen,font=font_2, text_color='midnightblue', text= 'Classification of BMI', fg_color='pink', hover_color='lightblue', bg_color='pink', cursor='fleur', corner_radius=5, width=200)
range_chart_button.place(x=270, y=320)

#for main loop

app_main_win.mainloop()