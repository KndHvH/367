
master = list('ghz_4mWDZQbamb4w4uyifYRJOdlrONgtkq3vshL4')

senha = input()
upper = senha.upper()
senha = senha + upper

senha = list(senha)

for i, v in enumerate(master):
    for j, b in enumerate(senha):
        if v == b:
            if j < 5 or (j > 9 and j < 15):
                master[i] = senha[j+5]
            else:
                master[i] = senha[j-5]



string = ""
for i in master:
    string += i
print(string)
