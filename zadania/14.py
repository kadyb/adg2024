
def decimal_to_dms(decimal):
    """
    decimal = float
    """
    
    degrees = decimal - (decimal % 1)
    minutes = (decimal - degrees) - ((decimal - degrees) % 1/60)
    seconds = (decimal - degrees - minutes) - ((decimal - degrees - minutes) % 1/3600)
    degrees *= 1
    minutes *= 60
    seconds *= 3600
    
    degrees = int(degrees)
    minutes = int(minutes - (minutes % 1))
    seconds = round(seconds, 1)
    
    dms = str(degrees) + "°" + str(minutes) +  "'" + str(seconds) + '"'
    
    return dms

def direction(decimal, is_lat):
    if is_lat:
        if decimal < 0:
            direction = "S"
        else:
            direction = "N"
    else:
        if decimal < 0:
            direction = "W"
        else:
            direction = "E"
    return direction

def decimals_to_dms(decimal, is_lat = True):
    '''
    decimal = tuple(float, float)
    is_lat = bool - specifies whether the first number is latitude
    '''
    
    direction1 = direction(decimal[0], is_lat)
    direction2 = direction(decimal[1], is_lat != True)
    
    dms1 = decimal_to_dms(abs(decimal[0])) + direction1
    dms2 = decimal_to_dms(abs(decimal[1])) + direction2
    
    dms = dms1 + " " + dms2
    
    return dms


coord = (52.45723413650722, -16.92653416299568)
dms  = decimals_to_dms(coord, True)
print(dms)




