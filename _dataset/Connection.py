class Connection: 

    def __init__(self,start, end, weight,other={}) -> None:
        self.start = start
        self.end = end
        self.weight = int(weight)
        for key in other.keys():
            setattr(Connection, key, other[key])

    # temp method for checking - will remove later
    def _detail(self):
        details={"start":self.start, "end":self.end, "weight":self.weight, "line":self.line}
        return details
    



        
