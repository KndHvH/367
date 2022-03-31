import pickle

my_dict = { 'Apple': 4, 'Banana': 2, 'Orange': 6, 'Grapes': 11}

with open("myDictionary.txt", "w") as tf:
    pickle.dump(my_dict,tf)

with open('bd.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)