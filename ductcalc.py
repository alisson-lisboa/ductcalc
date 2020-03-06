from math import pi, sqrt, log10
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from datetime import date


pasta = os.path.dirname(os.path.realpath(__file__))
data = date.today()

# Insert here the system's id
sistema = 'UE-01'

# Insert here the information about the supply duct branches
trechos_i = [
{'id': '1', 'comprimento [m]': 5.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': 'fan', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '2', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '1', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '3', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '2', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '4', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '3', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '5', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '3', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '6', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '5', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '7', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '5', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '8', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '2', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '9', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '1', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '10', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '9', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '11', 'comprimento [m]': 12.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '9', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30}]

# Insert here the information about the extraction duct branches
trechos_e = [
{'id': '1', 'comprimento [m]': 5.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': 'fan', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '2', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '1', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '3', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '2', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '4', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '3', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '5', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '3', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0, 'difusor [Pa]': 0},
{'id': '6', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '5', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '7', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '5', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '8', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '2', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '9', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '1', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 0.0, 'difusor [Pa]': 0},
{'id': '10', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '9', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30},
{'id': '11', 'comprimento [m]': 4.0, 'curvas': 0.0, 'angulo total [°]': 0.0, 'deriva de': '9', 'vazao [m³/h]': 0, 'diametro [mm]': 0, 'velocidade [m/s]': 0.0, 'difusor [m³/h]': 720, 'difusor [Pa]': 30}]

def calcula_trechos(trechos, funcao):
    
    #distribui as vazões

    for i in range(len(trechos) -1, -1, -1):
        if trechos[i]['difusor [m³/h]'] != 0:
            trechos[i]['vazao [m³/h]'] = trechos[i]['difusor [m³/h]']
        vazao = trechos[i]['vazao [m³/h]']
        deriva_de = trechos[i]['deriva de']
        for f in trechos:
            if f['id'] == deriva_de:
                f['vazao [m³/h]'] += vazao 

    vent_vazao = trechos[0]['vazao [m³/h]']

    if funcao == 'i':
        metodo = 'Static Regain'
    elif funcao == 'e':
        metodo = 'Equal Friccion'


    # Calcula diametro, velocidade e perda de carga do trecho - BEYER

    # for i in range(len(trechos)):
    #     if i == 0:
    #         trechos[i]['diametro [mm]'] = int(32 * (trechos[i]['vazao [m³/h]'] * 1000 / 3600) ** 0.38)
    #         trechos[i]['velocidade [m/s]'] = (trechos[i]['vazao [m³/h]'] / 3600) / ((pi * (trechos[i]['diametro [mm]']/1000) ** 2) / 4)
    #         trechos[i]['velocidade [m/s]'] = float(f"{trechos[i]['velocidade [m/s]'] : .2f}")
                        
    #         dia = trechos[i]['diametro [mm]'] / 1000
    #         Re = (1.2 * trechos[i]['velocidade [m/s]'] * dia) / 0.00001723 # viscosidade absoluta a 0°C
    #         v = trechos[i]['velocidade [m/s]']
    #         L = trechos[i]['comprimento [m]']
    #         f = 0.008
    #         while f <= 0.1:
    #                 xx = (0.00004054 / dia) + (0.00003242 / (v * dia * sqrt(f))) # rugosidade = 0,15mm e viscosidade absoluta a ?°C
    #                 if (1 / sqrt(f)) < -2 * log10(xx):
    #                     break
    #                 f += 0.0001
            
    #         trechos[i]['perda carga [Pa]'] = float(f'{f * (L /dia) * 1.2 * (v ** 2) / 2 : .2f}')

    #     else:
    #         for f in trechos:
    #             if trechos[i]['deriva de'] == f['id']:
    #                 v1 = f['velocidade [m/s]'] 
    #         v2 = v1
    #         va = trechos[i]['vazao [m³/h]'] / 3600
    #         L = trechos[i]['comprimento [m]']
    #         at = trechos[i]['angulo total [°]']

    #         f = 0.008
    #         while v2 >= 0:
    #             dia = sqrt((4 * va)/(pi * v2))
    #             while f <= 0.1:
    #                 xx = (0.00004054 / dia) + (0.00003242 / (v2 * dia * sqrt(f)))  # rugosidade = 0,15mm e viscosidade absoluta a ?°C
    #                 if (1 / sqrt(f)) < -2 * log10(xx):
    #                     break
    #                 f += 0.0001
    #             if 0.75 * (v1 ** 2 - v2 ** 2) > ((f * L * v2 ** 2) / dia + 0.1 * (at / 90) * v2 ** 2):
    #                 break
    #             v2 -= 0.001
            
    #         trechos[i]['diametro [mm]'] = int(dia * 1000)
    #         trechos[i]['velocidade [m/s]'] = float(f'{v2 : .2f}')
    #         trechos[i]['perda carga [Pa]'] = float(f'{f * (L /dia) * 1.2 * (v2 ** 2) / 2 : .2f}')


    #    Calcula diametro, velocidade e perda de carga do trecho - ALISSON

    if funcao == 'i': # Se for insuflamento ou ar exterior usa recuperação de pressão estática

        for i in range(len(trechos)):
            if i == 0: # Calculo por fricção constante
                trechos[i]['diametro [mm]'] = int(32 * (trechos[i]['vazao [m³/h]'] * 1000 / 3600) ** 0.38)
                trechos[i]['velocidade [m/s]'] = (trechos[i]['vazao [m³/h]'] / 3600) / ((pi * (trechos[i]['diametro [mm]']/1000) ** 2) / 4)
                trechos[i]['velocidade [m/s]'] = float(f"{trechos[i]['velocidade [m/s]'] : .2f}")
                            
                dia = trechos[i]['diametro [mm]'] / 1000
                Re = (1.2 * trechos[i]['velocidade [m/s]'] * dia) / 0.00001772 # viscosidade absoluta a 10°C
                v = trechos[i]['velocidade [m/s]']
                L = trechos[i]['comprimento [m]']
                f = 0.008
                while f <= 0.1:
                        if (1 / sqrt(f)) < -2 * log10((0.00015 / 3.7 * dia) + (2.51 / Re * sqrt(f))): # rugosidade = 0,15mm
                            break
                        f += 0.0001
                
                trechos[i]['perda carga [Pa]'] = float(f'{f * (L /dia) * 1.2 * (v ** 2) / 2 : .2f}')

            else: # Calculo por Recuperação de Pressão Estática
                for g in trechos:
                    if trechos[i]['deriva de'] == g['id']:
                        v1 = g['velocidade [m/s]'] 
                v2 = v1
                va = trechos[i]['vazao [m³/h]'] / 3600
                L = trechos[i]['comprimento [m]']
                at = trechos[i]['angulo total [°]']

                f = 0.008
                while v2 >= 0:
                    dia = sqrt((4 * va)/(pi * v2))
                    Re = (1.2 * v2 * dia) / 0.00001772 # viscosidade absoluta a 10°C
                    while f <= 0.1:
                        if (1 / sqrt(f)) < -2 * log10((0.00015 / 3.7 * dia) + (2.51 / Re * sqrt(f))): # rugosidade = 0,15mm
                            break
                        f += 0.0001
                    if 0.75 * (v1 ** 2 - v2 ** 2) > ((f * L * v2 ** 2) / dia + 0.1 * (at / 90) * v2 ** 2):
                        break
                    v2 -= 0.001
                
                trechos[i]['diametro [mm]'] = int(dia * 1000)
                trechos[i]['velocidade [m/s]'] = float(f'{v2 : .2f}')
                trechos[i]['perda carga [Pa]'] = float(f'{f * (L /dia) * 1.2 * (v2 ** 2) / 2 : .2f}')
    
    elif funcao == 'e': # Se for para exaustão ou retorno utiliza fricção constante

        for i in range(len(trechos)):
            trechos[i]['diametro [mm]'] = int(32 * (trechos[i]['vazao [m³/h]'] * 1000 / 3600) ** 0.38)
            trechos[i]['velocidade [m/s]'] = (trechos[i]['vazao [m³/h]'] / 3600) / ((pi * (trechos[i]['diametro [mm]']/1000) ** 2) / 4)
            trechos[i]['velocidade [m/s]'] = float(f"{trechos[i]['velocidade [m/s]'] : .2f}")
                        
            dia = trechos[i]['diametro [mm]'] / 1000
            Re = (1.2 * trechos[i]['velocidade [m/s]'] * dia) / 0.00001772 # viscosidade absoluta a 10°C
            v = trechos[i]['velocidade [m/s]']
            L = trechos[i]['comprimento [m]']
            f = 0.008
            while f <= 0.1:
                    if (1 / sqrt(f)) < -2 * log10((0.00015 / 3.7 * dia) + (2.51 / Re * sqrt(f))): # rugosidade = 0,15mm
                        break
                    f += 0.0001
            
            trechos[i]['perda carga [Pa]'] = float(f'{f * (L /dia) * 1.2 * (v ** 2) / 2 : .2f}')

    # Estipula Caminhos

    derivacoes = []

    for i in range(len(trechos)):
        derivacoes.append([[trechos[i]['id']]])
        aux = []
        for j in trechos:
            if j['deriva de'] == trechos[i]['id']:
                aux.append(j['id'])
        derivacoes[i].append(aux)
    
    saidas = []
    
    for i in derivacoes:
        if len(i[1]) == 0:
            saidas.append(i[0][0])

    caminhos = []

    for i in saidas:
        aux1 = [i]
        aux2 = i
        perda = 0
        for f in range(len(trechos) -1, -1, -1):
            if aux2 == trechos[f]['id']:
                aux1.append(trechos[f]['deriva de'])
                aux2 = trechos[f]['deriva de']
                perda += trechos[f]['perda carga [Pa]'] + trechos[f]['difusor [Pa]']
                perda = float(f'{perda : .2f}')
                if f == 0:
                    aux1.append(perda)

        caminhos.append(aux1)

    perda_critica = 0
    for i in caminhos:
        if i[-1] > perda_critica:
            caminho_critico = i
            perda_critica = i[-1]


    return trechos, saidas, caminhos, caminho_critico, perda_critica, vent_vazao, metodo

def balanceamento(trechos, caminhos, caminho_critico):

    alvo = caminho_critico[-1]

    for i in caminhos:
        if i[-1] < alvo:
            for t in trechos:
                if t['id'] == i[0]:
                    dia = t['diametro [mm]'] / 1000
                    while alvo - i[-1] > 0.1:
                        dia -= 0.001
                        t['velocidade [m/s]'] = (t['vazao [m³/h]'] / 3600) / ((pi * dia ** 2) / 4)
                        t['velocidade [m/s]'] = float(f"{t['velocidade [m/s]'] : .2f}")
                        Re = (1.2 * t['velocidade [m/s]'] * dia) / 0.00001772 # viscosidade absoluta a 10°C
                        
                        f = 0.008
                        while f <= 0.1:
                            if (1 / sqrt(f)) < -2 * log10((0.00015 / 3.7 * dia) + (2.51 / Re * sqrt(f))): # rugosidade = 0,15mm
                                break
                            f += 0.0001
                        
                        perda_posterior = float(f"{f * (t['comprimento [m]'] / dia) * 1.2 * (t['velocidade [m/s]'] ** 2) / 2 : .2f}")
                        perda_anterior = t['perda carga [Pa]']
                        adicional = perda_posterior - perda_anterior
                        t['perda carga [Pa]'] = perda_posterior
                        t['diametro [mm]'] = int(dia * 1000)

                        i[-1] = float(f'{i[-1] + adicional : .2f}')

    return trechos, caminhos


def retangular(trechos):
    
    limite = input('Possui limite de altura [s] [n]? ')
    if limite == 's':
        limite = int(input('limite [mm]: ')) - 50 # menos 50mm (isolamento de 25mm em cima e embaixo)
        for i in trechos:
            a = 100
            b = 100
            dia1 = i['diametro [mm]']
            dia2 = 0
            while dia1 - dia2 >= 0:    
                if limite - a >= 10:
                    a += 10
                b += 10
                dia2 = int((1.30 * (a * b) ** 0.625) / ((a + b) ** 0.25))
            i['altura [mm]'] = a
            i['largura [mm]'] = b

             
    else:
        for i in trechos:
            a = 100
            b = 100
            dia1 = i['diametro [mm]']
            dia2 = 0
            while dia1 - dia2 >= 0:    
                a += 10
                b += 10
                dia2 = int((1.30 * (a * b) ** 0.625) / ((a + b) ** 0.25))
            i['altura [mm]'] = a
            i['largura [mm]'] = b



# Executa funções e calcula ventilador

ventilador_i = 0
ventilador_e = 0
perda_critica_i = 0
perda_critica_e = 0

trechos_i, saidas_i, caminhos_i, caminho_critico_i, perda_critica_i, ventilador_i, metodo_i = calcula_trechos(trechos_i, 'i')
trechos_i, caminhos_i = balanceamento(trechos_i, caminhos_i, caminho_critico_i)
retangular(trechos_i)

trechos_e, saidas_e, caminhos_e, caminho_critico_e, perda_critica_e, ventilador_e, metodo_e = calcula_trechos(trechos_e, 'e')
trechos_e, caminhos_e = balanceamento(trechos_e, caminhos_e, caminho_critico_e)
retangular(trechos_e)

ventilador = {'vazão [m³/h]': ventilador_i, 'perda carga [Pa]': float(f'{perda_critica_i + perda_critica_e : .2f}')}


# Começa o relatório

c = canvas.Canvas(f"{pasta}\\{sistema}_report.pdf", A4)

c.setFont('Times-Roman', 11)

def mm2p(milimetros):
    return milimetros / 0.352777


# Imprime Titulo
c.setFont('Times-Roman', 16)
c.drawString(mm2p(80), mm2p(270), f'Duct Calculation Memory')
c.line(mm2p(20), mm2p(260), mm2p(190), mm2p(260))
c.setFont('Times-Roman', 11)
c.drawString(mm2p(20), mm2p(250), f'System name: {sistema}')
c.drawString(mm2p(20), mm2p(245), f'Date Prepared: {data}')

posY = mm2p(235)


def escrevetrechos(trechos, funcao, caminho_critico, perda_critica, posY):

    # Começa Cabeçalho
    if funcao == 'i':
        c.drawString(mm2p(20), posY, f'Supply Method: Static Regain')
    elif funcao == 'e':
        c.drawString(mm2p(20), posY, f'Extraction Method: Equal Friction')
    posY -= mm2p(1.5)
    c.line(mm2p(20), posY, mm2p(190), posY)

    # Cabeçalho - Linha Superior
    posY -= mm2p(3.5)
    c.drawString(mm2p(20.5), posY, f'Section')
    c.drawString(mm2p(41.5), posY, f'From')
    c.drawString(mm2p(57), posY, f'Height / Dia.')
    c.drawString(mm2p(82), posY, f'Width')
    c.drawString(mm2p(100), posY, f'Volume')
    c.drawString(mm2p(120), posY, f'Velocity')
    c.drawString(mm2p(145), posY, f'Static Pressure Loss [Pa]')

    posY -= mm2p(1.5)
    c.line(mm2p(140), posY, mm2p(190), posY)

    # Cabeçalho - Linha Inferior
    posY -= mm2p(3.5)
    c.drawString(mm2p(20), posY, f'Number')
    c.drawString(mm2p(40), posY, f'Section')
    c.drawString(mm2p(62), posY, f'[mm]')
    c.drawString(mm2p(82.5), posY, f'[mm]')
    c.drawString(mm2p(101.5), posY, f'[m³/h]')
    c.drawString(mm2p(122), posY, f'[m/s]')
    c.drawString(mm2p(140), posY, f'Duct')
    c.drawString(mm2p(157), posY, f'Diffuser')
    c.drawString(mm2p(178), posY, f'Section')
    posY -= mm2p(1.5)
    c.line(mm2p(20), posY, mm2p(190), posY)

    # Escreve trechos
    for i in trechos:
        posY -= mm2p(3.5)
        c.drawString(mm2p(20), posY, i['id'])
        c.drawString(mm2p(40), posY, i['deriva de'])
        c.drawString(mm2p(62), posY, str(i['altura [mm]']))
        c.drawString(mm2p(82.5), posY, str(i['largura [mm]']))
        c.drawString(mm2p(101.5), posY, str(i['vazao [m³/h]']))
        c.drawString(mm2p(122), posY, str(i['velocidade [m/s]']))
        c.drawString(mm2p(140), posY, str(i['perda carga [Pa]']))
        c.drawString(mm2p(157), posY, str(i['difusor [Pa]']))
        c.drawString(mm2p(178), posY, str(i['perda carga [Pa]'] + i['difusor [Pa]']))

    posY -= mm2p(1.5)
    c.line(mm2p(20), posY, mm2p(190), posY)

    # Escreve caminho Critico e pressão critica

    posY -= mm2p(3.5)
    c.drawString(mm2p(20), posY, f'Critical path: ')
    
    posX = mm2p(41.5)
    for i in caminho_critico[:-1]:
        c.drawString(posX, posY, i)
        posX += mm2p(3 + (len(i) - 1) * 1.7)
        # if len(i) == 1:
        #     posX += mm2p(3)
        # elif len(i) == 2:
        #     posX += mm2p(4.5)
        # elif len(i) == 3:
        #     posX += mm2p(6)

        if i != caminho_critico[-2]:
            c.drawString(posX, posY, '-')
            posX += mm2p(2)

    posY -= mm2p(5)
    c.drawString(mm2p(20), posY, f'Critical pressure loss [Pa]: {caminho_critico[-1]}')
    
    posY -= mm2p(8.5)
    
    return posY


if len(trechos_i) > 0:
    posY = escrevetrechos(trechos_i, 'i', caminho_critico_i, perda_critica_i, posY)
if len(trechos_e) > 0:
    posY = escrevetrechos(trechos_e, 'e', caminho_critico_e, perda_critica_e, posY)

# Escreve resultados do ventilador

c.drawString(mm2p(20), posY, f'Fan Results')

posY -= mm2p(1.5)
c.line(mm2p(20), posY, mm2p(190), posY)
posY -= mm2p(3.5)


if ventilador_i != 0:
    vazao = ventilador_i
elif ventilador_e != 0:
    vazao = ventilador_e

c.drawString(mm2p(20), posY, f'Flow Rate [m³/h]: {vazao}')
posY -= mm2p(5)
c.drawString(mm2p(20), posY, f'Available Static Pressure [Pa]: {caminho_critico_e[-1] + caminho_critico_i[-1] : .2f}')


# c.showPage() #fecha a folha e passa para a proxima.
c.save()
