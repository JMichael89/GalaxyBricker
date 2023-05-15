class Dimension:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Dimension [ width={self.width}, height={self.height} ]"

    def get_geometry(self):
        return f"{self.width}x{self.height}"
