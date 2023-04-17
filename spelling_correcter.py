from tkinter import *
from textblob import TextBlob

app=Tk()
app.configure(background='greenyellow')
app.geometry("750x350")
app.resizable(0,0)
app.title("Spell Checker and Corrector App")

heading_text=Label(app,text="Welcome to Spell Checker and Corrector App",font='Arial 16 bold',fg='yellow',bg='black')
lbl_input=Label(app,text="input word here",font='Arial 14 bold', fg='white', bg='magenta')
lbl_corrected=Label(app,text="corrected word",font='Arial 14 bold', fg='white', bg='green')

heading_text.grid(row=0, column=1,pady=20)
lbl_input.grid(row=1, column=0,padx=10)
lbl_corrected.grid(row=3, column=0,padx=10)

input_word_box=Entry(app,width=40,font='Arial 14 bold')
corrected_word_box=Entry(app,width=40,font='Arial 14 bold')

input_word_box.grid(row=1, column=1,pady=10)
corrected_word_box.grid(row=3, column=1,pady=10)


def spellCorrection():
    word_input=input_word_box.get()
    text=TextBlob(word_input)
    
    corrected_word=str(text.correct())
    
    corrected_word_box.insert(10,corrected_word)

def clearAllWords():
    input_word_box.delete(0,END)
    corrected_word_box.delete(0,END)


btn1=Button(app, text='Correction',font='Arial 14 bold', fg='black', bg='aqua', border=5,command=spellCorrection)
btn1.grid(row=2,column=1)

btn1=Button(app, text='Clear All',font='Arial 14 bold', fg='black', bg='red', border=5,command=clearAllWords)
btn1.grid(row=4,column=1)

app.mainloop()
