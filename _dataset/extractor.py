# def dataExtractor(linePath, connectionsPath, stationsPath):
#     stationCatalog=set()
#     connections=set()
#     lines=LinesBuilding(linePath)

#     rows=extractRows(connectionsPath)
#         connections=set()
#         for row in rows:
#             stationCatalog.add(row["station1"])
#             connections.append(Connection(row["station1"],row["station2"],row["line"],row["time"]))
    
#     extractRows(linePath)
#     extractRows(connectionsPath)
#     extractRows(stationsPath)
import csv

class Line:
    def __init__(self,name,colour,stripe) -> None:
        self.name = name
        self.colour = colour
        self.stripe = stripe

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour
    
    def get_stripe(self):
        return self.stripe

class Station: 

    def __init__(self,latitude,longtitude,name,display_name,zone,total_lines,rail) -> None:
        self.longtitude = longtitude
        self.name = name
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail=rail

    def get_longitude(self):
        return self.longtitude

    def get_name(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name

    def get_zone(self):
        return self.zone
    
    def get_total_lines(self):
        return self.total_lines
        

def extractRows(path):
    with open(path) as csvFile:
        csvreader = csv.DictReader(csvFile)
        # next(csvreader)

        rows = []
        for row in csvreader:
            rows.append(row)
        csvFile.close()
    return rows

def StationsBuilding(path):
    rows=extractRows(path)
    stations=dict()
    for row in rows:
        if(row["id"] not in stations):
            stations.update({int(row["id"]):Station(row["latitude"],row["longitude"],row["name"],row["display_name"],row["zone"],row["total_lines"],row["rail"])})
    return stations

# def ConnectionBuilding(path):
#         rows=extractRows(path)
#         connections=set()
#         for row in rows:
#             if(row["station1"] not in )
#             connections.append(Connection(row["station1"],row["station2"],row["line"],row["time"]))
#         return connections

def LinesBuilding(path):
    rows=extractRows(path)
    lines=dict()
    for row in rows:
        if(row["line"] not in lines):
            lines.update({int(row["line"]):Line(row["name"],row["colour"],row["stripe"])})
    return lines


lines=(StationsBuilding('_dataset/london.stations.csv'))
print(len(lines))