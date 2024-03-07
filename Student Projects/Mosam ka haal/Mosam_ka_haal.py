
# Team Member Name: 
# 1)Name: Abdul Ahad 2) Email: aabdulahad142@gmail.com 3)Phone Number: 03212704991 
# 2)Name: Muhammad Hanzala 2) Email: hanzalakhan6226@gmail.com 3)Phone Number:03141030925


# tkinter is built-in GUI(Graphical User interface) from Python libraray
from tkinter import * 
from tkinter import ttk

# request module for handle the data of server
import requests 

# Json for human-readability and data exchange
import json



def data_get():
        
        city = city_name.get()
        
        #api get data from server
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3afd0903c794a931a87fc09cba6110e5").json()

        #show weather data on application and linked with api
        weather_data = data['weather'][0]["main"]
        wheather_label1.config(text=str(weather_data))


        #show weather description data on application and linked with api
        wheather_description1.config(text=data["weather"][0]["description"])
        
        #show weather description data on application and linked with api
        temperature_label1.config(text=str(data["main"]["temp"]-273.15))
         
        #show  pressure data on application and linked with api
        pressure_label1.config(text=data["main"]["pressure"])
  


win = Tk() #create a window frame
win.title("Mousam ka Haal") #set title of the window

win.config(bg = "blue")  #window background color
win.geometry("500x520")  #window width and height size

# Weather app name in box and place (width and height)
name_label = Label(win,text="Mosam ka Haal",font=("Time New Roman",35,"bold")) 
name_label.place(x=25, y=50, height=50, width=450)

city_name=StringVar()

#list of city Name for drop down menu 
list_name = ["Karachi","Islamabad","Lahore","Faisalabad","Quetta","Peshawar","Murree","Larkana","Sukkar","Mirpur Khas", "Heydrabad","Gilkit Baltistan","Rawal Pindi","Guranwala"] 

#combo box for selecting city name and make drop down menu use tkk
com = ttk.Combobox(win,text="Mosam ka Haal",values=list_name,font=("Time New Roman",25,"bold"),textvariable=city_name) 

#size of combo box is (width,height)
com.place(x=25, y=120, height=50, width=450)



#show in window wheather climate name in label box place and width and height
wheather_label = Label(win,text="Wheather climate",font=("Time New Roman",10))
wheather_label.place(x=25, y=268, height=50, width=200)

#show data whats get your wheather api
wheather_label1= Label(win,text="",font=("Time New Roman",10))
wheather_label1.place(x=250, y=268, height=50, width=200)

#show in window weather description name in label box place and width and height
wheather_description = Label(win,text="Wheather Description",font=("Time New Roman",10))
wheather_description.place(x=25, y=330, height=50, width=200)

#show data whats get your wheather api & place and width and height
wheather_description1= Label(win,text="",font=("Time New Roman",10))
wheather_description1.place(x=250, y=330, height=50, width=200)

#show in window temperature name in label box place and width and height
temperature_label = Label(win,text="Temperature",font=("Time New Roman",10))
temperature_label.place(x=25, y=390, height=50, width=200)

#show temperature data whats get your wheather api & place and width and height
temperature_label1=Label(win,text="",font=("Time New Roman",10))
temperature_label1.place(x=250, y=390, height=50, width=200)

#show in window Pressure name in label box place and width and height
pressure_label = Label(win,text="Presure",font=("Time New Roman",10))
pressure_label.place(x=25, y=450, height=50, width=200)

#show Pressure data whats get your wheather api & place and width and height
pressure_label1= Label(win,text="",font=("Time New Roman",10))
pressure_label1.place(x=250, y=450, height=50, width=200)


#search button for show data in window and place (width & height)
Search_button= Button(win,text="Search",  
                      font=("Time New Roman",20,"bold"),command=data_get) 
Search_button.place(y=198,height=50,width=100,x=200)



win.mainloop()