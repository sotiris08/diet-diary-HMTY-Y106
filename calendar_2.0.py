import tkinter as tk
import tkcalendar
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
import os

#-----------------

class MyApp() :
    def __init__(self,root) :
        self.root = root
        root.title('Calendar')
        root.geometry("500x500+400+200")
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.f2 = tk.Frame(root)
        self.f2.pack()
        self.create_calendar()
        self.create_button1()
        self.create_button2()
        

    def create_calendar(self):
        self.cal = Calendar(self.f1, selectmode = 'day')
        self.cal.pack(pady = "50")

    def create_button1(self) :
        self.button = tk.Button(self.f2, text = "Προσθήκη \n Γεύματος" , font = "Arial 20" , bg = "green" , height = 10 , width = 10 , command = self.listbox)
        self.button.pack(pady = '30'  , padx = "20" , side = 'left')

    def create_button2(self) :
        self.button = tk.Button(self.f2 , text = "Γεύματα \n Ημερας" , font = "Arial 20" , bg = "blue" , height = 10 , width = 10 , command = self.show_meals)
        self.button.pack(pady = "30" , padx = "20" , side = 'right')
        
    def listbox(self) :
        self.w = tk.Toplevel()
        self.w.geometry("300x300+300+300")
        var2 = tk.StringVar()
        var2.set(('πρωινό' , 'δεκατιανό' , 'μεσημεριανό' , 'απογευματινό' , 'βραδινό'))
        self.lb = tk.Listbox(self.w , bg = 'grey' , fg = "white" , activestyle = "dotbox" , font = "Arial 30" , listvariable = var2)
        self.lb.pack(fill = "both" , expand =1)
        self.lb.bind('<<ListboxSelect>>', self.getElement)

    def getElement(self , event):
        selection = event.widget.curselection()
        value = event.widget.get(selection)
        self.value = value
        if value != '' :
            self.w.destroy()
            self.w1 = tk.Toplevel()
            self.w1.geometry('300x300+300+400')
            self.f3 = tk.Frame(self.w1)
            self.f3.pack()
            self.f4 = tk.Frame(self.w1)
            self.f4.pack()
            self.f5 = tk.Frame(self.w1)
            self.f5.pack()
            self.label1 = tk.Label(self.f3 , text = 'προσθήκη γεύματος ' + self.cal.get_date())
            self.label1.pack()
            self.meal_selection()

    def meal_selection(self) :
        self.combobox = ttk.Combobox(self.f3, width = 27, textvariable = tk.StringVar())
        self.label = tk.Label(self.f4 , text = 'ποσα γραμμαρια :' , font = 'Arial 20')
        self.entry = tk.Entry(self.f4)
        if self.value == 'πρωινό' :
            string1 = ''
            f = open('πρωινό.txt', 'r' , encoding='utf-8')
            morning = f.read()
            for self.line in morning.split('\n') :
                self.line = self.line.split('\t')
                self.name = self.line[0]
                string1 = string1 + ' ' + self.name
            self.combobox['values'] = (string1.split())
        elif self.value == 'δεκατιανό' :
            string2 = ''
            f = open('δεκατιανό.txt', 'r' , encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('\t')
                self.name = line[0]
                string2 = string2 + ' ' + self.name
            self.combobox['values'] = (string2.split())
        elif self.value == 'μεσημεριανό' :
            string3 = ''
            f = open('μεσημεριανό.txt', 'r' , encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('\t')
                self.name = line[0]
                string3 = string3 + ' ' + self.name
            self.combobox['values'] = (string3.split())
        elif self.value == 'απογευματινό' :
            string4 = ''
            f = open('απογευματινό.txt', 'r' , encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('\t')
                self.name = line[0]
                string4 = string4 + ' ' + self.name
            self.combobox['values'] = (string4.split()) 
        elif self.value == 'βραδινό' :
            string5 = ''
            f = open('βραδινό.txt', 'r' , encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('\t')
                self.name = line[0]
                string5 = string5 + ' ' + self.name
            self.combobox['values'] = (string5.split())
        self.combobox.pack(pady='30')
        self.label.pack(fill = 'both' , expand = 1 , side = 'left')
        self.entry.pack(fill = 'both' , expand = 1 , side = 'right')
        self.w1.bind('<Return>' , self.handler)

        
    def handler(self , event) :
        grams = ''
        cals = ''
        self.cals = cals
        self.grams = grams
        self.grams = self.entry.get()
        self.grams = int(self.grams)
        self.cals_per_100 = int(self.line[1])
        self.cals = self.cals_per_100 * self.grams
        self.lb = tk.Label(self.f5 , text = 'Υπολογισμός θερμιδών : ' + str(self.cals) + ' calories')
        self.lb.pack(fill = 'both' , expand = 1)
        self.save_in_file()


    def save_in_file(self) :
        date = self.cal.get_date()
        self.month , self.day , self.year = self.cal.get_date().split('/')
        
        f = open(str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '.txt' , 'a' ,  encoding='utf-8')
        f.write('Πρόγραμμα Διατροφής :' + str(date) + '\n')
        f.write(self.value + ':' + '\n')
        f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + 'gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
        f.close()
        
            
    def show_meals(self) :
        self.m = tk.Toplevel()
        self.m.geometry("400x400+300+300")
        self.f6 = tk.Frame(self.m)
        self.f6.pack()
        f = open(str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '.txt' , 'r' ,  encoding='utf-8')
        self.meals = tk.Label(self.m , text = f.read())
        self.meals.pack()

        
        f.close()
        
        
        
        
#-----------------

root = tk.Tk()
app = MyApp(root)
root.mainloop()
