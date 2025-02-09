

def decimal_to_dms(degrees, is_lat=True):
    """
    Konwertuje stopnie dziesiętne na wartość DMS (stopnie, minuty, sekundy).
    
    :param degrees: Wartość w stopniach dziesiętnych
    :param is_lat: True, jeśli to szerokość geograficzna, False jeśli długość geograficzna
    :return: String z wartością DMS i odpowiednim oznaczeniem kierunku (N, S, E, W)
    """
    # Określenie kierunku geograficznego
    if is_lat:
        direction = 'N' if degrees >= 0 else 'S'
    else:
        direction = 'E' if degrees >= 0 else 'W'

    # Przekształcenie na wartość bezwzględną
    abs_degrees = abs(degrees)
    
    # Rozbicie na stopnie, minuty i sekundy
    d = int(abs_degrees)
    m = int((abs_degrees - d) * 60)
    s = round(((abs_degrees - d) * 60 - m) * 60, 2)

    # Korekta jeśli sekundy wynoszą 60
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        d += 1

    return f"{d}° {m}' {s}'' {direction}"

# Przykłady użycia
print(decimal_to_dms(52.2296, is_lat=True))   # 52° 13' 46.56'' N
print(decimal_to_dms(21.0122, is_lat=False))  # 21° 0' 43.92'' E
print(decimal_to_dms(-16.94161, is_lat=True)) # 16° 56' 29.8'' S
print(decimal_to_dms(-46.6358, is_lat=False)) # 46° 38' 8.88'' W

