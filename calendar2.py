from re import L
import tkinter as tk
import tkcalendar
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
import os
import importlib

#-----------------

class MyApp() :
    def init(self,root) :
        self.root = root
        root.title('Calendar')
        root.geometry("500x350+400+200")
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.f2 = tk.Frame(root)
        self.f2.pack()
        self.create_calendar()
        self.profile_button()
        self.create_button1()
        self.create_button2()
        self.number = 1

    def profile_button(self) :
        self.button = tk.Button(self.f1 , text = 'profile' , font = 'Arial 10' , bg = 'black' , fg = 'white' , width = 20 , height = 3, command= self.showProfile)
        self.button.pack(pady = '25' , padx = '15' , side = 'right' , fill = 'x' , expand = 1)
        
    def create_calendar(self):
        self.cal = Calendar(self.f1, selectmode = 'day')
        self.cal.pack(pady = "25" , padx = '15', side = 'left' , fill = 'both' , expand = 1)

    def create_button1(self) :
        self.button = tk.Button(self.f2, text = "Προσθήκη \n Γεύματος" , font = "Arial 20" , bg = "green" , height = 2 , width = 8 , command = self.listbox)
        self.button.pack(pady = '10' , padx = '10' , side = 'left')

    def create_button2(self) :
        self.button = tk.Button(self.f2 , text = "Γεύματα \n Ημερας" , font = "Arial 20" , bg = "blue" , height = 2 , width = 8 , command = self.show_meals)
        self.button.pack(pady = "10" , padx = "20" , side = 'right')
        
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
        self.btn = tk.Button(self.f3 , width = 3 , text = '+' , command = self.extrafood)
        self.label = tk.Label(self.f4 , text = 'ποσα γραμμαρια :' , font = 'Arial 20')
        self.entry = tk.Entry(self.f4)
        if self.value == 'πρωινό' :
            string1 = ''
            f = open('data/morning.txt', 'r', encoding='utf-8')
            morning = f.read()
            for self.line in morning.split('\n') :
                self.line = self.line.split('-')
                self.name = self.line[0]
                string1 = string1 + self.name + '+'
            self.combobox['values'] = (string1.split('+'))
        elif self.value == 'δεκατιανό' :
            string2 = ''
            f = open('data/decatan.txt', 'r', encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('-')
                self.name = line[0]
                string2 = string2 + self.name + '+'
            self.combobox['values'] = (string2.split('+'))
        elif self.value == 'μεσημεριανό' :
            string3 = ''
            f = open('data/lunch.txt', 'r', encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('-')
                self.name = line[0]
                string3 = string3 + self.name + '+'
            self.combobox['values'] = (string3.split('+'))
        elif self.value == 'απογευματινό' :
            string4 = ''
            f = open('data/evening.txt', 'r', encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('-')
                self.name = line[0]
                string4 = string4 + self.name + '+'
            self.combobox['values'] = (string4.split('+')) 
        elif self.value == 'βραδινό' :
            string5 = ''
            f = open('data/diner.txt', 'r', encoding='utf-8')
            morning = f.read()
            for line in morning.split('\n') :
                line = line.split('-')
                self.name = line[0]
                string5 = string5 + self.name + '+'
            self.combobox['values'] = (string5.split('+'))
        f.close()
        self.combobox.pack(pady='30' , side = 'left')
        self.btn.pack(padx = 2 , side = 'right')
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
        self.date = self.cal.get_date()
        self.month , self.day , self.year = self.cal.get_date().split('/')
        dates = str(self.day) + '-' + str(self.month) + '-' + str(self.year) 
        self.all_dates()
        f = open('data/all_dates.txt' , 'r' ,  encoding='utf-8')
        if str(dates) not in str(f.read()) :
            self.number = 1
            f.close()
        if self.number == 1 :
            self.create_meal_files()
            self.number = self.number + 1
        self.month , self.day , self.year = self.cal.get_date().split('/')
        self.check_for_date()
        self.check_for_meal()
        
        
    def check_for_date(self) :
        count = 1
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'morning' + '.txt' , 'r' ,  encoding='utf-8')
        if self.date not in f.read() :
            f.close()
            if count == 1 :
                f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'morning' + '.txt' , 'a' ,  encoding='utf-8')
                f.write('Πρόγραμμα Διατροφής :' + str(self.date) + '\n')
                f.write('πρωινό' + ' : ' + '\n')
                f.close()
                f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'decatan' + '.txt' , 'a' ,  encoding='utf-8')
                f.write('δεκατιανό' + ' : ' + '\n')
                f.close()
                f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'lunch' + '.txt' , 'a' ,  encoding='utf-8')
                f.write('μεσημεριανό' + ' : ' + '\n')
                f.close()
                f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'evening' + '.txt' , 'a' ,  encoding='utf-8')
                f.write('απογευματινό' + ' : ' + '\n')
                f.close()
                f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'diner' + '.txt' , 'a' ,  encoding='utf-8')
                f.write('βραδινό' + ' : ' + '\n')
                f.close()
                count += 1
                
    def check_for_meal(self) :
        if self.value == 'πρωινό' :
            f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'morning' + '.txt' , 'a' ,  encoding='utf-8')
            f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + ' gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
            f.close()
        elif self.value == 'δεκατιανό' :
            f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'decatan' + '.txt' , 'a' ,  encoding='utf-8')
            f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + ' gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
            f.close()
        elif self.value == 'μεσημεριανό' :
            f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'lunch' + '.txt' , 'a' ,  encoding='utf-8')
            f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + ' gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
            f.close()
        elif self.value == 'απογευματινό' :
            f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'evening' + '.txt' , 'a' ,  encoding='utf-8')
            f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + ' gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
            f.close()
        elif self.value == 'βραδινό' :
            f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'diner' + '.txt' , 'a' ,  encoding='utf-8')
            f.write('φαγητο : ' + str(self.name) + '\t' + 'γραμμάρια : ' + str(self.grams) + ' gr' + '\t' + 'θερμιδες : ' + str(self.cals) + '\n')
            f.close()
            
        
    def extrafood(self) :
        self.extrafoodwindow()
        self.eflabel = tk.Label(self.f6 , text = 'επιλογη επιπλεον γευματος' )
        self.eflabel.pack(pady = '20')
        # food name
        self.namelabel = tk.Label(self.f7 , text = 'ονομα \n φαγητου' , justify = 'left')
        self.namelabel.pack(side = 'left' , padx = '20')
        self.entry1 = tk.Entry(self.f7)
        self.entry1.pack(side = 'right' , padx = '20')
        self.name = self.entry1.get()
        # food calories
        self.calslabel = tk.Label(self.f8 , text = 'θερμιδες ανα \n 100 gr.' , justify = 'left')
        self.calslabel.pack(side = 'left' , padx = '20')
        self.entry2 = tk.Entry(self.f8 )
        self.entry2.pack(side = 'right' , padx = '20')
        self.cals = self.entry2.get()
        # food grams
        self.gramslabel = tk.Label(self.f9 , text = 'γραμμαρια \n καταναλωσης' , justify = 'left')
        self.gramslabel.pack(side = 'left' , padx = '20')
        self.entry3 = tk.Entry(self.f9 )
        self.entry3.pack(side = 'right' , padx = '20')
        self.grams = self.entry3.get()
        # entry button
        self.entrybutton = tk.Button(self.f10 , text = 'αποθηκευση' , command = self.getvalue)
        self.entrybutton.pack(pady = '20')

        
    def show_meals(self) :
        self.m = tk.Toplevel()
        self.m.geometry("400x400+300+300")
        self.fr1 = tk.Frame(self.m)
        self.fr1.pack(fill = 'both' , expand = 1)
        self.fr2 = tk.Frame(self.m)
        self.fr2.pack(fill = 'both' , expand = 1)
        self.fr3 = tk.Frame(self.m)
        self.fr3.pack(fill = 'both' , expand = 1)
        self.fr4 = tk.Frame(self.m)
        self.fr4.pack(fill = 'both' , expand = 1)
        self.fr5 = tk.Frame(self.m)
        self.fr5.pack(fill = 'both' , expand = 1)
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'morning' + '.txt' , 'r' ,  encoding='utf-8')
        self.morning_meals = tk.Label(self.fr1 , text = str(f.read()))
        f.close()
        self.morning_meals.pack()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'decatan' + '.txt' , 'r' ,  encoding='utf-8')
        self.decatan_meals = tk.Label(self.fr2 , text = str(f.read()))
        f.close()
        self.decatan_meals.pack()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'lunch' + '.txt' , 'r' ,  encoding='utf-8')
        self.lunch_meals = tk.Label(self.fr3 , text = str(f.read()))
        f.close()
        self.lunch_meals.pack()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'evening' + '.txt' , 'r' ,  encoding='utf-8')
        self.evening_meals = tk.Label(self.fr4 , text = str(f.read()))
        f.close()
        self.evening_meals.pack()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'diner' + '.txt' , 'r' ,  encoding='utf-8')
        self.diner_meals = tk.Label(self.fr5 , text = str(f.read()))
        f.close()
        self.diner_meals.pack()

    def create_meal_files(self) :
        self.month , self.day , self.year = self.cal.get_date().split('/')
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'morning' + '.txt' , 'a' ,  encoding='utf-8')
        f.close()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'decatan' + '.txt' , 'a' ,  encoding='utf-8')
        f.close()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'lunch' + '.txt' , 'a' ,  encoding='utf-8')
        f.close()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'evening' + '.txt' , 'a' ,  encoding='utf-8')
        f.close()
        f = open('data/' + str(self.day) + '-' + str(self.month) + '-' + str(self.year) + '-' + 'diner' + '.txt' , 'a' ,  encoding='utf-8')
        f.close()

    def extrafoodwindow(self) :
        self.w2 = tk.Toplevel()
        self.w2.geometry('250x250+400+500')
        self.f6 = tk.Frame(self.w2)
        self.f6.pack()
        self.f7 = tk.Frame(self.w2)
        self.f7.pack()
        self.f8 = tk.Frame(self.w2)
        self.f8.pack()
        self.f9 = tk.Frame(self.w2)
        self.f9.pack()
        self.f10 = tk.Frame(self.w2)
        self.f10.pack()

    def all_dates(self) :
        f = open('data/' + 'all_dates.txt' , 'a' ,  encoding='utf-8')
        f.write(str(self.date))
        f.write('\n')
        f.close()
        
    def getvalue(self) :
        self.name = self.entry1.get()
        self.cals = self.entry2.get()
        self.grams = self.entry3.get()
        self.w2.destroy()
        # save_in_file call
        self.save_in_file()
        self.save_in_listbox()

    def save_in_listbox(self) :
        if self.value == 'πρωινό' :
            f = open('data/morning.txt', 'a', encoding='utf-8')
            f.write('\n' + self.name + '-' + self.cals)     
        elif self.value == 'δεκατιανό' :
            f = open('data/decatan.txt', 'a', encoding='utf-8')
            f.write('\n' + self.name + '-' + self.cals)
        elif self.value == 'μεσημεριανό' :
            f = open('data/lunch.txt', 'a', encoding='utf-8')
            f.write('\n' + self.name + '-' + self.cals)
        elif self.value == 'απογευματινό' :
            f = open('data/evening.txt', 'a', encoding='utf-8')
            f.write('\n' + self.name + '-' + self.cals)
        elif self.value == 'βραδινό' :
            f = open('data/diner.txt', 'a', encoding='utf-8')
            f.write('\n' + self.name + '-' + self.cals)
        f.close()

    def showProfile(self):
        c = importlib.import_module('Client')
        Client = c.Client
        self.root.destroy()
        Client.Gui.beginView(Client.Gui.ProfileView)

#-----------------

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
