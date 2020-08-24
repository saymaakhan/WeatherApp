from tkinter import *


# Functions

def search():
    pass


# Set Up View of App
app = Tk()
app.title("Weather Application")
app.geometry('350x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_button = Button(app, text='Search', width=12, command=search)
search_button.pack()

location_label = Label(app, text='', font=('bold', 21))
location_label.pack()

temp_label = Label(app, text='')
temp_label.pack()

weather_label = Label(app, text='')
weather_label.pack()

app.mainloop()
