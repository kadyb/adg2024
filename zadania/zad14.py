def DecimalToDMS(coord, is_lat = True):
    if coord == 0:
        result = str(coord) + '°'
        return result
    if coord > 0:
        if is_lat is True:
            w_dir = 'N'
        else:
            w_dir = 'E'
    if coord < 0:
        if is_lat is True:
            w_dir = 'S'
        else:
            w_dir = 'W'
    minutes = (coord - int(coord)) * 60
    seconds = round(((minutes-int(minutes))*60),5)
    result = str(abs(int(coord))) + "°"\ 
            + str(abs(int(minutes))) + "'"\ 
            + str(abs(seconds)) + "\""\ 
            + w_dir
    return result 

dms = DecimalToDMS(52.2928)
dms2 = DecimalToDMS(-17.63582,False)
dms0 = DecimalToDMS(0)

