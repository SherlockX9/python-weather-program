from tkinter import font
from tkinter import *   
import tkinter as tk
import requests

HEIGHT = 700
WIDTH = 800

def test_function(bb):
    print("This is what you entered: ", bb)


def clear_entry(event, entry):
    entry.delete(0, END)

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# 71dfc3ce774a02c5ebb6256e511691fb

def format_response(weather):
    try:   
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        end_str = 'City: %s  \n Conditions: %s   \n Temperature (°C): %s ' % (name, description, temp)
    except:
        end_str = 'Cannot retrieve that information'
    
    return end_str


def get_weather(city):
    weather_key = '71dfc3ce774a02c5ebb6256e511691fb'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    paramX = {'q': city,  'appid': weather_key, 'units': 'Metric'}
    response = requests.get(url, params = paramX)
    weather = response.json()
    # print(weather)
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    label['text'] = format_response(weather)

background_image = tk.PhotoImage(file='weatherbackgroundv3.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='purple', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Fixedsys', 13))
entry.place(relwidth=0.65, relheight=1)

# entry.pack()
placeholder_text = 'London, UK'
entry.insert(0, placeholder_text)

entry.bind("<Button-1>", lambda event: clear_entry(event, entry))

button = tk.Button(frame, text="Find Weather", command = lambda: get_weather(entry.get()), font=('Tempus Sans ITC', 15))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='purple', bd=10)
lower_frame.place(relx =0.5, rely = 0.25, relwidth= 0.75, relheight =0.6, anchor ='n')
label = tk.Label(lower_frame, font=('Lucida Fax', 20))
label.place(relwidth=1, relheight=1)

print(tk.font.families())
root.mainloop()