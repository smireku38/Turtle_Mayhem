import turtle
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
backround = turtle.Turtle()
entrance = turtle.Turtle()
backround.penup()
screen.register_shape('cover(1).gif')
backround.shape('cover(1).gif')
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color('green')
player.shape('turtle')
player.goto(0,0)
player2 = turtle.Turtle()
player2.speed(0)
player2.penup()
player3 = turtle.Turtle()
player3.speed(0)
player3.penup()
entrance.speed(0)
entrance.penup()
entrance.goto(100,200)
entrance.shape('square')
entrance.turtlesize(3,3)
entrance.color('blue')
entrance2 = turtle.Turtle()
entrance2.speed(0)
entrance2.penup()
entrance2.goto(150,200)
entrance2.shape('square')
entrance2.turtlesize(3,3)
entrance2.color('blue')


GameT_1_A1 = turtle.Turtle()
GameT_2_A2 = turtle.Turtle()
GameT_3_A3 = turtle.Turtle()
T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
GameT_1_A1.penup()
GameT_2_A2.penup()
GameT_2_A2.shape('square')
GameT_2_A2.color('red')

Game_charcters =  { 'turtles':{player, player2, player3},
                    'Chracters':{'Sam', 'bob', 'pam'},
                    
                    'current_turtle':backround, 'current_info':'backround',
                    'backround': {'direction': 'none','state':False,'ani_count':20, 'set_timer':False,
                           'up':False,'down':False,'left':False,'right':False,
                           'LPS':5,'RPS':5,'UPS':5,'DPS':5,
                           },
    
                    'Sam': {'direction': 'none','lock':False,'ani_count':20, 'set_timer':False,
                            "condtion":"none",'animation': "none",
                           'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                           'LPS':5,'RPS':5,'UPS':5,'DPS':5, 'move_timer':-4, 'move_lock':True,
                           'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                           'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                           'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                           'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                           },

                    'bob': {'direction': 'none',"condtion":"none",'animation': "none",'lock':True,'ani_count':20,
                            'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                           'LPS':5,'RPS':5,'UPS':5,'DPS':5, 'move_timer':-4, 'move_lock':True,
                           'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                           'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                           'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                           'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                           },

                    'pam': {'direction': 'none',"condtion":"none",'animation': "none",'lock':True,'ani_count':20,
                           'up':False,'down':False,'left':False,'right':False, 'Can_speak': False,
                            'LPS':5,'RPS':5,'UPS':5,'DPS':5, 'move_timer':-4, 'move_lock':True,
                            'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                            'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                            'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                            'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'}
                            }
                   
                  }
game_phases = {   'playing_story':False, 'current_Act': 'none', 'current_phase': 'none', 'current_scene': 'none', 'current_turtle': 'none',
                'Act1':{'phase1':{
                                'scene1':'inactive', 'scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive',},
                        'phase2':{
                               'scene1':'inactive', 'scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive',},
                        'phase3':{
                               'scene1':'inactive', 'scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive',}
                    }
            }
Game_dialogue = {    'current_scene':'none', 'current_name':'none',
                'Act1':{
                    'Phase1':{
                            'Scene1':{
                                'General': [],'Bob':[],'paper':[],'phone':[]},
                            'Scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive'},
                    'Phase2':{
                            'Scene1':'inactive', 'scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive'},
                    'Phase3':{
                            'Scene1':'inactive', 'scene2':'inactive', 'scene3':'inactive','scene4':'inactive','scene5':'inactive',}}
            }


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

# Text box definitions
#===================================================================
word_space = {'A':20,'B':20,'C':22,'D':20,'E':20,'F':20,'G':25,'H':22,'I':8,'J':18,'K':22,'L':19,'M':26,
              'N':23,'O':26,'P':23,'Q':26,'R':24,'S':21,'T':21,'U':25,'V':23,'W':34,'X':24,'Y':22,'Z':22,
              'a':18,'b':19,'c':18,'d':18,'e':18,'f':10,'g':18,'h':18,'i':8,'j':7,'k':17,'l':7,'m':26,
              'n':18,'o':18,'p':19,'q':18,'r':12,'s':18,'t':10,'u':19,'v':17,'w':24,'x':16,'y':16,'z':20,
              ' ':10,'.':10,',':10,'!':11,'?':20,'-':11, '(':10,')':10, ':':10, '\'':11,
              'Text_stm':False,'printing_text':'case1','textbox_on':False, 'currline':0, 'spam_lock':False,
              'Can_print':False}



#=========================================================================
Tbox = turtle.Turtle()
Tbox.color("white")
Tbox.speed(0)
currentmap = "None"
maze_cor = []
lobby_cor = []
currentbounds = lobby_cor
def proccesWallCOl(file_name, list_name):
    numfile =open(file_name)
    numfile = numfile.readlines()
    wall_values = []
    X_values = []
    Y_values = []
    str_num =""
    for num in numfile:
        for i in num:
            if i=='-':
                str_num = str_num + i
            elif i!=',':
                str_num = str_num + i
            if i==',':
                str_num = str_num.strip('\n')
                wall_values.append(int(str_num))
                str_num = ""
    for i in range(len(wall_values)):
        if i%2==0:
            X_values.append(wall_values[i])
    for i in range(len(wall_values)):
        if i%2==1:
            Y_values.append(wall_values[i])
    for j in range(len(X_values)):
        list_name.append((X_values[j], Y_values[j]))
def proccesmaps():
    global maze_cor, lobby_cor
    map_files = ["lobby_cor.txt", "maze_cor.txt"]
    map_list = [lobby_cor, maze_cor]
    for i in range(len(map_files)):
        file_name = map_files[i]
        list_name = map_list[i]
        proccesWallCOl(file_name, list_name)

def loadmap(next_map, boundslist):
    global currentbounds
    Tbox.clear()
    currentbounds=boundslist
    # DrawBoxes(boundslist)

def mazemap(new_x, new_y):
    global currentbounds,currentmap
    if 20 <= new_x <= 55 and 212 <= new_y <= 250:
        player.hideturtle()
        player.goto(-289,-281)
        currentmap = lobbymap
        loadmap('Cover.png', lobby_cor)
        player.showturtle()
        return True
    else:
        return False

def lobbymap(new_x, new_y):
    global currentmap, Playgame
    if Playgame == True:
        player.hideturtle()
        player.goto(39,193)
        currentmap = lobbymap
        loadmap('Cover.png', lobby_cor)
        player.showturtle()
        Playgame = False
        return True

    elif -316 <= new_x <= -269 and -303 <= new_y <= -281:
        player.hideturtle()
        player.goto(38,200)
        currentmap = mazemap
        loadmap("maze.png", maze_cor)
        player.showturtle()
        return True
    else:
        return False
def startgame(x,y):
    lobbymap(0,0)

def DrawBoxes(boundslist):
    for cor in range(0, len(boundslist), 2):
        Tbox.penup()
        Tbox.goto(boundslist[cor][0], boundslist[cor][1])
        Tbox.pendown()
        Tbox.goto(boundslist[cor][0], boundslist[cor+1][1])
        Tbox.goto(boundslist[cor+1][0], boundslist[cor+1][1])
        Tbox.goto(boundslist[cor+1][0], boundslist[cor][1])
        Tbox.goto(boundslist[cor][0], boundslist[cor][1])

def is_collisions(new_x, new_y):
    if len(currentbounds)>0:
        for cor in range(0, len(currentbounds), 2):
            # print (currentbounds[cor][0], currentbounds[cor+1][0], currentbounds[cor][1], currentbounds[cor+1][1])
            if backround.xcor()+currentbounds[cor][0] <= new_x <= backround.xcor()+currentbounds[cor+1][0] and backround.ycor()+currentbounds[cor][1] <= new_y <= backround.ycor()+currentbounds[cor+1][1]:
                return True
    if currentmap!='None':
        if currentmap(new_x, new_y):
            return True
    return False

def check_collisions(object = player, info = "none"):
    if Game_charcters[info]['direction'] == "up":
        if is_collisions(object.xcor(), object.ycor()+23):
            print("colided up")
            Game_charcters[info]['up'] = False
            if object == player: Game_charcters["backround"]['down'] = False
    elif Game_charcters[info]['direction'] == "down":
        if is_collisions(object.xcor(), object.ycor()-10):
            print("colided down")
            Game_charcters[info]['down'] = False
            if object == player: Game_charcters["backround"]['up'] = False
    elif Game_charcters[info]['direction'] == "left":
        if is_collisions(object.xcor()-20, object.ycor()):
            print("colided left")
            Game_charcters[info]['left'] = False
            if object == player: Game_charcters["backround"]['right'] = False
    elif Game_charcters[info]['direction'] == "right":
        if is_collisions(object.xcor()+20, object.ycor()):
            print("colided right")
            Game_charcters[info]['right'] = False
            if object == player: Game_charcters["backround"]['left'] = False

proccesmaps()
currentbounds = lobby_cor
print(currentbounds)
#=========================================================

def procces_dialouge(file, game_txt): #open file and make it useable
    d_file= open(file)
    d_text= d_file.readlines()
    current_act, current_phase, current_scene, current_object= 'none'
    box_text=[]
    set_text = False
    line = 0
    for i in range(0,len(d_text)):
        if d_text[i][0] == '\n': continue
        else: box_text.append(d_text[i].strip()) # make sure it is the chr we want, get rid of /n
    while  line < len(box_text):
        if box_text[line][0] in ['=', '+']:
            if box_text[line][0] == '+': set_text = not set_text
            line += 1
            continue

        if box_text[line][:len(box_text[line])-1] in ["Act", "Phase", "Scene"]:
            if box_text[line][:len(box_text[line])-1] == "Act": current_act = box_text[line]
            if box_text[line][:len(box_text[line])-1] == "Phase": current_phase = box_text[line]
            if box_text[line][:len(box_text[line])-1] == "Scene": current_scene = box_text[line]

        elif set_text == False:
            name = ""
            ch = 0
            while ch < len(box_text[line])-1 and box_text[line][ch] !=':':
                name += box_text[line][ch]
                ch+=1
            current_object = name

        else:
            game_txt[current_act][current_phase][current_scene][current_object].append(box_text[line])
        
        line+=1
    d_file.close()
def set_turtle(turtleName, shape='turtle', color='black', width= 0, length=0, outline=0, set_x=0, set_y=0):
    turtleName.shape(shape)
    turtleName.color(color)
    turtleName.penup()
    if turtleName == T_box: turtleName.turtlesize(length, width, outline)
    turtleName.hideturtle()
    if set_x != 0 or set_y != 0: turtleName.goto(set_x, set_y)
    turtleName.clear()
def set_textbox_turtles(text_size = 'none'):
    x, y= -390, -200 # where texts starts
    if word_space['currline'] == text_size:word_space['currline'] = 0
    set_turtle(line1, 'arrow', 'white', set_x=x, set_y=y)
    set_turtle(line2, 'arrow', 'white', set_x=x, set_y=y-40)
    set_turtle(line3, 'arrow', 'white', set_x=x, set_y=y-80)
    set_turtle(line4, 'arrow', 'white', set_x=x, set_y=y-120) 
    if word_space['textbox_on'] == False: set_turtle(T_box, 'square', 'black', length=10, width=40, outline=10, set_x=0, set_y=-250)
    word_space['textbox_on'] = True
    T_box.showturtle()      
def print_Text(dialoge):
    current_turtle = line1
    x, y= -390, -200 # where texts starts
    for i in dialoge:
        curr_index = 0
        current_turtle.goto(x,y)
        current_turtle.write(i, font =("Ariel", 25, "normal"))
        x+= word_space[i] # space between text
        if word_space['printing_text'] != 'case2': time.sleep(0.01) #time between letter

        if i ==' ':
            word_len = 0
            while dialoge[curr_index+word_len] not in ['.', ' ']: word_len += 1 #
            T_space = x
            for j in range(word_len): T_space += word_space[dialoge[j]]

            if T_space > 350: 
                x = -390 # start new line and continue
                y-=40 # New line
                if current_turtle == line1: current_turtle = line2
                elif current_turtle == line2: current_turtle = line3
                elif current_turtle == line3: current_turtle = line4
                elif current_turtle == line4: current_turtle = line1
        curr_index += 1
    word_space['printing_text'] = 'case3'         
def manage_printing(dialoge = 'none'):
    # if word_space['printing_text'] == 'case3':
    #     word_space['printing_text'] = 'case1'
    #     line1.clear()
    #     line2.clear()
    #     line3.clear()
    #     line4.clear()
    #     if word_space['currline'] < len(dialoge)-1:word_space['currline'] += 1

    if word_space['printing_text'] == 'case1':
        set_textbox_turtles()
        word_space['printing_text'] = 'case2'
        screen.tracer(1)
        print_Text(dialoge[word_space['currline']])
        screen.tracer(0)

    # elif word_space['printing_text'] == 'case2':
    #     word_space['spam_lock'] = False
    #     screen.tracer(0)
    #     print_Text(dialoge[word_space['currline']])
    #     if word_space['currline'] < len(dialoge)-2: word_space['printing_text'] = 'case3'
    #     else:word_space['printing_text'] = 'case4' # end of text
    #     word_space['spam_lock'] = True

    # if word_space['printing_text'] == 'case4':
    #     T_box.hideturtle()
    #     line1.clear()
    #     line2.clear()
    #     line3.clear()
    #     line4.clear()
    #     word_space['printing_text'] = 'case1'
    #     word_space['currline'] = 0
    #     word_space['textbox_on'] = False
    #     screen.update()
def manual_print(dialoge = 'none'):
    manage_printing(dialoge)
def auto_print(dialoge = 'none'):
    while word_space['currline'] < len(dialoge)-1:
        manage_printing(dialoge)
        time.sleep(1.5)
    word_space['printing_text'] = 'case4'
    manage_printing(dialoge)
procces_dialouge('Game_D.txt', Game_dialogue)
#====================================================================

# Player movement and animation
#===================================================================
# Track raw key states so releasing one key doesn't block movement if another
# movement key is still held.
def animate_player(turtle = player, info = 'Sam'):
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
        Game_charcters['backround']['direction'] = 'down'
        Game_charcters['backround']['down'] = True
        player.setheading(90)
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
        Game_charcters['backround']['down'] = False
def press_down():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'up'
        Game_charcters['backround']['up'] = True
        player.setheading(270)
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
        Game_charcters['backround']['up'] = False
def press_left():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'right'
        Game_charcters['backround']['right'] = True
        player.setheading(180)
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
        Game_charcters['backround']['right'] = False
def press_right():
    if not Game_charcters['Sam']['lock']:
        Game_charcters['backround']['direction'] = 'left'
        Game_charcters['backround']['left'] = True
        player.setheading(0)
        if not Game_charcters['Sam']['set_timer']:
            if Game_charcters['Sam']['direction'] == 'up':
                Game_charcters['Sam']['move_timer'] = -4
                Game_charcters['Sam']['move_lock'] = True
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
        Game_charcters['backround']['left'] = False
def map_range(info =  'none'):
    if Game_charcters[info]['direction'] == 'up':
        if backround.ycor() < 100:
            Game_charcters['backround']['state'] = True
        else:
            Game_charcters['backround']['up'] = False
            Game_charcters['backround']['state'] = False

    if Game_charcters[info]['direction'] == 'down' and Game_charcters[info]['down'] == True:
        if backround.ycor() > -100:
            Game_charcters['backround']['state'] = True
        else:
            Game_charcters['backround']['down'] = False
            Game_charcters['backround']['state'] = False
    if Game_charcters[info]['direction'] == 'left' and Game_charcters[info]['left'] == True:
        if backround.xcor() > -200:
            Game_charcters['backround']['state'] = True
        else:
            Game_charcters['backround']['left'] = False
            Game_charcters['backround']['state'] = False
    if Game_charcters[info]['direction'] == 'right':
        if backround.xcor() < 200:
            Game_charcters['backround']['state'] = True
        else:
            Game_charcters['backround']['right'] = False
            Game_charcters['backround']['state'] = False
def move_objects():
    if Game_charcters['backround']['state']:
        for turtle in Game_charcters['turtles']:
            if turtle != player:
                if Game_charcters['backround']['direction'] == 'up' and Game_charcters['backround']['up'] == True: turtle.sety(turtle.ycor()+Game_charcters['backround']['UPS'])
                if Game_charcters['backround']['direction'] == 'down' and Game_charcters['backround']['down'] == True: turtle.sety(turtle.ycor()-Game_charcters['backround']['DPS'])
                if Game_charcters['backround']['direction'] == 'left' and Game_charcters['backround']['left'] == True: turtle.setx(turtle.xcor()-Game_charcters['backround']['LPS'])
                if Game_charcters['backround']['direction'] == 'right' and Game_charcters['backround']['right'] == True: turtle.setx(turtle.xcor()+Game_charcters['backround']['RPS'])

def character_controls(turtle = 'none', info = 'Sam'):
    if (not Game_charcters['backround']['state'] and turtle != backround) or (Game_charcters['backround']['state'] and turtle != player):
        if Game_charcters[info]['direction'] == 'up' and Game_charcters[info]['up'] == True:turtle.sety(turtle.ycor()+Game_charcters[info]['UPS'])
        if Game_charcters[info]['direction'] == 'down' and Game_charcters[info]['down'] == True: turtle.sety(turtle.ycor()-Game_charcters[info]['DPS'])
        if Game_charcters[info]['direction'] == 'left' and Game_charcters[info]['left'] == True: turtle.setx(turtle.xcor()-Game_charcters[info]['LPS'])
        if Game_charcters[info]['direction'] == 'right' and Game_charcters[info]['right'] == True: turtle.setx(turtle.xcor()+Game_charcters[info]['RPS'])
def adjust_movement(info = 'none', direction = 'none', up = False, down = False, left = False, right = False):
    Game_charcters[info]['down'] = down
    Game_charcters[info]['up'] = up
    Game_charcters[info]['left'] = left
    Game_charcters[info]['right'] = right
    Game_charcters[info]['direction'] = direction
def character_funct(turtle = 'none', character = 'none'):
    # if game_phases['playing_story'] == False: 
    #     if turtle == backround: map_range(character)
    if turtle != backround: check_collisions(object = turtle, info = character)
    # if turtle != backround: animate_player(turtle = turtle, info = character)
    character_controls(turtle = turtle, info = character)
    # if inventory_screen.isvisible(): player_animation(turtle = modle)
def move_game():
    character_funct(turtle = player, character = 'Sam')
    character_funct(turtle = backround, character = 'backround')
    # move_objects()
    screen.update()
    screen.ontimer(move_game, 15)  # Use 16ms for ~60fps, or 20 for 50fps

screen.listen()
screen.onkeypress(press_up, 'w')
screen.onkeyrelease(release_up, 'w')
screen.onkeypress(press_down, 's')
screen.onkeyrelease(release_down, 's')
screen.onkeypress(press_left, 'a')
screen.onkeyrelease(release_left, 'a')
screen.onkeypress(press_right, 'd')
screen.onkeyrelease(release_right, 'd')
# if word_space['spam_lock'] == False: screen.onkey(start_T, 'e')
move_game()
screen.mainloop()