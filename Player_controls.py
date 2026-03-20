from Turtle_Game_Data import Game_entities
from Game_Turtles import player_1
def press_up():
    if not Game_entities['Sam']['lock']:
        Game_entities['backround']['direction'] = 'down'
        Game_entities['backround']['down'] = True
        player_1.setheading(90)
        Game_entities['Sam']['direction'] = 'up'
        Game_entities['Sam']['up']=True
def release_up():
    if not Game_entities['Sam']['lock']:
        Game_entities['Sam']['up'] = False
        Game_entities['backround']['down'] = False
def press_down():
    if not Game_entities['Sam']['lock']:
        Game_entities['backround']['direction'] = 'up'
        Game_entities['backround']['up'] = True
        player_1.setheading(270)
        Game_entities['Sam']['direction'] = 'down'
        Game_entities['Sam']['down']=True
def release_down():
    if not Game_entities['Sam']['lock']:
        Game_entities['Sam']['down'] = False
        Game_entities['backround']['up'] = False
def press_left():
    if not Game_entities['Sam']['lock']:
        Game_entities['backround']['direction'] = 'right'
        Game_entities['backround']['right'] = True
        player_1.setheading(180)
        Game_entities['Sam']['direction'] = 'left'
        Game_entities['Sam']['left']=True
def release_left():
    if not Game_entities['Sam']['lock']:
        Game_entities['Sam']['left'] = False
        Game_entities['backround']['right'] = False
def press_right():
    if not Game_entities['Sam']['lock']:
        Game_entities['backround']['direction'] = 'left'
        Game_entities['backround']['left'] = True
        player_1.setheading(0)
        Game_entities['Sam']['direction']='right'
        Game_entities['Sam']['right']=True
def release_right():
    if not Game_entities['Sam']['lock']:
        Game_entities['Sam']['right'] = False
        Game_entities['backround']['left'] = False

# def character_controls(turtle = 'none', entitie = 'Sam'):
#     if (Game_entities['backround']['switch'] == False and turtle != backround) or (Game_entities['backround']['switch'] == True and turtle != player_1):
#         if Game_entities[entitie]['direction'] == 'up' and Game_entities[entitie]['up'] == True: turtle.sety(turtle.ycor()+Game_entities[entitie]['UPS'])
#         if Game_entities[entitie]['direction'] == 'down' and Game_entities[entitie]['down'] == True: turtle.sety(turtle.ycor()-Game_entities[entitie]['DPS'])
#         if Game_entities[entitie]['direction'] == 'left' and Game_entities[entitie]['left'] == True: turtle.setx(turtle.xcor()-Game_entities[entitie]['LPS'])
#         if Game_entities[entitie]['direction'] == 'right' and Game_entities[entitie]['right'] == True: turtle.setx(turtle.xcor()+Game_entities[entitie]['RPS'])
