#Zadanie_3: Napisz funkcję, która sprawdzi czy dany rok jest przestępny.
def przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    return False

rok = 2021
if przestepny(rok):
    print("Jest")
else: 
    print("Nie jest")