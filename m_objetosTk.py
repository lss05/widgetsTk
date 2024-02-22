from tkinter import *
from Funcoes_Auxiliares import F_Auxiliares
from m_constantesP_objetos import *
from datetime import date
from time import strftime
from calendar import Calendar

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
class FrameScrollVert(Frame):
    def __init__(self,master,width_,height_,root=None,**kwargs) -> None:
        super(FrameScrollVert,self).__init__(master,**kwargs)
        self.flagRolar = False
        self.cvs = Canvas(self,width=width_,height=height_,bg="white")
        self.scrVert = Scrollbar(self,orient=VERTICAL,command=self.cvs.yview)
        self.conteiner = Frame(self.cvs,bg="white")

        self.conteiner.bind("<Configure>",lambda e: self.cvs.configure(scrollregion=self.cvs.bbox("all")))
        self.cvs.configure(yscrollcommand=self.scrVert.set)

        self.n_conteiner = self.cvs.create_window(0,0,window=self.conteiner)

        self.scrVert.pack(side=RIGHT,fill=Y,padx=(0,0))
        self.cvs.pack(side=LEFT,fill=BOTH)

        self.cvs.itemconfigure(self.n_conteiner,anchor=NW,width=width_)
        if root:
            root.bind("<MouseWheel>",self.mousewheel,add="+")
            self.bind("<Enter>",lambda e: self.ativarFlagRolar(True))
            self.bind("<Leave>",lambda e: self.ativarFlagRolar(False))
        self.configure(bg="white")
    def mousewheel(self,event=None):
        if self.flagRolar:
            value = int(-1*(event.delta/120))
            self.cvs.yview_scroll(value, "units")
            print(value)
    def ativarFlagRolar(self,flag:bool):
        self.flagRolar = flag
    def resetconfigwidgets(self,widget_=None,config={}):
        for widget in self.conteiner.children.values():
            if widget != widget_:
                widget.configure(bg="SystemButtonFace",fg="SystemButtonText")
        widget_.configure(**config)
    def clearConteiner(self):
        def limpar():
            for w in self.conteiner.winfo_children():
                w.destroy()
        #td = Thread(target=limpar)
        #td.start()
        limpar()
        print("LIMPANDO CONTEINER - Linha 249 m_objTk.py")
    def configure_(self,obj:str,kw):
        #self.__dict__[obj].configure(**kw)
        self.cvs.itemconfigure(self.n_conteiner,**kw)    
class Datedatapicker(BaseToplevel):
    def __init__(self,root,varstring,force_data_output:bool,*args,**kwargs):
        super(Datedatapicker,self).__init__(root,*args,**kwargs)
        self.geometry("304x400")
        self.d = (304,400)
        self.cordabarra = "white"
        self.dia,self.hoje = date.today().day,date.today()
        self.mes = date.today().month
        self.ano = date.today().year
        self.var = varstring
        self.force_data_output = force_data_output
        self.configbtnsmescorrent = dict(bg="#00BFFF",fg="red")
        self.configbtnsmesnotcorrent = dict(bg="#00FFFF",fg="red")
        self.configbtnselected = dict(bg="#0000FF",fg="white")
        self.configbtnhoje = dict(bg="#6495ED",fg="white")

        self.configEnter = dict(bg="#2F4F4F",fg="white")
        self.configLeave = {}
        #print(self.attributes())
        self.criarwidgets()
        self.funtions = {
            "00:00:00" : self.__atualizaData
        }
        self.__relogion()      
    def __atualizaData(self):
        self.dia,self.hoje = date.today().day,date.today()
        self.mes = date.today().month
        self.ano = date.today().year
        self.loaddiasmes(self.meses[self.mes-1])
    def __setdata(self,data:str):
        self.var.set(data)
    def __relogion(self):
        def tic():
            hora = strftime("%H:%M:%S")
            self.title_.configure(text=hora)
            if hora in self.funtions:
                self.funtions[hora]()
            self.after(1000,self.__relogion)
        tic()
    def criarwidgets(self):
        self.frmTOP = Frame(self,background="#4682B4",bd="0p",height="18p",relief=SOLID) # #4682B4   "#00FFFF"
        self.frmTOP.pack(side=TOP,fill=X,pady=("0p","0p"),ipadx="0p")
        
        self.frmTOP.bind("<Button-1>",self.pressedStart)
        self.frmTOP.bind("<B1-Motion>",lambda e: self.movetomouse(e,self.d))

        font_ = ("Arial",12,"bold")
        self.title_ = Label(self.frmTOP,bg=self.frmTOP["bg"],fg="white",font=font_,relief=SOLID,bd=0,anchor=CENTER)
        self.title_.pack(side=LEFT,padx=("4px","4px"))

        self.img_close = PhotoImage(data=IMG_CLOSE_32X32)
        self.btnClose = Button(self.frmTOP,text="Fechar",width=32,height=32,relief=SOLID,bd="0p",command=self.destroy_,image=self.img_close,background="#4682B4")
        self.btnClose.pack(side=RIGHT,padx=("5p","5p"),pady=("5p","5p"))

        self.img_minimizar = PhotoImage(data=IMG_MINIMIZAR_32X32)
        self.btnminimizar = Button(self.frmTOP,width=32,height=32,relief=SOLID,bd="0p",command=lambda : self.minimizar() ,image=self.img_minimizar,background="#4682B4")
        self.btnminimizar.pack(side=RIGHT,padx=("5p","5p"),pady=("5p","5p"))

        self.frmHeader = Frame(self,padx=("1px","1px")) ##F8F8FF  #E0FFFF
        self.frmHeader.pack(side=TOP,fill=BOTH,expand=True,pady=("0p","0p"))


        corbarra = "white"
        self.frmbarratop = Frame(self.frmHeader,bg=corbarra,height="10px")
        self.frmbarratop.pack(side=TOP,fill=X)

        hbtn = 1
        fontbtnmes = ("Arial",14,"bold")
        fontbtnano = ("Arial",18,"bold")
        fgbtnmesano = "blue"
        ano = date.today().year

        self.btnmes = Button(self.frmbarratop,command=self.loadmeses,text="Janeiro",fg=fgbtnmesano,bg=corbarra,bd=0,relief=SOLID,width=16,height=hbtn,font=fontbtnmes)
        self.btnmes.pack(side=LEFT,fill=Y)
        self.btnmes.bind("<Enter>",lambda e: e.widget.configure(fg="red"))
        self.btnmes.bind("<Leave>",lambda e: e.widget.configure(fg=fgbtnmesano))

        self.btnano = Button(self.frmbarratop,command=self.loaddiasanos,text=str(ano),fg=fgbtnmesano,bd=0,bg=corbarra,relief=SOLID,width=20,height=hbtn,font=fontbtnano)
        self.btnano.pack(side=RIGHT,fill=Y)
        self.btnano.bind("<Enter>",lambda e: e.widget.configure(fg="red"))
        self.btnano.bind("<Leave>",lambda e: e.widget.configure(fg=fgbtnmesano))

        self.frmsubheader = Frame(self.frmHeader,bg="yellow")
        self.frmsubheader.pack(side=TOP,fill=BOTH,expand=True)

        h,w = 400,300
        columnspan = 1
        self.frmsubheaderdiasmes = Frame(self.frmsubheader,bg="white",height=h,width=w)
        self.frmsubheaderdiasmes.grid(row=0,column=0,sticky=NSEW,columnspan=columnspan)

        self.frmsubheadermes = Frame(self.frmsubheader,bg="white",height=h,width=w)
        self.frmsubheadermes.grid(row=0,column=0,sticky=NSEW,columnspan=columnspan)

        self.meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                 "Julho","Agosto","Setembro","Outubro","Novembro","Desembro"]
        row = 0
        for i,mes in enumerate(self.meses):
            if i%4==0:
                row+=1
            btn = Button(self.frmsubheadermes,width=10,height=5,command=lambda mes=mes: self.loaddiasmes(mes),text=mes,bd=0,relief=SOLID,bg="white")
            btn.grid(row=row,column=i%4,sticky=NSEW)
            btn.bind("<Enter>",lambda e: e.widget.configure(bg="#ADD8E6"))
            btn.bind("<Leave>",lambda e: e.widget.configure(bg="white"))

        self.frmsubheaderanos = Frame(self.frmsubheader,bg="black",height=h,width=w)
        self.frmsubheaderanos.grid(row=0,column=0,sticky=NSEW,columnspan=columnspan)

        self.scrll_v = FrameScrollVert(self.frmsubheaderanos,295,335,self)
        self.scrll_v.pack(side=TOP,fill=BOTH,expand=True)
        self.scrll_v.scrVert.configure(width=1)
        
        anos = [ano for ano in range(1900,ano+1)][::-1]
        row = 0
        for i,ano in enumerate(anos):
            if i%4==0:
                row+=1
            btn = Button(self.scrll_v.conteiner,width=10,height=2,command=lambda ano=ano: self.btnloadano(ano),text=str(ano),bd=0,relief=SOLID,bg="white")
            btn.grid(row=row,column=i%4,sticky=NSEW)
            btn.bind("<Enter>",lambda e: e.widget.configure(bg="#ADD8E6"))
            btn.bind("<Leave>",lambda e: e.widget.configure(bg="white"))


        self.loaddiasmes(self.meses[self.mes-1])
    def limparfrmdiasdomes(self):
        for w in self.frmsubheaderdiasmes.winfo_children():
            w.destroy()
    def loaddiasmes(self,mes):
        self.btnselection=None
        self.btnhoje = None
        self.flagleave:bool = True
        def leavebtn(event):
            if self.btnhoje==self.btnselection==event.widget:
                event.widget.configure(**self.configbtnselected)
            else:
                if event.widget != self.btnselection:
                    event.widget.configure(**self.configLeave)
                if self.flagleave:
                    event.widget.configure(**self.configLeave)
        def enterbtn(event):
            self.configLeave["bg"] = event.widget["bg"]
            self.configLeave["fg"] = event.widget["fg"]
            event.widget.configure(**self.configEnter)
            if self.btnselection == event.widget:
                self.flagleave = True
            else:
                self.flagleave = False
        #@validahoje
        def clickbtndia(event):
            if self.btnselection==None:
                self.btnselection = event.widget
                self.btnselection.configure(**self.configbtnselected)
            else:
                if self.btnselection.mescorrente:
                    self.btnselection.configure(**self.configbtnsmescorrent)
                else:
                    self.btnselection.configure(**self.configbtnsmesnotcorrent)

                if self.btnhoje == event.widget:
                    self.btnhoje.configure(**self.configbtnselected)
                else:
                    if self.btnhoje:
                        self.btnhoje.configure(**self.configbtnhoje)
                
                event.widget.configure(**self.configbtnselected)

                self.btnselection = event.widget
            data:date = event.widget.data_
            self.dia = data.day
            data_ = f"{self.dia:02d}/{data.month:02d}/{data.year}"

            self.btnmes.configure(text=self.meses[data.month-1])
            self.btnano.configure(text=str(data.year))

            self.__setdata(data_)
        self.limparfrmdiasdomes()
        def filtrardias(meses,hoje:date):
            mesescorrent = []
            for row in meses:
                for dia in row:
                    if dia.month == hoje.month:
                        mesescorrent.append(dia)
            return mesescorrent
        
        self.btnmes.configure(text=mes)
        
        self.mes = self.meses.index(mes)+1

        self.newdata = date(self.ano,self.mes,self.dia)

        self.frmbarraWeek = Frame(self.frmsubheaderdiasmes,bg=self.cordabarra,height="25px")
        self.frmbarraWeek.pack(side=TOP,fill=X)
        print("ATUALIZANDO DATAPICKER")
        diadasemana = {6:"Dom",
                       0:"Seg",
                       1:"Ter",
                       2:"Qua",
                       3:"Qui",
                       4:"Sex",
                       5:"Sáb"}

        nameweek = ["Dom","Seg","Ter","Qua","Qui","Sex","Sáb"]
        padx = ("0px","0px")
        for lbl in nameweek:
            if lbl=="Sáb":
                padx = ("0px","2px")
            self.frm = Frame(self.frmbarraWeek,name=lbl.lower(),bg=self.cordabarra)
            self.frm.pack(side=LEFT,fill=X,expand=True,padx=padx)
            self.lblweek = Label(self.frm,text=lbl,anchor=CENTER,bg=self.cordabarra,width=5)
            self.lblweek.pack()
            

        calend = Calendar(6)
        diasdomes = calend.monthdatescalendar(self.newdata.year,self.newdata.month)
        mescorrente_ = filtrardias(diasdomes,self.newdata)

        for i,rowdatesweek in enumerate(diasdomes):
            cont = 0
            for key,diaseman_ in diadasemana.items():
                data:date = rowdatesweek[cont]

                if data.year!=self.newdata.year or data.month!=self.newdata.month: #or if data not in mescorrente_: 
                    config = self.configbtnsmesnotcorrent
                    mescorrente = False
                else:
                    mescorrente = True
                    config = self.configbtnsmescorrent if data != self.hoje else self.configbtnhoje

                frame = self.frmbarraWeek.nametowidget(name=diaseman_.lower())
                dia = f"{data.day:02d}"
                btndia = Button(frame,text=dia,bd=0,relief=SOLID,anchor=CENTER,height=2,width=5,**config)
                btndia.pack(side=TOP,pady=("0px","1px"))
                btndia.mescorrente = mescorrente
                btndia.data_ = data
                btndia.bind("<Enter>",enterbtn)
                btndia.bind("<Leave>",leavebtn)
                btndia.bind("<Button-1>",lambda e: clickbtndia(e))
                cont += 1

                if data == self.hoje:
                    self.btnhoje = btndia
        
        self.frmsubheaderdiasmes.tkraise()
    def btnloadano(self,ano):
        self.btnano["text"] = ano

        self.ano = ano
        self.dia = 1
    
        newdata = f"{1:02d}/{self.mes:02d}/{ano}"
        self.loaddiasmes(self.meses[self.mes-1])

        self.__setdata(newdata)
    def loaddiasanos(self):
        self.frmsubheaderanos.tkraise()
    def loadmeses(self):
        self.frmsubheadermes.tkraise()
    def destroy_(self, event=None):
        if not self.var.get() and self.force_data_output:
            self.var.set(f"{self.hoje.day:02d}/{self.hoje.month:02d}/{self.hoje.year}")
        self.destroy()
class GradientFrame(Canvas):
    '''Um quadro de gradiente que usa uma tela para desenhar o plano de fundo'''
    def __init__(self, parent, color1="#C6CCFF", color2="gray35", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        #super().__init__(parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)
    def _draw_gradient(self, event=None):
        '''Desenhando o gradiente'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))

            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient"), fill=color)
        self.lower("gradient")
class FrmLabelCalendar(Frame):
    def __init__(self,master):
        super(FrmLabelCalendar,self).__init__(master)
        self.configure(
            bd=1,
            relief=SOLID
        )
        self.vardata = StringVar(value="__/__/____")
        self.imgdata = PhotoImage(data=IMG_CALENDAR_24X24)
        self.font_ = ("Arial",12)
        self.criarjanela()
    def criarjanela(self):
        def invokarDatedatapicker():
            calendario = Datedatapicker(self,self.vardata,True)
        self.lbldata = Label(self,bd=0,relief=SOLID,anchor=CENTER,width=25,textvariable=self.vardata,font=self.font_)
        self.lbldata.pack(side=LEFT,fill=X,expand=True)

        self.btndata = Button(self,bd=0,command=invokarDatedatapicker,relief=SOLID,image=self.imgdata)
        self.btndata.pack(side=RIGHT,expand=True,fill=X,padx=("2px","2px"),pady=("2px","2px"))
    def getdata(self):
        return self.vardata.get()