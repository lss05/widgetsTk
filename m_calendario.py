from tkinter import *
from m_basetoplevel import BaseToplevel
from m_scrollvertical import FrameScrollVert
from m_constantesP_objetos import IMG_CLOSE_32X32,IMG_MINIMIZAR_32X32
from datetime import date
from calendar import Calendar,month
from time import strftime
#from datetime import timedelta

class FrmCalendar(BaseToplevel):
    def __init__(self,root,varstring,force_data_output:bool,*args,**kwargs):
        super(FrmCalendar,self).__init__(root,*args,**kwargs)
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
