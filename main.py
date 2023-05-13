from game_engine.GameEngine import GameEngine
from models.utils.Dimension import Dimension

dimension = Dimension(700, 780)
game_engine = GameEngine("Galaxy Bricker", False, dimension)
game_engine.dimensionGeometry()
game_engine.createWindow()
