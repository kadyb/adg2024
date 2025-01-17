

def decimal_to_dms(x, kierunek):
    
    if kierunek == "dlugosc":
        znak = "E" if x >= 0 else "W"
    elif kierunek == "szerokosc":
        znak = "N" if x >= 0 else "S"
    else:
        raise ValueError("Nieprawidłowy kierunek. Użyj 'dlugosc' lub 'szerokosc'.")
    
   
    abs_x = abs(x)
    stopnie = int(abs_x)
    minuty = int((abs_x - stopnie) * 60)
    sekundy = round(((abs_x - stopnie) * 60 - minuty) * 60, 2)
    
    return f"{stopnie}° {minuty}' {sekundy}'' {znak}"

    

decimal_to_dms(-16.94161, "szerokosc")