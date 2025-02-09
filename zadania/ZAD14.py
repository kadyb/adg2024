def decimal_to_dms(lat, long):
    decimal_lat = abs(lat)
    degrees_lat = int(decimal_lat)
    minutes_lat = int((decimal_lat - degrees_lat) * 60)
    secondes_lat = round((decimal_lat - degrees_lat - minutes_lat/60)*3600)
    decimal_long = abs(long)
    degrees_long = int(decimal_long)
    minutes_long = int((decimal_long - degrees_long) * 60)
    secondes_long = round((decimal_long - degrees_long - minutes_long/60)*3600)
    if lat<0:
        dms_lat = f"{degrees_lat}°{minutes_lat}'{secondes_lat}/S"
    else:
        dms_lat = f"{degrees_lat}°{minutes_lat}'{secondes_lat}/N"
    if long<0:
        dms_long = f"{degrees_long}°{minutes_long}'{secondes_long}/W"
    else:
        dms_long = f"{degrees_long}°{minutes_long}'{secondes_long}/E"
    return(dms_lat, dms_long)
    
decimal_to_dms(52.2928,16.7356)