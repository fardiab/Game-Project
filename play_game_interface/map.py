class Map:
    def __init__(self, map_name="Helodek"):
        self.map_name = map_name

    def show_maps(self):
        return """Helodek - 1
Nuken - 2
Containment - 3
Deadlock - 4
Decay - 5
Vertigo - 6
Shelter - 7"""

    def join(self):
        return f"Joining {self.map_name}"
