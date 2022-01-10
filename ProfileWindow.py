#Profile-Window

import importlib
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from tkcalendar import Calendar

class ProfileWindow():

    curr_year, curr_month, curr_day = str(datetime.date.today()).split("-")
    #curr_day = curr_day.lstrip("0")
    #curr_month = curr_month.lstrip("0")
    curr_date = "{}-{}-{}".format(curr_day, curr_month, curr_year)

    def init(self, root):
        c = importlib.import_module('Client')
        global Client
        Client = c.Client

        self.root = root
        self.root.title("Profile {}".format(ProfileWindow.curr_date))
        self.root.geometry("600x600+450+100")
        self.root.resizable(0, 0)
        self.canvas = tk.Canvas(self.root, width=595, height=600)
        self.canvas.grid(rowspan=4, columnspan=3)

        self.w_label = tk.Label(self.root, text="Weight (kg):", font="Arial 15")
        self.w_label.grid(row=0, column=0)
        self.weight_entry = ttk.Entry(self.root, font="Arial 15")
        self.weight_entry.grid(row=0, column=1, sticky="w")
        self.create_waddbutton()
        
        self.height_label = tk.Label(self.root, text="Height:\n({}cm)".format(Client.ProfileData.get_height()), font="Arial 15")
        self.height_label.grid(row=1, column=0)
        self.height_entry = ttk.Entry(self.root, font="Arial 15")
        self.height_entry.grid(row=1, column=1, sticky="w")
        self.create_heightaddbutton()
        
        self.hyd_label = tk.Label(self.root, text="Hydration:", font="Arial 15")
        self.hyd_label.grid(row=2, column=0)
        self.create_hydbar()
        self.create_hydaddbutton()

        self.create_calendarbutton()
        self.create_historybutton()

    
    #Κουμπί προσθήκης weight
    def create_waddbutton(self):
        self.wadd_button = tk.Button(self.root, text="+" ,font="Arial 15", background="green", command=self.addweight)
        self.wadd_button.bind("<Enter>", self.waddmouse_entry)
        self.wadd_button.bind("<Leave>", self.waddmouse_exit)
        self.wadd_button.grid(row=0, column=1, sticky="e")

    def waddmouse_entry(self, event):
        self.wadd_button.config(background="#1FA04C")

    def waddmouse_exit(self, event):
        self.wadd_button.config(background="green")

    def addweight(self):
        if self.weight_entry.get().isdigit() or "." in self.weight_entry.get():
            Client.ProfileData.weightData.updateWeightForDay(self.curr_date, self.weight_entry.get())
            Client.ProfileData.bmiData.updateBMIForDay(self.curr_date, self.bmi_calculator(self.weight_entry.get(), Client.ProfileData.get_height()))
            self.weight_entry.delete(0, "end")
        else:
            self.errorwindow()
            self.weight_entry.delete(0, "end")

    def bmi_calculator(self, weight, height):
        weight = int(weight)
        height = int(height)
        bmi = (weight/(height**2))*10000
        return "{:.2f}".format(bmi)


    #Κουμπί προσθήκης height
    def create_heightaddbutton(self):
        self.heightadd_button = tk.Button(self.root, text="+" ,font="Arial 15", background="green", command=self.addheight)
        self.heightadd_button.bind("<Enter>", self.heightaddmouse_entry)
        self.heightadd_button.bind("<Leave>", self.heightaddmouse_exit)
        self.heightadd_button.grid(row=1, column=1, sticky="e")

    def heightaddmouse_entry(self, event):
        self.heightadd_button.config(background="#1FA04C")

    def heightaddmouse_exit(self, event):
        self.heightadd_button.config(background="green")

    def addheight(self):
        if self.height_entry.get().isdigit():
            Client.ProfileData.change_height(self.height_entry.get())
            self.height_label.config(text="Height:\n({}cm)".format(self.height_entry.get()))
            self.height_entry.delete(0, "end")
        else:
            self.errorwindow()
            self.height_entry.delete(0, "end")

    
    #Κουμπί προσθήκης hydration
    def create_hydaddbutton(self):
        self.hydadd_button = tk.Button(self.root, text="+", font="Arial 15", background="#00A2E8", command=self.addtobar)
        self.hydadd_button.bind("<Enter>", self.hydaddmouse_entry)
        self.hydadd_button.bind("<Leave>", self.hydaddmouse_exit)
        self.hydadd_button.grid(row=2, column=1, sticky="e")

    def hydaddmouse_entry(self, event):
        self.hydadd_button.config(background="#64B9DD")

    def hydaddmouse_exit(self, event):
        self.hydadd_button.config(background="#00A2E8")

    def addtobar(self):
        if Client.ProfileData.get_gender()=="male": 
            if self.hyd_bar["value"] == 9:
                self.hyd_bar["value"] = 10
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, 10)
            elif self.hyd_bar["value"] == 10:
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, 11)
            else:
                self.hyd_bar.step()
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, self.hyd_bar["value"])
        else:
            if self.hyd_bar["value"] == 6:
                self.hyd_bar["value"] = 7
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, 7)
            elif self.hyd_bar["value"] == 7:
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, 8)
            else:
                self.hyd_bar.step()
                Client.ProfileData.hydrationData.updateHydrationForDay(ProfileWindow.curr_date, self.hyd_bar["value"])
            

    #Παράθυρο ERROR
    def errorwindow(self):
        self.errorwin = messagebox.showwarning(title="ERROR", message="Σφάλμα στην μορφή των στοιχείων που δώσατε.\nΠροσπαθήστε ξανά.")

    
    #Κουμπί calendar
    def create_calendarbutton(self):
        self.calendar_button = tk.Button(self.root, text="Ημερολόγιο", font="Arial 20", background="grey", command=self.go_to_calendar)
        self.calendar_button.bind("<Enter>", self.calendarbuttonmouse_entry)
        self.calendar_button.bind("<Leave>", self.calendarbuttonmouse_exit)
        self.calendar_button.grid(row=3, column=1, sticky="e")

    def calendarbuttonmouse_entry(self, event):
        self.calendar_button.config(background="light grey")

    def calendarbuttonmouse_exit(self, event):
        self.calendar_button.config(background="grey")

    def go_to_calendar(self):
        self.root.destroy()
        Client.Gui.beginView(Client.Gui.CalendarView)

    
    #Μπάρα hydration
    def create_hydbar(self):
        if Client.ProfileData.get_gender()=="male":
            maxh=10
        else:maxh=7
        barstyle = ttk.Style()
        barstyle.theme_use('default')
        barstyle.configure("blue.Horizontal.TProgressbar", thickness=35, background="#00A2E8", foreground="#00A2E8", bordercolor="#00A2E8")
        self.hyd_bar = ttk.Progressbar(self.root, style="blue.Horizontal.TProgressbar", orient="horizontal", length=225, mode="determinate", maximum=maxh, value=Client.ProfileData.hydrationData.getHydrationForDays([self.curr_date])[self.curr_date])
        self.hyd_bar.place(x=208, y=354)


    #Κουμπί ιστορικού
    def create_historybutton(self):
        self.history_button = tk.Button(self.root, text="Ιστορικό", font="Arial 20", background="grey", command=self.history_window)
        self.history_button.bind("<Enter>", self.historybutton_entry)
        self.history_button.bind("<Leave>", self.historybutton_exit)
        self.history_button.grid(row=3, column=0, sticky="e")

    def historybutton_entry(self, event):
        self.history_button.config(background="light grey")

    def historybutton_exit(self, event):
        self.history_button.config(background="grey")


    #Παράθυρο Ιστορικού
    def history_window(self):
        self.h = tk.Toplevel()
        self.h.title("Profile Database")
        self.h.geometry("400x400+550+185")
        self.h.resizable(0, 0)
        self.hcanvas = tk.Canvas(self.h, width=400, height=400)
        self.hcanvas.grid(rowspan=5, columnspan=5)
       
        self.calframe = tk.Frame(self.h, background="black")
        self.calframe.grid(row=0, column=2)
        self.datacal = Calendar(self.calframe, font="Arial 12", selectmode="day")
        self.datacal.pack(pady=5, padx=5)
        
        self.create_searchbutton()
        self.weightlabel = tk.Label(self.h, text="Weight (kg):", font="Arial 15")
        self.weightlabel.grid(row=2, column=2, sticky="w")
        self.bmilabel = tk.Label(self.h, text="BMI:", font="Arial 15")
        self.bmilabel.grid(row=3, column=2, sticky="w")
        self.hydrationlabel = tk.Label(self.h, text="Hydration (glasses):", font="Arial 15")
        self.hydrationlabel.grid(row=4, column=2, sticky="w")

    
    #Κουμπί search
    def create_searchbutton(self):
        self.search_button = tk.Button(self.h, text="Search", font="Arial 14", width=15, background="grey", command=self.showdata)
        self.search_button.bind("<Enter>", self.searchbutton_entry)
        self.search_button.bind("<Leave>", self.searchbutton_exit)
        self.search_button.grid(row=1, column=2)

    def searchbutton_entry(self, event):
        self.search_button.config(background="light grey")

    def searchbutton_exit(self, event):
        self.search_button.config(background="grey")

    def showdata(self):
        year, month, day = str(self.datacal.selection_get()).split("-")
        #day = day.lstrip("0")
        #month = month.lstrip("0")
        date = "{}-{}-{}".format(day, month, year)
        weight = Client.ProfileData.weightData.getWeightForDays([date])[date]
        if weight == None:
            weight = "-"
        bmi = Client.ProfileData.bmiData.getBMIForDays([date])[date]
        if bmi == None:
            bmi = "-"
        hydration = Client.ProfileData.hydrationData.getHydrationForDays([date])[date]
        if hydration == None:
            hydration = "-"
        self.weightlabel.config(text="Weight (kg):\t\t{}".format(weight))
        self.bmilabel.config(text = "BMI:\t\t\t{}".format(bmi))
        self.hydrationlabel.config(text="Hydration (glasses):\t{}".format(str(hydration).replace(".0", "")))

#--------------------------

if __name__ == '__main__':
    #Client.init()
    root=tk.Tk()
    profile = ProfileWindow(root)
    root.mainloop()
