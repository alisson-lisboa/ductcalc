from funcoes import *

equipamento = ''
trechos = []
trechos_i = []
trechos_r = []
saidas = []
caminhos = []
caminho_critico = []
perda_critica = 0
ventilador = {}
metodo = ''

while True:

    escolha = input('''\
        [e] nome equipamento
        [i] incluir trecho
        [d] deletar trecho
        [v] incluir vazão
        [c] calcular
        [r] relatorio
        [s] sair

        >>>''')

    if escolha == 'e':
        equipamento = input('Qual o nome do equipamento?:')
    
    elif escolha == 'i':
        
        trechos.append(cria_trecho())

    elif escolha == 'd':
        pass
    elif escolha == 'v':

        incluir_vazao(trechos)
    
    elif escolha == 'c':
        trechos, saidas, caminhos, caminho_critico, perda_critica, ventilador['vazao [m³/h]'], metodo =  calcula_trechos(trechos)
        trechos, caminhos = balanceamento(trechos, caminhos, caminho_critico)
        retangular(trechos)

    elif escolha == 'r':
        pass
    elif escolha == 's':
        break

