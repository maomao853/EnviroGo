import logging

class Location:
    def __init__(self, lat, long, datetime):
        self.lat = lat
        self.long = long
        self.date, self.time = self._splitDateTime(datetime)

    def __repr__(self):
        return("lat:{}\nlong:{}\n{}\n{}".format(self.lat, self.long, self.date, self.time))

    def _splitDateTime(self, datetime):
        dateRaw, timeRaw = datetime.split(" ")

        dateFormat = "year:month:day"
        timeFormat = "hour:minute:second"

        dateFinal = self._stripFormat(dateFormat.split(":"), dateRaw.split(":"))
        timeFinal = self._stripFormat(timeFormat.split(":"), timeRaw.split(":"))

        return(dateFinal, timeFinal)

    def _stripFormat(self, keys, values):
        d = {}

        for index, key in enumerate(keys):
            key = key.strip()
            d[key] = int(values[index].strip())

        return(d)
