## 5. Napisz funkcję, która obliczy wielkość komórki na podstawie zakresu przestrzennego oraz liczby kolumn i wierszy rastra.

def wielkosc_komorki(raster_layer):
    extent = raster_layer.extent()
    liczba_kolumn = raster_layer.width()
    liczba_wierszy = raster_layer.height()
    szerokosc_komorki = extent.width() / liczba_kolumn
    wysokosc_komorki = extent.height() / liczba_wierszy
    return szerokosc_komorki, wysokosc_komorki