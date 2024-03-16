from tkinter import *
from p_objetosTk.m_objetosTk import *

def printar(value=""):
    print(f"o valor de value: {value}")

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
    # print("mode_selection - [onerow - multrows - checkbox - onecheckbox]")
    # names =("ID","NAME","MARCAR","RECEBIDO","RESULTADO","OUTRO","TESTANDO OUTRO")
    # typescolumns = ("#str","#str","#chk","#str","#str","#str","#str")
    # widthcolumns = (15,20,13,15,16,20,25)
    # tree = TreeRows(root,mode_selection="onerow",lineselection=True,bdrows=0,
    #                 bgcolor="#00FFFF",colorrows="#87CEFA",names_bar=names,
    #                 height_bar=2,height_=300,root=root,
    #                 width_scroll=2,typecampos=typescolumns,
    #                 widthcolumns=widthcolumns)
    # tree.pack(side=TOP)
    # imgmoney = PhotoImage(data=IMG_MONEY_16X16)
    # for w in range(50):
    #     row= (f"CO-00000{w}",f"CLIENTE {w:03d}","#chk",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}")
    #     tree.insertrow(row)

    # #Entry formatada para money
    # ety = MoneyMasked(root,simbols="R$ ",length=10) #logica do length está incorreta.
    # ety.pack()

    # #Entry formatada para qualquer padrao
    # ety2 = Masked_all(root,simbol="",formato="2dig/2dig/4dig")
    # ety2.pack(pady=(4,4))
    

    #Radio button personalizado
    # frmRbd = FrmRadioBtn(root)
    # varoption = StringVar(value="cpf")
    # calbackcpf = lambda *args: print(args)
    # calbackrg = lambda *args: print(args)
    # calbacknome = lambda *args: print(args)
    # frmRbd.add_btn("cpf",varoption,calbak=calbackcpf,text="CPF")
    # frmRbd.add_btn("rg",varoption,calbak=calbackrg,text="RG")
    # frmRbd.add_btn("nome",varoption,calbak=calbacknome,text="Nome")
    # frmRbd.pack()

    #Topelevel personalizado
    tp = BaseToplevel(root,titulojanela="Sistema de gestão e orçamentos")
    tp.config_all("lbllogo",anchor=W,padx=5)
    tp.config_all("frmHeader",bg="#87CEFA")


    #Sistema de coordenadas no reportelab


    root.mainloop()