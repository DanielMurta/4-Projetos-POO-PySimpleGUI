import random
import PySimpleGUI as sg


class JogoAdvinhacao:
    def __init__(self):
        self.layout = [[sg.Text('Acerte o número escolhido entre 0 e 100!')],
                       [sg.Text('Resposta:')],
                       [sg.InputText(key='resposta')],
                       [sg.Button('Chutar')],
                       [sg.Text('', key='msg2')],
                       [sg.Text('', key='msg')]]

    def Iniciar(self):
        self.janela = sg.Window('Jogo Advinhação', layout=self.layout)
        self.GerarValor()
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            resposta = int(valores['resposta'])
            if evento == 'Chutar':
                if resposta == self.valor:
                    self.janela['msg'].update('Parabéns, você acertou!')
                elif resposta > self.valor:
                    self.ValorMaisBaixo()
                    self.janela['resposta'].update('')
                elif resposta < self.valor:
                    self.ValorMaisAlto()
                    self.janela['resposta'].update('')


    def ValorMaisAlto(self):
        return self.janela['msg2'].update('Chute um valor mais Alto!')

    def ValorMaisBaixo(self):
        return self.janela['msg2'].update('Chute um valor mais Baixo!')


    def GerarValor(self):
        self.valor = random.randint(0, 100)
        return self.valor


Jogador = JogoAdvinhacao()
Jogador.Iniciar()
