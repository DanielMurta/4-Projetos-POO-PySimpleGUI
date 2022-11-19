import random
import PySimpleGUI as psg


class SimuladorDados():
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.layout = [[psg.Text('Jogar o Dado?')], [psg.Button('sim'), psg.Button('não')]]

    def Iniciar(self):
        self.janela = psg.Window('Simulador de Dado', layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Programa Encerrado!')
            else:
                print('Digite "sim" ou "não"')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDados()
simulador.Iniciar()
