import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

for i in _online:
    _grapth_online.append(i[0])
    _grapth_tempo.append(str(i[1])+':00h')


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = list(_grapth_online)
ingredients = [x.split()[-1] for x in _grapth_tempo]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} reQ)".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Tempo Médio",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Tempo de uso do Whatsapp")

plt.show()




