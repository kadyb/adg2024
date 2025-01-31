def decimal_to_dms(decimal, is_lat=True):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = int(decimal - degrees - minutes / 60) * 3600
    
    if is_lat:
        direction = 'N' if decimal >=0 else 'S'
    else:
        direction = 'E' if decimal >=0 else 'W'
    return degrees, minutes, round(seconds, 1), direction
    
latitude = 131.052235
longitude = -118.243683

dms_lat = decimal_to_dms(latitude, is_lat=True)
print(f"Szerokość geograficzna: {dms_lat[0]}° {dms_lat[1]}' {dms_lat[2]}'' {dms_lat[3]}")


dms_lon = decimal_to_dms(longitude, is_lat=False)
print(f"Długość geograficzna: {dms_lon[0]}° {dms_lon[1]}' {dms_lon[2]}'' {dms_lon[3]}")