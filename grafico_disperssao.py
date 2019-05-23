import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random

df = pd.read_csv('data/spyZap.csv')

hora = None
online = 0
offline = 0
_online = []
_tempo = []

for y in df.values:
    if hora is None:
        hora = y[3]

    if hora == y[3]:
        online += 1 if y[1] == 1 else 0
        offline += 1 if y[1] == 0 else 0
    else:
        _online.append([online, hora])
        online = 0
        offline = 0
    hora = y[3]

if online > 0:
    _online.append([online,hora])

_grapth_online = []
_grapth_tempo = []
_all = []

for i in _online:
    _grapth_online.append(i[0])
    _grapth_tempo.append(str(i[1])+':00h')
    _all.append(i[1])




plt.plot(_grapth_tempo,_grapth_online)
plt.title('Tempo de uso do Whatsapp')
#plt.scatter(_grapth_tempo,_grapth_online)
plt.gcf().autofmt_xdate()
plt.show()