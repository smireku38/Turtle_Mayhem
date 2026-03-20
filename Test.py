import turtle
import time
from Turtle_Game_Data import*
from Game_Turtles import*
from Player_controls import*
# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
images = ['PT_FR.gif', 'PT_FL.gif', 'PT_FS.gif', 'PT_BR.gif', 'PT_BL.gif', 'PT_BS.gif',
          'PT_LR.gif', 'PT_LL.gif', 'PT_LS.gif', 'PT_RR.gif', 'PT_RL.gif', 'PT_RS.gif',
          'Cover(1).gif'
         ]
for image in images:
    screen.register_shape(image)

eniIndex, turtIndex = 0, 0
while (turtIndex < len(game_turtles_in)):
    if eniIndex < len(Game_entities['enities']):
        curr_enentity = Game_entities['enities'][eniIndex]
        if turtIndex%2 == 0: 
            Game_entities[curr_enentity]['turtle'] = game_turtles_in[turtIndex]
            eniIndex += 1
        elif turtIndex%2 == 1:
            Game_entities[curr_enentity]['turtle2'] = game_turtles_in[turtIndex]
    
    turtIndex += 1
    
for turt in game_turtles:
    turt.speed(0)
    turt.penup()
    turt.shape('PT_FR.gif')
player_1.goto(0,300)
entrance = turtle.Turtle()
# player_1.sety(player_1.ycor()+1)
# player2_1.goto(-100,0)
entrance.goto(100,200)
entrance.shape('square')
entrance.turtlesize(3,3)
entrance.color('blue')
entrance.penup()
backround.shape('Cover(1).gif')
backround.showturtle()



# Text box definitions
#===================================================================

#====================================================================

# Player movement and animation
#===================================================================
# Track raw key states so releasing one key doesn't block movement if another
# movement key is still held.
# Player movement and animation
#===================================================================

def map_range():
    backroundData = Game_entities['backround']
    if backroundData['lock_Obj'] == False:
        x, y, speed = backround.xcor(), backround.ycor(),Game_entities['backround']['speed']
        up, down, left, right = backroundData['up'], backroundData['down'], backroundData['left'], backroundData['right']
        direction = backroundData['direction']
        switch = False
        if direction == 'up' and up and y > 100: Game_entities['backround']['UPS'], switch = 0, False
        elif direction == 'down' and down and y < -100: Game_entities['backround']['DPS'], switch = 0, False
        elif direction == 'left' and left and x < -100: Game_entities['backround']['LPS'], switch = 0, False
        elif direction == 'right' and right and x > 100: Game_entities['backround']['RPS'], switch = 0, False

        if direction == 'up' and up and y <= 100: Game_entities['backround']['UPS'], switch = speed, True
        elif direction == 'down' and down and y >= -100: Game_entities['backround']['DPS'], switch = speed, True
        elif direction == 'left' and left and x >= -100: Game_entities['backround']['LPS'], switch = speed, True
        elif direction == 'right' and right and x <= 100: Game_entities['backround']['RPS'], switch = speed, True
        move_objects(direction, up, down, left, right)
        Game_entities['backround']['switch'] = switch
    else:
        if backroundData['switch'] == True: backroundData['switch'] = False
        if 0 not in [backroundData['UPS'], backroundData['DPS'], backroundData['LPS'], backroundData['RPS']]:
            Game_entities['backround']['UPS'], Game_entities['backround']['DPS'], Game_entities['backround']['LPS'], Game_entities['backround']['RPS'] = 0, 0, 0, 0
def move_objects(dir = 'none', up = False, down = False, left = False, right = False):
    if Game_entities['backround']['switch'] == True:
        for turtle in Game_entities['turtles']:
            if turtle != backround and turtle not in [player_1, player_2]:
                if dir == 'up' and up == True: turtle.sety(turtle.ycor()+Game_entities['backround']['UPS'])
                if dir == 'down' and down == True: turtle.sety(turtle.ycor()-Game_entities['backround']['DPS'])
                if dir == 'left' and left == True: turtle.setx(turtle.xcor()-Game_entities['backround']['LPS'])
                if dir == 'right' and right == True: turtle.setx(turtle.xcor()+Game_entities['backround']['RPS'])

def animation_timer(entitie = 'Sam', direction = 'down'):
    if Game_entities[entitie]['animation_enabled']==True or Game_entities[entitie][direction] == True:
        if Game_entities[entitie]['Oscillate_ani']==True:
            if Game_entities[entitie]['move_timer']!=4:
                Game_entities[entitie]['move_timer']+=1
            else:Game_entities[entitie]['Oscillate_ani']=False
        elif Game_entities[entitie]['Oscillate_ani']==False:
            if Game_entities[entitie]['move_timer']!=-4:
                Game_entities[entitie]['move_timer']-=1
            else:Game_entities[entitie]['Oscillate_ani']=True
    elif (Game_entities[entitie]['move_timer'] != 0): Game_entities[entitie]['move_timer'] = 0
def animate_player(turtle = player_1, entitie = 'Sam'):
    direction, timer = Game_entities[entitie]['direction'], Game_entities[entitie]['move_timer']
    if direction == 'up':
        if timer==0:turtle.shape(Game_entities[entitie]['up_ani']['frame2'])
        if timer==4:turtle.shape(Game_entities[entitie]['up_ani']['frame3'])
        if timer==-4:turtle.shape(Game_entities[entitie]['up_ani']['frame1'])
    if direction == 'down':
        if timer==0:turtle.shape(Game_entities[entitie]['down_ani']['frame2'])
        elif timer==4:turtle.shape(Game_entities[entitie]['down_ani']['frame3'])
        elif timer==-4:turtle.shape(Game_entities[entitie]['down_ani']['frame1'])
    if direction == 'left':
        if timer==0:turtle.shape(Game_entities[entitie]['left_ani']['frame2'])
        elif timer==4:turtle.shape(Game_entities[entitie]['left_ani']['frame3'])
        elif timer==-4:turtle.shape(Game_entities[entitie]['left_ani']['frame1'])
    if direction == 'right':
        if timer==0:turtle.shape(Game_entities[entitie]['right_ani']['frame2'])
        elif timer==4:turtle.shape(Game_entities[entitie]['right_ani']['frame3'])
        elif timer==-4:turtle.shape(Game_entities[entitie]['right_ani']['frame1'])
    animation_timer(entitie, direction)

def adjust_movement(entitie = 'none', direction = 'none', default = 'none', up = False, down = False, left = False, right = False):
    if (default != 'none'): Game_entities[entitie]['default_direction'] = default
    if (direction == 'none'): direction = Game_entities[entitie]['default_direction']
    Game_entities[entitie]['down'] = down
    Game_entities[entitie]['up'] = up
    Game_entities[entitie]['left'] = left
    Game_entities[entitie]['right'] = right
    Game_entities[entitie]['direction'] = direction
    Game_entities[entitie]['animation_enabled'] = False
def character_controls(turtle = 'none', entitie = 'Sam'):
    if (Game_entities['backround']['switch'] == False and turtle != backround) or (Game_entities['backround']['switch'] == True and turtle != player_1):
        if Game_entities[entitie]['direction'] == 'up' and Game_entities[entitie]['up'] == True: turtle.sety(turtle.ycor()+Game_entities[entitie]['UPS'])
        if Game_entities[entitie]['direction'] == 'down' and Game_entities[entitie]['down'] == True: turtle.sety(turtle.ycor()-Game_entities[entitie]['DPS'])
        if Game_entities[entitie]['direction'] == 'left' and Game_entities[entitie]['left'] == True: turtle.setx(turtle.xcor()-Game_entities[entitie]['LPS'])
        if Game_entities[entitie]['direction'] == 'right' and Game_entities[entitie]['right'] == True: turtle.setx(turtle.xcor()+Game_entities[entitie]['RPS'])
def character_funct(turtle = 'none', character = 'none'):
    if turtle != backround and Game_entities[character]['lock_Animation'] == False: animate_player(turtle = turtle, entitie = character)
    elif Game_story['playing_story'] == False and turtle == backround: map_range()
    character_controls(turtle = turtle, entitie = character)
    # if inventory_screen.isvisible(): player_animation(turtle = modle)
def hideObjects(objects):
    objects['turtle'].hideturtle()
    objects['turtle2'].hideturtle()
    objects['turtle'].goto(-300,-300)
    objects['turtle2'].goto(-300,-300)


#===================================================================
# Story Phases
#===================================================================

def characters():
    # if Game_settings['HitBoxes_on']:
    #     for character in Game_entities['characters']:
    #         if character != 'Sam':
    #             object_hitbox(entitie1 = character, entitie2 = 'Sam')
    #     for character in Game_entities['objects']:
    #         object_hitbox(entitie1 = character, entitie2 = 'Sam')
    
    character_funct(turtle = backround, character = 'backround')
    character_funct(turtle = player_1, character = 'Sam')
#===================================================================

def move_game():
    if Game_story['pause_Game'] == False:
        characters()
        # if player_1.ycor() >= 0:
        #     player_1.sety(player_1.ycor()-5)
        #     player_2.sety(player_1.ycor()-5)
        screen.update() 
        screen.ontimer(move_game, 30)  # Use 16ms for ~60fps, or 20 for 50fps

screen.listen()
screen.onkeypress(press_up, 'w')
screen.onkeyrelease(release_up, 'w')
screen.onkeypress(press_down, 's')
screen.onkeyrelease(release_down, 's')
screen.onkeypress(press_left, 'a')
screen.onkeyrelease(release_left, 'a')
screen.onkeypress(press_right, 'd')
screen.onkeyrelease(release_right, 'd')
# screen.onkey(interactable_objects, 'space')
move_game()
screen.mainloop()

# def same_turtle(enti):
#     turtle1, turtle2 = Game_entities[enti]['turtle'], Game_entities[enti]['turtle2']
#     if turtle1.shape() != turtle2.shape():
#         turtle2.shape(turtle2)
#     if turtle1.xcor() != turtle1.xcor():
#         turtle2.setx(turtle1.xcor())
#     if turtle1.ycor() != turtle2.ycor():
#         turtle2.setx(turtle1.xcor())