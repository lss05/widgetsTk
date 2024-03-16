from tkinter import *
from string import ascii_letters,digits

class Formato_Invalido(Exception):
    def __str__(self):
        self.msg = "Formato Inválido," \
              "Ex: (2dig) 5dig-4dig onde dig representa digitos e o número a quantidade de digitos."
        return self.msg
class Masked_all(Entry):
    def __init__(self,master,simbol="",local_simbol="left",formato="(2dig) 5dig-4dig",**kwargs):
        super(Masked_all,self).__init__(master,**kwargs)
        self.configure(bd=1,relief=SOLID)
        self.simbol = simbol
        self.bind("<KeyRelease>",self.formated)
        self.localsimbol = local_simbol
        self.blocos = []
        self.formato = self.__validar_formato(formato)
        self.nwformatAux = self.gerarMaskedAux(self.formato)
    def redefinirFormato(self,newformato):
        self.formato = ""
        self.blocos = []
        self.formato = self.__validar_formato(newformato)
        self.nwformatAux = self.gerarMaskedAux(self.formato)
        self.delete(0,"end")
        self.focus()
    def gerarMaskedAux(self,formato):                
        masked = formato
        for bloco in self.blocos:
            if bloco[1] == f"{bloco[2]}dig":
                aux = bloco[2]*"#"
            elif bloco[1] == f"{bloco[2]}alf":
                aux = bloco[2]*"*"
            else:
                aux = bloco[2]*"&"
            masked = masked.replace(bloco[1],aux)
        return masked
    def __validar_formato(self,formato):
        numbers = ""
        for ind,ch in enumerate(formato):
            aux = f"{numbers}{formato[ind:ind+3]}"
            if ch in "1234567890":
                numbers += ch
            elif aux in [f"{numbers}dig",f"{numbers}alf",f"{numbers}all"]:
                try:
                    valor = int(numbers)
                    self.blocos.append([ind-1,aux,valor])
                    numbers = ""
                except:
                    raise Formato_Invalido
        return formato
    def __aplicarMasked(self,txt,nwformataux):
        formato = nwformataux
        txtaux =""
        for ch in formato:
            if ch in ["#","*","&"]:
                if ch == "#":
                    achou = False
                    for i,ct in enumerate(txt):
                        if ct in "0123456789":
                            txtaux += ct
                            txt = txt.replace(ct,"",1)
                            achou = True
                            break
                    if not achou:
                        break
                elif ch == "*":
                    achou = False
                    for i,ct in enumerate(txt):
                        if ct in ascii_letters:
                            txtaux += ct
                            txt = txt.replace(ct,"",1)
                            achou = True
                            break
                    if not achou:
                        break
                elif ch == "&":
                    achou = False
                    for i,ct in enumerate(txt):
                        if ct in ascii_letters+digits+" -":
                            txtaux += ct
                            txt = txt.replace(ct,"",1)
                            achou = True
                            break
                    if not achou:
                        break
            else:
                txtaux += ch                
        return txtaux
    def formated(self,event):
        txt = event.widget.get()
      
        if event.keysym in ["Tab","BackSpace",]:
            return
       
        newtxt = self.__aplicarMasked(txt,self.nwformatAux)
        
        self.delete(0,"end")
        if self.localsimbol == "left":
            novatxt = f"{self.simbol}{newtxt}"
        else:
            novatxt = f"{newtxt}{self.simbol}"
        self.insert(0,novatxt)
    def setvalue(self,valor):
        self.insert(0,valor)
        evento = Event()
        evento.widget = self
        evento.keysym = "0"
        self.formated(evento)
    def clearvalues(self):
        state = self["state"]
        if state != NORMAL:
            self.configure(state=NORMAL)
            self.delete(0,END)
            self.configure(state=state)
            return
        self.delete(0,END)
    def getvalue(self,simbol=False):
        if not simbol:
            return self.get().replace(self.simbol,"")
        return self.get()
if __name__ == "__main__":
    root = Tk()

    lbltel = Label(root,text="Tel/Whatsaap Ex: 55+ (99) 99999-9999")
    lbltel.pack()
    tel = Masked_all(root,formato="2dig+ (2dig) 5dig-4dig",width=45,simbol="Cel ")
    tel.setvalue("5599991309642")
    tel.pack()

    """
    lbltel = Label(root,text="Data Ex: 00/00/0000")
    lbltel.pack()
    data = Masked_all(root,formato="2dig/2dig/4dig")
    data.pack()

    lbltel = Label(root,text="Cep Ex: 00.000-000")
    lbltel.pack()
    cep = Masked_all(root,formato="2dig.3dig-3dig")
    cep.pack()

    lbltel = Label(root,text="Cpf Ex: 000.000.000-00")
    lbltel.pack()
    cpf = Masked_all(root,formato="3dig.3dig.3dig-2dig")
    cpf.pack()

    lbltel = Label(root,text="Cnpj Ex: 00.000.000/0000-00")
    lbltel.pack()
    cnpj = Masked_all(root,formato="2dig.3dig.3dig/4dig-2dig")
    cnpj.pack()

    lbltel = Label(root,text="Time Ex: 00:00:00")
    lbltel.pack()
    cnpj = Masked_all(root,formato="2dig:2dig:2dig")
    cnpj.pack()

    lbltel = Label(root,text="6 digitos Ex: 100000")
    lbltel.pack()
    numbers = Masked_all(root,formato="6dig")
    numbers.pack()

    lbltel = Label(root,text="padrão qualquer Ex: Base: 2dig Ano: 4dig Serial: 6dig")
    lbltel.pack()
    numbers = Masked_all(root,formato="Base: 2dig Ano: 4dig Serial: 6dig",width=45)
    numbers.pack()
    """
    root.mainloop()
