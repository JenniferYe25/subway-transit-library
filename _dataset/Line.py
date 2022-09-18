class Line:
    def __init__(self,line,other={}) -> None:
        self.line = line
        for key in other.keys():
            setattr(self, key, other[key])
    
    def _detail(self):
        print("line: ", self.line," name:", self.name, "colour: ", self.colour, "stripe: ", self.stripe)
