import turtle
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
images = ["PT_FR.gif", "PT_FL.gif", "PT_FS.gif", "PT_BR.gif", "PT_BL.gif", "PT_BS.gif",
          "PT_LR.gif", "PT_LL.gif", "PT_LS.gif", "PT_RR.gif", "PT_RL.gif", "PT_RS.gif",
          "Cover(1).gif"
         ]
for image in images:
    screen.register_shape(image)
backdrop1 = turtle.Turtle()
backdrop2 = turtle.Turtle()
backdrop1.sety(400)
backdrop2.sety(-400)
entrance = turtle.Turtle()
entrance2 = turtle.Turtle()
player = turtle.Turtle()
temp = -1

game_turtles = [backdrop1, backdrop2, entrance, entrance2, player]
for turt in game_turtles:
    turt.speed(0)
    turt.penup()
    turt.shape("PT_FR.gif")
player.speed(0)
player.penup()
# backdrop1.hideturtle()
# backdrop2.hideturtle()

Game_charcters =  { 
                    'Sam': {'direction': 'none','lock':False,'ani_count':20, 'set_timer':False,
                            "condtion":"none",'animation': "none",
                           'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                           'LPS':5,'RPS':5,'UPS':5,'DPS':5, 'move_timer':-4, 'move_lock':True,
                           'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                           'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                           'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                           'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                           }
                  }

# Track raw key states so releasing one key doesn't block movement if another
# movement key is still held.
def animate_Bipeds(turtle = "none", info = 'Sam'):
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
def press_up():
    if not Game_charcters['Sam']['lock']:
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'left':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['animation'] = 'up'
        Game_charcters['Sam']['direction'] = 'up'
        Game_charcters['Sam']['up']=True
def release_up():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['up'] = False
        Game_charcters['Sam']['set_timer'] = False
def press_down():
    if not Game_charcters['Sam']['lock']:
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'right':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['animation'] = 'down'
        Game_charcters['Sam']['direction'] = 'down'
        Game_charcters['Sam']['down']=True
def release_down():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['down'] = False
        Game_charcters['Sam']['set_timer'] = False
def press_left():
    if not Game_charcters['Sam']['lock']:
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'down':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['animation'] = 'left'
        Game_charcters['Sam']['direction'] = 'left'
        Game_charcters['Sam']['left']=True
def release_left():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['left'] = False
        Game_charcters['Sam']['set_timer'] = False
def press_right():
    if not Game_charcters['Sam']['lock']:
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'up':
                Game_charcters['Sam']['move_timer'] = -4
            else:
                Game_charcters['Sam']['move_timer'] = 4
                Game_charcters['Sam']['move_lock'] = False
            Game_charcters['Sam']['set_timer'] = True
        Game_charcters['Sam']['animation'] = 'right'
        Game_charcters['Sam']['direction']='right'
        Game_charcters['Sam']['right']=True
def release_right():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['Sam']['right'] = False
        Game_charcters['Sam']['set_timer'] = False
def character_controls(turtle = 'none', info = 'Sam'):
    if Game_charcters[info]['direction'] == 'up' and Game_charcters[info]['up'] == True:turtle.sety(turtle.ycor()+Game_charcters[info]['UPS'])
    if Game_charcters[info]['direction'] == 'down' and Game_charcters[info]['down'] == True: turtle.sety(turtle.ycor()-Game_charcters[info]['DPS'])
    if Game_charcters[info]['direction'] == 'left' and Game_charcters[info]['left'] == True: turtle.setx(turtle.xcor()-Game_charcters[info]['LPS'])
    if Game_charcters[info]['direction'] == 'right' and Game_charcters[info]['right'] == True: turtle.setx(turtle.xcor()+Game_charcters[info]['RPS'])
def character_funct(turtle = 'none', character = 'none'):
    animate_Bipeds(turtle = turtle, info = character)
    character_controls(turtle = turtle, info = character)
def behind():
    if player.ycor() <= entrance.ycor():
        entrance.shape("PT_FR.gif")
        entrance.showturtle()
        entrance2.hideturtle()
    else:
        entrance2.shape("PT_FR.gif")
        entrance.hideturtle()
        entrance2.showturtle()
        
def move_game():
    global temp
    # behind()
    if temp == -1:
        temp = 20
        entrance2.shape('circle')
    if temp == 19:
        entrance.sety(400)
        entrance.showturtle()
        entrance.shape('circle')
        entrance.shapesize(stretch_wid=5, stretch_len=10) # Temp line
        entrance2.sety(-10)
        entrance2.showturtle()
        entrance2.shapesize(stretch_wid=2, stretch_len=10) # Temp line
        player.showturtle()
        player.sety(400)
    if temp > 0:
        for backdrop in [backdrop1, backdrop2]:
            if backdrop.ycor() <= 500:
                backdrop.shape("Cover(1).gif")
                backdrop.sety(backdrop.ycor()+40)
            else :
                backdrop.sety(-500)
                temp -= 1
                print(temp)
        if player.ycor() >= 0:
            player.sety(player.ycor()-5)
        else:
            entrance.sety(entrance.ycor()+2)
    elif (player.ycor() >= -300):
        player.showturtle()
        player.sety(player.ycor()-5)
        backdrop1.hideturtle()
        backdrop2.hideturtle()
        entrance2.sety(entrance2.ycor()-5)
        # entrance2.shape('PT_FS.gif')
    character_funct(turtle = player, character = 'Sam')
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
move_game()
screen.mainloop()