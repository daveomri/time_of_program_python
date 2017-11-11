# David Omrai
# It is just a simply timer, but it could help someone
import tkinter
from tkinter import *

s1 = 0
s2 = 0
m1 = 0
m2 = 0
h1 = 0
h2 = 0

master = Tk()
master.title("Time of program")
lokop = Canvas(master, width=500, height=500, bg="black")
lokop.pack()
text = Label(lokop, text="Time of program", font="Courier 18 bold", fg="green", bg="black")
text.pack(padx=50, pady = 25)
cas = Label(lokop, text = str(h2)+str(h1) + ":" + str(m2)+str(m1) + ":" + str(s2)+str(s1), font="Courier 30", fg="white", bg="black")
cas.pack(pady= 50)
def yup():
    global s2
    global s1
    global m2
    global m1
    global h2
    global h1
    s1 +=1
    if s1 > 9:s1 = 0;s2 += 1
    if s2 > 5:s2 = 0;m1 += 1
    if m1 > 9:m1 = 0;m2 += 1
    if m2 > 5:m2 = 0;h1 += 1
    if h1 > 9:h1 = 0;h2 += 1
    cas.config(text=str(h2)+str(h1) + ":" + str(m2)+str(m1) + ":" + str(s2)+str(s1))
    cas.after(1000, yup)
yup()
master.mainloop()
