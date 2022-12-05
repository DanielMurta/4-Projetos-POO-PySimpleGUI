# Importando módulo p/ gerar o número aleatório
import random
# Importando módulo p/ criar a interface gráfica
import PySimpleGUI as psg

# Criando classe
class SimuladorDados():
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Difinindo o layout da interface gráfica
        self.layout = [[psg.Text('Jogar o Dado?')], [psg.Button('sim'), psg.Button('não')]]

    # Função para inciar o programa
    def Iniciar(self):
        # Criando a janela da interface
        janela = psg.Window('Simulador de Dado', layout=self.layout)
        # Lendo a janela
        eventos, valores = janela.Read()
        try:
            if eventos == 'sim' or eventos == 's':
                self.GerarValorDado()
            elif eventos == 'não' or eventos == 'n':
                print('Programa Encerrado!')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    # Gerando o valor aleatório
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


# Instância da classe SimuladorDados
simulador = SimuladorDados()
# Chama a função Iniciar
simulador.Iniciar()
