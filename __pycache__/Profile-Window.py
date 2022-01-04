#Profile Window

import tkinter as tk
from tkinter import ttk
import datetime

class ProfileWindow:

    curr_year, curr_month, curr_day = str(datetime.date.today()).split("-")
    curr_date = "{}-{}-{}".format(curr_day, curr_month, curr_year)

    def __init__(self, root):
        self.root = root
        self.root.title("Profile {}".format(ProfileWindow.curr_date))
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        self.canvas = tk.Canvas(self.root, width=595, height=600)
        self.canvas.grid(columnspan=3, rowspan=4)

        self.w_label = tk.Label(self.root, text="Weight (kg):", font="Arial 15")
        self.w_label.grid(row=0, column=0)
        self.w_text = ttk.Entry(self.root, font="Arial 15")
        self.w_text.grid(row=0, column=1)
        self.create_waddbutton()
        self.create_wdatabutton()
        
        self.bmi_label = tk.Label(self.root, text="BMI:", font="Arial 15")
        self.bmi_label.grid(row=1, column=0)
        self.bmi_text = ttk.Entry(self.root, font="Arial 15")
        self.bmi_text.grid(row=1, column=1,)
        self.create_bmiaddbutton()
        self.create_bmidatabutton()
        
        self.hyd_label = tk.Label(self.root, text="Hydration:", font="Arial 15")
        self.hyd_label.grid(row=2, column=0)
        self.create_hydbar()
        self.create_hydaddbutton()
        self.create_hyddatabutton()

        self.create_leavebutton()

   
    #Κουμπί ιστορικού weight
    def create_wdatabutton(self):
        self.wdata_button = tk.Button(self.root, text="ΙΣΤΟΡΙΚΟ", font="Arial 15", background="green")
        self.wdata_button.bind("<Enter>", self.wmouse_entry)
        self.wdata_button.bind("<Leave>", self.wmouse_exit)
        self.wdata_button.grid(row=0, column=2,)

    def wmouse_entry(self, event):
        self.wdata_button.config(background="#1FA04C")

    def wmouse_exit(self, event):
        self.wdata_button.config(background="green")

    
    #Κουμπί προσθήκης weight
    def create_waddbutton(self):
        self.wadd_button = tk.Button(self.root, text="+" ,font="Arial 12", background="green")
        self.wadd_button.bind("<Enter>", self.waddmouse_entry)
        self.wadd_button.bind("<Leave>", self.waddmouse_exit)
        self.wadd_button.grid(row=0, column=1, sticky="e")

    def waddmouse_entry(self, event):
        self.wadd_button.config(background="#1FA04C")

    def waddmouse_exit(self, event):
        self.wadd_button.config(background="green")

    
    #Κουμπί ιστορικού bmi
    def create_bmidatabutton(self):
        self.bmidata_button = tk.Button(self.root, text="ΙΣΤΟΡΙΚΟ", font="Arial 15", background="green")
        self.bmidata_button.bind("<Enter>", self.bmimouse_entry)
        self.bmidata_button.bind("<Leave>", self.bmimouse_exit)
        self.bmidata_button.grid(row=1, column=2,)

    def bmimouse_entry(self, event):
        self.bmidata_button.config(background="#1FA04C")

    def bmimouse_exit(self, event):
        self.bmidata_button.config(background="green")


    #Κουμπί προσθήκης weight
    def create_bmiaddbutton(self):
        self.bmiadd_button = tk.Button(self.root, text="+" ,font="Arial 12", background="green")
        self.bmiadd_button.bind("<Enter>", self.bmiaddmouse_entry)
        self.bmiadd_button.bind("<Leave>", self.bmiaddmouse_exit)
        self.bmiadd_button.grid(row=1, column=1, sticky="e")

    def bmiaddmouse_entry(self, event):
        self.bmiadd_button.config(background="#1FA04C")

    def bmiaddmouse_exit(self, event):
        self.bmiadd_button.config(background="green")

    
    #Κουμπί προσθήκης hydration
    def create_hydaddbutton(self):
        self.hydadd_button = tk.Button(self.root, text="+", font="Arial 20", background="#00A2E8", command=self.addtobar)
        self.hydadd_button.bind("<Enter>", self.hydaddmouse_entry)
        self.hydadd_button.bind("<Leave>", self.hydaddmouse_exit)
        self.hydadd_button.grid(row=2, column=1, sticky="e")

    def hydaddmouse_entry(self, event):
        self.hydadd_button.config(background="#64B9DD")

    def hydaddmouse_exit(self, event):
        self.hydadd_button.config(background="#00A2E8")

    def addtobar(self):
        if self.hyd_bar["value"] == 9:
            self.hyd_bar["value"] = 10
        elif self.hyd_bar["value"] == 10: pass
        else:
            self.hyd_bar.step()

    
    #Κουμπί ιστορικού hydration
    def create_hyddatabutton(self):
        self.hyddata_button = tk.Button(self.root, text="ΙΣΤΟΡΙΚΟ", font="Arial 15", background="green")
        self.hyddata_button.bind("<Enter>", self.hydmouse_entry)
        self.hyddata_button.bind("<Leave>", self.hydmouse_exit)
        self.hyddata_button.grid(row=2, column=2)

    def hydmouse_entry(self, event):
        self.hyddata_button.config(background="#1FA04C")

    def hydmouse_exit(self, event):
        self.hyddata_button.config(background="green")

    
    #Κουμπί αποχώρησης
    def create_leavebutton(self):
        self.leave_button = tk.Button(self.root, text="Calendar", font="Arial 20", background="grey", command=self.leave)
        self.leave_button.bind("<Enter>", self.leavebuttonmouse_entry)
        self.leave_button.bind("<Leave>", self.leavebuttonmouse_exit)
        self.leave_button.grid(row=3, column=1)

    def leavebuttonmouse_entry(self, event):
        self.leave_button.config(background="light grey")

    def leavebuttonmouse_exit(self, event):
        self.leave_button.config(background="grey")

    def leave(self):
        pass

    
    #Μπάρα hydration
    def create_hydbar(self):
        barstyle = ttk.Style()
        barstyle.theme_use('default')
        barstyle.configure("blue.Horizontal.TProgressbar", thickness=35, background="#00A2E8", foreground="#00A2E8", bordercolor="#00A2E8")
        self.hyd_bar = ttk.Progressbar(self.root, style="blue.Horizontal.TProgressbar", orient="horizontal", length=200, mode="determinate", maximum=10, value=0)
        self.hyd_bar.place(x=189, y=347)

        

#------------------

root = tk.Tk()
profile = ProfileWindow(root)
root.mainloop()
