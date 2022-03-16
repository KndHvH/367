import re


def ident(field):
     match = re.search('(?i)(gank)|(elo)|(troll)|(sucumba)|(esquisito)|(nerd)|(nerdola)| (intando)| (gg)| (smurf)| (jungle)| (adc)| (elojob)| (ff)| (ff15)| (ult)| (q)| (w)| (e)| (r)| (flash)| (tp)| (ignite)| (prata)| (gold)| (lowelo)| (urf)| (aram)| (tft)| (ranked)| (duo)| (solo)| (flex)| (skin)', field.lower())

     if match:
         print("PROIBIDO")
     else:
         print("PERMITIDO")

ident(input())