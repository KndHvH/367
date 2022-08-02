
lista= [
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

lol='(?i)'

for i in lista:
    lol += f"({i})|"

lol = lol[:-1]

print(lol)