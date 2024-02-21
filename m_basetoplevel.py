from tkinter import *
from m_constantesP_objetos import IMG_CLOSE_32X32,IMG_MINIMIZAR_32X32,IMG_LOGO_128X128B
from Funcoes_Auxiliares import F_Auxiliares
class BaseToplevel(Toplevel):
    def __init__(self,root,cnxBD=None,logo="",modo="add",titulojanela="",namebtnCadclient="Registrar Cliente",dimensao=(750,550),imglogo=IMG_LOGO_128X128B,**kwargs) -> None:
        super(BaseToplevel,self).__init__(root,**kwargs)
        self.logo128x128 = logo
        self.root = root
        self.cnxBD = cnxBD
        self.d = dimensao
        self.modo = modo
        self.titulojanela = titulojanela
        self.imglogo = imglogo
        self.func = F_Auxiliares(self)
        self.geometry(self.func.disposicao_janela(self.d))

        self["background"] = '#000fff000' # "#4682B4"
        self.protocol("WM_DELETE_WINDOW",self.destroy_)
        self.nomebtnCadastrarPessoa = namebtnCadclient
        self.overrideredirect(True)
        self.propagate(False)
        self.grab_set()
    def to_overrideredirect(self,event=None):
        self.update_idletasks()
        self.overrideredirect(True)
        self.state("normal")
    def minimizar(self,event=None):
        self.update_idletasks()
        self.overrideredirect(False)
        self.iconify()
        self.state("iconic")
    def destroy_(self,event=None):
        self.destroy()
    def criarwidgets(self):
        #self.bind("<Map>",self.to_overrideredirect)
        self.frmTOP = Frame(self,background="#4682B4",bd="0p",height="18p",relief=SOLID) # #4682B4   "#00FFFF"
        self.frmTOP.pack(side=TOP,fill=X,pady=("0p","2p"),ipadx="0p")
        
        self.frmTOP.bind("<Button-1>",self.pressedStart)
        self.frmTOP.bind("<B1-Motion>",lambda e: self.movetomouse(e,self.d))

        self.img_close = PhotoImage(data=IMG_CLOSE_32X32)
        self.btnClose = Button(self.frmTOP,text="Fechar",width=32,height=32,relief=SOLID,bd="0p",command=self.destroy_,image=self.img_close,background="#4682B4")
        self.btnClose.pack(side=RIGHT,padx=("5p","5p"),pady=("5p","5p"))

        self.img_minimizar = PhotoImage(data=IMG_MINIMIZAR_32X32)
        self.btnminimizar = Button(self.frmTOP,width=32,height=32,relief=SOLID,bd="0p",command=lambda : self.minimizar() ,image=self.img_minimizar,background="#4682B4")
        self.btnminimizar.pack(side=RIGHT,padx=("5p","5p"),pady=("5p","5p"))

        self.frmlogo = Frame(self,background="white",border="0p",height="300p",relief=SOLID)
        self.frmlogo.pack(side=TOP,fill=X,pady=("0p","0p"),ipady=0)

        self.imgLogo = PhotoImage(data=self.imglogo,width=128)
        self.lblimgLogo = Label(self.frmlogo, height=128,image=self.imgLogo,justify=LEFT,background="white",relief=SOLID,bd="0p")
        self.lblimgLogo.pack(side=LEFT,expand=True,pady="10p")

        font_ = ("Helvetica",18,"bold")
        self.lblLogo = Label(self.frmlogo, text=self.titulojanela,relief=SOLID,justify=CENTER,background="white",font=font_,foreground="Blue",height=4,bd="0p")
        self.lblLogo.pack(side=LEFT,fill=X,expand=True,pady=("0p","9p"))

        #self.frmclose = Frame(self.frmTOP,background="white",border="0p",width="0p",padx="0p",height=4)
        #self.frmclose.pack(side=RIGHT,fill=X,expand=True,padx=("20p","0p"),pady=("0p","20p"))

        self.frmHeader = Frame(self,background="#F8F8FF",height="600p",padx="0p",pady="0p") ##F8F8FF  #E0FFFF
        self.frmHeader.pack(side=TOP,fill=BOTH,expand=True,pady=("0p","0p"))

        self.frmTOP.bind("<Map>",self.to_overrideredirect)
        #self.frmTOP.bind("<Visibility>",self.to_overrideredirect) não funciona
        #self.frmTOP.bind("<Activate>",self.to_overrideredirect) não funciona
        self.frmWidgets = Frame(self.frmHeader,background="#00BFFF")
        self.frmWidgets.pack(side=TOP,fill=BOTH,expand=True,ipadx=0,ipady=0,pady=("0p","0p"))     
        
        self.frmFooter = Frame(self,background="blue",height="0p",padx="0p",pady="0p") ##F8F8FF  #E0FFFF
        self.frmFooter.pack(side=BOTTOM,fill=X,pady=("0p","0p"))  
    def pressedStart(self,event):
        self.x = event.x
        self.y = event.y
        print(f"ButtonPress: {event.x, event.y}")
    def movetomouse(self,event,dimensao):
        #print(f"movemouse: {event.x_root,event.y_root}")
        x= (event.x_root - self.x - self.winfo_rootx()+self.winfo_rootx())
        y= (event.y_root - self.y - self.winfo_rooty()+self.winfo_rooty())
        #print(x,y)
        self.geometry(f"{dimensao[0]}x{dimensao[1]}+{x}+{y}")
    def addnew_widgets(self,obj,side=LEFT):
        self.novowidgets = obj(self.frmWidgets)
        self.novowidgets.pack(side=side)
    def addnew_widgtesFooter(self,obj):
        self.novowidgetsfooter = obj(self.frmFooter)
        self.novowidgetsfooter.pack(side=TOP,fill=X)
    def getFrmWidgets(self)->Frame:
        return self.frmWidgets