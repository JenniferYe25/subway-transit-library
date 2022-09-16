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