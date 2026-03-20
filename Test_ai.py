import turtle
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.tracer(0)
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color('green')
player.shape('turtle')
player_movements={'up':False,'down':False,'left':False,'right':False,
                  'lock':True,'ani_ply':'down','ani_lcok':True,
                  'ani_count':20,'flap_speed':5, 'move_timer':-5, 'move_lock':True}
settings={'Current_boss':'goto_KB','Kboss_lock':True,'Pboss_lock':True,'Tboss_lock':True,'next_phase':True,'setG':True,'tracer_val':0}

STB1 = turtle.Turtle()
STB2 = turtle.Turtle()
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
T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()

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
word_space = {'A':20,'B':20,'C':22,'D':20,'E':20,'F':20,'G':25,'H':22,'I':8,'J':18,'K':22,'L':19,'M':26,
              'N':23,'O':26,'P':23,'Q':26,'R':24,'S':21,'T':21,'U':25,'V':23,'W':34,'X':24,'Y':22,'Z':22,
              'a':18,'b':19,'c':18,'d':18,'e':18,'f':10,'g':18,'h':18,'i':8,'j':7,'k':17,'l':7,'m':26,
              'n':18,'o':18,'p':19,'q':18,'r':12,'s':18,'t':10,'u':19,'v':17,'w':24,'x':16,'y':16,'z':20,
              ' ':10,'.':10,',':10,'!':11,'?':20,'-':11, '(':10,')':10, ':':10, '\'':11,
              'Text_stm':False,'printing_text':'case1','textbox_on':False, 'currline':0, 'spam_lock':False}

# Player movement and animation
#===================================================================
def player_animation():
    if player_movements['ani_ply']=='up':
        if player_movements['up']==True:
            if player_movements['move_timer']==-5:player.shape('PT_BL.gif')
            if player_movements['move_timer']==0:player.shape('PT_BS.gif')
            if player_movements['move_timer']==5:player.shape('PT_BR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_BS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='down':
        if player_movements['down']==True:
            if player_movements['move_timer']==-5:player.shape('PT_FL.gif')
            if player_movements['move_timer']==0:player.shape('PT_FS.gif')
            if player_movements['move_timer']==5:player.shape('PT_FR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_FS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='left':
        if player_movements['left']==True:
            if player_movements['move_timer']==-5:player.shape('PT_LL.gif')
            if player_movements['move_timer']==0:player.shape('PT_LS.gif')
            if player_movements['move_timer']==5:player.shape('PT_LR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_LS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='right':
        if player_movements['right']==True:
            if player_movements['move_timer']==-5:player.shape('PT_RL.gif')
            if player_movements['move_timer']==0:player.shape('PT_RS.gif')
            if player_movements['move_timer']==5:player.shape('PT_RR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_RS.gif')
            player_movements['move_timer']=-5
def press_up(): 
    player_movements['up']=True
    player_movements['down']=False
    player_movements['left']=False
    player_movements['right']=False
def release_up(): player_movements['up']=False
def press_down():
    player_movements['up']=False
    player_movements['down']=True
    player_movements['left']=False
    player_movements['right']=False
def release_down(): player_movements['down']=False
def press_left():
    player_movements['up']=False
    player_movements['down']=False
    player_movements['left']=True
    player_movements['right']=False
def release_left(): player_movements['left']=False
def press_right():
    player_movements['up']=False
    player_movements['down']=False
    player_movements['left']=False
    player_movements['right']=True
def release_right(): player_movements['right']=False
def player_controls():
    if player_movements['up']==True:
        player.sety(player.ycor()+3)
        if player_movements['ani_ply']!='up':player_movements['ani_ply']='up'
    if player_movements['down']==True:
        player.sety(player.ycor()-3)
        if player_movements['ani_ply']!='down':player_movements['ani_ply']='down'
    if player_movements['left']==True:
        player.setx(player.xcor()-3)
        if player_movements['ani_ply']!='left':player_movements['ani_ply']='left'
    if player_movements['right']==True:
        player.setx(player.xcor()+3)
        if player_movements['ani_ply']!='right':player_movements['ani_ply']='right'

#===================================================================

# Text box definitions
#===================================================================

def procces_dialouge(dialouge_text): #open file and make it useable
    d_file= open(dialouge_text)
    d_text= d_file.readlines()
    box_text=[]
    for i in range(0,len(d_text)): box_text.append(d_text[i].strip()) # make sure it is the chr we want, get rid of /n
    d_file.close() 
    return box_text
def set_turtle(turtleName, shape='turtle', color='black', width= 0, length=0, outline=0, set_x=0, set_y=0):
    turtleName.shape(shape)
    turtleName.color(color)
    turtleName.penup()
    if turtleName == T_box: turtleName.turtlesize(length, width, outline)
    turtleName.hideturtle()
    if set_x != 0 or set_y != 0: turtleName.goto(set_x, set_y)
    turtleName.clear()
def set_textbox_turtles():
    x, y= -390, -200 # where texts starts
    if word_space['currline'] == len(game_txt):word_space['currline'] = 0
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
def start_T():
    if word_space['currline'] < len(game_txt)-1 :
        word_space['Text_stm'] = True
    if word_space['printing_text'] == 'case3':
        word_space['printing_text'] = 'case1'
        line1.clear()
        line2.clear()
        line3.clear()
        line4.clear()
        if word_space['currline'] < len(game_txt)-1:word_space['currline'] += 1
        else:word_space['printing_text'] = 'case4' # end of text

    if word_space['printing_text'] == 'case1':
        set_textbox_turtles()
        word_space['printing_text'] = 'case2'
        screen.tracer(1)
        print_Text(game_txt[word_space['currline']])
        screen.tracer(0)

    elif word_space['printing_text'] == 'case2':
        word_space['spam_lock'] = False
        screen.tracer(0)
        print_Text(game_txt[word_space['currline']])
        word_space['printing_text'] = 'case3'
        word_space['spam_lock'] = True

    elif word_space['printing_text'] == 'case4':
        T_box.hideturtle()
        line1.hideturtle()
        word_space['printing_text'] = 'case1'
        word_space['currline'] = 0
        word_space['textbox_on'] = False
        screen.update()
        word_space['Text_stm'] = False
        move_game()

game_txt = procces_dialouge('Game_D.txt')
#====================================================================

def move_game():
    if word_space['Text_stm'] == False: 
        player_animation()
        player_controls()
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
if word_space['spam_lock'] == False: screen.onkey(start_T, 'e')
move_game()
screen.mainloop()