from scripts.utils.Vector import Vector


class Dimension(Vector):
    def get_geometry(self):
        return f"{self.x}x{self.y}"
