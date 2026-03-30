import turtle
from Turtle_Game_Data import entity, static_entity

# prop_1 = turtle.Turtle()
# prop_2 = turtle.Turtle()
# prop_3 = turtle.Turtle()

T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
for turt in [T_box, line1, line2, line3, line4]: turt.hideturtle()
Sam = entity(name = 'Sam', sprite = 'PT')
Bob = entity(name = 'Bob', sprite = 'PT')
Pam = entity(name = 'Pam', sprite = 'PT')
Static_Turtle_1 = static_entity(name = 'Computer', sprite = 'PT', hide = True)
Static_Turtle_2 = static_entity(name = 'Paper', sprite = 'PT', hide = True)
Static_Turtle_3 = static_entity(name = 'Phone', sprite = 'PT', hide = True)
entity.active_player = Sam

# Game__objects = [line1, line2, line3, line4, T_box]
Game_Objects = [Pam.actor, Bob.actor, Sam.actor]
# eniIndex, turtIndex = 0, 0
# entrance.turtlesize(3,3)
