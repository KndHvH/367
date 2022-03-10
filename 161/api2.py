import requests
link = 'http://127.0.0.1:5000/tabela'

reqs=requests.get(link)

print(reqs)
print(reqs.json())
dici = reqs.json()

print(dici['total_vendas'])
