Zad_2

def przeliczanie(wartosc, jednostka):
    if jednostka == 'kg':
        return wartosc * 2.204
    elif jednostka == 'funt':
        return wartosc * 0.453
    
print(przeliczanie(100,'funt'))
print(przeliczanie(100,'kg'))
