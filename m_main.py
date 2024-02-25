from tkinter import *
from m_objetosTk import *





if __name__ == "__main__":
    root = Tk()
    root.geometry("1050x500")

    #datedatapicker
    #s = StringVar(root,value="")
    #lbldata = Label(root,text="",textvariable=s,width=25,bd=1,relief=SOLID)
    #lbldata.pack()
    #toplevel = Datedatapicker(root,s,True) # s==StringVar, True== Força saida de dados caso usuario não escolha data.

    #Canvas gradiente
    #gra = GradientFrame(root,color1="#7FFFD4",color2="#66CDAA")
    #gra.pack(side=TOP,fill=BOTH,expand=True)

    #Frame com Label e datedatapicker - uma personalização com icone de calendario lateral
    #lbldata = FrmLabelCalendar(root)
    #lbldata.pack()

    #Treeview que aceita imagens em qualquer tupla
    print("mode_selection - [onerow - multrows - checkbox - onecheckbox]")
    names =("ID","NAME","MARCAR","RECEBIDO","RESULTADO","OUTRO","TESTANDO OUTRO")
    typescolumns = ("#str","#str","#chk","#str","#str","#str","#str")
    widthcolumns = (15,20,13,15,16,20,25)
    tree = TreeRows(root,mode_selection="onerow",lineselection=True,bdrows=0,
                    bgcolor="#00FFFF",colorrows="#87CEFA",names_bar=names,
                    height_bar=2,height_=300,root=root,
                    width_scroll=2,typecampos=typescolumns,
                    widthcolumns=widthcolumns)
    tree.pack(side=TOP)

    imgmoney = PhotoImage(data=IMG_MONEY_16X16)
    for w in range(50):
        row= (f"CO-00000{w}",f"CLIENTE {w:03d}","#chk",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}")
        tree.insertrow(row)
    

    #Radio button personalizado

    #Sistema de coordenadas no reportelab


    root.mainloop()