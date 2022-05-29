import exifread as ef
import os

try:
    import latlong as ll
    from location import Location
except:
    import utils.latlong as ll
    from utils.location import Location

global lat, long, datetime

def processImage(filePath):
    with open(filePath, "rb") as image:
        tags = ef.process_file(image)
        geo = {i:tags[i] for i in tags.keys() if i.startswith("GPS") or i.startswith("EXIF")}

        lat = geo["GPS GPSLatitude"]
        long = geo["GPS GPSLongitude"]

        datetime = geo["EXIF DateTimeDigitized"]

    loc = Location(lat, long, str(datetime))
    coordDict = ll.toDegree(loc.lat, loc.long)

    if(str(geo["GPS GPSLatitudeRef"]) != 'N'):
        coordDict["lat"] = -coordDict["lat"]

    if(str(geo["GPS GPSLongitudeRef"]) != 'E'):
        coordDict["long"] = -coordDict["long"]

    # Not good code
    coordDict["time"] = loc.time

    return(coordDict)
