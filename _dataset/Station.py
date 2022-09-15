class Station: 

    def __init__(self,id,latitude,longtitude,name,display_name,zone,total_lines) -> None:
        self.id = id
        self.longtitude = longtitude
        self.name = name
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines

    def get_id(self):
        return self.id

    def get_longitude(self):
        return self.longtitude

    def get_name(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name

    def get_zone(self):
        return self.zone
    
    def get_total_lines(self):
        return self.total_lines
        