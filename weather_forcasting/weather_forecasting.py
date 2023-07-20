from tkinter import *

from configparser import ConfigParser
from tkinter import messagebox
import requests
import customtkinter




url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file='weather.key' 
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']

def weather_find(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file=final.json()
        city=json_file['name'] 
        country_name=json_file['sys']['country']
        k_temp=json_file['main']['temp']
        c_temp=k_temp-273.15
        f_temp=(k_temp-273.15)*9/5+32
        weather_display=json_file["weather"][0]["main"]
        result=(city,country_name,c_temp,f_temp,weather_display)

        return result
    else:
        return None

def print_weather():
    city=search_city.get()  
    weather = weather_find(city)
    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temperature_entry['text']='{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
        weather_entry['text']=weather[4]
        
        
    else:
         messagebox.showerror('Error','Please enter a valid city')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.title("Weather App using Python")
root.geometry("750x450")


frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label2=customtkinter.CTkLabel(master=frame,text="Weather Application", font=("Roboto",25))
label2.pack(pady=12,padx=10)

label1=customtkinter.CTkLabel(master=frame,text="Enter the name of the city", font=("Roboto",12))
label1.pack()

search_city=StringVar()
enter_city= customtkinter.CTkEntry(master=frame,textvariable=search_city,font=("Roboto",25))
                               
enter_city.pack()


label3=customtkinter.CTkLabel(master=frame,text="City & Country", font=("Roboto",12))
label3.pack()

location_entry=Label(master=frame,text='',bg="grey",font=("Roboto",25))
location_entry.pack(padx=10)

label4=customtkinter.CTkLabel(master=frame,text="Temperature in celcius & fahrenheit", font=("Roboto",12))
label4.pack()

temperature_entry=Label(master=frame,text='',bg="grey",font=("Robto",25))
temperature_entry.pack(padx=10)

label5=customtkinter.CTkLabel(master=frame,text="Weather", font=("Roboto",12))
label5.pack()

weather_entry=Label(master=frame,text='',bg="grey",font=("Roboto",25))
weather_entry.pack(pady=12,padx=10)



search_button=customtkinter.CTkButton(master=frame,width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=3,text='SEARCH TEMP',command=print_weather)
search_button.pack(pady=12,padx=10)
root.mainloop()