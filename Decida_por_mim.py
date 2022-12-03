import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.resposta = ['Sim', 'Não', 'Não me interessa', 'Não importa', 'Talvez você não deva fazer isso',
                         'Vire à direita', 'Vire à esquerda', 'Passe protetor solar', 'O messi é calvo',
                         'Que pergunta idiota!', 'Você é um otário', 'Você não tem amigos', 'Faz sentido',
                         'Talvez você devesse pular da ponte', 'Nem fudendo', 'Fodase!!', 'Isso não é verdade',
                         'Se isso acontecer eu sou uma geladeira eletroux', 'Seu nome é josisvaldo',
                         'Sim, mas não agora', 'Que tipo de pergunta é essa?', 'Stars wars morreu', 'Indonésia',
                         'Brasil é o país com mais brasileros no mundo', 'Que porra é essa???', 'Fudeu!',
                         'Tu não tem o que fazer não?', 'A solução é vender drogas', '1 + 1 é 2', '1988', '2058',
                         '2022', 'Sim e não', 'Raíz quadrada'
                         ]
        self.theme = sg.theme('DarkAmber')
        self.layout = [[sg.Text('Qual sua dúvida?', size=(40, 2))],
                       [sg.InputText('', key='Pergunta')],
                       [sg.Button('Resposta',), sg.Button('Outra pergunta')],
                       [sg.Text('', key='msg')]
                       ]

    def Iniciar(self):
        self.janela = sg.Window('Decida por mim', layout=self.layout)
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Resposta':
                self.janela['msg'].update(random.choice(self.resposta))
            elif evento == 'Outra pergunta':
                self.janela['Pergunta'].update('')
                self.janela['msg'].update('')

Jogador = DecidaPorMim()
Jogador.Iniciar()