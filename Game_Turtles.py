import turtle
from Turtle_Game_Data import Charcter, static_entity, Generate_Maze

Karel_maze_1 = Generate_Maze(3, 3, 'center') # max size of 15x15
Generate_Maze.current_maze = Karel_maze_1

# prop_1 = turtle.Turtle()
# prop_2 = turtle.Turtle()
# prop_3 = turtle.Turtle()

T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
for turt in [T_box, line1, line2, line3, line4]: turt.hideturtle()
Sam = Charcter(name = 'Sam', sprite = 'PT')
Bob = Charcter(name = 'Bob', sprite = 'PT')
Pam = Charcter(name = 'Pam', sprite = 'PT')
Static_Turtle_1 = static_entity(name = 'Computer', sprite = 'tempWall', hide = True)
# Static_Turtle_2 = static_entity(name = 'paper', sprite = 'tempWall', hide = True)
# Static_Turtle_3 = static_entity(name = 'phone', sprite = 'PT', hide = True)
# Static_Turtle_4 = static_entity(name = 'N/C', sprite = 'PT', hide = True)
# Static_Turtle_5 = static_entity(name = 'Computer', sprite = 'tempWall', hide = True)
# Static_Turtle_6 = static_entity(name = 'paper', sprite = 'tempWall', hide = True)
# Static_Turtle_7 = static_entity(name = 'phone', sprite = 'PT', hide = True)
# Static_Turtle_8 = static_entity(name = 'N/C', sprite = 'PT', hide = True)


# Static_Turtle_2.set_Wall(0, 100)
# Static_Turtle_1.set_Wall(0, -100)
# Static_Turtle_3.set_Wall(0, -300)
# Static_Turtle_4.set_Wall(0, 300)
# Static_Turtle_5.set_Wall(100,-100)
# Static_Turtle_6.set_Wall(100,-100)


# Static_Turtle_5 = static_entity(name = 'N/C', sprite = 'PT', hide = True)
# Static_Turtle_6 = static_entity(name = 'N/C', sprite = 'PT', hide = True)
Charcter.active_player = Sam

# Game__objects = [line1, line2, line3, line4, T_box]
# Game_Objects = [Pam.actor, Bob.actor, Sam.actor]
# eniIndex, turtIndex = 0, 0
# entrance.turtlesize(3,3)