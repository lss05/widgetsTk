#from uuid import uuid4
from pprint import pprint


class TypeNotAllowedError(Exception):
    def __str__(self):
        return "Tipo não permitido - Apenas Booleano"

class Observer:
    def __init__(self):
        self.iid = id(self)
        self.iniciando = True
        self.status = False
        if "conteiner" not in globals():
            globals()["conteiner"] = [self]
        else:
            globals()["conteiner"].append(self)
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,newstatus):
        if isinstance(newstatus,bool):
            self.__status = newstatus
            if self.iniciando:
                self.iniciando = False
            else:
                for obj in globals()["conteiner"]:
                    if obj.iid != self.iid:
                        obj.setstatus(not newstatus)
        else:
            raise TypeNotAllowedError
    def setstatus(self,newvalue):
        self.__status = newvalue
        # aqui pode ser executado metodos com base em quem ficou Verdadeiro e Falso
        # o objeto que mudou status chamou o metodo dos outros obj para que invertece status
        # sendo assim pode ser acionado metodos dos mesmo com base na mudança do status do obj que os invocou
        # print("\n")
        # print("Executando metodo 1")
        # print("Executando metodo 2")
        # print("Executando metodo 3")    
        
if __name__ == "__main__":
    p1 = Observer()
    p2 = Observer()
    p3 = Observer()

    #rowObjects = p1,p2,p3,
    #printarstatus = lambda objcts: [print(obj.status,end="") for obj in objcts]
    
    p1.status = True
    print(p1.status,p2.status,p3.status)
    p2.status = True
    print(p1.status,p2.status,p3.status)
    p3.status = True
    print(p1.status,p2.status,p3.status)

    #pprint(globals())

