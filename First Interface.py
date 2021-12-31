import tkinter as tk
import os
from PIL import ImageTk,Image,ImageSequence

class Client():
    def __init__(self,parent):
        self.canvas=tk.Canvas(parent,width=520,height=400)
        self.canvas.grid(columnspan=3,rowspan=3)
        self.bg=ImageTk.PhotoImage(Image.open("diary.jpg"))
        self.labelimage=tk.Label(parent,image=self.bg)
        self.labelimage.grid(column=0,row=0,columnspan=3,rowspan=3)
        self.BUTTON=tk.Button(parent,text="Get Started",font="Arial 20"\
                              ,bg="#deeee1",command=self.ProfileData)
        self.BUTTON.bind("<Enter>",self.mouse_entered)
        self.BUTTON.bind("<Leave>",self.mouse_exit)
        self.BUTTON.grid(column=0,row=0,pady=5)

    def mouse_entered(self,event):
        parent.BUTTON.config(font="Arial 23")
        
    def mouse_exit(self,event):
        parent.BUTTON.config(font="Arial 20")

    def ProfileData(self):
        if not os.path.isdir("Data"):
            os.mkdir("Data")
            root.destroy()
            self.char=tk.Tk()
            self.char.config(bg="white")
            self.canvas=tk.Canvas(self.char,width=600,height=600)
            self.canvas.grid(columnspan=6,rowspan=6)

            self.namelabel=tk.Label(self.char,text="Name:",font="Arial 15")
            self.namelabel.grid(row=0,column=0)
            self.nameentry=tk.Entry(self.char,font="Arial 15")
            self.nameentry.grid(row=0,column=1)

            self.genderlabel=tk.Label(self.char,text="Gender:",font="Arial 15")
            self.genderlabel.grid(row=1,column=0)
            self.genderentry=tk.Entry(self.char,font="Arial 15")
            self.genderentry.grid(row=1,column=1)

            self.heightlabel=tk.Label(self.char,text="Height(m):",font="Arial 15")
            self.heightlabel.grid(row=2,column=0)
            self.heightentry=tk.Entry(self.char,font="Arial 15")
            self.heightentry.grid(row=2,column=1)

            self.weightlabel=tk.Label(self.char,text="Weight(kg):",font="Arial 15")
            self.weightlabel.grid(row=3,column=0)
            self.weightentry=tk.Entry(self.char,font="Arial 15")
            self.weightentry.grid(row=3,column=1)

            self.callabel=tk.Label(self.char,text="Cal/day:",font="Arial 15")
            self.callabel.grid(row=4,column=0)
            self.calentry=tk.Entry(self.char,font="Arial 15")
            self.calentry.grid(row=4,column=1)

            self.errorlb=tk.Label(self.char,text="",font="Arial 15")
            self.errorlb.grid(row=5,column=0)

            self.infolabel=tk.Label(self.char,font="Arial 15",\
                                    text="Βοήθησέ μας\nσυμπληρώνοντας\nτα κενά")
            self.infolabel.grid(row=0,column=2,rowspan=2)

            self.sequence=[ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                               Image.open('food.gif'))]
            self.image=self.canvas.create_image(500,315,image=self.sequence[0])
            self.animate(1)

            self.readybutton=tk.Button(self.char,text="Ready",font="Arial 18",command=self.\
                                       readybutton_clicked)
            self.readybutton.grid(row=5,column=2)
        else:
            root.destroy()
            self.Gui()

    def animate(self,counter):
        self.canvas.itemconfig(self.image,image=self.sequence[counter])
        self.char.after(27,lambda:self.animate((counter+1)%len(self.sequence)))

    def readybutton_clicked(self):
        name=parent.nameentry.get()
        gender=parent.genderentry.get()
        height=parent.heightentry.get()
        weight=parent.weightentry.get()
        cal=parent.calentry.get()
        if name and gender and height and weight and cal !="":
            name=name+"\n"
            height=height+"\n"
            gender=gender+"\n"
            weight=weight+"\n"
            cal=cal+"\n"
            li=[name,gender,height,weight,cal]
            with open("Data/data","w",encoding="utf-8") as f:
                for i in li:
                    f.write(i)
            self.char.destroy()
            self.Gui()
        else:
            self.errorlb=tk.Label(parent.char,text="Fill in all options",\
                                  font="Arial 18")
            self.errorlb.grid(row=5,column=1)

    def Gui(self):
        self.main=tk.Tk()
        
        
        
if __name__=='__main__':
    root=tk.Tk()
    root.title("Food Diary")
    parent=Client(root)
    root.mainloop()

