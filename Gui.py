from FirstInterface import First as StartView
from calendar2 import MyApp as CalendarView
from ProfileWindow import ProfileWindow as ProfileView
import tkinter as tk

class Gui:
    ProfileView = ProfileView()
    StartView = StartView()
    CalendarView = CalendarView()

    def beginView(view):
        root = tk.Tk()
        view.init(root)