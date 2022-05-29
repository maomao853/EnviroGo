from math import radians, cos, sin, asin, sqrt

def getDistance(lat1, lat2, long1, long2):
    long1 = radians(long1)
    long2 = radians(long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlong = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2

    c = 2 * asin(sqrt(a))

    r = 6371

    return(c * r)

def toDegree(latRaw, longRaw):
    d = {}

    lat = _strip(latRaw)
    latFinal = lat["deg"] + (lat["min"] / 60) + (lat["sec"]/3600)

    long = _strip(longRaw)
    longFinal = long["deg"] + (long["min"] / 60) + (long["sec"]/3600)

    d["lat"] = float(latFinal)
    d["long"] = float(longFinal)

    return(d)

def _strip(input):
    d = {}

    keys = ["deg", "min", "sec"]
    stripped = str(input).strip("[]")
    raw = stripped.split(",")

    for index, key in enumerate(keys):
        if(index == 2):
            x, y = raw[index].split("/")
            d[key] = float(x) / float(y)
        else:
            d[key] = float(raw[index].strip())

    return(d)
