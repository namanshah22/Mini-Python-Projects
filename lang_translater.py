from tkinter import *
from translate import Translator

Screen = Tk()
Screen.title("Language Translator App")
Screen.geometry("450x350")
Screen.resizable(0, 0)
Screen.config(bg="pink")

InputLanguageChoice = StringVar()
InputLanguageChoice.set("English")
LanguageChoice = OptionMenu(Screen, InputLanguageChoice, 'Hindi', 'English', 'French', 'German', 'Spanish')
LanguageChoice.config(bg="green", fg="white")
LanguageChoice["menu"].config(bg="red")
LanguageChoice.grid(row=2, column=2, pady=10, ipadx=15)

OutputLanguageChoice = StringVar()
OutputLanguageChoice.set("English")
LanguageChoice = OptionMenu(Screen, OutputLanguageChoice, 'Hindi', 'English', 'French', 'German', 'Spanish', 'Amharic')
LanguageChoice.config(bg="green", fg="white")
LanguageChoice["menu"].config(bg="red")
LanguageChoice.grid(row=2, column=3, pady=10, ipadx=15)

Label(Screen, text="Enter Text Here").grid(row=3, column=1)
TextVar = StringVar()
Textbox = Entry(Screen, textvariable=TextVar)
Textbox.grid(row=3, column=2, ipadx=15, ipady=20)

Label(Screen, text="Output").grid(row=3, column=3)
OutputVar = StringVar()
OutputTextbox = Entry(Screen, textvariable=OutputVar)
OutputTextbox.grid(row=3, column=4, ipadx=15, ipady=20)

def Translate():
    translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=OutputLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

B = Button(Screen, text="Translate", command=Translate, relief=GROOVE)
B.grid(row=4, column=3)

Screen.mainloop()
