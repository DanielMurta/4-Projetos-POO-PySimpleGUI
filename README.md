4 Projetos utilizando Programação Orientada a Objetos (POO) + Interface gráfica PySimpleGUI

Projeto 1 - Simulador de Dados: 

O primeiro passo são as importações dos módulos. O módulo random gera um número aleatório, já o módulo PySimpleGUI cria a 
interface gráfica. O próximo passo é a criação da classe "SimuladorDados". A classe possui uma função inicializadora que
define o valor max e mín, simulando um dado real e define o layout da interface gráfica. Logo abaixo a função "Iniciar", 
que tem como atribuição criar a interface gráfica baseada no layout já definido, chamar a funcão "GerarValorDado" e 
desenvolver a lógica por trás da interface.

A lógica é muito simples. Assim que a função "Iniciar" for executada, aparecerá uma tela com 3 elemtentos: Uma pergunta
"Quer jogar o dado?" e dois botões com as respostas "sim" e "não". Ao pressionar o botão "sim", o programa vai gerar um
número aleatório entre 1 e 6 como se fosse um dado real. Se o botão pressionado for "não", o programa será encerrado. Caso
o usuário clique no botão "X" no canto direito acima da tela, o programa será fechado.


Projeto 2 - Jogo Advinhação:

O primeiro passo são as importações dos módulos. O módulo random gera um número aleatório, já o módulo PySimpleGUI cria a 
interface gráfica. O próximo passo é a criação da classe "JogoAdvinhacao". A classe possui uma função inicializadora que
define define o layout da interface gráfica. A função "Iniciar" cria a interface gráfica, chama a função "GerarValor" e 
entra em um while True (loop Infinito).

Dentro do while True é armazenado toda a lógica por trás da interface gráfica. Quando a função "Iniciar" é incializada,
a interface é criada com algumas informações na tela: Um texto "Acerte o número escolhido entre 0 e 100!", outro texto
"Resposta:", abaixo um input para o usuário digitar o valor e por fim um botão "chutar". Caso o valor chutado seja
igual ao valor gerado aleatoriamente será printado "Parabéns, você acertou!". Caso o valor chutado seja
menor ao valor gerado aleatoriamente, a função "ValorMaisAlto" será chamada e será printado "Chute um valor mais Alto!".
Caso o valor chutado seja maior ao valor gerado aleatoriamente, a função "ValorMaisBaixo" será chamada e será printado 
"Chute um valor mais Baixo!". A cada erro, o input será limpado e o jogador terá a chance de tentar acertar novamente. 
Caso o usuário clique no botão "X" no canto direito acima da tela, o programa será fechado.

Projeto 3 - Decida por Mim:

