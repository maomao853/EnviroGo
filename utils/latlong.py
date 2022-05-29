from math import radians, cos, sin, asin, sqrt

def getDistance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    r = 6371

    return(c * r)

def toDegree(lat, long):
    # Needs to be fixed
    latSecList = str(lat[2]).split("/")
    latSec = latSecList[0]/latSecList[1]
    latFinal = lat[0] + (lat[1] / 60) + (latSec/3600)

    longSecList = str(long[2]).split("/")
    longSec = longSecList[0]/longSecList[1]
    longFinal = long[0] + (long[1] / 60) + (longSec/3600)

    return({
        lat: int(latFinal),
        long: int(longFinal)
    })
