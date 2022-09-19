import csv
import re
from Line import Line
from Station import Station
from Connection import Connection 

class DataExtractor:
    def __init__(self):
        pass
    
    # String path
    # required[] - list of required headings, assume it's in the same order as the obj it wants to create
    # obj - object type to create
    # assume all required info is in one file 
    def extractRows(self,path,required,obj):
        fileType=path[-3:].lower()

        if fileType == "csv":
                with open(path) as csvFile:
                    csvreader = list(csv.reader(csvFile))
                    header=csvreader[0] #list of all headings in file
                    neededIndex=[] #index of all the required headings in refernce to header list
                    otherIndex=[] #index of all other headings
                    objects=[] #list of obj to return 

                    for r in header: #filling list 
                        if(r not in required):
                            otherIndex.append(header.index(r))
                        else:
                            neededIndex.append(header.index(r)) 
                 
                    #creating objs                        
                    for row in csvreader[1:]:
                        req=[row[neededIndex[i]] for i in range(len(neededIndex))] 
                        other={header[otherIndex[i]]: row[otherIndex[i]] for i in range(len(otherIndex))}
                        # print("req ", req)
                        objects.append(obj(*req,other))
                    csvFile.close()
        # add new if stament if have different file type to handle 
        return objects

# testing
data=DataExtractor()
# data.extractRows('_dataset/london.stations.csv',['id'],Station)
data.extractRows('_dataset/london.connections.csv',['station1', 'station2', 'time'],Connection)

