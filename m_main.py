from tkinter import *
from m_calendario import Datedatapicker





if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200")

    #datedatapicker
    s = StringVar(root,value="")
    lbldata = Label(root,text="",textvariable=s,width=25,bd=1,relief=SOLID)
    lbldata.pack()
    toplevel = Datedatapicker(root,s,True) # s==StringVar, True== Força saida de dados caso usuario não escolha data.

    #Canvas gradiente
    
    #Treeview que aceita imagens em qualquer tupla

    #Radio button personalizado

    #Sistema de coordenadas no reportelab


    root.mainloop()