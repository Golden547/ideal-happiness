# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:31:48 2022

@author: shn99
"""

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Fever_report")
root.geometry("600x600")

question1_radiobutton=StringVar(value="0")

Question1=Label(root, text = "Do you experience shortness of breath?")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radiobutton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text ="no", variable=question1_radiobutton, value="no")
question1_r2.pack

question2_radiobutton=StringVar(value="0")
Question2=Label(root, text = "Are you ever confused, disoriented, or forget things easily?")
Question2.pack()
question2_r1=Radiobutton(root, text = "yes", variable=question2_radiobutton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "no", variable=question2_radiobutton, value="no")
question2_r2.pack()

question3_radiobutton=StringVar(value="0")
Question3=Label(root, text = "Does your body swell at all?")
Question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question3_radiobutton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question3_radiobutton, value="no")
question3_r2.pack()

def fever_score():
    score=0
    if question1_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question2_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question3_radiobutton.get()=="yes":
        score=score+20
        print(score)    
        
        if score<= 20:
            messagebox.showinfo("Report", "You don't need to visit a doctor.")
        elif score > 20 and score <= 40:
            messagebox.showinfo("Report", "You may have to visit a doctor.")
        else :
            messagebox.showinfo("Report", "You should visit a doctor.")
btn = Button(root, text="click me", command= fever_score)
btn.pack()
root.mainloop()