class Dimension:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def getGeometry(self):
        return f"{self.width}x{self.height}"

