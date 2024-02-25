from tkinter import *

from m_constantesP_objetos import (IMG_MONEY_16X16,
                                 IMG_CHECKED_OFF_16X16_OUTLINE,
                                 IMG_CHECKED_ON_16X16_OUTLINE)

class SimbolsMathInvalidErro(Exception):
    def __str__(self):
        return "Simbols Math invalid Error - Simbols Permission: '+' or  '-' "
class ExpectedRootTk(Exception):
    def __str__(self) -> str:
        return "Instance Tk() not found - required kwarg root=instance[Tk]"
class ItemNotListError(Exception):
    def __str__(self) -> str:
        return "Item not found list Error"
class InspectValues(Exception):
    def __str__(self) -> str:
        return "valores requeridos e não presentes"   
class TypeCamposExpected(Exception):
    def __str__(self) -> str:
        return "Error! Type campos expected"
class ValueCamposInvalid(Exception):
    def __str__(self) -> str:
        return "Error! value campo invalid"
class ItemNameInvalid(Exception):
    def __str__(self) -> str:
        return "Name to Item Invalid! - Expectend(I0001,I0002,I0003...)"
class ItemDuplicateErro(Exception):
    def __str__(self) -> str:
        return "Error! Duplicate items are not allowed"
class KeyItemIndexError(Exception):
    def __init__(self,item, *args: object) -> None:
        self.item = item
    def __str__(self):
        return f"Item already exists - {self.item}"
class ContItem:
    def __init__(self) -> None:
        self.__items = []
    def validarItem(funtion):
        def validar(*args):
            self_ = args[0]
            nameitem = args[1]
            if not isinstance(nameitem,str):
                raise ItemNameInvalid()
            if len(nameitem) != 5:
                raise ItemNameInvalid()
            if nameitem[0].upper() != "I":
                raise ItemNameInvalid()
            if not all([d in "0123456789"] for d in nameitem[1:]):
                raise ItemNameInvalid()
            if nameitem in self_.__items:
                raise ItemDuplicateErro()
            funtion(*args)
        return validar
    @validarItem
    def itemExists(self,item:str):
        return item in self.__items
    def gerarItem(self):
        nitem = len(self.__items)+1
        return f"I{nitem:04d}"
    @validarItem
    def setitem(self,item:str):
        self.__items.append(item)
class Event_:
    def __init__(self,framechecked,obj_triggered_event,valuesrows) -> None:
        self.frmrow:FrameChecked = framechecked
        self.widget  = obj_triggered_event
        self.values = valuesrows
    def printkwargs(self):
        print("kwargs: frmrow - Class FrameChecked")
        print("kwargs: obj_triggered_event - Class object that triggered event")
        print("Values input")

class FrameChecked(Frame):
    def __init__(self,master,treerows,values:tuple,*args,**kwargs):
        super(FrameChecked,self).__init__(master,*args,**kwargs)
        self.state = 0
        self.treerows:TreeRows = treerows
        self.focus_ = False
        self.selection_args = dict(bg=self.treerows.__dict__["colorrows"])
        self.des_selection_args = dict(bg="SystemButtonFace")
        self.values = values   
    def validar(function):
        def modo_selection(*args):
            self_ = args[0]
            event_ = args[1]
            if self_.treerows.__dict__["mode_selection"] == "onerow":
                for row in self_.treerows.framerowsSelections:
                    row.des_selection_all(None)
                self_.treerows.framerowsSelections = []
                function(*args)
            elif self_.treerows.__dict__["mode_selection"] == "multrows":
                print("VALIDAÇÃO - DEU MULTROWS")
                function(*args)
            elif self_.treerows.__dict__["mode_selection"] == "checkbox":
                self_.selection_args = dict(bg="SystemButtonFace")
                function(*args)
            elif self_.treerows.__dict__["mode_selection"] == "onecheckbox":
                self_.selection_args = dict(bg="SystemButtonFace")
                for row in self_.treerows.framerowsSelections:
                    row.des_selection_all(None)
                self_.treerows.framerowsSelections = []
                function(*args)
        return modo_selection
    def selection_(self):
        self.state = 1
        self.focus_ = True
        self.configure(**self.selection_args)
    def des_selection(self):
        self.state = 0
        self.focus_ = False
        self.configure(**self.des_selection_args)
    def des_selection_all(self,event):
        self.des_selection()
        try:
            for w in self.winfo_children():
                w.des_selection()
            #self.treerows.framerows.remove(self)
        except:
            print("SEM ITEM PARA EXCLUIR")
    @validar
    def mudarEstado(self,state):
        if state:
            self.state = 1
            self.focus_ = True
            self.selection_()
            if self not in self.treerows.framerowsSelections:
                self.treerows.framerowsSelections.append(self)
        else:
            self.state = 0
            self.focus_ = False
            self.des_selection()
            if self in self.treerows.framerowsSelections:
                self.treerows.framerowsSelections.remove(self)
        return self.focus_         
    def forceMudarEstado(self,state):
        widgets = self.winfo_children()
        for w in widgets:
            w.mudarStateForce(state)
        self.mudarEstado(state)
class CheckeBox(Label):
    def __init__(self,master,*args,**kwargs):
        super(CheckeBox,self).__init__(master,*args,**kwargs)
        self.on = PhotoImage(data=IMG_CHECKED_ON_16X16_OUTLINE,master=master)
        self.off = PhotoImage(data=IMG_CHECKED_OFF_16X16_OUTLINE,master=master)
        self.configure(image=self.off)
        self.state = 0
        #self.bind("<Button-1>",lambda e: self.master.mudarEstado(e),add="+")
        self.bind("<Button-1>",lambda e: self.mudarState(e))
    def selection_(self):
        self.configure(image=self.on,**self.master.selection_args)
        self.state = 1
    def des_selection(self):
        self.configure(image=self.off,**self.master.des_selection_args)
        self.state = 0
    def mudarState(self,event):
        if self.master.winfo_name() == "columns":
            return
        widgets = self.master.winfo_children()
        if self.state == 0:
            self.state = 1
            self.master.mudarEstado(self.state)
            for w in widgets:
                if w != event.widget:
                    w.selection_()
            self.selection_()
        else:
            self.state = 0
            self.master.mudarEstado(self.state)
            for w in widgets:
                if w != event.widget:
                    w.des_selection()
            self.des_selection()
    def mudarStateForce(self,state):
        if state==1:
            self.selection_()
        else:
            self.des_selection()
class LabelRows(Label):
    def __init__(self,master,*args,executbind=True,**kwargs):
        super(LabelRows,self).__init__(master,*args,**kwargs)
        self.state = 0
        self.bind("<Button-1>",lambda e: self.mudarState(e)) if executbind else print("não faz nada")
    def selection_(self):
        self.state = 1
        self.configure(**self.master.selection_args)
    def des_selection(self):
        self.state = 0
        self.configure(**self.master.des_selection_args)
    def mudarState(self,event):
        if self.master.winfo_name == "columns":
            return
        widgets = self.master.winfo_children()
        if self.state == 0:
            self.state = 1
            print(f"linha 188 m_treewidgets: {self.master}")
            self.master.mudarEstado(self.state)
            for w in widgets:
                if w != event.widget:
                    w.selection_()
            self.selection_()
        else:
            self.state = 0
            #self.configure(**self.master.des_selection_args)
            self.master.mudarEstado(self.state)
            for w in widgets:
                if w != event.widget:
                    w.des_selection()
            self.des_selection()
    def mudarStateForce(self,state):
        if state==1:
            self.selection_()

        else:
            self.des_selection()
    def bindvalidate(self):
        ...
class FrameScrollVert(Frame):
    def __init__(self,master,width_,height_,root=None,**kwargs) -> None:
        super(FrameScrollVert,self).__init__(master,**kwargs)
        self.flagRolar = False
        self.cvs = Canvas(self,width=width_,height=height_,bd=0,relief=SOLID,highlightthickness=0)
        self.scrVert = Scrollbar(self,orient=VERTICAL,command=self.cvs.yview)
        self.conteiner = Frame(self.cvs,name="conteiner")

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

class TreeRows:
    def __init__(self, master, **kwargs):
        self.options_default = dict(mode_selection="multrows",bgcolor="SystemButtonFace",lineselection=False,optionscolumn=(CENTER,),color_row="#00BFFF",
                                    height_rows=2,height_bar=2,names_bar = (),
                                    height_=0,root=None,width_scroll=1,
                                    typecampos=(),widthcolumns=(15,),namefontrows="TkDefaultFont",
                                    sizefontrows=10,fgrows="#000000",colorrows="SystemButtonFace",
                                    bdrows=0,pdyrows=("0px","4px"),widthrows=(15,))

        self.__dict__ = {**self.options_default,**kwargs}
        self.fuctions = None
        self.chek = PhotoImage(data=IMG_MONEY_16X16,master=master)

        if self.__dict__["mode_selection"] not in ["onerow", "multrows", "checkbox", "onecheckbox"]:
            raise ValueCamposInvalid("Valores permitidos -> onerow - multrows - checkbox - onecheckbox")
        if not self.__dict__["typecampos"]:
            raise TypeCamposExpected()
        if self.__dict__["root"] == None:
            raise ExpectedRootTk()
        self.frmmestre = Frame(master,bd=0,relief=SOLID)
        self.frmbar = Frame(self.frmmestre,bd=1,relief=SOLID,name="columns")
        self.frmbar.pack(side=TOP,padx=("0px","1px"))
        self.framerows = []
        self.rowswidgets = []
        self.contitem = ContItem()
        self.framerowsSelections = []
        self.__criarinterface()
    def helpOptions(self):
        print("modeseletion = onerow,multrows - padrao[onerow]")
        print("optionscolumn = (namecolumn,dimensaowidth,imagebyte[b''],positionImage=LEFTorRIGHT) - padrao[()]")
        print("color_row = color em hexadecimal[str] - padrao[#00BFFF]")
    def insertrow(self,values:tuple,item="END"):
        if item == "END":
            newitem = self.contitem.gerarItem()
            item = newitem
        self.contitem.setitem(item)

        pady = self.__dict__["pdyrows"]
        bdrows = self.__dict__["bdrows"]

        namefontrows=self.__dict__["namefontrows"]
        sizefontrows=self.__dict__["sizefontrows"]
        fgrows=self.__dict__["fgrows"]
        colorrows=self.__dict__["colorrows"]

        font = (namefontrows,sizefontrows)
        if len(self.frmScroll.conteiner.winfo_children()) == 0 and pady == ("0px","4px"):
            pady = ("4px","4px")
        self.frmrow = FrameChecked(self.frmScroll.conteiner,self,values,bd=bdrows,relief=SOLID,name=item.lower())
        self.frmrow.pack(side=TOP,fill=X,pady=pady)
        typecampos      = self.__dict__["typecampos"]
        #widthcolumns    = self.__dict__["widthrows"]
        widthcolumns    = self.__dict__["widthcolumns"]
        h_bar           = self.__dict__["height_bar"]
        optionscolumn   = self.__dict__["optionscolumn"]
        for i,typecampo in enumerate(typecampos):
            try:
                v = values[i]
            except:
                v = "-"
            try:
                widthcolumn = widthcolumns[i]
            except:
                widthcolumn = widthcolumns[0]
           
            if isinstance(v,str) and typecampo=="#str":
                lbl = LabelRows(self.frmrow,font=font,fg=fgrows,text=v,width=widthcolumn,height=h_bar,relief=SOLID,bd=0,justify=optionscolumn[0])
                lbl.grid(row=0,column=i,sticky=NSEW)

                objEvent = Event_(self.frmrow,lbl,values)
                lbl.bind("<Button-1>",lambda e: self.__executarFuntion(objEvent),add="+")
                self.rowswidgets.append(lbl)
            elif isinstance(v,PhotoImage) and typecampo == "#img":
                lbl = LabelRows(self.frmrow,text="",image=v,width=widthcolumn,height=h_bar,relief=SOLID,bd=0,justify=optionscolumn[0])
                lbl.grid(row=0,column=i,sticky=NSEW)

                objEvent = Event_(self.frmrow,lbl,values)
                lbl.bind("<Button-1>",lambda e: self.__executarFuntion(objEvent),add="+")
                self.rowswidgets.append(lbl)
            elif isinstance(v,str) and typecampo == "#chk":
                #Label(self.frmrow,text="",image=self.chek,width=widthcolumn,height=h_bar,relief=SOLID,bd=0,justify=optionscolumn[0]).grid(row=0,column=i,sticky=NSEW)
                widthcolumn *= 8
                widthcolumn += 2
                checked = CheckeBox(self.frmrow,text="",width=widthcolumn,height=h_bar,relief=SOLID,bd=0,justify=optionscolumn[0])
                checked.grid(row=0,column=i,sticky=NSEW)

                objEvent = Event_(self.frmrow,checked,values)
                checked.bind("<Button-1>",lambda e: self.__executarFuntion(objEvent),add="+")
                self.rowswidgets.append(checked)
                checked.objEvent = objEvent
            else:
                raise ValueCamposInvalid()
        self.framerows.append(self.frmrow)
        return item
    def __criarinterface(self):
        def somarproporcional(widthcolumns):
            p = 7.133333333333333
            tot = 0
            for v in widthcolumns:
                tot+= v*p+v
            return tot
        if self.__dict__["names_bar"]:
            namescols       = self.__dict__["names_bar"]
            widthcolumn_     = self.__dict__["widthcolumns"]
            h_bar           = self.__dict__["height_bar"]
            optionscolumn   = self.__dict__["optionscolumn"]

            namefontrows=self.__dict__["namefontrows"]
            sizefontrows=self.__dict__["sizefontrows"]
            fgrows=self.__dict__["fgrows"]
            colorrows=self.__dict__["colorrows"]
            font = (namefontrows,sizefontrows)

            for i,v in enumerate(namescols):
                try:
                    widthcolumn = widthcolumn_[i]
                except:
                    widthcolumn = widthcolumn_[0]
                
                lbl = LabelRows(self.frmbar,executbind=False,font=font,fg=fgrows,text=v,width=widthcolumn,height=h_bar,relief=SOLID,bd=0,justify=optionscolumn[0])
                lbl.grid(row=0,column=i,sticky=NSEW)

        width_ = int(somarproporcional(self.__dict__["widthcolumns"]))
        
        self.__dict__["width_"] = width_ #sum(self.__dict__["widthcolumns"])

        print("criando header")
        self.frmheader = Frame(self.frmmestre,bg="yellow")
        self.frmheader.pack(side=TOP,fill=BOTH)

        print("criando scroll")
        self.frmScroll = FrameScrollVert(self.frmheader,
                                         width_=self.__dict__["width_"],
                                         height_=self.__dict__["height_"],bd=0,relief=SOLID,root=self.__dict__["root"])
        self.frmScroll.pack(side=TOP,fill=BOTH)

        
        self.frmScroll.scrVert.configure(width=self.__dict__["width_scroll"])
        self.frmScroll.conteiner.configure(bg=self.__dict__["bgcolor"])
    def __executarFuntion(self,event):
        if self.fuctions:
            self.fuctions(event)
    def bindcheck(self,func,args=()):
        self.fuctions = lambda event,x=args: func(event,x)
    def getitem(self,item:str):
        if item not in self.frmScroll.conteiner.children:
            raise ItemNotListError()
        frmrow = self.frmScroll.conteiner.nametowidget(name=item)
        return frmrow.values
    def removeItem(self,item:str):
        if item not in self.frmScroll.conteiner.children:
            raise ItemNotListError()
        
        framerow:Frame = self.frmScroll.conteiner.nametowidget(item.lower())

        # verifica se o item está na lista de selecionados para remover.
        if framerow in self.framerows:
            self.framerows.remove(framerow)

        if framerow in self.framerowsSelections:
            self.framerowsSelections.remove(framerow)
        framerow.destroy()
    def getitemselected(self):
        return [row.winfo_name() for row in self.framerowsSelections]
    def clean_all(self):
        for w in self.framerows:
            w.destroy()
        #bbox = self.frmScroll.cvs.bbox("all")
        self.frmScroll.cvs.yview_moveto(0.0)
        self.framerows.clear()
        self.framerowsSelections.clear()
    def selection_setall(self,state:int):
        for frm in self.frmScroll.conteiner.winfo_children():
            frm.forceMudarEstado(state)
            for w in frm.winfo_children():
                #print(f"VERIFICANDO TYPE: {type(w)}")
                if isinstance(w,CheckeBox):
                    self.__executarFuntion(w.objEvent)
    def pack(self,**kwargs):
        self.frmmestre.pack(**kwargs)
    def grid(self,**kwargs):
        self.frmmestre.grid(**kwargs)
    def place(self,**kwargs):
        self.frmmestre.place(**kwargs)
    def configure_(self,width:int):
        width_ = int(self.frmScroll.cvs["width"])
        width_ = width_ + width
        self.frmScroll.cvs.configure(width=width_)
    
if __name__ == "__main__":
    def removeitem(item):
        try:
            tree.removeItem(item)
        except:
            print("Item não existe")
    def getitemselections():
        listname = tree.getitemselected()
        print(listname)
    print("mode_selection - onerow - multrows - checkbox - onecheckbox")
    root = Tk()
    root.geometry("700x500")
    

    names =("ID","NAME","MARCAR","RECEBIDO","RESULTADO","OUTRO","TESTANDO OUTRO")
    typescolumns = ("#str","#str","#chk","#str","#str","#str","#str")
    widthcolumns = (15,20,13,15,16,20,25)
    ind = 7
    tree = TreeRows(root,mode_selection="onerow",lineselection=True,bdrows=0,
                    bgcolor="#00FFFF",colorrows="#87CEFA",names_bar=names[:ind],
                    height_bar=2,height_=300,root=root,
                    width_scroll=2,typecampos=typescolumns[:ind],
                    widthcolumns=widthcolumns[:ind])
    tree.pack(side=TOP)

    imgmoney = PhotoImage(data=IMG_MONEY_16X16)
    for w in range(50):
        row= (f"CO-00000{w}",f"CLIENTE {w:03d}","#chk",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}",f"RS {w*2}")
        tree.insertrow(row)

    #tree.configure_(-3)

    print(tree.frmScroll.cvs["width"])
    args = ("luan","de sousa silva")
    tree.bindcheck(print,args)
    
    ety = Entry(root)
    ety.pack()

    btn = Button(root,text="Excluir")
    btn.pack()

    btn1 = Button(root,text="Items selecionados")
    btn1.pack()
        
    btn.bind("<Button-1>",lambda e: removeitem(ety.get()))
    btn1.bind("<Button-1>",lambda e: getitemselections())

    root.mainloop()