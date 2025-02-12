# zad 14 Zaimplementuj funkcję decimal_to_dms() umożliwiającą konwersję stopni dziesiętnych na wartość DMS. W funkcji uwzględnij argument logiczny is_lat, który pozwoli określić czy współrzędna wejściowa reprezentuje szerokość czy długość geograficzną i zwróci wynik z odpowiednim kierunkiem geograficznym.

def decimal_to_dms(decimal, is_lat):
    stopnie10 = abs(decimal)
    stopnie = int(stopnie10)
    minuty = int((stopnie10 - stopnie) * 60)
    sekundy = int(((stopnie10 - stopnie) * 60 - minuty) * 60)
    if is_lat:
        if decimal > 0:
            kier = "N"
        else:
            kier = "S"
    else:
        if decimal > 0:
            kier = "E"
        else:
            kier = "W"
    return str(stopnie) + "°" + str(minuty) + "'" + str(sekundy) + '" ' + str(kier)
    
decimal_to_dms(52.2928, True)
decimal_to_dms(16.7356, False)
