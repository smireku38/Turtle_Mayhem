from Turtle_Game_Data import map_settings, entity, static_entity
from Screen_Init import backround
def press_up():
    if not map_settings['lock_map']:
        map_settings['direction'] = 'up'
        map_settings['up'] = True
        entity.active_player.direction = 'up'
def release_up():
    map_settings['up'] = False
def press_down():
    if not map_settings['lock_map']:
        map_settings['direction'] = 'down'
        map_settings['down'] = True
        entity.active_player.direction = 'down'
def release_down():
    map_settings['down'] = False
def press_left():
    if not map_settings['lock_map']:
        map_settings['direction'] = 'left'
        map_settings['left'] = True
        entity.active_player.direction = 'left'
def release_left():
    map_settings['left'] = False
def press_right():
    if not map_settings['lock_map']:
        map_settings['direction'] = 'right'
        map_settings['right'] = True
        entity.active_player.direction = 'right'
def release_right():
    map_settings['right'] = False

def move_backround():
    direction = map_settings['direction']
    if direction == 'up' and map_settings['up'] == True: backround.sety(backround.ycor()-map_settings['UPS'])
    if direction == 'down' and map_settings['down'] == True: backround.sety(backround.ycor()+map_settings['DPS'])
    if direction == 'left' and map_settings['left'] == True: backround.setx(backround.xcor()+map_settings['LPS'])
    if direction == 'right' and map_settings['right'] == True: backround.setx(backround.xcor()-map_settings['RPS'])
    move_objects(direction)

def move_objects(direction):
    all_entitys = entity.entity_pool + static_entity.entity_pool
    for enti in all_entitys:
        if enti != entity.active_player:
            if direction == 'up' and map_settings['up'] == True: enti.actor.sety(enti.actor.ycor()-map_settings['UPS'])
            if direction == 'down' and map_settings['down'] == True: enti.actor.sety(enti.actor.ycor()+map_settings['DPS'])
            if direction == 'left' and map_settings['left'] == True: enti.actor.setx(enti.actor.xcor()+map_settings['LPS'])
            if direction == 'right' and map_settings['right'] == True: enti.actor.setx(enti.actor.xcor()-map_settings['RPS'])
