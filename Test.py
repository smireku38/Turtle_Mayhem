import turtle
import time
from Turtle_Game_Data import Game_story, Game_dialogue, entity, static_entity, map_settings
from Game_Story1 import phase1
from Game_Turtles import*
from Player_controls import*
from Screen_Init import screen, Canvas
from Procces_Game_Dio import word_space, manual_print, auto_print
entity.active_player = Sam

def character_funct():
    entity.activate_entitys()

def find_interactable_object():
    if word_space['Can_print'] == True:
        for enti in entity.entity_pool:
            if enti.conversant:
                if entity.active_player.actor.distance(enti.actor) < 50:
                    return enti
def interactable_objects():
    enti = find_interactable_object()
    if enti != None and (enti.actor.isvisible() or enti.actor.isvisible()):
        if enti.print_type == 'auto':
            auto_print(Game_dialogue['Enti_W_Dio'][enti.name])
        elif enti.print_type == 'manual':
            manual_print(Game_dialogue['Enti_W_Dio'][enti.name])
            word_space['manual_lock'] = False
            # print(Game_story['MacGuffin'], ' ',enti.name, Game_story['Re_MacGuffin'])
        if Game_story['MacGuffin'] == enti.name and Game_story['Re_MacGuffin'] == True:
            Game_story['MacGuffin'] = 'none'
            Game_story['Re_MacGuffin'] = False
        if Game_story['pause_Game'] == False: move_game()

# #===================================================================
# # Story Phases
# #===================================================================
# #===================================================================
next_enti = entity.entitys.index(entity.active_player.name)
def Change_active_player():
    global next_enti
    next_enti += 1
    if next_enti == len(entity.entity_pool): next_enti = 0
    if entity.active_player.direction != entity.active_player.default_direction:
        entity.active_player.default_direction = entity.active_player.direction
        print(entity.active_player.direction)
    entity.active_player = entity.entity_pool[next_enti]
    map_settings['direction'] = entity.active_player.direction
    sft_y = entity.active_player.actor.ycor()
    sft_x = entity.active_player.actor.xcor()
    for enti in Game_Objects: enti.goto(enti.xcor()-sft_x, enti.ycor()-sft_y)
    print(f"Active turtle is know: {entity.active_player.name}!")

def move_game():
    if Game_story['pause_Game'] == False:
        phase1()
        character_funct()
        move_backround()
        screen.update()
        screen.ontimer(move_game, 30)  # Use 16ms for ~60fps, or 20 for 50fps
screen.listen()
screen.onkey(Change_active_player, 'c')
screen.onkeypress(press_up, 'w')
screen.onkeyrelease(release_up, 'w')
screen.onkeypress(press_down, 's')
screen.onkeyrelease(release_down, 's')
screen.onkeypress(press_left, 'a')
screen.onkeyrelease(release_left, 'a')
screen.onkeypress(press_right, 'd')
screen.onkeyrelease(release_right, 'd')
screen.onkey(interactable_objects, 'space')
move_game()
screen.mainloop()

