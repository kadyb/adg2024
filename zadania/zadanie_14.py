def decimal_to_dms(coords, is_lat):
    if is_lat:
        if coords > 0:
            hs = "N"
        elif coords < 0:
            hs = "S"
        else:
            hs = ""
    else:
        if coords > 0:
            hs = "E"
        elif coords < 0:
            hs = "W"
        else: 
            hs = ""
    
    coords = abs(coords)
    deg = int(coords)
    min = int((coords - deg) * 60)
    sec = round((((coords - deg) * 60 - min) * 60), 4)
    
    dms = print("{}°{}'{}\"{}".format(deg, min, sec, hs))
    return dms