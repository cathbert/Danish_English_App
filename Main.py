# Danish Dictionary Application
# Project commenced on: 16 Jan 2019
# Project completed on: -- --- ----
# Developed by Cathbert Mutaurwa

import tkinter as tk
from PIL import Image, ImageTk
import sys

class DanishDictionary(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("800x500+300+100")
        self.title("CCH's Danish Dictionary")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0,column=0,sticky='nwes')

        self.showFrame(StartPage)

            # Frame for the main window bottom credit bar
        credit_frame = tk.Frame(self, bg='turquoise', relief='groove', bd=1)
        credit_frame.pack(fill='x')

        label = tk.Label(credit_frame,bg='turquoise',text='',font=('Arial',8,'bold'))
        label.pack(anchor='center')

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(bg='lightblue')

            # Frame for main title label and logo
        mainlabel_frame = tk.Frame(self, bg='turquoise', relief='groove', bd=1)
        mainlabel_frame.pack(fill='x')

            # Loading logo using PIL
        img = Image.open("images/dmk.jpg")
        render = ImageTk.PhotoImage(img)

            # Rendering logo to output label
        l = tk.Label(mainlabel_frame, image=render, bg='turquoise')
        l.image = render
        l.pack()

            # Application's main title label
        main_label = tk.Label(mainlabel_frame, text="Danish Dictionary 0.1", fg="red", bg='turquoise', font=('Verdana',14))
        main_label.pack(fill='x')

            # Subtitle label containing credits and trademark name
        label = tk.Label(mainlabel_frame,bg='turquoise',text='Trademark CCH All rights reserved 2019',font=('Arial',8))
        label.pack(anchor='center')

            # Frame for menu below main title
        menu_frame = tk.Frame(self, bg='lightblue')
        menu_frame.pack(fill='x')

            # This label is being used as a double tab on the menu
        space = tk.Label(menu_frame, text="\t\t", bg="lightblue")
        space.pack(side='left')

        def about():
            root = tk.Tk()
            root.title("About Danish Dictionary")
            root.geometry("400x300+500+150")
            root.resizable(False, False)
            root.mainloop()

            # About button within the menu section
        about_label = tk.Button(menu_frame, text="About", relief='flat',\
                                bg="lightblue", font=("Verdana", 10), command=about)
        about_label.pack(side='left')

if __name__ == "__main__":
    app = DanishDictionary()
    app.mainloop()
