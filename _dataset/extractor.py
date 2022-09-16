def dataExtractor(linePath, connectionsPath, stationsPath):
    stationCatalog=set()
    connections=set()
    lines=LinesBuilding(linePath)

    rows=extractRows(connectionsPath)
        connections=set()
        for row in rows:
            stationCatalog.add(row["station1"])
            connections.append(Connection(row["station1"],row["station2"],row["line"],row["time"]))
    
    extractRows(linePath)
    extractRows(connectionsPath)
    extractRows(stationsPath)

def extractRows(path):
    with open(path) as csvFile:
        csvreader = csv.DictReader(csvFile)
        next(csvreader)

        rows = []
        for row in csvreader:
                rows.append(row)
        csvFile.close()
    return rows

  def StationsBuilding(path,connection):
        rows=extractRows(path)
        stations=set()
        for row in rows:
            stations.append(Station(row["id"],connection,row["latitude"],row["longitude"],row["name"],row["display_name"],row["zone"],row["total_lines"],row["rail"]))
        return stations

def ConnectionBuilding(path):
        rows=extractRows(path)
        connections=set()
        for row in rows:
            if(row["station1"] not in )
            connections.append(Connection(row["station1"],row["station2"],row["line"],row["time"]))
        return connections

def LinesBuilding(path):
    rows=extractRows(path)
    lines=[]
    for row in rows:
        lines.add([row["line"],row["name"],row["colour"],row["stripe"])
    return lines