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
backround = turtle.Turtle()

#GT(Game turtles)

game_turtles = [backround, player2_1, player3_1, player_1, player2_2, player3_2, player_2,
                T_box, line1, line2, line3, line4, GT_1_1, GT_2_1, GT_3_1, GT_1_2, GT_2_2, GT_3_2]
for turt in game_turtles:
    turt.speed(0)
    turt.penup()
    turt.shape('PT_FR.gif')
    turt.hideturtle()
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
word_space = {'A':20,'B':20,'C':22,'D':20,'E':20,'F':20,'G':25,'H':22,'I':8,'J':18,'K':22,'L':19,'M':26,
              'N':23,'O':26,'P':23,'Q':26,'R':24,'S':21,'T':21,'U':25,'V':23,'W':34,'X':24,'Y':22,'Z':22,
              'a':18,'b':19,'c':18,'d':18,'e':18,'f':10,'g':18,'h':18,'i':8,'j':7,'k':17,'l':7,'m':26,
              'n':18,'o':18,'p':19,'q':18,'r':12,'s':18,'t':10,'u':19,'v':17,'w':24,'x':16,'y':16,'z':20,
              ' ':10,'.':10,',':10,'!':11,'?':20,'-':11, '(':10,')':10, ':':10, '\'':11,
              'Text_stm':False,'printing_text':'case1','textbox_on':False, 'currline':0, 'manual_lock':False,
              'auto_lock':False,'Can_print':False, 'temp': ''}
def procces_dialouge(dialouge_text, game_txt): #open file and make it useable
    d_file= open(dialouge_text)
    d_text= d_file.readlines()
    current_act, current_phase, current_Scene, current_object = 'none'
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

        if box_text[line][:len(box_text[line])-1] in ['Act', 'Phase', 'Scene']:
            if box_text[line][:len(box_text[line])-1] == 'Act': current_act = box_text[line]
            if box_text[line][:len(box_text[line])-1] == 'Phase': current_phase = box_text[line]
            if box_text[line][:len(box_text[line])-1] == 'Scene': current_Scene = box_text[line]

        elif set_text == False:
            name = ''
            ch = 0
            while ch < len(box_text[line])-1 and box_text[line][ch] !=':':
                name += box_text[line][ch]
                ch+=1
            current_object = name

        else:
            game_txt[current_act][current_phase][current_Scene][current_object].append(box_text[line])
        
        line+=1
    d_file.close()
def print_Text(dialoge):
    current_turtle = line1
    x, y= -390, -200 # where texts starts
    for i in dialoge:
        curr_index = 0
        current_turtle.goto(x,y)
        current_turtle.write(i, font =('Ariel', 25, 'normal'))
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
def manage_printing(dialoge = 'none'):
    if word_space['printing_text'] == 'case3':
        line1.clear()
        line2.clear()
        line3.clear()
        line4.clear()
        
        if word_space['currline'] < len(dialoge)-1:
            word_space['printing_text'] = 'case1'
            word_space['currline'] += 1
        else:word_space['printing_text'] = 'case4' # end of text

    if word_space['printing_text'] == 'case1':
        set_textbox_turtles()
        word_space['printing_text'] = 'case2'
        screen.tracer(1)
        print_Text(dialoge[word_space['currline']])
        screen.tracer(0)
        word_space['printing_text'] = 'case3'

    elif word_space['printing_text'] == 'case2':
        word_space['manual_lock'] = False
        screen.tracer(0)
        print_Text(dialoge[word_space['currline']])
        word_space['printing_text'] = 'case3'
        word_space['manual_lock'] = True

    if word_space['printing_text'] == 'case4':
        T_box.hideturtle()
        line1.clear()
        line2.clear()
        line3.clear()
        line4.clear()
        word_space['printing_text'] = 'case1'
        word_space['currline'] = 0
        word_space['textbox_on'] = False
        if word_space['Can_print'] == True: Game_story['Re_MacGuffin'] = True
        screen.update()
def manual_print(text):
    if word_space['currline'] == 0 and word_space['printing_text'] == 'case1': Game_story['pause_Game'] = True # pauses game
    if word_space['manual_lock'] == False:
        manage_printing(text)
    if word_space['currline'] == 0 and word_space['printing_text'] == 'case1': # resume game
        Game_story['pause_Game'] = False
def auto_print(text):
    if word_space['auto_lock'] == False:
        if word_space['currline'] == 0 and word_space['printing_text'] == 'case1': Game_story['pause_Game'] = True # pauses the game
        word_space['auto_lock'] = True
        while word_space['currline'] < len(text)-1:
            manage_printing(text)
            time.sleep(1.5)
        manage_printing(text)
        if word_space['currline'] == 0 and word_space['printing_text'] == 'case1': # resume game
            Game_story['pause_Game'] = False
        word_space['auto_lock'] = False

def set_dialouges():
    for Enti in Game_dialogue[Game_dialogue['currAct']][Game_dialogue['currPhs']][Game_dialogue['currSce']]:
        Game_dialogue['Enti_W_Dio'][Enti] = Game_dialogue[Game_dialogue['currAct']][Game_dialogue['currPhs']][Game_dialogue['currSce']][Enti]
procces_dialouge('Game_D.txt', Game_dialogue)
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

def phase1():
    if Game_story['Act1']['phase1']['Scene1'] == 'inactive':
        if player_1.ycor() > 0:
            if Game_entities['Sam']['direction'] != 'down' and not Game_entities['Sam']['down']:
                player_1.goto(0,300)
                Game_story['playing_story'] = True
                Game_entities['Sam']['lock'] = True
                Game_entities['backround']['lock_Obj'] = True
                player_1.goto(0,300)
                player2_1.goto(50,340)
                player3_1.goto(-35,320)
                adjust_movement(entitie = 'Sam', direction = 'down', down = True)
                adjust_movement(entitie = 'Bob', direction = 'down', down = True)
                adjust_movement(entitie = 'Pam', direction = 'down', down = True)
                player_1.showturtle()
                player2_1.showturtle()
                player3_1.showturtle()
                backround.showturtle()
        else:
            Game_dialogue['currAct'] = 'Act1'
            Game_dialogue['currSce'] = 'Scene1'
            Game_dialogue['currPhs'] = 'Phase1'
            set_dialouges()
            Game_story['Act1']['phase1']['Scene1'] = 'pending'
            adjust_movement(entitie = 'Sam', direction = 'down')
            adjust_movement(entitie = 'Bob', direction = 'down')
            adjust_movement(entitie = 'Pam', direction = 'down')
            auto_print(Game_dialogue['Enti_W_Dio']['General'])
            return
    elif Game_story['Act1']['phase1']['Scene1'] == 'pending' and Game_story['Act1']['phase1']['Scene2'] == 'inactive':
        Game_story['Act1']['phase1']['Scene1'] = 'complete'
        adjust_movement(entitie = 'Sam', direction = 'down')
        return
    elif Game_story['Act1']['phase1']['Scene2'] == 'inactive':
        if player_1.ycor() < 400:
            if Game_entities['Sam']['direction'] != 'up' and not Game_entities['Sam']['up']:
                adjust_movement(entitie = 'Sam', direction = 'up', up = True)
                adjust_movement(entitie = 'Bob', direction = 'up', up = True)
                adjust_movement(entitie = 'Pam', direction = 'up', up = True)
        else:
            Game_story['Act1']['phase1']['Scene2'] = 'pending'
            return
    elif Game_story['Act1']['phase1']['Scene2'] == 'pending' and Game_story['Act1']['phase1']['Scene3'] == 'inactive':
        player_1.goto(0,-440)
        player2_1.goto(50,-400)
        player3_1.goto(-35,-420)
        Game_story['Act1']['phase1']['Scene2'] = 'complete'
        return
    elif Game_story['Act1']['phase1']['Scene3'] == 'inactive':
        if player_1.ycor() > -100:
            if Game_entities['Sam']['direction'] == 'up' and  Game_entities['Sam']['up']:
                adjust_movement(entitie = 'Sam')
                Game_entities['Sam']['lock'] = False
        if player2_1.ycor() > 200 and player2_1.xcor() <=100:
            if Game_entities['Bob']['direction'] == 'up' and  Game_entities['Bob']['up']:
                adjust_movement(entitie = 'Bob', direction = 'right', right = True)
        elif player2_1.xcor() > 100 and player2_1.isvisible():
            if Game_entities['Bob']['direction'] == 'right' and  Game_entities['Bob']['right']:
                adjust_movement(entitie = 'Bob', direction = 'right', right = False)
                player2_1.hideturtle()
        if player3_1.ycor() > 200 and player3_1.xcor() <= 100:
            if Game_entities['Pam']['direction'] == 'up' and  Game_entities['Pam']['up']:
                adjust_movement(entitie = 'Pam', direction = 'right', right = True)
                player2_1.hideturtle()
        elif player3_1.xcor() > 100 and player3_1.isvisible():
            if Game_entities['Pam']['direction'] == 'right' and  Game_entities['Pam']['right']:
                adjust_movement(entitie = 'Pam', direction = 'right', right = False)
                player3_1.hideturtle()
        if not player2_1.isvisible() and not player3_1.isvisible():
            Game_story['playing_story'] = False
            Game_entities['backround']['lock_Obj'] = False
            Game_story['Act1']['phase1']['Scene3'] = 'pending'
    elif Game_story['Act1']['phase1']['Scene3'] == 'pending':
        if player_1.distance(entrance) < 50:
            Game_story['Act1']['phase1']['Scene3'] = 'complete'
            return
    elif Game_story['Act1']['phase1']['Scene4'] == 'inactive':
        if Game_entities['Bob']['Can_speak'] == False:
            player2_1.goto(350,50)
            player3_1.goto(400,50)
            player2_1.showturtle()
            player3_1.showturtle()
            adjust_movement(entitie = 'Sam', direction = 'right')
            adjust_movement(entitie = 'Bob', direction = 'up')
            adjust_movement(entitie = 'Pam', direction = 'up')
            word_space['Can_print'] =  True
            Game_entities['Bob']['Can_speak'] = True
            Game_story['MacGuffin'] = 'Bob'
            Game_settings['HitBoxes_on'] = True
        if Game_story['MacGuffin'] == 'none':
            print('starting Scene 4')
            hideObjects(Game_entities['Bob'])
            hideObjects(Game_entities['Pam'])
            Game_story['Act1']['phase1']['Scene4'] = 'pending'
    elif Game_story['Act1']['phase1']['Scene4'] == 'pending':
        if GT_2_1.isvisible() == False:
            Game_story['MacGuffin'] = 'Computer'
            Game_entities['Computer']['turtle'].showturtle()
            Game_entities['Computer']['Can_speak'] = True
            Game_entities['Computer']['turtle'].goto(380,80)
        if Game_story['MacGuffin'] == 'none':
            player_1.goto(0,300)
            Game_entities['backround']['lock_Obj'] = True
            Game_story['Act1']['phase1']['Scene4'] = 'complete'
    elif Game_story['Act1']['phase1']['Scene5'] == 'inactive':
        if Game_settings['General_timer'] == -1:
            Game_settings['General_timer'] = 20
            GT_1_1.shape('circle')
            GT_1_2.shape('circle')
            GT_1_1.color('red')
            GT_1_2.color('yellow')
            GT_2_1.shape("Cover(1).gif")
            GT_2_2.shape("Cover(1).gif")
            GT_2_1.goto(0, 200)
            GT_2_2.goto(0,-400)
            GT_1_1.goto(0,400)
            GT_1_2.goto(0,-10)
            GT_1_1.shapesize(stretch_wid=5, stretch_len=10) # Temp line
            GT_1_2.shapesize(stretch_wid=2, stretch_len=10) # Temp line
            player_1.goto(0, 400)
            for turtle in [player_1, GT_1_1, GT_1_2, GT_2_1, GT_2_2] : turtle.showturtle()
        if Game_settings['General_timer'] > 0:
            for backdrop in [GT_2_1, GT_2_2]:
                if backdrop.ycor() <= 500:
                    backdrop.sety(backdrop.ycor()+40)
                else :
                    backdrop.sety(-500)
                    Game_settings['General_timer'] -= 1
                    print(Game_settings['General_timer'])
            if player_1.ycor() >= 0:
                player_1.sety(player_1.ycor()-5)
            else:
                GT_1_1.sety(GT_1_1.ycor()+2)
        elif (player_1.ycor() >= -300):
            player_1.showturtle()
            player_1.sety(player_1.ycor()-5)
            GT_2_1.hideturtle()
            GT_2_2.hideturtle()
            GT_1_2.sety(GT_1_2.ycor()-5)
        else:
            Game_story['Act1']['phase1']['Scene5'] = 'pending'
        

def object_hitbox(entitie1 = 'none', entitie2 = 'none'):
    object1, object2 = Game_entities[entitie1]['turtle'], Game_entities[entitie2]['turtle']
    speed = Game_entities[entitie2]['speed']
    if object1.distance(object2) <= 55 and (Game_entities[entitie1]['turtle'].isvisible() or Game_entities[entitie1]['turtle2'].isvisible()):
        key, direction = get_player_direction(object_type = 'turn', game_object1 = object1, game_object2 = object2)
        if (direction != "None" and (Game_settings['Talking_to'] == 'None' or object1 == Game_settings['Talking_to'])):
            Game_settings['Talking_to'] = object1
            priority(entitie1, entitie2)
            Game_entities[entitie1]['direction'] = direction
        if object1.distance(object2) <= 45:
            if Game_entities['backround']['switch'] == False:
                Game_entities[entitie2][key] = 0
            else:
                Game_entities['backround'][key] = 0
        else:
            if Game_entities['backround']['switch'] == False:Game_entities[entitie2][key] = speed
            else: Game_entities['backround'][key] = speed
        for dir in ['LPS','DPS', 'RPS', 'UPS']:
                if Game_entities[entitie2][dir] == 0 and dir != key:
                    Game_entities[entitie2][dir] = speed
            
    elif object1.distance(object2) > 55 and object1 == Game_settings['Talking_to']:
        Game_settings['Talking_to'] = 'None'
    else:
        if Game_entities[entitie1]['direction'] != Game_entities[entitie1]['default_direction']:
            adjust_movement(entitie = entitie1, direction = Game_entities[entitie1]['default_direction'])
            if 0 in [Game_entities[entitie2]['LPS'], Game_entities[entitie2]['DPS'], Game_entities[entitie2]['RPS'], Game_entities[entitie2]['UPS']]:
                for dir in ['LPS','DPS', 'RPS', 'UPS']:
                    Game_entities[entitie2][dir] = speed

def get_player_direction(object_type = 'none', game_object1 = 'none', game_object2 = 'none'):
    angel = game_object1.towards(game_object2)
    if 315 < angel <= 360 or 0 <= angel <= 45:
        return 'LPS', 'right'
    elif 45 < angel <= 135:
        return 'DPS', 'up'
    elif 135 < angel <= 225:
        return 'RPS', 'left'
    elif 225 < angel <= 315:
        return 'UPS', 'down'
    return 'None', 'None'
def priority(turtle1, turtle2):
    obj1_1, obj1_2, obj2_1 = Game_entities[turtle1]['turtle'], Game_entities[turtle1]['turtle2'], Game_entities[turtle2]['turtle'] 
    if obj1_1.shape() != obj1_2.shape(): obj1_2.shape(obj1_1.shape())
    if obj1_1.xcor() != obj1_2.xcor() or obj1_1.ycor() != obj1_2.ycor(): obj1_2.goto(obj1_1.xcor(), obj1_1.ycor())
    if player_1.ycor() <= obj1_1.ycor():
        if obj1_2.isvisible():
            obj1_1.showturtle()
            obj1_2.hideturtle()
    elif player_1.ycor() > obj1_1.ycor():
        if obj1_1.isvisible():
            obj1_1.hideturtle()
            obj1_2.showturtle()
def find_interactable_object():
    if word_space['Can_print'] == True:
        for character in Game_entities['characters']:
            print('Checking:', character)
            if Game_entities[character]['Can_speak']:
                if player_1.distance(Game_entities[character]['turtle']) < 50:
                    return character
    return 'none'
def interactable_objects():
    Name = find_interactable_object()
    if Name != 'none' and (Game_entities[Name]['turtle'].isvisible() or Game_entities[Name]['turtle2'].isvisible()):
        if Game_entities[Name]['print_type'] == 'auto':
            auto_print(Game_dialogue['Enti_W_Dio'][Name])
        elif Game_entities[Name]['print_type'] == 'manual':
            manual_print(Game_dialogue['Enti_W_Dio'][Name])
            word_space['manual_lock'] = False
            print(Game_story['MacGuffin'], ' ',Name, Game_story['Re_MacGuffin'])
        if Game_story['MacGuffin'] == Name and Game_story['Re_MacGuffin'] == True:
            Game_story['MacGuffin'] = 'none'
            Game_story['Re_MacGuffin'] = False
        if Game_story['pause_Game'] == False: move_game()
def characters():
    if Game_settings['HitBoxes_on']:
        for character in Game_entities['characters']:
            if character != 'Sam':
                object_hitbox(entitie1 = character, entitie2 = 'Sam')
        for character in Game_entities['objects']:
            object_hitbox(entitie1 = character, entitie2 = 'Sam')
    
    character_funct(turtle = backround, character = 'backround')
    character_funct(turtle = player_1, character = 'Sam')
    character_funct(turtle = player2_1, character = 'Bob')
    character_funct(turtle = player3_1, character = 'Pam')
#===================================================================

def move_game():
    if Game_story['pause_Game'] == False:
        phase1()
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
screen.onkey(interactable_objects, 'space')
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