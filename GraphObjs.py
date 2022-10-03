# edge type
# weighted edge
# unweighted edge

class Edge:
    def __init__(self, start, end, other={}):
        if (start.isdigit()):
            self.start = int(start)
        else:
            self.start = start
        if (end.isdigit()):
            self.end = int(end)
        else:
            self.end = end
        for key in other.keys():
            setattr(self, key, other[key])


class WeightedEdge(Edge):
    def __init__(self, start, end, weight, other={}):
        super().__init__(start, end)
        self.weight = int(weight)
        for key in other.keys():
            setattr(self, key, other[key])


class Line:
    def __init__(self, line, other={}):
        self.line = line
        for key in other.keys():
            setattr(self, key, other[key])


class Station:
    def __init__(self, key, other={}):
        self.id = key
        for key in other.keys():
            setattr(self, key, other[key])
