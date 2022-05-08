import tkinter
from tkinter import ttk

import CountryService
import StatsService

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

form = tkinter.Tk()

form.title("Api rozkład temperatury w dni wolne")
form.geometry("1000x600")

lblInfo = tkinter.Label(form, text="Temperaty panujące we wskazane dni wolne", font=("Times New Roman", 20), fg="blue")
lblInfo.grid(row=0, column=0, columnspan=2, )

center_frame_1 = tkinter.Frame(form, highlightbackground="black", highlightthickness=2)
center_frame_1.grid(row=1, column=0, padx=20, ipady=20, ipadx=20, sticky="N")


plot_frame = tkinter.Frame(form, bg="gray", highlightbackground="black", highlightthickness=2)
plot_frame.grid(row=1, column=1, rowspan=2)

countries = CountryService.CountryService.get_countries()
holidays = CountryService.HolidaysList.get_holidays()
lata = CountryService.YearsList.get_years()


def SelectedHolidayChanged(event):
    global selectedHoliday
    selectedHoliday = event.widget.get()


def SelectedYearStartChanged(event):
    global selectedYearStart
    selectedYearStart = int(event.widget.get())


def SelectedYearEndChanged(event):
    global selectedYearEnd
    selectedYearEnd = int(event.widget.get())



# Etykieta +combo dla święta (holiday)
lblh = tkinter.Label(center_frame_1, text="Wybierz święto", )
lblh.grid(row=1, column=0, sticky='w', padx=20, pady=10)

cbh = ttk.Combobox(center_frame_1, values=holidays)
cbh.grid(row=2, column=0, sticky='w', padx=20)
cbh.bind("<<ComboboxSelected>>", SelectedHolidayChanged)

# Etykieta +combo dla roku początkowego
lblys = tkinter.Label(center_frame_1, text="Rok początkowy", )
lblys.grid(row=1, column=1, sticky='w', padx=20)

cbrs = ttk.Combobox(center_frame_1, values=lata)
cbrs.grid(row=2, column=1, sticky='w', padx=20)
cbrs.bind("<<ComboboxSelected>>", SelectedYearStartChanged)

# Etykieta +combo dla roku końcowego
lblye = tkinter.Label(center_frame_1, text="Rok końcowy", )
lblye.grid(row=3, column=1, sticky='w', padx=20, pady=10)

cbrk = ttk.Combobox(center_frame_1, values=lata)
cbrk.grid(row=4, column=1, sticky='w', padx=20)
cbrk.bind("<<ComboboxSelected>>", SelectedYearEndChanged)



def btnShowClick():
    drawPlot()


btnShow = tkinter.Button(center_frame_1, width=30, height=2, text="Show plot", command=btnShowClick)
btnShow.grid(row=5, column=0, columnspan=2, pady=20)

def drawPlot():
    fig = Figure(figsize=(5, 5), dpi=100)
    fig.suptitle(f'Rozkład temperatury Warszawa {selectedHoliday}')

    myplot = fig.add_subplot(111)

    data = StatsService.StatTempService.get_temperature(selectedYearStart, selectedYearEnd, selectedHoliday)
    print(data)
    names = list(data.keys())
    values = list(data.values())

    myplot.bar(range(len(data)), values, tick_label=names)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()

    canvas.get_tk_widget().grid(row=0, column=0)

tkinter.mainloop()
