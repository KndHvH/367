import re

texto = "A Professora é legal!"

x = re.search("e", texto)

print(x)
print(x.span())
print(x.string)
print(x.group())




