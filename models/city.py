class City:
    
    def __init__(self, name, country, notes=None, visited=False, id=None):
        self.name = name
        self.country = country
        self.notes = notes
        self.visited = visited

    def mark_as_visited(self):
        self.visited = True