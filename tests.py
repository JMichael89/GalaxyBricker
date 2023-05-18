from scripts.models.Element import Element
from scripts.utils.Dimension import Dimension
from scripts.utils.Vector import Vector

element = Element(Vector(0, 0), Dimension(10, 10))
center = Vector(element.position + (element.dimension * 2))
print(element.dimension * 2)
print(element.dimension)

'''
        # Teste Randon
        ball_test = Ball(dimension=Dimension(20, 20))
        ball_test.select_ball(BallType.basic_white)
        ball_test.set_position(0, 0)
        ball_test.set_speed(random(), random())

        block_test = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block_test.select_bloc(BlockType.b1)
        
        # Tests A1
        ball_test.set_position(290, 500)
        ball_test.set_position(490, 500)
        ball_test.set_speed(0, -0.5)

        # Tests A2
        ball_test.set_position(600, 190)
        ball_test.set_position(600, 390)
        ball_test.set_speed(-0.5, 0)

        # Tests A3
        ball_test.set_position(290, 0)
        ball_test.set_position(490, 0)
        ball_test.set_speed(0, 0.5)

        # Tests A4
        ball_test.set_position(0, 190)
        ball_test.set_position(0, 390)
        ball_test.set_speed(0.5, 0)
        
        block_test = Block(Vector(300, 200), Dimension(200, 200))
        block_test.select_bloc(BlockType.b1)
        '''