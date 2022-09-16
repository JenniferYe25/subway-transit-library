import csv

class Connection: 

    def __init__(self,station1,station2,line,time) -> None:
        self.station1 = station1
        self.station2 = station2
        self.line = line
        self.time = time

    def get_station1(self):
        return self.station1

    def get_station2(self):
        return self.station2

    def get_line(self):
        return self.line
    
    def get_time(self):
        return self.time
    
class Line:
    def __init__(self,line,name,colour,stripe) -> None:
        self.line= line
        self.name = name
        self.colour = colour
        self.stripe = stripe

    def get_line(self):
        return self.line

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour
    
    def get_stripe(self):
        return self.stripe

class graphExtractor:

    def __init__(self, connections,lines,stations):
    #     self.connectionsFile = connections
    #     self.linesFile = lines
    #     self.stationsFile = stations
        self.connectionsFile='london.connections.csv'
        self.linesFile='london.lines.csv'
        self.stationsFile='london.stations.csv'

    # read all the files
    def extractRows(path):
        with open(path) as csvFile:
            csvreader = csv.DictReader(csvFile)
            next(csvreader)

            rows = []
            for row in csvreader:
                    rows.append(row)
            csvFile.close()
        return rows


    def ConnectionBuilding(path):
        rows=extractRows(path)
        connections=[]
        for row in rows:
            connections.append(Connection(row["station1"],row["station2"],row["line"],row["time"]))
        return connections

    def LinesBuilding(self,path):
        rows=extractRows(path)
        lines=[]
        for row in rows:
            lines.append(Line(row["line"],row["name"],row["colour"],row["stripe"]))
        return lines

    def StationsBuilding(self,path):
        rows=extractRows(path)
        stations=[]
        for row in rows:
            stations.append(Station(row["id"],connection{},row["latitude"],row["longitude"],row["name"],row["display_name"],row["zone"],row["total_lines"],row["rail"]))
        return stations


extractor = graphExtractor()
hello = graphExtractor.LinesBuilding(path='_dataset\london.lines.csv')
for i in hello:
    print(i.name)

