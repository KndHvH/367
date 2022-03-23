import re

lista = [
         'gg',
         'ff',
         'tp',
         'elo',
         'tft',
         'urf',
         'adc',
         'duo',
         'ult',
         'solo',
         'skin',
         'nerd',
         'main',
         'aram',
         'item',
         'flex',
         'mono',
         'gank',
         'gold',
         'ff15',
         'troll',
         'prata',
         'smurf',
         'flash',
         'build',
         'ignite',
         'ranked',
         'elojob',
         'lowelo',
         'jungle',
         'intando',
         'sucumba',
         'nerdola',
         'esquisito',
         'mid',
         'top',
         'minions',
         'cs',
         'farm',
         'gold',
         'xp',
         'yasuo',
         'riven',
         'shaco',
         'zed',
         'lee',
         'gank',
         'sup',
         'bot',
         ]


texto = input()
if (texto in lista):
    print("Item proibido")

else:
    print("Item permitido")