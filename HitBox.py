import turtle
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
images = ["PT_FR.gif", "PT_FL.gif", "PT_FS.gif", "PT_BR.gif", "PT_BL.gif", "PT_BS.gif",
          "PT_LR.gif", "PT_LL.gif", "PT_LS.gif", "PT_RR.gif", "PT_RL.gif", "PT_RS.gif",
          "cover(1).gif"
         ]
for image in images:
    screen.register_shape(image)
backround = turtle.Turtle()
backround.shape('cover(1).gif')
player2_1 = turtle.Turtle()
player3_1 = turtle.Turtle()
player_1 = turtle.Turtle()
player2_2 = turtle.Turtle()
player3_2 = turtle.Turtle()
player_2 = turtle.Turtle()

T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
game_turtles = [backround, player2_1, player3_1, player_1, player2_2, player3_2, player_2,
                T_box, line1, line2, line3, line4]
for turt in game_turtles:
    turt.speed(0)
    turt.penup()
    turt.shape("PT_FR.gif")
    # turt.hideturtle()

Game_charcters =  { 'turtles':{player_1, player2_1, player3_1},
                    'Charcters':{'Sam', 'Bob', 'pam'},
                    
                    'current_turtle':backround, 'current_info':'backround',
                    'backround': {"turtle": backround,'direction': 'none','state':False,'ani_count':20, 'set_timer':False,
                           "speed":3,'up':False,'down':False,'left':False,'right':False,
                           'LPS':3,'RPS':3,'UPS':3,'DPS':3,
                           },

                    'Sam': {"turtle": player_1, 'turtle2': player_2,'direction': 'none','lock':False,'ani_count':20, 'set_timer':False,
                           "print_type":"auto",'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                           "speed":3,'LPS':3,'RPS':3,'UPS':3,'DPS':3, 'move_timer':-4, 'move_lock':True,
                           'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                           'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                           'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                           'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                           },

                    'Bob': {"turtle": player2_1, 'turtle2': player2_2,'direction': 'none', 'default_direction':'up','lock':True,'ani_count':20,
                            "print_type":"manual",'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                           "speed":3,'LPS':3,'RPS':3,'UPS':3,'DPS':3, 'move_timer':-4, 'move_lock':True,
                           'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                           'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                           'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                           'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                           },

                    'pam': {"turtle": player3_1, 'turtle2': player3_2,'direction': 'none', 'default_direction':'up','lock':True,'ani_count':20,
                           "print_type":"auto",'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                            "speed":3,'LPS':3,'RPS':3,'UPS':3,'DPS':3, 'move_timer':-4, 'move_lock':True,
                            'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                            'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                            'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                            'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                            }
                   
                  }

# Experimental features
#===================================================================
# def teleport():
#     print('works')
#     if player_movements['up']:
#         player.sety(player.ycor()+100)
#     if player_movements['down']: player.sety(player.ycor()-100)
#     if player_movements['left']: player.setx(player.xcor()-100)
#     if player_movements['right']: player.setx(player.xcor()+100)



# def inventory():
#     if inventory_screen.isvisible():
#         inventory_screen.hideturtle()
#     else:
#         inventory_screen.showturtle()
#===================================================================

# Player movement and animation
#===================================================================
def press_up():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'down'
        Game_charcters['backround']['down'] = True
        player_1.setheading(90)
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'left':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['direction'] = 'up'
        Game_charcters['Sam']['up']=True
def release_up():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['up'] = False
        Game_charcters['Sam']['set_timer'] = False
        Game_charcters['backround']['down'] = False
def press_down():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'up'
        Game_charcters['backround']['up'] = True
        player_1.setheading(270)
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'right':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['direction'] = 'down'
        Game_charcters['Sam']['down']=True
def release_down():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['down'] = False
        Game_charcters['Sam']['set_timer'] = False
        Game_charcters['backround']['up'] = False
def press_left():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'right'
        Game_charcters['backround']['right'] = True
        player_1.setheading(180)
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'down':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['direction'] = 'left'
        Game_charcters['Sam']['left']=True
def release_left():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['left'] = False
        Game_charcters['Sam']['set_timer'] = False
        Game_charcters['backround']['right'] = False
def press_right():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'left'
        Game_charcters['backround']['left'] = True
        player_1.setheading(0)
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'up':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['direction']='right'
        Game_charcters['Sam']['right']=True
def release_right():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['right'] = False
        Game_charcters['Sam']['set_timer'] = False
        Game_charcters['backround']['left'] = False

def animate_player(turtle = player_1, info = 'Sam'):
    if Game_charcters[info]['direction'] == 'up':
        if Game_charcters[info]['up']==True:
            if Game_charcters[info]['move_timer']==-4:turtle.shape(Game_charcters[info]['up_ani']['frame1'])
            if Game_charcters[info]['move_timer']==0:turtle.shape(Game_charcters[info]['up_ani']['frame2'])
            if Game_charcters[info]['move_timer']==4:turtle.shape(Game_charcters[info]['up_ani']['frame3'])
        else:
            turtle.shape(Game_charcters[info]['up_ani']['frame2'])
            Game_charcters[info]['move_timer']=-4
    if Game_charcters[info]['direction'] == 'down':
        if Game_charcters[info]['down']==True:
            if Game_charcters[info]['move_timer']==-4:turtle.shape(Game_charcters[info]['down_ani']['frame1'])
            if Game_charcters[info]['move_timer']==0:turtle.shape(Game_charcters[info]['down_ani']['frame2'])
            if Game_charcters[info]['move_timer']==4:turtle.shape(Game_charcters[info]['down_ani']['frame3'])
        else:
            turtle.shape(Game_charcters[info]['down_ani']['frame2'])
            Game_charcters[info]['move_timer']=-4
    if Game_charcters[info]['direction'] == 'left':
        if Game_charcters[info]['left']==True:
            if Game_charcters[info]['move_timer']==-4:turtle.shape(Game_charcters[info]['left_ani']['frame1'])
            if Game_charcters[info]['move_timer']==0:turtle.shape(Game_charcters[info]['left_ani']['frame2'])
            if Game_charcters[info]['move_timer']==4:turtle.shape(Game_charcters[info]['left_ani']['frame3'])
        else:
            turtle.shape(Game_charcters[info]['left_ani']['frame2'])
            Game_charcters[info]['move_timer']=-4
    if Game_charcters[info]['direction'] == 'right':
        if Game_charcters[info]['right']==True:
            if Game_charcters[info]['move_timer']==-4:turtle.shape(Game_charcters[info]['right_ani']['frame1'])
            if Game_charcters[info]['move_timer']==0:turtle.shape(Game_charcters[info]['right_ani']['frame2'])
            if Game_charcters[info]['move_timer']==4:turtle.shape(Game_charcters[info]['right_ani']['frame3'])
        else:
            turtle.shape(Game_charcters[info]['right_ani']['frame2'])
            Game_charcters[info]['move_timer']=-4
    if Game_charcters[info]['move_lock']==True:
        if Game_charcters[info]['move_timer']!=4:
            Game_charcters[info]['move_timer']+=1
        else:Game_charcters[info]['move_lock']=False
    elif Game_charcters[info]['move_lock']==False:
        if Game_charcters[info]['move_timer']!=-4:Game_charcters[info]['move_timer']-=1
        else:Game_charcters[info]['move_lock']=True
def adjust_movement(info = 'none', direction = 'none', up = False, down = False, left = False, right = False):
    Game_charcters[info]['down'] = down
    Game_charcters[info]['up'] = up
    Game_charcters[info]['left'] = left
    Game_charcters[info]['right'] = right
    Game_charcters[info]['direction'] = direction
def character_controls(turtle = 'none', info = 'Sam'):
    if (not Game_charcters['backround']['state'] and turtle != backround) or (Game_charcters['backround']['state'] and turtle != player_1):
        if Game_charcters[info]['direction'] == 'up' and Game_charcters[info]['up'] == True: turtle.sety(turtle.ycor()+Game_charcters[info]['UPS'])
        if Game_charcters[info]['direction'] == 'down' and Game_charcters[info]['down'] == True: turtle.sety(turtle.ycor()-Game_charcters[info]['DPS'])
        if Game_charcters[info]['direction'] == 'left' and Game_charcters[info]['left'] == True: turtle.setx(turtle.xcor()-Game_charcters[info]['LPS'])
        if Game_charcters[info]['direction'] == 'right' and Game_charcters[info]['right'] == True: turtle.setx(turtle.xcor()+Game_charcters[info]['RPS'])
def character_controls(turtle = 'none', info = 'Sam'):
    if (not Game_charcters['backround']['state'] and turtle != backround) or (Game_charcters['backround']['state'] and turtle != player_1):
        if Game_charcters[info]['direction'] == 'up' and Game_charcters[info]['up'] == True: turtle.sety(turtle.ycor()+Game_charcters[info]['UPS'])
        if Game_charcters[info]['direction'] == 'down' and Game_charcters[info]['down'] == True: turtle.sety(turtle.ycor()-Game_charcters[info]['DPS'])
        if Game_charcters[info]['direction'] == 'left' and Game_charcters[info]['left'] == True: turtle.setx(turtle.xcor()-Game_charcters[info]['LPS'])
        if Game_charcters[info]['direction'] == 'right' and Game_charcters[info]['right'] == True: turtle.setx(turtle.xcor()+Game_charcters[info]['RPS'])
def character_funct(turtle = 'none', character = 'none'):
    animate_player(turtle = turtle, info = character)
    character_controls(turtle = turtle, info = character)
def charcters():
    set_wall(entitie1 = "Bob", entitie2 = "Sam")
    character_funct(turtle = player_1, character = 'Sam')
    character_funct(turtle = player2_1, character = 'Bob')
    character_funct(turtle = player3_1, character = 'pam')

#===================================================================

            
            

def set_wall(entitie1 = 'none', entitie2 = "none"):
    object1, object2 = Game_charcters[entitie1]["turtle"], Game_charcters[entitie2]["turtle"]
    speed = Game_charcters[entitie2]['speed']
    if object1.distance(object2) <= 100:
        key, direction = get_player_direction(object_type = "turn", game_object1 = object1, game_object2 = object2), get_player_direction(object_type = "charcter", game_object1 = object1, game_object2 = object2)
        if direction == 'right':
            if object2.xcor() <= object1.xcor()+30 and object1.ycor()-30 <= object2.ycor() <= object1.ycor()+30:
                Game_charcters[entitie2]['LPS'] = 0
            else:
                Game_charcters[entitie2]['LPS'] = speed
        elif direction == 'up':
            if object2.ycor() <= object1.ycor()+30 and object1.xcor()-30 <= object2.xcor() <= object1.xcor()+30:
                Game_charcters[entitie2]['DPS'] = 0
            else:
                Game_charcters[entitie2]['DPS'] = speed
        elif direction == 'left':
            if object2.xcor() >= object1.xcor()-30 and object1.ycor()-30 <= object2.ycor() <= object1.ycor()+30:
                Game_charcters[entitie2]['RPS'] = 0
            else:
                Game_charcters[entitie2]['RPS'] = speed
        elif direction == 'down':
            if object2.ycor() >= object1.ycor()-30 and object1.xcor()-30 <= object2.xcor() <= object1.xcor()+30:
                Game_charcters[entitie2]['UPS'] = 0
            else:
                Game_charcters[entitie2]['UPS'] = speed
        for dir in ['LPS','DPS', 'RPS', 'UPS']:
                if Game_charcters[entitie2][dir] == 0 and dir != key:
                    Game_charcters[entitie2][dir] = 3

def get_player_direction(object_type = "none", game_object1 = "none", game_object2 = "none"):
    angel = game_object1.towards(game_object2)
    # print("Angel:", angel)
    if 315 < angel <= 360 or 0 <= angel <= 45:
        if object_type == "charcter": return 'right'
        if object_type == "turn": return 'LPS'
    elif 45 < angel <= 135:
        if object_type == "charcter": return 'up'
        if object_type == "turn": return 'DPS'
    elif 135 < angel <= 225:
        if object_type == "charcter": return 'left'
        if object_type == "turn": return 'RPS'
    elif 225 < angel <= 315:
        if object_type == "charcter": return 'down'
        if object_type == "turn": return 'UPS'

def move_game():
    charcters()
    screen.update()
    screen.ontimer(move_game, 16)  # Use 16ms for ~60fps, or 20 for 50fps


screen.listen()
screen.onkeypress(press_up, 'Up')
screen.onkeyrelease(release_up, 'Up')
screen.onkeypress(press_down, 'Down')
screen.onkeyrelease(release_down, 'Down')
screen.onkeypress(press_left, 'Left')
screen.onkeyrelease(release_left, 'Left')
screen.onkeypress(press_right, 'Right')
screen.onkeyrelease(release_right, 'Right')
#========================================
screen.onkeypress(press_up, '5')
screen.onkeyrelease(release_up, '5')
screen.onkeypress(press_down, '2')
screen.onkeyrelease(release_down, '2')
screen.onkeypress(press_left, '1')
screen.onkeyrelease(release_left, '1')
screen.onkeypress(press_right, '3')
screen.onkeyrelease(release_right, '3')
#========================================
move_game()
screen.mainloop()