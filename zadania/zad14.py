#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zaimplementuj funkcję decimal_to_dms() umożliwiającą konwersję stopni 
dziesiętnych na wartość DMS. W funkcji uwzględnij argument logiczny 
is_lat, który pozwoli określić czy współrzędna wejściowa reprezentuje 
szerokość czy długość geograficzną i zwróci wynik z odpowiednim kierunkiem geograficznym.
"""


def decimal_to_dms(stopnie_dziesietne, is_lat):

    if is_lat:
        kierunek = "N" if stopnie_dziesietne >= 0 else "S"
    else:
        kierunek = "E" if stopnie_dziesietne >= 0 else "W"

    wartosc_bezwzgledna = abs(stopnie_dziesietne)
    stopnie = int(wartosc_bezwzgledna)
    minuty = int((wartosc_bezwzgledna - stopnie) * 60)
    sekundy = round(((wartosc_bezwzgledna - stopnie) * 60 - minuty) * 60, 2)

    return f"{stopnie}° {minuty}' {sekundy}'' {kierunek}"


# Przykład wywołania funkcji
decimal_to_dms(17.275930318082096, True)

