from Turtle_Game_Data import Turtle_Game, entity, Charcter
from Screen_Init import backround
def press_up():
    if not Turtle_Game.map_settings['lock_map']:
        Turtle_Game.map_settings['direction'] = 'up'
        Turtle_Game.map_settings['up'] = True
        Charcter.active_player.direction = 'up'
def release_up():
    Turtle_Game.map_settings['up'] = False
def press_down():
    if not Turtle_Game.map_settings['lock_map']:
        Turtle_Game.map_settings['direction'] = 'down'
        Turtle_Game.map_settings['down'] = True
        Charcter.active_player.direction = 'down'
def release_down():
    Turtle_Game.map_settings['down'] = False
def press_left():
    if not Turtle_Game.map_settings['lock_map']:
        Turtle_Game.map_settings['direction'] = 'left'
        Turtle_Game.map_settings['left'] = True
        Charcter.active_player.direction = 'left'
def release_left():
    Turtle_Game.map_settings['left'] = False
def press_right():
    if not Turtle_Game.map_settings['lock_map']:
        Turtle_Game.map_settings['direction'] = 'right'
        Turtle_Game.map_settings['right'] = True
        Charcter.active_player.direction = 'right'
def release_right():
   Turtle_Game. map_settings['right'] = False

def move_backround():
    direction = Turtle_Game.map_settings['direction']
    if direction == 'up' and Turtle_Game.map_settings['up'] == True: backround.sety(backround.ycor()-Turtle_Game.map_settings['UPS'])
    if direction == 'down' and Turtle_Game.map_settings['down'] == True: backround.sety(backround.ycor()+Turtle_Game.map_settings['DPS'])
    if direction == 'left' and Turtle_Game.map_settings['left'] == True: backround.setx(backround.xcor()+Turtle_Game.map_settings['LPS'])
    if direction == 'right' and Turtle_Game.map_settings['right'] == True: backround.setx(backround.xcor()-Turtle_Game.map_settings['RPS'])
    Turtle_Game.move_objects(direction)
