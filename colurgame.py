from tkinter import *
import random

c=['green','yellow','blue','black','red','orange','purple','pink','brown']
sc=0
tleft=30
n=0
def startGame(event):
    
    if tleft==30:
        countdown()
    nextcolour()

def nextcolour():

    global n,sc,tleft
    if tleft>0:
         n+=1
         b1.focus_set()
         
         if b1.get()==c[1]:
             
             sc+=1
         b1.delete(0,'end')
         random.shuffle(c)
         word.config(fg=str(c[1]),text=str(c[0]))
         print(c[1],c[0])
         s.config(text="score:"+str(sc))
         t1.config(text="total number of attempts:"+str(n))

def countdown():
    global tleft
    if tleft>0:
        tleft-=1
        t.config(text="time left:"+str(tleft))
        t.after(1000,countdown)
        
        


w=Tk()
w.geometry("400x400")
w.configure(bg="grey")
w.title("colour game")


l=Label(w,text="write the colour of word not the word in given space",font=('Helvetica',12))
l.pack()
s=Label(w,text="press enter to start",font=('Arial',12))
s.pack()
t=Label(w,text="time left:"+str(tleft),font=('Arial',12))
t.pack()
t1=Label(w,font=('Arial',12))
t1.pack()
word=Label(w,font=('Arial',20))
word.pack()
b2=Button(w,text="press",command=lambda:startGame(True))
b2.pack()

b1=Entry(w)

b1.pack()
b1.focus_set()





w.mainloop()
