# Zaimplementuj funkcję decimal_to_dms() umożliwiającą konwersję stopni dziesiętnych na wartość DMS. Pamiętaj, aby zwrócona wartość posiadała odpowiedni kierunek geograficzny.


def decimal_to_dms(decimal, is_latitude=True): 
    # Kierunki geograficzne
    if is_latitude:
        direction = "N" if decimal >= 0 else "S"
    else:
        direction = "E" if decimal >= 0 else "W"
   
    # Konwersja na wartości absolutne
    decimal = abs(decimal)
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60) * 3600, 2)
   
    return f"{degrees}°{minutes}'{seconds}\" {direction}"

# Testowanie funkcji
latitude_dd = 52.2296
longitude_dd = 21.0122

print(decimal_to_dms(latitude_dd))  
print(decimal_to_dms(longitude_dd, is_latitude=False))  





