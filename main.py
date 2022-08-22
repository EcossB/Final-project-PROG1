from tkinter import *
from tkinter import ttk
import sqlite3
from Register import *
from Register import anime_crud

root = Tk()

def create_CUI():
    class interface():
        def __init__(self, root):
            self.root = root
            self.root.title("Proyecto Final")
            root.configure(background= "#add8e6")

            x = (self.root.winfo_screenwidth()//2) - 1
            y = int(self.root.winfo_screenheight() * 0.1)
            self.root.geometry('380x565+'+ str(x) + '+' + str(y))

            #Frame

            mainframe = Frame()
            mainframe.pack()
            mainframe.config(width= 380 ,height=565, bg= "#add8e6")
            
            maintitle = Label(mainframe, text= "Anime \n Manager", font= ("Times New Roman", 24),bg= "#add8e6" )
            maintitle.grid(column=0, row=0,  pady= 20, columnspan= 3)

            def manager():
                pass

            def reports():
                pass

            def settings():
                pass

            def info():
                pass

            def close():
                pass

            #Buttons
            animeButton = ttk.Button(mainframe, text= "Gestionar personajes", command= manager())
            animeButton.grid(column = 2, row = 2, ipadx=10, ipady= 10, padx=20, pady=20)

            reportbutton = ttk.Button(mainframe, text = "Reportes", command= reports())
            reportbutton.grid(column= 2, row = 3, ipadx=10, ipady= 10, padx=20, pady=20 )

            configbutton = ttk.Button(mainframe, text = "Configuracion", command= settings())
            configbutton.grid(column= 2 , row = 4, ipadx=10, ipady= 10, padx=10, pady=20)

            infobutton = ttk.Button(mainframe, text= "Acerca De", command= info())
            infobutton.grid(column= 2, row = 5, ipadx=10, ipady= 10, padx=20, pady=20)

            closebutton = ttk.Button(mainframe, text = "Salir", command= close())
            closebutton.grid(column=2, row = 6, ipadx=10, ipady= 10, padx=20, pady=20)



    win = interface(root)
    root.mainloop()


if __name__ == "__main__":
    create_CUI()