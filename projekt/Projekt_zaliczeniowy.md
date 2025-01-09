Napisz funkcję, która umożliwi wczytanie danych wektorowych (geometria i atrybuty) z pliku
tekstowego (.csv) i zapis do formatu przestrzennego (np. *geopackage*). Do wczytania danych
wykorzystaj moduł [csv](https://docs.python.org/3/library/csv.html). Rozważ następujące aspekty:

1. **Geometria:**
    - Plik może zawierać dane punktowe o współrzędnych X, Y i opcjonalnie Z.
    - Plik może zawierać geometrię w formacie WKT (*Well-Known Text*).
3. **Układ współrzędnych** -– wskazanie układu współrzędnych jako kod EPSG.
3. **Separator kolumn** –- znak wykorzystany do oddzielenia kolumn (np. spacja, średnik, przecinek).
4. **Separator dziesiętny** -– znak wykorzystany do zapisu części dziesiętnej (kropka lub przecinek).
5. **Nazwy kolumn w pierwszym wierszu** -– określenie czy w pierwszym wierszu znajdują się nazwy
   kolumn. Jeśli nie, to należy nadać domyślne, np. "X1", "X2", …, "Xn".
7. **Zapis do pliku wektorowego:**
    - Wybór docelowego formatu zapisu pliku przestrzennego.
    - Określenia czy wejściowe kolumny z geometrią (tj. "X", "Y" lub "WKT") mają zostać zapisane
      jako osobne atrybuty czy usunięte.

Funkcja przykładowo może mieć następującą postać:

```
csv_converter(
  filepath,
  col.sep = ",",
  dec.sep = ".", 
  header = [TRUE|FALSE],
  x.col = ["X", NULL],
  y.col = ["Y", NULL],
  z.col = ["Z", NULL],
  wkt.col = ["WKT", "geom", NULL],
  crs = ["EPSG:2180"],
  output.format = ["GPKG"],
  keep.geom.columns = [TRUE|FALSE]
)
```
