# -*- coding: utf-8 -*-

# 3. Napisz funkcję, która sprawdzi czy dany rok jest przestępny. 
# Rok jest przestępny, gdy jest podzielny przez 4 i nie jest podzielny przez 100 lub jest podzielny przez 400. 
# Przykładowo lata 2000 i 2004 były przestępne, natomiast lata 1990, 2010 czy 2021 nie były.


def czy_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        print(f"rok {rok} jest przestępny")
    else: 
        print(f"rok {rok} nie jest przestępny")
        
czy_przestepny(2021)
