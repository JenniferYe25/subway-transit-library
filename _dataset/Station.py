class Station: 

    def __init__(self,key,other={}) -> None:
        self.id = key
        for key in other.keys():
            setattr(self, key, other[key])
