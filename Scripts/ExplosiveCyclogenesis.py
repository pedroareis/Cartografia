#Esse script é baseado no metodo de x para identificação de ciclogenese explosiva
#e para a classificação quanto sua intensidade

import numpy as N

lat = 1
while lat !=0:
    lat = float(input('Latitude 24h prévia ao ponto de máximo aprofundamento: '))
    lat2 = float(input('Latitude do ponto de máximo aprofundamento: '))
    slp1 = float(input('SLP 24h previa ao ponto de máximo aprofundamento: '))
    slp2 = float(input('SLP no ponto de máximo aprofundamento: '))
    media = (lat + lat2) / 2
    sin60 = N.sin(N.deg2rad(60))
    sinx = N.sin(N.deg2rad(media))
    p1 = sin60 / sinx
    p2 = (slp1 - slp2) / 24
    TNAc = p1 * p2
    if TNAc < 1.:
        print('Com {:.2} B, o ciclone não é explosivo.\n   '.format(TNAc))
    elif TNAc >= 1. and TNAc < 1.3:
        print('Com uma queda de {:.1f} hPa em 24 horas, e {:.2f} B,\n o ciclone é explosivo FRACO.\n   '.format(slp1-slp2, TNAc))
    elif TNAc >= 1.3 and TNAc < 1.8:
        print('Com uma queda de {:.1f} hPa em 24 horas, e {:.2f} B,\n o ciclone é explosivo MODERADO.\n   '.format(slp1-slp2, TNAc))
    elif TNAc > 1.8:
        print('Com uma queda de {:.1f} hPa em 24 horas, e {:.2f} B,\n o ciclone é explosivo FORTE.\n   '.format(slp1-slp2, TNAc))
