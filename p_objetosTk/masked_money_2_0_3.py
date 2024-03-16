from tkinter import *

class MoneyMasked(Entry):
    def __init__(self,master,simbols="",length=100,**kwargs):
        super(MoneyMasked,self).__init__(master,**kwargs)
        self.configure(bd=1,relief=SOLID)
        self["width"] = 20
        self["fg"]= "green"
        self.simbols = simbols
        self.length=length
        self.insert(0,f"{self.simbols}0,00")
        self.bind("<KeyRelease>",self.captureKey)
        self.bind("<KeyPress>",self.verificavalor)
    def getvaluePython(self):
        return self.get().replace(self.simbols,"").replace(".","").replace(",",".")
    def getvalueForSimbols(self):
        return self.get().replace(".","").replace(",",".")
    def getvalue(self):
        return self.get()
    def verificavalor(self,event):
        text = event.widget.get()
        if not text:
            self.simbols = self.simbols.replace("-","")
    def setvalue(self,text):
        event_ = Event()
        event_.widget = self
        for ch in text[:self.length]:
            if ch == "-" and ch not in self.simbols:
                self.simbols += ch
                continue
            self.insert("end",ch)
            event_.keysym = ch
            self.captureKey(event_)
    def mascarar(self,text):
        text = text[:self.length]
        if len(text) <=2:
            q = 3 - len(text)
            text = text.zfill(3)
        if len(text) >= 4 and text[0] == "0":
            text = text[1:]
            
        fra = text[-2:]
        res = text[:-2]
        newtext = ""
        for i,char in enumerate(res[::-1],1):
            newtext+=char
            if i%3==0:
                if not i == len(res):
                    newtext+="."
        
        return f"{newtext[::-1]},{fra}"
    def captureKey(self,event):
        ety = event.widget
        text_ety = ety.get()
                
        if event.keysym in ["BackSpace","backspace"]:
            newtext = ""
            for char in text_ety:
                if char in "0123456789-":
                    if char == "-" and char not in self.simbols:
                        self.simbols += char
                    else:
                        if char == "-":
                            if text_ety == f"{self.simbols}0,0":
                                self.simbols = self.simbols.replace("-","")
                            continue
                        newtext += char
            text_ety = f"{self.simbols}{self.mascarar(newtext)}"
        if event.keysym in "0123456789-":
            newtext = ""
            for char in text_ety:
                if char in "0123456789-":
                    if char == "-" and char not in self.simbols:
                        self.simbols += char
                    else:
                        if char == "-":
                            if text_ety == f"{self.simbols}0,00":
                                self.simbols = self.simbols.replace("-","")
                            continue
                        newtext += char
            text_ety = f"{self.simbols}{self.mascarar(newtext)}"
        else:
            text_ety = text_ety.replace(event.keysym,"")

        ety.delete(0, "end")
        ety.insert(0,text_ety)
    def clearvalues(self):
        if self["state"] != "normal":
            state = self["state"]
            self.configure(state=NORMAL)
            self.delete(0,END)
            self.setvalue("000")
            self.configure(state=state)
            return
        self.delete(0,END)
        self.setvalue("000")

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x300+200+50")
    ety = MoneyMasked(root,simbols="R$ ",length=10)
    ety.setvalue("-100000")
    ety.pack()
    print(ety.getvaluePython())
    print(ety.getvalue())
    root.mainloop()
