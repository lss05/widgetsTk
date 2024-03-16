class F_Auxiliares():
    def __init__(self, janela=None):
        self.janelaPai = janela
        self.__WidthMonitor = None
        self.__HeightMonitor = None
        self.coordX = 0
        self.coordY = 0
    def disposicao_janela(self,dimensao,janela=None):
        if janela != None:
            self.janelaPai = janela
        width = 0
        height = 0

        self.dimensao = dimensao
        print(dimensao)
        self.__WidthMonitor = self.janelaPai.winfo_screenwidth()
        self.__HeightMonitor = self.janelaPai.winfo_screenheight()
        width = self.__WidthMonitor//2 - int(self.dimensao[0])//2
        height = self.__HeightMonitor//2 - int(self.dimensao[1])//2

        self.janelaPai.geometry('{}x{}+{}+{}'.format(self.dimensao[0],self.dimensao[1],width,height))