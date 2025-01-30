def DecimalToDMS(coords, is_lat = True):
    if coords == 0:
        result = str(coords) + '°'
        return result
    if coords > 0:
        if is_lat is True:
            w_dir = 'N'
        else:
            w_dir = 'E'
    if coords < 0:
        if is_lat is True:
            w_dir = 'S'
        else:
            w_dir = 'W'
    minutes = round(coords - int(coords),len(str(coords))) * 60
    seconds = round(minutes - int(minutes),len(str(minutes))) * 60
    result = str(abs(int(coords))) + "°" + str(abs(int(minutes))) + "'" + str(abs(seconds)) + "\"" + w_dir
    return result 

dms = DecimalToDMS(52.2928)
dms2 = DecimalToDMS(-17.63582,False)
dms0 = DecimalToDMS(0)

