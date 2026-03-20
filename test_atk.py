import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color('green')
player.shape('turtle')

STB1 = turtle.Turtle()
STB2 = turtle.Turtle()
enemy = turtle.Turtle()
enemy.penup()
butten1 = turtle.Turtle()
butten2 = turtle.Turtle()
butten1.shape('circle')
butten2.shape('circle')
butten1.color('red')
butten2.color('blue')
butten1.turtlesize(5,5)
butten2.turtlesize(5,5)
butten1.penup()
butten2.penup()
butten1.goto(500,-300)
butten2.goto(600,-300)
STB1.speed(0)
STB2.speed(0)
STB1.penup()
STB2.penup()
STB1.shape('square')
STB2.shape('square')
STB1.turtlesize(0.5, 1.5)
STB2.turtlesize(0.5, 1.5)
GameT_1_A1 = turtle.Turtle()
GameT_2_A2 = turtle.Turtle()
GameT_3_A3 = turtle.Turtle()
GameT_4_A4 = turtle.Turtle()
GameT_5_A5 = turtle.Turtle()
GameT_6_A6 = turtle.Turtle()
GameT_7_A7 = turtle.Turtle()
GameT_8_A8 = turtle.Turtle()
GameT_9_A9 = turtle.Turtle()
GameT_10_A10 = turtle.Turtle()
screen.register_shape('PT_FR.gif')
screen.register_shape('PT_FL.gif')
screen.register_shape('PT_FS.gif')
screen.register_shape('PT_BR.gif')
screen.register_shape('PT_BL.gif')
screen.register_shape('PT_BS.gif')
screen.register_shape('PT_LR.gif')
screen.register_shape('PT_LL.gif')
screen.register_shape('PT_LS.gif')
screen.register_shape('PT_RR.gif')
screen.register_shape('PT_RL.gif')
screen.register_shape('PT_RS.gif')
STB_info={
    'ST_turtles':{
                 'STB1':STB1,'STB2':STB2,
                 'MB1':GameT_1_A1,'MB2':GameT_2_A2,'MB3':GameT_3_A3,'MB4':GameT_4_A4,'MB5':GameT_5_A5,
                 'MB6':GameT_6_A6,'MB7':GameT_7_A7,'MB8':GameT_8_A8,'MB9':GameT_9_A9,'MB10':GameT_10_A10
    },
    'MB_locks':{
                'MB1':True,'MB2':True,'MB3':True,'MB4':True,'MB5':True,
                'MB6':True,'MB7':True,'MB8':True,'MB9':True,'MB10':True
    },
    'Blaster_pos':{
                   'Current_pos':{'Rx':0,'Ry':0,'Lx':0,'Ly':0},
                      'up':{'Rx':15,'Ry':-20,'Lx':-15,'Ly':-20},
                    'down':{'Rx':-15,'Ry':20,'Lx':15,'Ly':20},
                    'left':{'Rx':15,'Ry':20,'Lx':15,'Ly':-20},
                   'right':{'Rx':-15,'Ry':-20,'Lx':-15,'Ly':20}
    },
    'STB1':{
        'MB1':{'x':0,'y':0},
        'MB2':{'x':0,'y':0},
        'MB3':{'x':0,'y':0},
        'MB4':{'x':0,'y':0},
        'MB5':{'x':0,'y':0}
    },
    'STB2':{
        'MB6':{'x':0,'y':0},
        'MB7':{'x':0,'y':0},
        'MB8':{'x':0,'y':0},
        'MB9':{'x':0,'y':0},
        'MB10':{'x':0,'y':0}
    },
    'enemys':{enemy},
    'mouse':0,'reloding_STB1':False,'reloding_STB2':False,'BH1':0,'BH2':0, "set_B1":False, "set_B2":False, "timer": 10
}
for key in STB_info['ST_turtles']:
    if key not in ['STB1', 'STB2']:
        STB_info['ST_turtles'][key].penup()
        STB_info['ST_turtles'][key].color('turquoise')
        STB_info['ST_turtles'][key].shape('circle')
        STB_info['ST_turtles'][key].turtlesize(0.5, 0.5)
        STB_info['ST_turtles'][key].speed(0)

# Player movement and animation
#===================================================================
player_movements={'direction': 'down', 'direction_lock': True, 'up':False,'down':False,'left':False,'right':False,
                  'lock':True,'ani_ply':'down','ani_lcok':True,
                  'ani_count':20,'LPS':3,'RPS':3,'UPS':3,'DPS':3, 'move_timer':-5, 'move_lock':True}
# Track raw key states so releasing one key doesn't block movement if another
# movement key is still held.
player_keys = {'up': False, 'down': False, 'left': False, 'right': False}

def animate_player(turtle = player):
    if player_movements['direction'] == 'up':
        if player_movements['up']==True:
            if player_movements['move_timer']==-5:turtle.shape('PT_BL.gif')
            if player_movements['move_timer']==0:turtle.shape('PT_BS.gif')
            if player_movements['move_timer']==5:turtle.shape('PT_BR.gif')
        else:
            player.shape('PT_BS.gif')
            if turtle == player: player_movements['move_timer']=-5
    if player_movements['direction']== 'down':
        if player_movements['down']==True:
            if player_movements['move_timer']==-5:turtle.shape('PT_FL.gif')
            if player_movements['move_timer']==0:turtle.shape('PT_FS.gif')
            if player_movements['move_timer']==5:turtle.shape('PT_FR.gif')
        else:
            turtle.shape('PT_FS.gif')
            player_movements['move_timer']=-5
    if player_movements['direction']== 'left':
        if player_movements['left']==True:
            if player_movements['move_timer']==-5:turtle.shape('PT_LL.gif')
            if player_movements['move_timer']==0:turtle.shape('PT_LS.gif')
            if player_movements['move_timer']==5:turtle.shape('PT_LR.gif')
        else:
            player.shape('PT_LS.gif')
            player_movements['move_timer']=-5
  
    if player_movements['direction']=='right':
        if player_movements['right']==True:
            if player_movements['move_timer']==-5:turtle.shape('PT_RL.gif')
            if player_movements['move_timer']==0:turtle.shape('PT_RS.gif')
            if player_movements['move_timer']==5:turtle.shape('PT_RR.gif')
        else:
            player.shape('PT_RS.gif')
            player_movements['move_timer']=-5
    if turtle == player:
        if player_movements['move_lock']==True:
            if player_movements['move_timer']!=5:player_movements['move_timer']+=1
            else:player_movements['move_lock']=False
        if player_movements['move_lock']==False:
            if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
            else:player_movements['move_lock']=True
def press_up():
    player.setheading(90)
    player_movements['direction'] = 'up'
    player_movements['up']=True
def release_up(): player_movements['up'] = False
def press_down():
    player.setheading(270)
    player_movements['direction'] = 'down'
    player_movements['down']=True
def release_down(): player_movements['down'] = False
def press_left():
    player.setheading(180)
    player_movements['direction'] = 'left'
    player_movements['left']=True
def release_left(): player_movements['left'] = False
def press_right():
    player.setheading(0)
    player_movements['direction']='right'
    player_movements['right']=True
def release_right(): player_movements['right'] = False
def player_controls():
    if player_movements['direction'] == 'up' and player_movements['up'] == True: player.sety(player.ycor()+player_movements['UPS'])
    if player_movements['direction'] == 'down' and player_movements['down'] == True: player.sety(player.ycor()-player_movements['DPS'])
    if player_movements['direction'] == 'left' and player_movements['left'] == True: player.setx(player.xcor()-player_movements['LPS'])
    if player_movements['direction'] == 'right' and player_movements['right'] == True: player.setx(player.xcor()+player_movements['RPS'])

def player_animation(turtle = player):
    animate_player(turtle)

def player_funct():
    player_animation()
    player_controls()
    # if inventory_screen.isvisible(): player_animation(turtle = modle)


#===================================================================
def set_blast_direction(blaster ='none'):
    target = 'none'
    for  turtle in STB_info['enemys']:
        if blaster.distance(turtle) < 300:
            target = turtle
            break
    if target != 'none' and blaster.distance(target) < 300:
        target_pos = blaster.towards(target)
        lower_bound = 0
        upper_bound = 15
        for i in range(24):
            if lower_bound < target_pos <= upper_bound:
                blaster.setheading(lower_bound + 9)
                Blast_STBs(blaster)
                break
            else:
                lower_bound += 15
                upper_bound += 15
def track_mouse():
    x, y = screen._root.winfo_pointerx() - screen._root.winfo_rootx(), screen._root.winfo_pointery() - screen._root.winfo_rooty()
    x = screen.cv.canvasx(x)
    y = -screen.cv.canvasy(y)
    player.setheading(player.towards(x, y))
    STB_info['mouse']=player.heading()
    if player_movements['ani_ply'] in ['up', 'down']:
        if 0<STB_info['mouse']<=15  and player_movements['ani_ply']=='up':STB_info['BH1'], STB_info['BH2']=30,0 # Right
        elif 346<=STB_info['mouse']<360  and player_movements['ani_ply']=='up':STB_info['BH1'], STB_info['BH2']=345,0 # Right
        elif 0<STB_info['mouse']<=15  and player_movements['ani_ply']=='down':STB_info['BH1'], STB_info['BH2']=0,30 # Right
        elif 346<=STB_info['mouse']<360  and player_movements['ani_ply']=='down':STB_info['BH1'], STB_info['BH2']=0,345 # Right
        elif 16<=STB_info['mouse']<=45:STB_info['BH1'], STB_info['BH2']= 30,30 # Up/Right
        elif 46<=STB_info['mouse']<=75:STB_info['BH1'], STB_info['BH2']= 60,60 # Up/Right
        elif 76<=STB_info['mouse']<=105:STB_info['BH1'], STB_info['BH2']= 90,90 # Up
        elif 106<=STB_info['mouse']<=135:STB_info['BH1'], STB_info['BH2']= 120,120 # Up/Left
        elif 136<=STB_info['mouse']<=165:STB_info['BH1'], STB_info['BH2']= 150,150 # Up/Left
        elif 166<=STB_info['mouse']<180 and player_movements['ani_ply']=='up':STB_info['BH1'], STB_info['BH2']= 180,150 # Left
        elif 180<STB_info['mouse']<=195 and player_movements['ani_ply']=='up':STB_info['BH1'], STB_info['BH2']= 180,210 # Left
        elif 166<=STB_info['mouse']<180 and player_movements['ani_ply']=='down':STB_info['BH1'], STB_info['BH2']= 150,180 # Left
        elif 180<STB_info['mouse']<=195 and player_movements['ani_ply']=='down':STB_info['BH1'], STB_info['BH2']= 210,180 # Left
        elif 196<=STB_info['mouse']<=225:STB_info['BH1'], STB_info['BH2']= 210,210 # Down/Left
        elif 226<=STB_info['mouse']<=255:STB_info['BH1'], STB_info['BH2']= 240,240 # Down/Left
        elif 256<=STB_info['mouse']<=285:STB_info['BH1'], STB_info['BH2']= 270,270 # Down
        elif 286<=STB_info['mouse']<=315:STB_info['BH1'], STB_info['BH2']= 300,300 # Down/Right
        elif 316<=STB_info['mouse']<=345:STB_info['BH1'], STB_info['BH2']= 330,330 # Down/Right
    elif player_movements['ani_ply'] in ['left', 'right']:
        if STB_info['mouse']<=15 or 346<=STB_info['mouse']:STB_info['BH1'], STB_info['BH2']=0,0 # Right
        elif 16<=STB_info['mouse']<=45:STB_info['BH1'], STB_info['BH2']=30,30 # Up/Right
        elif 46<=STB_info['mouse']<=75:STB_info['BH1'], STB_info['BH2']=60,60 # Up/Right
        elif 76<=STB_info['mouse']<90 and player_movements['ani_ply']=='right':STB_info['BH1'], STB_info['BH2']=90,60 # Up
        elif 90<STB_info['mouse']<=105 and player_movements['ani_ply']=='right':STB_info['BH1'], STB_info['BH2']=90,120 # Up
        elif 76<=STB_info['mouse']<90 and player_movements['ani_ply']=='left':STB_info['BH1'], STB_info['BH2']=60,90 # Up
        elif 90<STB_info['mouse']<=105 and player_movements['ani_ply']=='left':STB_info['BH1'], STB_info['BH2']=120,90 # Up
        elif 106<=STB_info['mouse']<=135:STB_info['BH1'], STB_info['BH2']=120,120 # Up/Left
        elif 136<=STB_info['mouse']<=165:STB_info['BH1'], STB_info['BH2']=150,150 #up/left
        elif 166<=STB_info['mouse']<195:STB_info['BH1'], STB_info['BH2']=180,180 #left
        elif 196<=STB_info['mouse']<=225:STB_info['BH1'], STB_info['BH2']=210,210 #Down/left
        elif 226<=STB_info['mouse']<=255:STB_info['BH1'], STB_info['BH2']=240,240 #Down/left
        elif 256<=STB_info['mouse']<270 and player_movements['ani_ply']=='right':STB_info['BH1'], STB_info['BH2']=240,270 #Down
        elif 270<STB_info['mouse']<=285 and player_movements['ani_ply']=='right':STB_info['BH1'], STB_info['BH2']=300,270 #Down
        elif 256<=STB_info['mouse']<270 and player_movements['ani_ply']=='left':STB_info['BH1'], STB_info['BH2']=270,240 #Down
        elif 270<STB_info['mouse']<=285 and player_movements['ani_ply']=='left':STB_info['BH1'], STB_info['BH2']=270,300 #Down
        elif 286<=STB_info['mouse']<=315:STB_info['BH1'], STB_info['BH2']=300,300 #Down/right
        elif 316<=STB_info['mouse']<=345:STB_info['BH1'], STB_info['BH2']=330,330 #Down/right
def Blast_STBs(blaster):
    if STB_info['timer']>0:
        STB_info['timer']-=1
    else:
        if (blaster == STB1): set_STB1_range()  # Sets the range for the first magic blast
        if (blaster == STB2): set_STB2_range()  # Sets the range for the second magic blast
        STB_info['timer']=10
def set_STB1_range():    # Sets the direction and range for a magic blast, depending on which one is available
    if not STB_info['reloding_STB1']:
        if not STB_info['MB_locks']['MB1']:
            if not STB_info['MB_locks']['MB2']:
                if not STB_info['MB_locks']['MB3']:
                    if not STB_info['MB_locks']['MB4']:
                        if not STB_info['MB_locks']['MB5']:
                            none='none'
                        else:
                            STB_info['STB1']['MB5']['x'], STB_info['STB1']['MB5']['y']=STB1.xcor(), STB1.ycor()
                            GameT_5_A5.setheading(STB1.heading())
                            STB_info['MB_locks']['MB4']=False
                    else:
                        STB_info['STB1']['MB4']['x'], STB_info['STB1']['MB4']['y']=STB1.xcor(), STB1.ycor()
                        GameT_4_A4.setheading(STB1.heading())
                        STB_info['MB_locks']['MB4']=False
                else:
                    STB_info['STB1']['MB3']['x'], STB_info['STB1']['MB3']['y']=STB1.xcor(), STB1.ycor()
                    GameT_3_A3.setheading(STB1.heading())
                    STB_info['MB_locks']['MB3']=False
            else:
                STB_info['STB1']['MB2']['x'], STB_info['STB1']['MB2']['y']=STB1.xcor(), STB1.ycor()
                GameT_2_A2.setheading(STB1.heading())
                STB_info['MB_locks']['MB2']=False
        else: 
            STB_info['STB1']['MB1']['x'], STB_info['STB1']['MB1']['y']=STB1.xcor(), STB1.ycor()
            GameT_1_A1.setheading(STB1.heading())
            STB_info['MB_locks']['MB1']=False   
def set_STB2_range():
    if not STB_info['reloding_STB2']:
        if not STB_info['MB_locks']['MB6']:
            if not STB_info['MB_locks']['MB7']:
                if not STB_info['MB_locks']['MB8']:
                    if not STB_info['MB_locks']['MB9']:
                        if not STB_info['MB_locks']['MB10']:
                            none='none'
                        else:
                            STB_info['STB2']['MB10']['x'], STB_info['STB2']['MB10']['y']=STB2.xcor(), STB2.ycor()
                            GameT_10_A10.setheading(STB2.heading())
                            STB_info['MB_locks']['MB10']=False
                    else:
                        STB_info['STB2']['MB9']['x'], STB_info['STB2']['MB9']['y']=STB2.xcor(), STB2.ycor()
                        GameT_9_A9.setheading(STB2.heading())
                        STB_info['MB_locks']['MB9']=False
                else:
                    STB_info['STB2']['MB8']['x'], STB_info['STB2']['MB8']['y']=STB2.xcor(), STB2.ycor()
                    GameT_8_A8.setheading(STB2.heading())
                    STB_info['MB_locks']['MB8']=False
            else:
                STB_info['STB2']['MB7']['x'], STB_info['STB2']['MB7']['y']=STB2.xcor(), STB2.ycor()
                GameT_7_A7.setheading(STB2.heading())
                STB_info['MB_locks']['MB7']=False
        else:
            STB_info['STB2']['MB6']['x'], STB_info['STB2']['MB6']['y']=STB2.xcor(), STB2.ycor()
            GameT_6_A6.setheading(STB2.heading())
            STB_info['MB_locks']['MB6']=False



def ammo():
    for key in STB_info['ST_turtles']:
        if key in ['STB1', 'STB2']:
            Blast_STBs(key)
            set_blast_direction(STB_info['ST_turtles'][key])
            if (key=='STB1' and STB_info['set_B1']) or (key=='STB2' and STB_info['set_B2']):
                move_turtles(turtle=STB_info['ST_turtles'][key],turtle_type=key, speed=4)

        if key in ['MB1', 'MB2', 'MB3', 'MB4', 'MB5']:
            move_turtles(turtle=STB_info['ST_turtles'][key],
                         turtle_type=key,STB='STB1',speed=10,
                         x=STB_info['STB1'][key]['x'],
                         y=STB_info['STB1'][key]['y'],
                         )
        if key in ['MB6', 'MB7', 'MB8', 'MB9', 'MB10']:
            move_turtles(turtle=STB_info['ST_turtles'][key],
                         turtle_type=key,STB='STB2',speed=6,
                         x=STB_info['STB2'][key]['x'],
                         y=STB_info['STB2'][key]['y'],
                         )
def move_syntax_blasters():
    if player_movements['direction']== 'up':
        STB_info['Blaster_pos']['Current_pos']=STB_info['Blaster_pos']['up']
    if player_movements['direction']== 'down':
        STB_info['Blaster_pos']['Current_pos']=STB_info['Blaster_pos']['down']
    if player_movements['direction']== 'left':
        STB_info['Blaster_pos']['Current_pos']=STB_info['Blaster_pos']['left']
    if player_movements['direction']== 'right':
        STB_info['Blaster_pos']['Current_pos']=STB_info['Blaster_pos']['right']
    ammo()

def battle_collisions(turtle):
    for enemy in STB_info['enemys']:
        if turtle.distance(enemy) < 20:
            enemy.goto(200,200)

def move_turtles(turtle='none',turtle_type='none',STB='none',speed=1, x=0, y=0):
    if turtle_type in STB_info['ST_turtles'] and turtle_type not in ['STB1', 'STB2']:
        if STB_info['MB_locks'][turtle_type]==False:
            if turtle.distance(x, y) < 100:
                turtle.forward(speed)
            else:
                STB_info['MB_locks'][turtle_type]=True
                if turtle_type=='MB4':STB_info['reloding']=False
        else:turtle.goto(STB_info['ST_turtles'][STB].xcor(), STB_info['ST_turtles'][STB].ycor())
    elif turtle_type=='STB1':
        dx=(player.xcor()+STB_info['Blaster_pos']['Current_pos']['Lx'])-turtle.xcor()
        dy=(player.ycor()+STB_info['Blaster_pos']['Current_pos']['Ly'])-turtle.ycor()
        dist= (dx**2 + dy**2) ** 0.4 # Contols speed of alignment
        if dist<speed:
            turtle.goto(player.xcor()+STB_info['Blaster_pos']['Current_pos']['Lx'],player.ycor()+STB_info['Blaster_pos']['Current_pos']['Ly'])
        else:
            turtle.setx(turtle.xcor() + speed * dx / dist)
            turtle.sety(turtle.ycor() + speed * dy / dist)
    elif turtle_type=='STB2':
        dx=(player.xcor()+STB_info['Blaster_pos']['Current_pos']['Rx'])-turtle.xcor()
        dy=(player.ycor()+STB_info['Blaster_pos']['Current_pos']['Ry'])-turtle.ycor()
        dist= (dx**2 + dy**2) ** 0.4 # Contols speed of alignment
        if dist<speed:
            turtle.goto(player.xcor()+STB_info['Blaster_pos']['Current_pos']['Rx'],player.ycor()+STB_info['Blaster_pos']['Current_pos']['Ry'])
        else:
            turtle.setx(turtle.xcor() + speed * dx / dist)
            turtle.sety(turtle.ycor() + speed * dy / dist)

def set_blaster(blaster):
    if blaster == 'STB1':
        if not STB_info['set_B1']:
            STB_info["set_B1"]=True
        else:
            STB_info["set_B1"]=False
    if blaster == 'STB2':
        if not STB_info['set_B2']:
            STB_info["set_B2"]=True
        else:
            STB_info["set_B2"]=False

def STB1_onclick(x,y):
    set_blaster('STB1')
def STB2_onclick(x,y):
    set_blaster('STB2')


    

def move_game():
    move_syntax_blasters()
    player_funct()
    # track_mouse()
    for turtle in STB_info['enemys']:
        turtle.setheading(turtle.towards(player))
        turtle.forward(3)
        battle_collisions(turtle)
    screen.update()
    screen.ontimer(move_game, 16)  # Use 16ms for ~60fps, or 20 for 50fps

screen.listen()
screen.onkeypress(press_up, 'w')
screen.onkeyrelease(release_up, 'w')
screen.onkeypress(press_down, 's')
screen.onkeyrelease(release_down, 's')
screen.onkeypress(press_left, 'a')
screen.onkeyrelease(release_left, 'a')
screen.onkeypress(press_right, 'd')
screen.onkeyrelease(release_right, 'd')
# screen.onscreenclick(Blast_STBs)
butten1 .onclick(STB1_onclick)
butten2.onclick(STB2_onclick)
move_game()
screen.mainloop()