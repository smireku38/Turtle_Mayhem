import turtle
screen=turtle.Screen()
screen.tracer(0)
GameT_1_M=turtle.Turtle()
GameT_2_M=turtle.Turtle()
GameT_3_M=turtle.Turtle() 
GameT_4_M=turtle.Turtle()
player=turtle.Turtle()
#Blue Python Body
GameT_5_PHB=turtle.Turtle() #Player's health bar
GameT_6_BHB=turtle.Turtle()
GameT_9_BB1_ST3=turtle.Turtle()
GameT_10_BB2_ST4=turtle.Turtle()
GameT_11_K2_BB3_ST5=turtle.Turtle()
GameT_12_K3_BB4_ST6=turtle.Turtle()
GameT_13_K4_BB5_ST7=turtle.Turtle()
GameT_14_BB6_ST8=turtle.Turtle()
GameT_15_BB7_BT1=turtle.Turtle()
GameT_16_BB8_BT2=turtle.Turtle()
GameT_17_BB9_KT1=turtle.Turtle()
GameT_18_BB10_KT2=turtle.Turtle()
GameT_19_BB11_KT3=turtle.Turtle() 
GameT_20_BB12_KT4=turtle.Turtle()
GameT_21_BB13_KC=turtle.Turtle()
GameT_22_BB14_W1=turtle.Turtle()
GameT_23_BB15_W2=turtle.Turtle()
GameT_24_BB16_CB1=turtle.Turtle()
GameT_25_BB17_CB2=turtle.Turtle()
GameT_26_BB18=turtle.Turtle()
GameT_27_BB19=turtle.Turtle()
GameT_28_BB20=turtle.Turtle()
GameT_29_BB21=turtle.Turtle()
GameT_30_BB22=turtle.Turtle()
GameT_31_BB23=turtle.Turtle()
GameT_32_BB24=turtle.Turtle()
GameT_33_BB25=turtle.Turtle()
GameT_34_BB26=turtle.Turtle()
GameT_35_BB27=turtle.Turtle()
GameT_36_BB28=turtle.Turtle()
GameT_37_BB29=turtle.Turtle()
GameT_38_BB30=turtle.Turtle()
GameT_39_BB31=turtle.Turtle()
GameT_40_BB32=turtle.Turtle()
GameT_41_BB33=turtle.Turtle()
GameT_42_BB34=turtle.Turtle()
GameT_43_BB35=turtle.Turtle()
GameT_44_BB36=turtle.Turtle()
GameT_45_BB37=turtle.Turtle()
GameT_46_BB38=turtle.Turtle()
GameT_47_BB39=turtle.Turtle()
GameT_48_BB40=turtle.Turtle()
python_body1=[GameT_9_BB1_ST3,GameT_10_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_BB6_ST8,
GameT_15_BB7_BT1,GameT_16_BB8_BT2,GameT_17_BB9_KT1,GameT_18_BB10_KT2,GameT_19_BB11_KT3,GameT_20_BB12_KT4,
GameT_21_BB13_KC,GameT_22_BB14_W1,GameT_23_BB15_W2,GameT_24_BB16_CB1,GameT_25_BB17_CB2,GameT_26_BB18,GameT_27_BB19,
GameT_28_BB20,GameT_29_BB21,GameT_30_BB22,GameT_31_BB23,GameT_32_BB24,GameT_33_BB25,GameT_34_BB26,GameT_35_BB27,
GameT_36_BB28,GameT_37_BB29,GameT_38_BB30,GameT_39_BB31,GameT_40_BB32,GameT_41_BB33,GameT_42_BB34,GameT_43_BB35,
GameT_44_BB36,GameT_45_BB37,GameT_46_BB38,GameT_47_BB39,GameT_48_BB40]
#Yellow Python Body
GameT_8_YB1_ST2=turtle.Turtle()
GameT_49_YB2=turtle.Turtle()
GameT_50_YB3=turtle.Turtle()
GameT_51_YB4=turtle.Turtle()
GameT_52_YB5=turtle.Turtle()
GameT_53_YB6=turtle.Turtle()
GameT_54_YB7=turtle.Turtle()
GameT_55_YB8=turtle.Turtle()
GameT_56_YB9=turtle.Turtle()
GameT_57_YB10=turtle.Turtle()
GameT_58_YB11=turtle.Turtle() 
GameT_59_YB12=turtle.Turtle()
GameT_60_YB13=turtle.Turtle()
GameT_61_YB14=turtle.Turtle() 
GameT_62_YB15=turtle.Turtle()
GameT_63_YB16=turtle.Turtle()
GameT_64_YB17=turtle.Turtle()
GameT_65_YB18=turtle.Turtle()
GameT_66_YB19=turtle.Turtle()
GameT_67_YB20=turtle.Turtle()
GameT_68_YB21=turtle.Turtle() 
GameT_69_YB22=turtle.Turtle()
GameT_70_YB23=turtle.Turtle()
GameT_71_YB24=turtle.Turtle()
GameT_72_YB25=turtle.Turtle()
GameT_73_YB26=turtle.Turtle()
GameT_74_YB27=turtle.Turtle()
GameT_75_YB28=turtle.Turtle()
GameT_76_YB29=turtle.Turtle()
GameT_77_YB30=turtle.Turtle()
GameT_78_YB31=turtle.Turtle()
GameT_79_YB32=turtle.Turtle()
GameT_80_YB33=turtle.Turtle()
GameT_81_YB34=turtle.Turtle()
GameT_82_YB35=turtle.Turtle()
GameT_83_YB36=turtle.Turtle()
GameT_84_YB37=turtle.Turtle()
GameT_85_YB38=turtle.Turtle()
GameT_86_YB39=turtle.Turtle()
GameT_87_YB40=turtle.Turtle()
MB_locks={'MB1':True,'MB2':True,'MB3':True,'MB4':True}
python_body2=[GameT_8_YB1_ST2,GameT_49_YB2,GameT_50_YB3,GameT_51_YB4,GameT_52_YB5,GameT_53_YB6,GameT_54_YB7,
GameT_55_YB8,GameT_56_YB9,GameT_57_YB10,GameT_58_YB11,GameT_59_YB12,GameT_60_YB13,GameT_61_YB14,GameT_62_YB15,
GameT_63_YB16,GameT_64_YB17,GameT_65_YB18,GameT_66_YB19,GameT_67_YB20,GameT_68_YB21,GameT_69_YB22,GameT_70_YB23,
GameT_71_YB24,GameT_72_YB25,GameT_73_YB26,GameT_74_YB27,GameT_75_YB28,GameT_76_YB29,GameT_77_YB30,GameT_78_YB31,
GameT_79_YB32,GameT_80_YB33,GameT_81_YB34,GameT_82_YB35,GameT_83_YB36,GameT_84_YB37,GameT_85_YB38,GameT_86_YB39,GameT_87_YB40]
player.penup()
player.color('green')
player.shape('turtle')
#Sets a turtle's shape,color,speed and initial position
def set_turtles(turtle="none", shape='circle',color='black',setx=0,sety=0):
    turtle.penup()
    turtle.speed(0)
    turtle.shape(shape)
    turtle.color(color)
    if turtle==GameT_5_PHB:
        turtle.goto(-setx,sety)
        turtle.turtlesize(25,3,10)
    if turtle==GameT_8_YB1_ST2:
        turtle.goto(player.xcor(),-2300)
    if turtle==GameT_9_BB1_ST3:
        turtle.goto(-2300,sety)

states={'Player_Health':25}

python_info={'set_python':True,'set_path1':True,'set_path_i1':0,'set_path2':True,'b1_go':True,'b2_go':True,'wait1':True,'wait2':True,'move_left_right1':True,'move_left_right2':True,
'set_path_i2':0,'count1':0,'count2':0,'BPBC':GameT_9_BB1_ST3.xcor()+1,'py1s':[],'py2s':[],
'python_vals1':[(800,player.ycor(),'green'),1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39],
'python_vals2':[(player.xcor(),450,'red'),1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]}
#This chechks if a snake is colliding with player, if so reduce the player's health
#and updates the bar size
def Collisions(turtle='none', damage_lock='none',range_x=0,range_y=0,damage=0):
    if (turtle in python_body1) or (turtle in python_body2):
        if turtle!=GameT_9_BB1_ST3 and GameT_8_YB1_ST2:
            if turtle.xcor()-range_x<=player.xcor()<=turtle.xcor()+range_x and turtle.ycor()-range_y<player.ycor()<turtle.ycor()+range_y:
                if states['Player_Health']>0:
                    states['Player_Health']-=damage
                    GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
def move_turtles(turtle="none",setx=0,sety=0,index=0,time_stop=0): # Controls movement logic for both python heads and all body parts (zigzag and path-following)
    if turtle ==GameT_9_BB1_ST3:#Moves Blue pytho head
        if python_info['b1_go']:set_val=turtle.xcor()+1
        elif not python_info['b1_go']:set_val=turtle.xcor()-1
        if python_info['move_left_right1']:
            python_info['wait1']=True
            if python_info['move_left_right1']:
                if python_info['set_path1']:
                    turtle.goto(set_val,turtle.ycor()+1)
                    python_info['py1s'].append((turtle.xcor(),turtle.ycor()))
                    python_info['set_path_i1']+=1
                    if python_info['set_path_i1']==50:python_info['set_path1']=False
                elif not python_info['set_path1']:
                    turtle.goto(set_val,turtle.ycor()-1)
                    python_info['set_path_i1']-=1
                    python_info['py1s'].append((turtle.xcor(),turtle.ycor()))
                    if python_info['set_path_i1']==-50:python_info['set_path1']=True
                if python_info['b1_go'] and turtle.xcor()>=setx:   #Swith direction when reaching screen limits
                    python_info['b1_go']=False
                    python_info['wait1']=False
                    turtle.sety(player.ycor())
                if not python_info['b1_go'] and turtle.xcor()<=-setx:
                    python_info['b1_go']=True
                    python_info['wait1']=False
                    turtle.sety(player.ycor())
    if turtle == GameT_8_YB1_ST2: #Moves Yellow pytho head
        if python_info['b2_go']==True:set_val=turtle.ycor()+1
        elif python_info['b2_go']==False:set_val=turtle.ycor()-1
        if python_info['move_left_right2']==True:     #Zig-zag movement while going up and down
            python_info['wait2']=True
            if python_info['move_left_right2']==True:
                if python_info['set_path2']==True:
                    turtle.goto(turtle.xcor()+1,set_val)
                    python_info['py2s'].append((turtle.xcor(),turtle.ycor()))
                    python_info['set_path_i2']+=1
                    if python_info['set_path_i2']==50:python_info['set_path2']=False
                elif python_info['set_path2']==False:
                    turtle.goto(turtle.xcor()-1,set_val)
                    python_info['set_path_i2']-=1
                    python_info['py2s'].append((turtle.xcor(),turtle.ycor()))
                    if python_info['set_path_i2']==-50:python_info['set_path2']=True 
                if python_info['b2_go']==True and turtle.ycor()>=sety:  #Swith direction when reaching vertical boundaries
                    python_info['b2_go']=False
                    python_info['wait2']=False
                    turtle.setx(player.xcor())
                if python_info['b2_go']==False and turtle.ycor()<=-sety:
                    python_info['b2_go']=True
                    python_info['wait2']=False
                    turtle.setx(player.xcor())
    if len(python_info['py1s'])>=1540: # Makes blue python bomdy follow the head
        if turtle in python_body1 and turtle!=GameT_9_BB1_ST3 and python_info['count1']>=time_stop:
            if index < len(python_info['py1s']):
                turtle.goto(python_info['py1s'][index][0],python_info['py1s'][index][1])
                Collisions(turtle=turtle,range_x=10,range_y=10,damage=1)
                if turtle==GameT_48_BB40 and python_info['wait1']==True:del python_info['py1s'][0]
            else:python_info['count1']+=1   #This cleans up the old path data if this 
        else:python_info['count1']+=1       #is the last body part
    if len(python_info['py2s'])>=1540:# Makes yellow python bomdy follow the head
        if turtle in python_body2 and turtle!=GameT_8_YB1_ST2 and python_info['count2']>=time_stop:
            if index < len(python_info['py2s']):
                turtle.goto(python_info['py2s'][index][0],python_info['py2s'][index][1])
                Collisions(turtle=turtle,range_x=10,range_y=10,damage=1)
                if turtle==GameT_87_YB40 and python_info['wait2']==True:del python_info['py2s'][0]
            else:python_info['count2']+=1
        else:python_info['count2']+=1
def python_ctrl():    # Sets up and moves both python snakes: blue and yellow
    global lock_turtles
    if python_info['set_python']:
        set_turtles(turtle=GameT_5_PHB,shape='square',color='green',setx=600)
        B1=0
        B2=0
        Y1=0
        Y2=0
        for i in range(len(python_body1)):
            if i==0:set_turtles(turtle=python_body1[i],color=python_info['python_vals1'][i][2])
            else:set_turtles(turtle=python_body1[i])
        for i in range(1,len(python_info['python_vals1'])):
            python_info['python_vals1'][i]=(B1,B2)
            python_info['python_vals2'][i]=(Y1,Y2)
            B1+=40
            B2+=30
            Y1+=40
            Y2+=30
        for i in range(len(python_body2)):
            if i==0:set_turtles(turtle=python_body2[i],color=python_info['python_vals2'][i][2],setx=python_info['python_vals2'][i][0],sety=python_info['python_vals2'][i][1])
            else:set_turtles(turtle=python_body2[i],color='yellow')
        python_info['set_python']=False
    for i in range(len(python_body1)): #Moves both pythons
        if python_body1[i]==GameT_9_BB1_ST3:move_turtles(turtle=python_body1[i],setx=python_info['python_vals1'][i][0],sety=python_info['python_vals1'][i][1])
        if python_body1[i] in python_body1 and python_body1[i]!=GameT_9_BB1_ST3:move_turtles(turtle=python_body1[i],index=python_info['python_vals1'][i][0],time_stop=python_info['python_vals1'][i][1])
        if python_body2[i]==GameT_8_YB1_ST2:move_turtles(turtle = python_body2[i],setx=python_info['python_vals2'][i][0],sety=python_info['python_vals2'][i][1])
        if python_body2[i] in python_body2 and python_body2[i]!=GameT_8_YB1_ST2:move_turtles(turtle=python_body2[i],index=python_info['python_vals2'][i][0],time_stop=python_info['python_vals2'][i][1])

#__________________________________________________________________________________________________________________#
player_movements={'up':False,'down':False,'left':False,'right':False}
MB_range={'MB1':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},'MB2':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},
'MB3':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},'MB4':{'min_x':0,'min_y':0,'max_x':0,'max_y':0}}

def press_up(): player_movements['up']=True
def release_up(): player_movements['up']=False
def press_down(): player_movements['down']=True
def release_down(): player_movements['down']=False
def press_left(): player_movements['left']=True
def release_left(): player_movements['left']=False
def press_right(): player_movements['right']=True
def release_right(): player_movements['right']=False

def set_magic_range(x,y):    # Sets the direction and range for a magic blast, depending on which one is available
    if not MB_locks['MB1']: #If a Magic Blast is already fired then the next one goes
        if not MB_locks['MB2']:
            if not MB_locks['MB3']:
                if not MB_locks['MB4']:
                    none='none'
                else:
                    MB_range['MB4']['min_x']=player.xcor()-500
                    MB_range['MB4']['max_x']=player.xcor()+500
                    MB_range['MB4']['min_y']=player.ycor()-500
                    MB_range['MB4']['max_y']=player.ycor()+500
                    angel=GameT_4_M.towards(x,y)
                    GameT_4_M.setheading(angel)
                    MB_locks['MB4']=False
            else:
                MB_range['MB3']['min_x']=player.xcor()-500
                MB_range['MB3']['max_x']=player.xcor()+500
                MB_range['MB3']['min_y']=player.ycor()-500
                MB_range['MB3']['max_y']=player.ycor()+500
                angel=GameT_3_M.towards(x,y)
                GameT_3_M.setheading(angel)
                MB_locks['MB3']=False
        else:
            MB_range['MB2']['min_x']=player.xcor()-500
            MB_range['MB2']['max_x']=player.xcor()+500
            MB_range['MB2']['min_y']=player.ycor()-500
            MB_range['MB2']['max_y']=player.ycor()+500
            angel=GameT_2_M.towards(x,y)
            GameT_2_M.setheading(angel)
            MB_locks['MB2']=False    
    else:
        MB_range['MB1']['min_x']=player.xcor()-200
        MB_range['MB1']['max_x']=player.xcor()+200
        MB_range['MB1']['min_y']=player.ycor()-200
        MB_range['MB1']['max_y']=player.ycor()+200
        angel=GameT_1_M.towards(x,y)
        GameT_1_M.setheading(angel)
        MB_locks['MB1']=False   

def move_game():
    python_ctrl()
    if player_movements['up']==True:
        player.sety(player.ycor()+5)
    if player_movements['down']==True:
        player.sety(player.ycor()-5)
    if player_movements['left']==True:
        player.setx(player.xcor()-5)
    if player_movements['right']==True:
        player.setx(player.xcor()+5)
    screen.update()
    screen.ontimer(move_game, 5)

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