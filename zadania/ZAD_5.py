import os
os.chdir("C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy/zaj_06_12")

raster_name = 'dem.tif'
raster = QgsRasterLayer(raster_name)

#liczba kolumn
num_col = raster.width()
#liczba wierszy
num_row = raster.height()
#zakres
zakres = raster.extent()


def wielkosc_komorki(zakres, num_col, num_row):
    szer = zakres.width()/num_col
    wys = zakres.height()/num_row
    return(szer, wys)
    
wielkosc_komorki(zakres, num_col, num_row)

