#Zaimplementuj funkcję decimal_to_dms() umożliwiającą konwersję stopni dziesiętnych na wartość DMS.
#Pamiętaj, aby zwrócona wartość posiadała odpowiedni kierunek geograficzny. Szerokość, czy długość.
import os

path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8")
os.chdir(path)


def decimal_to_dms(decimal, is_lat):
    if is_lat == True:
        if decimal >= 0:
            kierunek = 'N'
        elif decimal < 0:
            kierunek = 'S'
    else:
        if decimal >= 0:
            kierunek = 'E'
        elif decimal < 0:
            kierunek = 'W'
    stopnie = int(decimal)
    minuty = int((decimal-stopnie)*60)
    sekundy = int(((decimal-stopnie)*60-minuty)*60)
    stopnie = str(stopnie)
    minuty = str(minuty)
    sekundy = str(sekundy)
    dms = stopnie+"°"+minuty+"'"+sekundy+"°"+' '+kierunek
    return dms

print("DMS wynosi:", decimal_to_dms(52.2928, True))
print("DMS wynosi:", decimal_to_dms(16.7356, False))
