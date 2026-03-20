
import turtle
import time
import random

#---- Screen Setup ----
screen=turtle.Screen()
screen.bgcolor('black')
screen.bgpic('tut_bg.gif')
screen.tracer(0)
# ---- Game Turtles ----
#General Names:
#A-Arrows, PHB-Player health Bar, BHB Boss Health BarTURTLE

#Karel Boss fight names:
#KK-
#Python Boss fight names:
#Turtle Boss fight names:
#ST-Soldeir Turtle, BT-Bomb Traker, KC-King Cush ,KT-Turtle Knight, CB-bomb, W-Wave
GameT_1_M=turtle.Turtle()
GameT_2_M=turtle.Turtle()
GameT_3_M=turtle.Turtle() 
GameT_4_M=turtle.Turtle()
player=turtle.Turtle()
GameT_5_PHB=turtle.Turtle()
GameT_6_BHB=turtle.Turtle()
T_box=turtle.Turtle()
GameT_7_ST1_Dl=turtle.Turtle()
GameT_10_K1_BB2_ST4=turtle.Turtle()
GameT_11_K2_BB3_ST5=turtle.Turtle()
GameT_12_K3_BB4_ST6=turtle.Turtle()
GameT_13_K4_BB5_ST7=turtle.Turtle()
GameT_14_K5_BB6_ST8=turtle.Turtle()
GameT_15_K6_BB7_BT1=turtle.Turtle()
GameT_16_K7_BB8_BT2=turtle.Turtle()
GameT_17_K8_BB9_KT1=turtle.Turtle()
GameT_18_K9_BB10_KT2=turtle.Turtle()
GameT_19_K10_BB11_KT3=turtle.Turtle()
GameT_20_K11_BB12_KT4=turtle.Turtle()
GameT_21_K12_BB13_KC=turtle.Turtle()
GameT_22_K13_BB14_W1=turtle.Turtle()
GameT_23_K14_BB15_W2=turtle.Turtle() 
GameT_24_K15_BB16_CB1=turtle.Turtle()
GameT_25_K16_BB17_CB2=turtle.Turtle()
GameT_26_K17_BB18=turtle.Turtle()
GameT_27_K18_BB19=turtle.Turtle()
GameT_28_K19_BB20=turtle.Turtle()
GameT_29_K20_BB21=turtle.Turtle()
GameT_30_K21_BB22=turtle.Turtle()
GameT_31_K22_BB23=turtle.Turtle()
GameT_32_K23_BB24=turtle.Turtle()
GameT_33_K24_BB25=turtle.Turtle()
GameT_34_K25_BB26=turtle.Turtle()
GameT_35_K26_BB27=turtle.Turtle()
GameT_36_K27_BB28=turtle.Turtle()
GameT_37_K28_BB29=turtle.Turtle()
GameT_38_K29_BB30=turtle.Turtle()
GameT_39_K30_BB31=turtle.Turtle()
GameT_40_BB32=turtle.Turtle()
GameT_41_BB33=turtle.Turtle()
GameT_42_BB34=turtle.Turtle()
GameT_43_BB35=turtle.Turtle()
GameT_44_BB36=turtle.Turtle()
GameT_45_BB37=turtle.Turtle()
GameT_46_BB38=turtle.Turtle()
GameT_47_BB39=turtle.Turtle()
GameT_48_BB40=turtle.Turtle()
GameT_9_KW_BB1_ST3=turtle.Turtle()
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
GameT_8_KK_YB1_ST2=turtle.Turtle()
Every_turtle=[GameT_1_M,GameT_2_M,GameT_3_M,GameT_4_M,GameT_5_PHB,GameT_6_BHB,GameT_7_ST1_Dl,GameT_22_K13_BB14_W1,
GameT_9_KW_BB1_ST3,GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8,
GameT_15_K6_BB7_BT1,GameT_16_K7_BB8_BT2,GameT_17_K8_BB9_KT1,GameT_18_K9_BB10_KT2,GameT_19_K10_BB11_KT3,GameT_20_K11_BB12_KT4,
GameT_21_K12_BB13_KC,GameT_22_K13_BB14_W1,GameT_23_K14_BB15_W2,GameT_24_K15_BB16_CB1,GameT_25_K16_BB17_CB2,GameT_26_K17_BB18,GameT_27_K18_BB19,
GameT_28_K19_BB20,GameT_29_K20_BB21,GameT_30_K21_BB22,GameT_32_K23_BB24,GameT_33_K24_BB25,GameT_34_K25_BB26,GameT_35_K26_BB27,
GameT_35_K26_BB27,GameT_37_K28_BB29,GameT_38_K29_BB30,GameT_39_K30_BB31,GameT_40_BB32,GameT_41_BB33,GameT_42_BB34,GameT_43_BB35,
GameT_44_BB36,GameT_45_BB37,GameT_46_BB38,GameT_47_BB39,GameT_48_BB40,GameT_49_YB2,GameT_50_YB3,GameT_51_YB4,GameT_52_YB5,GameT_53_YB6,GameT_54_YB7,
GameT_55_YB8,GameT_56_YB9,GameT_57_YB10,GameT_58_YB11,GameT_59_YB12,GameT_60_YB13,GameT_61_YB14,GameT_62_YB15,
GameT_63_YB16,GameT_64_YB17,GameT_65_YB18,GameT_66_YB19,GameT_67_YB20,GameT_68_YB21,GameT_69_YB22,GameT_70_YB23,
GameT_71_YB24,GameT_72_YB25,GameT_73_YB26,GameT_74_YB27,GameT_75_YB28,GameT_76_YB29,GameT_77_YB30,GameT_78_YB31,
GameT_79_YB32,GameT_80_YB33,GameT_81_YB34,GameT_82_YB35,GameT_83_YB36,GameT_84_YB37,GameT_85_YB38,GameT_86_YB39,GameT_87_YB40]

#---- General Game info -----
settings={'Current_boss':'goto_KB','Kboss_lock':True,'Pboss_lock':True,'Tboss_lock':True,'next_phase':True,'setG':True,'tracer_val':0}
Each_boss=['goto_KB','goto_PB','goto_TB']
player_bod={'current_bod':'karel_bod','karel_bod':(450,100,250),'python_bod':(500,350,250),'turtle_bod':(500,300,500)}
states={'Player_Health':25,'Boss_Health':30}
player_movements={'up':False,'down':False,'left':False,'right':False,'lock':True,'ani_ply':'down','ani_lcok':True,'ani_count':5} #player movement locks
general_turltes=[player,GameT_5_PHB,GameT_6_BHB,GameT_1_M,GameT_2_M,GameT_3_M,GameT_4_M]
generalT_info=[(0,0,'turtle','lime'),(-600,0,'square','lime'),(0,-300,'square','red'),
    (player.xcor(),player.ycor(),'circle','orange','MB1'),(player.xcor(),player.ycor(),'circle','orange','MB2'), # magic blasts 1-2
    (player.xcor(),player.ycor(),'circle','orange','MB3'),(player.xcor(),player.ycor(),'circle','orange','MB4')] # magic blasts 3-4
screen.register_shape('Kiki_UL.gif')
screen.register_shape('Kiki_DL.gif')
screen.register_shape('Kiki_UR.gif')
screen.register_shape('Kiki_DR.gif')
screen.register_shape('Big_Karel.gif')
screen.register_shape('Karel_soldier.gif')
screen.register_shape('weak_Karel.gif')
screen.register_shape('Pythonhead_yel1.gif')
screen.register_shape('Pythonhead_yel2.gif')
screen.register_shape('Pythonbod_yel.gif')
screen.register_shape('Pythonhead_blu1.gif')
screen.register_shape('Pythonhead_blu2.gif')
screen.register_shape('Pythonbod_blu.gif')
screen.register_shape('King_Crush.gif')
screen.register_shape('Wave1.gif')
screen.register_shape('Wave2.gif')
screen.register_shape('Coco_bomb.gif')
screen.register_shape('POPBOMB.gif')
screen.register_shape('weak_Karel.gif')

#---- Magic Info ----
Magic_Blasts=[GameT_1_M,GameT_2_M,GameT_3_M,GameT_4_M]
MB_locks={'MB1':True,'MB2':True,'MB3':True,'MB4':True}
MB_range={'MB1':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},'MB2':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},
'MB3':{'min_x':0,'min_y':0,'max_x':0,'max_y':0},'MB4':{'min_x':0,'min_y':0,'max_x':0,'max_y':0}}
#----KArel Boss fight inofrmation ----
Karel_info={'Start_karel_game':False,'Change_speed':False,'count':0,'set_karels':True,
    'KW_sp':4,'K1_sp':4,'K2_sp':4,'K3_sp':4,'K4_sp':4,'K5_sp':4,'K6_sp':4,'K7_sp':4,'K8_sp':4,'K9_sp':4,'K10_sp':4,
    'K11_sp':4,'K12_sp':4,'K13_sp':4,'K14_sp':4,'K15_sp':4,'K16_sp':4,'K17_sp':4,'K18_sp':4,'K19_sp':4,'K20_sp':4,
    'Karel_pos':[(-450,110),(-400,120),(-350,130),(-300,140),(-250,130),(-200,140),(-150,130),(-100,120),(-50,110),(0,100),
    (50,110),(100,120),(150,130),(200,140),(250,150),(300,140),(350,130),(400,120),(450,110)]}
Karel_army=[GameT_8_KK_YB1_ST2,GameT_9_KW_BB1_ST3,
GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8,
GameT_15_K6_BB7_BT1,GameT_16_K7_BB8_BT2,GameT_17_K8_BB9_KT1,GameT_18_K9_BB10_KT2,GameT_19_K10_BB11_KT3,
GameT_20_K11_BB12_KT4,GameT_21_K12_BB13_KC,GameT_22_K13_BB14_W1,GameT_23_K14_BB15_W2,GameT_24_K15_BB16_CB1,GameT_25_K16_BB17_CB2,
GameT_26_K17_BB18,GameT_27_K18_BB19,GameT_28_K19_BB20,GameT_29_K20_BB21]

#---- Python Boss fight inofrmation---- 
python_info={'Start_python_game':False,'set_python':True,'set_path1':True,'set_path_i1':0,'set_path2':True,'b1_go':True,'b2_go':True,'wait1':True,'wait2':True,'move_left_right1':True,'move_left_right2':True,
'set_path_i2':0,'count1':0,'count2':0,'BPBC':GameT_9_KW_BB1_ST3.xcor()+1,'py1s':[],'py2s':[],
'python_vals1':[(800,player.ycor(),'green'),1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39],
'python_vals2':[(player.xcor(),450,'red'),1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]}
python_body1=[GameT_9_KW_BB1_ST3,GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8,
GameT_15_K6_BB7_BT1,GameT_16_K7_BB8_BT2,GameT_17_K8_BB9_KT1,GameT_18_K9_BB10_KT2,GameT_19_K10_BB11_KT3,GameT_20_K11_BB12_KT4,
GameT_21_K12_BB13_KC,GameT_22_K13_BB14_W1,GameT_23_K14_BB15_W2,GameT_24_K15_BB16_CB1,GameT_25_K16_BB17_CB2,GameT_26_K17_BB18,GameT_27_K18_BB19,
GameT_28_K19_BB20,GameT_29_K20_BB21,GameT_31_K22_BB23,GameT_30_K21_BB22,GameT_32_K23_BB24,GameT_33_K24_BB25,GameT_34_K25_BB26,GameT_35_K26_BB27,
GameT_35_K26_BB27,GameT_37_K28_BB29,GameT_38_K29_BB30,GameT_39_K30_BB31,GameT_40_BB32,GameT_41_BB33,GameT_42_BB34,GameT_43_BB35,
GameT_44_BB36,GameT_45_BB37,GameT_46_BB38,GameT_47_BB39,GameT_48_BB40]
python_body2=[GameT_8_KK_YB1_ST2,GameT_49_YB2,GameT_50_YB3,GameT_51_YB4,GameT_52_YB5,GameT_53_YB6,GameT_54_YB7,
GameT_55_YB8,GameT_56_YB9,GameT_57_YB10,GameT_58_YB11,GameT_59_YB12,GameT_60_YB13,GameT_61_YB14,GameT_62_YB15,
GameT_63_YB16,GameT_64_YB17,GameT_65_YB18,GameT_66_YB19,GameT_67_YB20,GameT_68_YB21,GameT_69_YB22,GameT_70_YB23,
GameT_71_YB24,GameT_72_YB25,GameT_73_YB26,GameT_74_YB27,GameT_75_YB28,GameT_76_YB29,GameT_77_YB30,GameT_78_YB31,
GameT_79_YB32,GameT_80_YB33,GameT_81_YB34,GameT_82_YB35,GameT_83_YB36,GameT_84_YB37,GameT_85_YB38,GameT_86_YB39,GameT_87_YB40]
#---- Turtle BOSS Fight inofrmation ----
TBOSS_locks={'Start_turlte_game':False, #locks for Turtle Boss fight
'Set_game_turtles':True,'set_set':True,'set_tim_1':True,'set_tim_2':True,'set_tim_3':True,'Wave1_lock':True,'Wave2_lock':True,'KC_tim_lock':True,
'lock_bombs':True,'lock_bomb2':False,'Bomb1_lock':True,'Bomb2_lock':True,'Setbomb1':True,'Setbomb2':True,'only_TB':False}
T_game_NS={'KC_timer':300,
'TS_nums':{'num_of_sol':'2','sol_speed':'1'},'TK_nums':'2','Bomb_nums':'3', 'Wave_nums':'1', 'KC_nums':'1',
'KC_vals':{'speed':{'1':400,'2':300,'3':200}},
'Turtle_knights_vals':{'numbers':{'2':2,'4':1}},
'Turtle_soldier_vals':{'numbers':{'2':4,'4':2,'8':1},'speed':{'1':2,'2':3,'3':5}},
'Bomb_vals':{'speed':{'1':2,'2':3,'3':4}},
'Wave1':{'speed':{'1':2,'2':5,'3':3}}, 'Wave2':{'speed':{'1':2,'2':3,'3':5}}}
bomb_info={'Start_bombing_in':1200,'Send_bomb1_in':200,'Send_bomb2_in':200,'Next_bomb_in':600,'Coconut_max_y1':0,'Coconut_max_y2':0}
OG_KC_pos=[(-200,200),(0,200),(200,200),(200,0),(200,-200),(-200,0),(-200,0),(-200,-200),(-200,0)]
KC_pos=OG_KC_pos
ST_pos=[(-420,-230),(420,230),(-470,-170),(470,170),(-420,230),(420,-230),(-470,170),(470,-170)]
Turtle_army=[GameT_22_K13_BB14_W1,GameT_23_K14_BB15_W2, #Waves
GameT_21_K12_BB13_KC,GameT_17_K8_BB9_KT1,GameT_18_K9_BB10_KT2,GameT_19_K10_BB11_KT3,GameT_20_K11_BB12_KT4, #King Cruh and his Knight Turtles
GameT_7_ST1_Dl,GameT_8_KK_YB1_ST2,GameT_9_KW_BB1_ST3,GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8, # Soldier Turtles
GameT_15_K6_BB7_BT1,GameT_24_K15_BB16_CB1,GameT_16_K7_BB8_BT2,GameT_25_K16_BB17_CB2] #Bombs and Trakers
Turtle_soldiers=[GameT_7_ST1_Dl,GameT_8_KK_YB1_ST2,GameT_9_KW_BB1_ST3,GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8]
Turtle_soldiers=[GameT_7_ST1_Dl,GameT_8_KK_YB1_ST2,GameT_9_KW_BB1_ST3,GameT_10_K1_BB2_ST4,GameT_11_K2_BB3_ST5,GameT_12_K3_BB4_ST6,GameT_13_K4_BB5_ST7,GameT_14_K5_BB6_ST8]
Turtle_knights=[GameT_17_K8_BB9_KT1,GameT_18_K9_BB10_KT2,GameT_19_K10_BB11_KT3,GameT_20_K11_BB12_KT4]
GameT_15_K6_BB7_BT1
#---- Game Proccessors ----
def set_turtles(shape='none',turtle='none',set_x=0,set_y=0,color='none'):
    if shape!='none':
            turtle.shape(shape)
    if color!='none':
        turtle.color(color)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(set_x,set_y)
    if turtle==GameT_5_PHB:
        turtle.turtlesize(states['Player_Health'],3,10) #Sets player health bar
    if turtle==GameT_6_BHB:
        turtle.turtlesize(3,states['Boss_Health'],10)   #Sets Boss health bar
    if TBOSS_locks['Start_turlte_game']:
        if turtle==GameT_22_K13_BB14_W1:
            turtle.turtlesize(10,3,10)
        if turtle==GameT_23_K14_BB15_W2:
            turtle.turtlesize(3,10,10)
        if turtle in Turtle_knights:
            turtle.turtlesize(10,10,10)
        if turtle in [GameT_15_K6_BB7_BT1,GameT_16_K7_BB8_BT2]:
            turtle.turtlesize(5,10,10)
            turtle.hideturtle()
        if turtle in [GameT_24_K15_BB16_CB1,GameT_25_K16_BB17_CB2]:
            turtle.turtlesize(2,2,10)
            turtle.hideturtle()
    if python_info['Start_python_game']:
        if turtle==GameT_8_KK_YB1_ST2:
            turtle.goto(player.xcor(),-2300)
        if turtle==GameT_9_KW_BB1_ST3:
            turtle.goto(-2300,set_y)
    if Karel_info['Start_karel_game']:
        turtle.showturtle()
def set_general_turtles():
    for i in range(len(general_turltes)):
        if general_turltes[i]!=player:
            general_turltes[i].hideturtle()
        set_turtles(turtle=general_turltes[i],shape=generalT_info[i][2],color=generalT_info[i][3],set_x=generalT_info[i][0],set_y=generalT_info[i][1])
def tracer():
    if settings['tracer_val']==0:
        settings['tracer_val']=1
        screen.tracer(settings['tracer_val'])
    else:
        settings['tracer_val']=0
        screen.tracer(settings['tracer_val'])
def Lock_blasts(turtle='none'):
    if turtle==GameT_1_M:MB_locks['MB1']=True
    if turtle==GameT_2_M:MB_locks['MB2']=True
    if turtle==GameT_3_M:MB_locks['MB3']=True
    if turtle==GameT_4_M:MB_locks['MB4']=True
def procces_dialouge(dialouge_text): #open file and make it useable
    d_text= open(dialouge_text)
    d_text= d_text.readlines()
    box_text=[]
    for i in range(0,len(d_text)): # make sure it is the chr we want, get rid of /n
        box_text.append(d_text[i].strip()) 
    return box_text
def boss_dialouge(text='none',index='none'): #reveal text letter by letter(index by index)
    GameT_17_K8_BB9_KT1.color('white')
    GameT_17_K8_BB9_KT1.penup()
    T_box.penup()
    T_box.shape('square')
    T_box.color('black')
    T_box.setheading(0)
    T_box.turtlesize(10,40,10)
    T_box.goto(0,-250)
    x= -390 # where texts starts
    y=-200
    GameT_17_K8_BB9_KT1.goto(x,y)
    tracer()
    for i in text:
        if GameT_17_K8_BB9_KT1.xcor()<400:
            GameT_17_K8_BB9_KT1.write(i, font =("Ariel", 25, "normal"))
            x+=15 # space between text
            GameT_17_K8_BB9_KT1.goto(x,y)
            time.sleep(0.1) #time between letter
        else:
            x=-390 # start new line and continue
            y-=40
            GameT_17_K8_BB9_KT1.goto(x,y)
            GameT_17_K8_BB9_KT1.write(i, font =("Ariel", 25, "normal"))
    time.sleep(1)
    GameT_17_K8_BB9_KT1.clear()
    if Karel_info['Start_karel_game'] and text:
        for karel in Karel_army:
            if karel!=GameT_8_KK_YB1_ST2:
                karel.hideturtle()
def karel_dialoge(dialogue):
    player_movements['lock']=False
    text=procces_dialouge('1.Karel_dialoge.txt')
    T_box.showturtle()
    if dialogue=='KBdio1':
        for i in text[0:2]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    if dialogue=='KBdio2':
        for i in text[2:]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    T_box.hideturtle()
    player_movements['lock']=True
def turtle_dialoge(dialogue):
    player_movements['lock']=False
    text=procces_dialouge('3.Turtle_boss_dialoge.txt')
    T_box.showturtle()
    for turtle in Turtle_army:
        turtle.hideturtle()
    set_turtles(turtle=GameT_21_K12_BB13_KC,shape='square',color='yellow',set_y=200)
    if dialogue=='TBdio1':
        for i in text[0:2]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    if dialogue=='TBdio2':
        for i in text[2:]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    T_box.hideturtle()
    player_movements['lock']=True
def python_dialoge(dialogue):
    player_movements['lock']=False
    text=procces_dialouge('2.Pytohn_dialoge.txt')
    for turtle in Turtle_army:
        turtle.hideturtle()
    T_box.showturtle()
    if dialogue=='PBdio1':
        for i in text[0:3]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    if dialogue=='PBdio2':
        for i in text[3:]:
            boss_dialouge(text=i,index=text.index(i))
            tracer()
    player_movements['lock']=True
    T_box.hideturtle()
#---- Game Collisions ----
def Collisions(turtle='none', damage_lock='none',range_x=0,range_y=0,damage=0):
    if TBOSS_locks['Start_turlte_game']: #sets colisions for Turtle Boss fight
        if turtle in Turtle_army:
            if turtle!=GameT_21_K12_BB13_KC:
                if turtle.xcor()-range_x<=player.xcor()<=turtle.xcor()+range_x and turtle.ycor()-range_y<=player.ycor()<=turtle.ycor()+range_y:
                    if states['Player_Health']>0:
                        states['Player_Health']-=damage
                        GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
                        if turtle in [GameT_22_K13_BB14_W1,GameT_23_K14_BB15_W2]:
                            TBOSS_locks[damage_lock]=False
                        if turtle in Turtle_army:
                            return True
                    else:settings['Current_boss']='Game over'
    if python_info['Start_python_game']:
        if (turtle in python_body1) or (turtle in python_body2):
            if turtle!=GameT_9_KW_BB1_ST3 and GameT_8_KK_YB1_ST2:
                if turtle.xcor()-range_x<=player.xcor()<=turtle.xcor()+range_x and turtle.ycor()-range_y<player.ycor()<turtle.ycor()+range_y:
                    if states['Player_Health']>0:
                        states['Player_Health']-=damage
                        GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
                    else:settings['Current_boss']='Game over'
    if Karel_info['Start_karel_game']:
        if turtle.xcor()-range_x<=player.xcor()<=turtle.xcor()+range_x and turtle.ycor()-range_y<player.ycor()<turtle.ycor()+range_y:
            if states['Player_Health']>0:
                states['Player_Health']-=damage
                GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
            else:settings['Current_boss']='Game over'
    if states['Player_Health']<=0:
        settings['Current_boss']='Game_over'
#---- Game Movements----
def move_turtles(turtle='none',x_val=0,y_val=0, feild_val=0,max_val=0,return_val='none',MB_lock='none',min_x=0,min_y=0,max_x=0,max_y=0,bomb_timer='none',bomb='none',bomb_lock='none',index=0,time_stop=0,K_sp=1):
    global KC_pos
    if turtle in Magic_Blasts:
        if player_movements['lock']:
            if MB_locks[MB_lock]==True:
                turtle.hideturtle()
                turtle.goto(player.xcor(),player.ycor())
            else:
                turtle.showturtle()
                if min_x<turtle.xcor()<max_x and min_y<turtle.ycor()<max_y:
                    turtle.forward(8)
                else:
                    Lock_blasts(turtle)
                    #colisions for Arrows
                if Karel_info['Start_karel_game']:
                    for i in range(len(Karel_army)):
                        if Karel_army[i].xcor()-15<=turtle.xcor()<=Karel_army[i].xcor()+15 and Karel_army[i].ycor()-15<=turtle.ycor()<=Karel_army[i].ycor()+15:
                            if Karel_army[i]==GameT_9_KW_BB1_ST3:
                                states['Boss_Health']-=0.2
                                if states['Boss_Health']>0:
                                    GameT_6_BHB.turtlesize(3,states['Boss_Health'],10)
                            else:
                                Lock_blasts(turtle)
                if python_info['Start_python_game']:
                    for i in range(len(python_body1)):
                        if (((python_body1[i].xcor()-16<=turtle.xcor()<=python_body1[i].xcor()+16 and python_body1[i].ycor()-16<=turtle.ycor()<=python_body1[i].ycor()+16) or
                        (python_body2[i].xcor()-15<=turtle.xcor()<=python_body2[i].xcor()+16 and python_body2[i].ycor()-16<=turtle.ycor()<=python_body2[i].ycor()+16))):
                            if python_body1[i]==GameT_9_KW_BB1_ST3 or python_body2[i]==GameT_8_KK_YB1_ST2:
                                states['Boss_Health']-=1
                                if states['Boss_Health']>0:
                                    GameT_6_BHB.turtlesize(3,states['Boss_Health'],10)
                                    Lock_blasts(turtle)
                            else:
                                Lock_blasts(turtle)
                if TBOSS_locks['Start_turlte_game']: #sets colisions for Turtle Boss fight
                    if GameT_21_K12_BB13_KC.xcor()-15<=turtle.xcor()<=GameT_21_K12_BB13_KC.xcor()+15 and GameT_21_K12_BB13_KC.ycor()-15<=turtle.ycor()<=GameT_21_K12_BB13_KC.ycor()+15:
                        states['Boss_Health']-=1
                        if states['Boss_Health']>0:
                            GameT_6_BHB.turtlesize(3,states['Boss_Health'],10)
                        Lock_blasts(turtle)
                    if GameT_22_K13_BB14_W1.xcor()-40<=turtle.xcor()<=GameT_22_K13_BB14_W1.xcor()+40 and GameT_22_K13_BB14_W1.ycor()-100<=turtle.ycor()<=GameT_22_K13_BB14_W1.ycor()+100:
                        Lock_blasts(turtle)
                    if GameT_23_K14_BB15_W2.xcor()-100<=turtle.xcor()<=GameT_23_K14_BB15_W2.xcor()+40 and GameT_23_K14_BB15_W2.ycor()-40<=turtle.ycor()<=GameT_23_K14_BB15_W2.ycor()+40:
                        Lock_blasts(turtle)
                    for i in range(len(Turtle_soldiers)):
                        if Turtle_soldiers[i].xcor()-15<=turtle.xcor()<=Turtle_soldiers[i].xcor()+15 and Turtle_soldiers[i].ycor()-15<=turtle.ycor()<=Turtle_soldiers[i].ycor()+15:
                            Lock_blasts(turtle)
                            Turtle_soldiers[i].goto(ST_pos[i][0],ST_pos[i][1])
    if Karel_info['Start_karel_game']:
        if turtle in Karel_army and turtle!=GameT_8_KK_YB1_ST2:
            if turtle.ycor()>-300:
                turtle.showturtle()
                turtle.sety(turtle.ycor()-Karel_info[K_sp])
                Collisions(turtle=turtle,range_x=15,range_y=15,damage=0.05)
            else:
                if Karel_info['Change_speed']:
                    speeds=[4,4.7,5]
                    rand_sp=random.choice(speeds)
                    Karel_info[K_sp]=rand_sp
                rand_loc=random.choice(Karel_info['Karel_pos'])
                turtle.goto(rand_loc[0],rand_loc[1])
    if python_info['Start_python_game']:
        if turtle ==GameT_9_KW_BB1_ST3:#Moves Blue pytho head
            turtle.showturtle()
            if python_info['b1_go']:
                turtle.shape('Pythonhead_yel1.gif')
                set_val=turtle.xcor()+1
            elif not python_info['b1_go']:
                turtle.shape('Pythonhead_yel2.gif')
                set_val=turtle.xcor()-1
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
                    if python_info['b1_go'] and turtle.xcor()>=x_val:
                        python_info['b1_go']=False
                        python_info['wait1']=False
                        turtle.sety(player.ycor())
                    if not python_info['b1_go'] and turtle.xcor()<=-x_val:
                        python_info['b1_go']=True
                        python_info['wait1']=False
                        turtle.sety(player.ycor())
        if turtle == GameT_8_KK_YB1_ST2: #Moves Yellow pytho head
            turtle.showturtle()
            if python_info['b2_go']==True:
                turtle.shape('Pythonhead_blu1.gif')
                set_val=turtle.ycor()+1
            elif python_info['b2_go']==False:
                turtle.shape('Pythonhead_blu2.gif')
                set_val=turtle.ycor()-1
            if python_info['move_left_right2']==True:
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
                    if python_info['b2_go']==True and turtle.ycor()>=y_val:
                        python_info['b2_go']=False
                        python_info['wait2']=False
                        turtle.setx(player.xcor())
                    if python_info['b2_go']==False and turtle.ycor()<=-y_val:
                        python_info['b2_go']=True
                        python_info['wait2']=False
                        turtle.setx(player.xcor())
        if len(python_info['py1s'])>=1540: # Makes blue python bomdy follow the head
            if turtle in python_body1 and turtle!=GameT_9_KW_BB1_ST3 and python_info['count1']>=time_stop:
                if index < len(python_info['py1s']):
                    turtle.goto(python_info['py1s'][index][0],python_info['py1s'][index][1])
                    turtle.showturtle()
                    Collisions(turtle=turtle,range_x=10,range_y=10,damage=2)
                    if turtle==GameT_48_BB40 and python_info['wait1']==True:del python_info['py1s'][0]
                else:python_info['count1']+=1
            else:python_info['count1']+=1
        elif turtle not in [GameT_9_KW_BB1_ST3,GameT_8_KK_YB1_ST2]:turtle.hideturtle()
        if len(python_info['py2s'])>=1540:# Makes yellow python bomdy follow the head
            if turtle in python_body2 and turtle!=GameT_8_KK_YB1_ST2 and python_info['count2']>=time_stop:
                if index < len(python_info['py2s']):
                    turtle.goto(python_info['py2s'][index][0],python_info['py2s'][index][1])
                    turtle.showturtle()
                    Collisions(turtle=turtle,range_x=10,range_y=10,damage=2)
                    if turtle==GameT_87_YB40 and python_info['wait2']==True:del python_info['py2s'][0]
                else:python_info['count2']+=1
            else:python_info['count2']+=1
        elif turtle not in [GameT_9_KW_BB1_ST3,GameT_8_KK_YB1_ST2]:turtle.hideturtle()
    if TBOSS_locks['Start_turlte_game']:
        if turtle==GameT_22_K13_BB14_W1:
            turtle.showturtle()
            if x_val>=-700:
                turtle.setx(x_val-T_game_NS['Wave1']['speed'][T_game_NS['Wave_nums']])
                if TBOSS_locks['Wave1_lock']:
                    Collisions(turtle=turtle,range_x=40,range_y=100,damage_lock='Wave1_lock',damage=1)
            else:
                turtle.goto(return_val,player.ycor())
                TBOSS_locks['Wave1_lock']=True
        if turtle==GameT_23_K14_BB15_W2:
            turtle.showturtle()
            if y_val>=-500:
                turtle.sety(y_val-T_game_NS['Wave2']['speed'][T_game_NS['Wave_nums']])
                if TBOSS_locks['Wave2_lock']:
                    Collisions(turtle=turtle,range_x=100,range_y=40,damage_lock='Wave2_lock',damage=1)
            else:
                turtle.goto(player.xcor(),return_val)
                
                TBOSS_locks['Wave2_lock']=True
        
        if turtle in Turtle_knights:
            turtle.showturtle()
            if Turtle_knights.index(turtle)<len(Turtle_knights)//T_game_NS['Turtle_knights_vals']['numbers'][T_game_NS['TK_nums']]:
                turtle.showturtle()
                turtle.setheading(turtle.towards(player))
            else:turtle.hideturtle()
        if turtle in Turtle_soldiers:
            turtle.showturtle()
            if Turtle_soldiers.index(turtle)<len(Turtle_soldiers)//T_game_NS['Turtle_soldier_vals']['numbers'][T_game_NS['TS_nums']['num_of_sol']]:
                if Collisions(turtle=turtle,range_x=15,range_y=15,damage=0.1):
                    turtle.goto(x_val,y_val)
                turtle.setheading(turtle.towards(player))
                turtle.forward(T_game_NS['Turtle_soldier_vals']['speed'][T_game_NS['TS_nums']['sol_speed']])
            else:turtle.hideturtle()
        if turtle in [GameT_15_K6_BB7_BT1,GameT_16_K7_BB8_BT2]:
            if TBOSS_locks['lock_bomb2']==True:
                TBOSS_locks['only_TB']=True
            else:
                TBOSS_locks['only_TB']=False
            if bomb_info['Start_bombing_in']==0:
                if turtle==GameT_15_K6_BB7_BT1 and bomb_info['Send_bomb1_in']>0:
                    bomb.showturtle()
                    turtle.showturtle()
                    turtle.goto(player.xcor(),player.ycor())
                    bomb.setx(player.xcor())
                    bomb_info['Send_bomb1_in']-=1
                elif turtle==GameT_16_K7_BB8_BT2 and bomb_info['Send_bomb2_in']>0 and bomb_info['Send_bomb1_in']==0 and bomb_info['Next_bomb_in']==0:
                    bomb.showturtle()
                    turtle.showturtle()
                    turtle.goto(player.xcor(),player.ycor())
                    bomb.setx(player.xcor())
                    bomb_info['Send_bomb2_in']-=1
                elif not (turtle==GameT_16_K7_BB8_BT2 and bomb_info['Next_bomb_in']>0):
                    if bomb.ycor()>turtle.ycor():
                        bomb.sety(bomb.ycor()-T_game_NS['Bomb_vals']['speed'][T_game_NS['Bomb_nums']])
                    else:
                        bomb.hideturtle()
                        turtle.hideturtle()
                        if TBOSS_locks[bomb_lock]==True:
                            Collisions(turtle=turtle,range_x=110,range_y=40,damage=1)
                            TBOSS_locks[bomb_lock]=False
                        if TBOSS_locks['only_TB']==True or (turtle==GameT_16_K7_BB8_BT2 and GameT_25_K16_BB17_CB2.ycor()<=GameT_16_K7_BB8_BT2.ycor()): # Resets Bombs
                            GameT_24_K15_BB16_CB1.sety(410)
                            GameT_25_K16_BB17_CB2.sety(410)
                            bomb_info['Start_bombing_in']=1200
                            bomb_info['Send_bomb1_in']=200
                            bomb_info['Send_bomb2_in']=200
                            bomb_info['Next_bomb_in']=600
                            TBOSS_locks['Setbomb1']=True
                            TBOSS_locks['Setbomb2']=True
                            TBOSS_locks['Bomb1_lock']=True
                            TBOSS_locks['Bomb2_lock']=True
                if bomb_info['Next_bomb_in']>0:
                    bomb_info['Next_bomb_in']-=1
            else:
                bomb_info['Start_bombing_in']-=1
        if turtle==GameT_21_K12_BB13_KC:
            turtle.showturtle()
            if T_game_NS['KC_timer']>0:
                T_game_NS['KC_timer']-=1
            else:
                if len(KC_pos)!=0:
                    next_cor=random.randint(0,len(KC_pos)-1)
                    GameT_21_K12_BB13_KC.goto(KC_pos[next_cor][0],KC_pos[next_cor][1])
                    KC_pos.pop(next_cor)
                    T_game_NS['KC_timer']=T_game_NS['KC_vals']['speed'][T_game_NS['KC_nums']]
                else:
                    KC_pos=[(-200,200),(0,200),(200,200),(200,0),(200,-200),(-200,0),(-200,0),(-200,-200),(-200,0)]
                    next_cor=random.randint(0,len(KC_pos)-1)
                    GameT_21_K12_BB13_KC.goto(KC_pos[next_cor][0],KC_pos[next_cor][1])
                    T_game_NS['KC_timer']=T_game_NS['KC_vals']['speed'][T_game_NS['KC_nums']]
#---- Boss fights ----
def move_TGAME():
    Tgame_Vals=[    #Set_up info for Boss fight
    (700,player.ycor(),'Wave1.gif','blue'),(player.xcor(),500,'Wave2.gif','blue'), #wave 1 and 2
    (0,200,'King_Crush.gif','yellow'),(-450,-200,'turtle','green'),(450,200,'turtle','green'),(-450,200,'turtle','green'),(450,-200,'turtle','green'), #King Crush and his knights
    (-420,-230,'turtle','green'),(420,230,'turtle','green'),(-470,-170,'turtle','green'),(470,170,'turtle','green'), #turtle soldeirs 1-4
    (-420,230,'turtle','green'),(420,-230,'turtle','green'),(-470,170,'turtle','green'),(470,-170,'turtle','green'), #turtle soldeirs 5-8
    (player.xcor(),player.ycor(),'circle','red'),(0,410,'Coco_bomb.gif','brown'),(player.xcor(),player.ycor(),'circle','red'),(0,410,'Coco_bomb.gif','brown')] # bomb traker, bombs, 1 and 2
    if TBOSS_locks['Set_game_turtles']: #Sets up turtles for Boss fights
        for i in range(len(Turtle_army)):
            set_turtles(turtle=Turtle_army[i],shape=Tgame_Vals[i][2],color=Tgame_Vals[i][3],set_x=Tgame_Vals[i][0],set_y=Tgame_Vals[i][1])
        TBOSS_locks['Set_game_turtles']=False
    for i in range(len(Turtle_army)): # Moves turtles in Boss fight
        if i<(len(general_turltes)):
            if general_turltes[i] in Magic_Blasts:
                move_turtles(turtle=general_turltes[i],MB_lock=generalT_info[i][4],
                min_x=MB_range[generalT_info[i][4]]['min_x'],max_x=MB_range[generalT_info[i][4]]['max_x'],min_y=MB_range[generalT_info[i][4]]['min_y'],max_y=MB_range[generalT_info[i][4]]['max_y'])
        if Turtle_army[i]==GameT_22_K13_BB14_W1:move_turtles(turtle=Turtle_army[i],x_val=Turtle_army[i].xcor(),y_val=Turtle_army[i].ycor(),return_val=Tgame_Vals[i][0])
        if Turtle_army[i]==GameT_23_K14_BB15_W2:move_turtles(turtle=Turtle_army[i],x_val=Turtle_army[i].xcor(),y_val=Turtle_army[i].ycor(),return_val=Tgame_Vals[i][1])
        if Turtle_army[i] in Turtle_soldiers:move_turtles(turtle=Turtle_army[i],x_val=Tgame_Vals[i][0],y_val=Tgame_Vals[i][1])
        if Turtle_army[i] in Turtle_knights:move_turtles(turtle=Turtle_army[i],y_val=Tgame_Vals[i][1])
        if TBOSS_locks['lock_bombs']==False:
            if Turtle_army[i]==GameT_15_K6_BB7_BT1:move_turtles(turtle=Turtle_army[i], bomb=GameT_24_K15_BB16_CB1, bomb_lock='Bomb1_lock')
            if TBOSS_locks['lock_bomb2']==False:
                if Turtle_army[i]==GameT_16_K7_BB8_BT2:move_turtles(turtle=Turtle_army[i], bomb=GameT_25_K16_BB17_CB2, bomb_lock='Bomb2_lock')
        if Turtle_army[i]==GameT_21_K12_BB13_KC:move_turtles(turtle=Turtle_army[i])
def move_PGAME():
    global lock_turtles
    if python_info['set_python']:
        B1=0
        B2=0
        Y1=0
        Y2=0
        for i in range(1,len(python_info['python_vals1'])):
            python_info['python_vals1'][i]=(B1,B2)
            python_info['python_vals2'][i]=(Y1,Y2)
            B1+=40
            B2+=30
            Y1+=40
            Y2+=30
        for i in range(len(python_body1)):
            if i==0:set_turtles(turtle=python_body1[i],shape='Pythonhead_yel1.gif',color=python_info['python_vals1'][i][2])
            else:set_turtles(turtle=python_body1[i],shape='Pythonbod_yel.gif',color='black')
        for i in range(len(python_body2)):
            if i==0:set_turtles(turtle=python_body2[i],shape='Pythonhead_blu1.gif',set_x=python_info['python_vals2'][i][0],set_y=python_info['python_vals2'][i][1])
            else:set_turtles(turtle=python_body2[i],shape='Pythonbod_blu.gif',color='yellow')
        python_info['set_python']=False
    for i in range(len(python_body1)): #Moves both pythons
        if i<7:
            if general_turltes[i] in Magic_Blasts:move_turtles(turtle=general_turltes[i],MB_lock=generalT_info[i][4],min_x=MB_range[generalT_info[i][4]]['min_x'],max_x=MB_range[generalT_info[i][4]]['max_x'],min_y=MB_range[generalT_info[i][4]]['min_y'],max_y=MB_range[generalT_info[i][4]]['max_y'])
        if python_body1[i]==GameT_9_KW_BB1_ST3:move_turtles(turtle=python_body1[i],x_val=python_info['python_vals1'][i][0],y_val=python_info['python_vals1'][i][1])
        if python_body1[i] in python_body1 and python_body1[i]!=GameT_9_KW_BB1_ST3:move_turtles(turtle=python_body1[i],index=python_info['python_vals1'][i][0],time_stop=python_info['python_vals1'][i][1])
        if python_body2[i]==GameT_8_KK_YB1_ST2:move_turtles(turtle = python_body2[i],x_val=python_info['python_vals2'][i][0],y_val=python_info['python_vals2'][i][1])
        if python_body2[i] in python_body2 and python_body2[i]!=GameT_8_KK_YB1_ST2:move_turtles(turtle=python_body2[i],index=python_info['python_vals2'][i][0],time_stop=python_info['python_vals2'][i][1])
def move_KGAME():
    Karel_vals=[(0,300,'Big_Karel.gif','none'),(0,-400,'weak_Karel.gif','KW_sp'),
    'K1_sp','K2_sp','K3_sp','K4_sp','K5_sp','K6_sp','K7_sp','K8_sp','K9_sp',
    'K10_sp','K11_sp','K12_sp','K13_sp','K14_sp','K15_sp','K16_sp','K17_sp',
    'K18_sp','K19_sp','K20_sp']
    if Karel_info['set_karels']:
        for i in range(len(Karel_army)):
            if i<=1:
                set_turtles(turtle=Karel_army[i],shape=Karel_vals[i][2],set_x=Karel_vals[i][0],set_y=Karel_vals[i][1])
            else:
                set_turtles(turtle=Karel_army[i],shape='Karel_soldier.gif',set_y=-400)
        Karel_info['set_karels']=False
    for i in range(1,len(Karel_army)):
        if i<7:
            if general_turltes[i] in Magic_Blasts:move_turtles(turtle=general_turltes[i],MB_lock=generalT_info[i][4],min_x=MB_range[generalT_info[i][4]]['min_x'],max_x=MB_range[generalT_info[i][4]]['max_x'],min_y=MB_range[generalT_info[i][4]]['min_y'],max_y=MB_range[generalT_info[i][4]]['max_y'])
        if i<=1:move_turtles(turtle=Karel_army[i],x_val=Karel_army[i].xcor(),y_val=Karel_army[i].ycor(),K_sp=Karel_vals[i][3])
        else:move_turtles(turtle=Karel_army[i],x_val=Karel_army[i].xcor(),y_val=Karel_army[i].ycor(),K_sp=Karel_vals[i])
#----Object Movements ---
def set_magic_range(x,y):
    if not MB_locks['MB1']: #If a Magic Blast is already fired Then the next one goese
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
#-Player Movment-
def press_up(): player_movements['up']=True
def release_up(): player_movements['up']=False
def press_down(): player_movements['down']=True
def release_down(): player_movements['down']=False
def press_left(): player_movements['left']=True
def release_left(): player_movements['left']=False
def press_right(): player_movements['right']=True
def release_right(): player_movements['right']=False
def TBoss_phases():
    screen.bgpic('tut_bg.gif')
    if settings['next_phase']:
        for i in range(len(python_body1)):
            python_body2[i].hideturtle()
            python_body1[i].hideturtle()
        for turtle in Turtle_army:
            turtle.hideturtle()
        for magic in Magic_Blasts:
            magic.hideturtle()
        turtle_dialoge('TBdio1')
        GameT_6_BHB.showturtle()
        GameT_5_PHB.showturtle()
        states['Boss_Health']=35
        states['Player_Health']=25
        GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
        GameT_6_BHB.turtlesize(3,states['Boss_Health'],10) 
        settings['next_phase']=False
    if states['Boss_Health']>=21:
        if TBOSS_locks['set_tim_1']:
            T_game_NS['KC_timer']=T_game_NS['KC_vals']['speed']['1']
            TBOSS_locks['set_tim_1']=False
        TBOSS_locks['Start_turlte_game']=True
        python_info['Start_python_game']=False
        T_game_NS['TS_nums']['num_of_sol']='2'
        T_game_NS['TS_nums']['sol_speed']='1'
        T_game_NS['TK_nums']='4'
        T_game_NS['Bomb_nums']='1'
        T_game_NS['Wave_nums']='1'
        T_game_NS['KC_nums']='1'
        if TBOSS_locks['set_set']:
            TBOSS_locks['Set_game_turtles']=True
            TBOSS_locks['set_set']=False
    elif 20>=states['Boss_Health']>=11:
        if TBOSS_locks['set_tim_2']:
            T_game_NS['KC_timer']=T_game_NS['KC_vals']['speed']['2']
            TBOSS_locks['set_tim_2']=False
        T_game_NS['TS_nums']['num_of_sol']='4'
        T_game_NS['TS_nums']['sol_speed']='2'
        T_game_NS['Bomb_nums']='2'
        T_game_NS['Wave_nums']='2'
        T_game_NS['KC_nums']='2'
        TBOSS_locks['lock_bombs']=False
        TBOSS_locks['lock_bomb2']=True
        if not TBOSS_locks['set_set']:
            TBOSS_locks['Set_game_turtles']=True
            TBOSS_locks['set_set']=True
    elif 10>=states['Boss_Health']>0:
        if TBOSS_locks['set_tim_3']:
            T_game_NS['KC_timer']=T_game_NS['KC_vals']['speed']['3']
            TBOSS_locks['set_tim_3']=False
        T_game_NS['TS_nums']['num_of_sol']='8'
        T_game_NS['TS_nums']['sol_speed']='3'
        T_game_NS['Bomb_nums']='3'
        T_game_NS['Wave_nums']='3'
        T_game_NS['KC_nums']='3'
        T_game_NS['TK_nums']='4'
        TBOSS_locks['lock_bomb2']=False
        if TBOSS_locks['set_set']:
            TBOSS_locks['Set_game_turtles']=True
            TBOSS_locks['set_set']=False
            TBOSS_locks['next_phase']=True
    elif states['Boss_Health']<0:
        if not settings['next_phase']:
            turtle_dialoge('TBdio2')
            settings['next_phase']=True
        settings['Current_boss']='You_win'
    move_TGAME()
def PBoss_phases():
    screen.bgpic('Python_Room.png')
    if settings['next_phase']:
        player_bod['current_bod']='python_bod'
        for i in range(len(python_body1)):
            python_body2[i].hideturtle()
            python_body1[i].hideturtle()
        for turtle in Turtle_army:
            turtle.hideturtle()
        for magic in Magic_Blasts:
            magic.hideturtle()
        python_dialoge('PBdio1')
        GameT_6_BHB.showturtle()
        GameT_5_PHB.showturtle()
        states['Boss_Health']=35
        states['Boss_Health']=25
        GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
        GameT_6_BHB.turtlesize(3,states['Boss_Health'],10) 
        TBOSS_locks['Start_turlte_game']=False
        python_info['Start_python_game']=True
        Karel_info['Start_karel_game']=False
        settings['next_phase']=False
    if states['Boss_Health']<=0:
        if not settings['next_phase']:
            python_dialoge('PBdio2')
            settings['Current_boss']='goto_TB'
            settings['next_phase']=True
    if states['Player_Health']<=0:
        settings['Current_boss']='Game_over'
    move_PGAME()
def KBoss_phases():
    screen.bgpic('karlbg.gif')
    if settings['next_phase']:
        player_bod['current_bod']='karel_bod'
        for i in range(len(python_body1)):
            python_body2[i].hideturtle()
            python_body1[i].hideturtle()
        for i in range(len(Turtle_army)):
            Turtle_army[i].hideturtle()
            GameT_6_BHB.showturtle()
            GameT_5_PHB.showturtle()
            states['Boss_Health']=35
            states['Boss_Health']=25
            GameT_5_PHB.turtlesize(states['Player_Health'],3,10)
            GameT_6_BHB.turtlesize(3,states['Boss_Health'],10) 
            settings['next_phase']=False
            TBOSS_locks['Start_turlte_game']=False
            python_info['Start_python_game']=False
            Karel_info['Start_karel_game']=True
        karel_dialoge('KBdio1')
        settings['next_phase']=False
    if 16>=states['Boss_Health']>0:
        Karel_info['Change_speed']=True
    elif states['Boss_Health']<=0:
        if not settings['next_phase']:
            karel_dialoge('KBdio2')
            settings['Current_boss']='goto_PB'
            settings['next_phase']=True
    move_KGAME()
def Bosses():
    if settings['Current_boss']=='goto_KB':
        KBoss_phases()
    elif settings['Current_boss']=='goto_PB':
        PBoss_phases()
    elif settings['Current_boss']=='goto_TB':
        TBoss_phases()
def player_animation():
    if player_movements['ani_ply']=='up':
        if player_movements['ani_lcok']==True:
            player.shape('Kiki_DL.gif')
            if player_movements['ani_count']==-5:player_movements['ani_lcok']=False
            else:player_movements['ani_count']-=1
        else:
            player.shape('Kiki_UL.gif')
            if player_movements['ani_count']==5:player_movements['ani_lcok']=True
            else:player_movements['ani_count']+=1
    if player_movements['ani_ply']=='down':
        if player_movements['ani_lcok']==True:
            player.shape('Kiki_DL.gif')
            if player_movements['ani_count']==-5:player_movements['ani_lcok']=False
            else:player_movements['ani_count']-=1
        else:
            player.shape('Kiki_UL.gif')
            if player_movements['ani_count']==5:player_movements['ani_lcok']=True
            else:player_movements['ani_count']+=1
    if player_movements['ani_ply']=='left':
        if player_movements['ani_lcok']==True:
            player.shape('Kiki_DL.gif')
            if player_movements['ani_count']==-5:player_movements['ani_lcok']=False
            else:player_movements['ani_count']-=1
        else:
            player.shape('Kiki_UL.gif')
            if player_movements['ani_count']==5:player_movements['ani_lcok']=True
            else:player_movements['ani_count']+=1
    if player_movements['ani_ply']=='right':
        if player_movements['ani_lcok']==True:
            player.shape('Kiki_DR.gif')
            if player_movements['ani_count']==-5:player_movements['ani_lcok']=False
            else:player_movements['ani_count']-=1
        else:
            player.shape('Kiki_UR.gif')
            if player_movements['ani_count']==5:player_movements['ani_lcok']=True
            else:player_movements['ani_count']+=1
def move_game():
    if settings['Current_boss']!='Game_over' and settings['Current_boss']!='You_win':
        if settings['setG']==True:
            for turtle in Every_turtle:
                turtle.hideturtle()
            set_general_turtles()
            settings['setG']=False
        if player_movements['up']==True and player.ycor()+10<player_bod[player_bod['current_bod']][1]:
            player.sety(player.ycor()+5)
            player_movements['ani_ply']='up'
        if player_movements['down']==True and player.ycor()-10>-player_bod[player_bod['current_bod']][2]:
            player.sety(player.ycor()-5)
            player_movements['ani_ply']='down'
        if player_movements['left']==True and player.xcor()-10>-player_bod[player_bod['current_bod']][0]:
            player.setx(player.xcor()-5)
            player_movements['ani_ply']='left'
        if player_movements['right']==True and player.xcor()+10<player_bod[player_bod['current_bod']][0]:
            player.setx(player.xcor()+5)
            player_movements['ani_ply']='right'
        player_animation()
        KBoss_phases()
        screen.update()
        screen.ontimer(move_game, 16)
    elif settings['Current_boss']=='Game_over':
        screen.bgpic('gameover.gif')
    elif settings['Current_boss']=='You_win':
        screen.bgpic('win.gif')
screen.listen()
if player_movements['lock']:
    screen.onkeypress(press_up, 'w')
    screen.onkeyrelease(release_up, 'w')
    screen.onkeypress(press_down, 's')
    screen.onkeyrelease(release_down, 's')
    screen.onkeypress(press_left, 'a')
    screen.onkeyrelease(release_left, 'a')
    screen.onkeypress(press_right, 'd')
    screen.onkeyrelease(release_right, 'd')
screen.onclick(set_magic_range)
move_game()
screen.mainloop()
