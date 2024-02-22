from tkinter import *
from m_objetosTk import *





if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")

    #datedatapicker
    #s = StringVar(root,value="")
    #lbldata = Label(root,text="",textvariable=s,width=25,bd=1,relief=SOLID)
    #lbldata.pack()
    #toplevel = Datedatapicker(root,s,True) # s==StringVar, True== Força saida de dados caso usuario não escolha data.

    #Canvas gradiente
    #gra = GradientFrame(root,color1="#7FFFD4",color2="#66CDAA")
    #gra.pack(side=TOP,fill=BOTH,expand=True)

    #Frame com Label e datedatapicker - uma personalização com icone de calendario lateral
    lbldata = FrmLabelCalendar(root)
    lbldata.pack()

    #Treeview que aceita imagens em qualquer tupla

    #Radio button personalizado

    #Sistema de coordenadas no reportelab


    root.mainloop()