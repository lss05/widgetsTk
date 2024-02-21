from tkinter import *

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