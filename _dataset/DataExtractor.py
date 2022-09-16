import csv
from Connection import Connection
from Line import Line
from Station import Station 

class DataExtractor:

    def __init__(self) -> None:
        pass

    def extractRows(self,path):
        with open(path) as csvFile:
            csvreader = csv.DictReader(csvFile)

            rows = []
            for row in csvreader:
                rows.append(row)
            csvFile.close()
        return rows

    def StationsBuilding(self,path):
        rows=self.extractRows(path)
        stations=dict()
        for row in rows:
            if(row["id"] not in stations):
                stations.update({int(row["id"]):Station(row["latitude"],row["longitude"],row["name"],row["display_name"],row["zone"],row["total_lines"],row["rail"])})
        return stations

    def ConnectionBuilding(self,path):
            rows=self.extractRows(path)
            connections=dict()
            for row in rows:
                station1=int(row["station1"])
                otherData=Connection(row["station2"],row["line"],row["time"])
                if(station1 not in connections):
                    connections.update({station1:[otherData]})
                else:
                    connections[station1].append(otherData)
            return connections

    def LinesBuilding(self,path):
        rows=self.extractRows(path)
        lines=dict()
        for row in rows:
            if(row["line"] not in lines):
                lines.update({int(row["line"]):Line(row["name"],row["colour"],row["stripe"])})
        return lines
