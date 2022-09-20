# edge type
# weighted edge
# unweighted edge

class Edge: 

    def __init__(self,start,end,other={}) -> None:
        if(start.isdigit()): self.start = int(start)
        else: self.start = start
        if(end.isdigit()): self.end = int(end)
        else: self.end = end
        for key in other.keys():
            setattr(self, key, other[key])

    
class WeightedEdge(Edge):
    def __init__(self,start, end, weight,other={}) -> None:
        super().__init__(start, end, other)
        self.weight = int(weight)

    # temp method for checking - will remove later
    def _detail(self):
        details={"start":self.start, "end":self.end, "weight":self.weight, "line":self.line}
        return details


    



        
