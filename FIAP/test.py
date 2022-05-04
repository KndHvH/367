import re

#checando se a String começa com “A” e termina com “Professora”:

aVerdade = 'A'
match = re.search("^A", aVerdade)
print(match)

if match:
  print("Sim! Nos temos um match!")
else:
  print("Não temos um match")
