import exifread as ef
import os
import utils.latlong as ll
from location import Location

FILE_NAME = "testImage.jpg"

global lat, long, datetime

def main():
    with open(os.path.join("resources", FILE_NAME), "rb") as image:
        tags = ef.process_file(image)
        geo = {i:tags[i] for i in tags.keys() if i.startswith("GPS") or i.startswith("EXIF")}

        lat = geo["GPS GPSLatitude"]
        long = geo["GPS GPSLongitude"]
        datetime = geo["EXIF DateTimeDigitized"]

    loc = Location(lat, long, str(datetime))
    print(loc)
    print(ll.toDegree(loc.lat, loc.long))

if __name__ == '__main__':
    main()
