import turtle

screen = turtle.Screen()
screen.tracer(1)
screen.bgcolor('black')
screen.bgpic('Cover.png')
screen.setup(1300,700)
MB_locks={'MB1':True,'MB2':True,'MB3':True,'MB4':True}
player_movements={'up':False,'down':False,'left':False,'right':False,
                  'lock':True,'ani_ply':'down','ani_lcok':True,
                  'ani_count':20,'flap_speed':5, 'move_timer':-5, 'move_lock':True} #player movement locks
player = turtle.Turtle()
player.color('teal')
player.penup()
player.speed(0)
Tbox = turtle.Turtle()
Tbox.color("white")
Tbox.speed(0)

Tbutten = turtle.Turtle()
Tbutten.color("pink")
Tbutten.shape("square")
Tbutten.shapesize(2,5)
Tbutten.penup()
Tbutten.goto(0,-300)

Playgame = True
currentbounds = []
currentmap = "None"
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

maze_cor = []
lobby_cor = []
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
    screen.bgpic(next_map)
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
            if currentbounds[cor][0] <= new_x <= currentbounds[cor+1][0] and currentbounds[cor][1] <= new_y <= currentbounds[cor+1][1]:
                return True
    if currentmap!='None':
        if currentmap(new_x, new_y):
            return True
    return False
def player_animation():
    if player_movements['ani_ply']=='up':
        if player_movements['up']==True and not is_collisions(player.xcor(), player.ycor()+23):
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
            player_movements['move_lock']=True
    if player_movements['ani_ply']=='down':
        if player_movements['down']==True and not is_collisions(player.xcor(), player.ycor()-10):
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
            player_movements['move_lock']=True
    if player_movements['ani_ply']=='left':
        if player_movements['left']==True and not is_collisions(player.xcor()-20, player.ycor()):
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
            player_movements['move_lock']=True
    if player_movements['ani_ply']=='right':
        if player_movements['right']==True and not is_collisions(player.xcor()+20, player.ycor()):
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
            player_movements['move_lock']=True

def player_cor():
    print(f"{player.xcor()},{player.ycor()}")

def click_cords(x, y):
    print (f'Clicked at: {x}, {y}')

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

def move_game():
    for ani in ['PT_FS.gif', 'PT_BS.gif', 'PT_LS.gif', 'PT_RS.gif']:
        player.shape(ani)
    # player_animation()
    # if player_movements['up']:
    #     if player_movements['ani_ply']!='up':player_movements['ani_ply']='up'
    #     if not is_collisions(player.xcor(), player.ycor()+23):player.sety(player.ycor()+5)
    # if player_movements['down']:
    #     if player_movements['ani_ply']!='down':player_movements['ani_ply']='down'
    #     if not is_collisions(player.xcor(), player.ycor()-10):player.sety(player.ycor()-5)
    # if player_movements['left']:
    #     if player_movements['ani_ply']!='left':player_movements['ani_ply']='left'
    #     if not is_collisions(player.xcor()-20, player.ycor()):player.setx(player.xcor()-5)
    # if player_movements['right']:
    #     if player_movements['ani_ply']!='right':player_movements['ani_ply']='right'
    #     if not is_collisions(player.xcor()+20, player.ycor()):player.setx(player.xcor()+5)
    screen.update()
    screen.ontimer(move_game, 5)

if __name__ == '__main__':
    proccesmaps()
    screen.listen()
    screen.onkeypress(press_up, 'w')
    screen.onkeyrelease(release_up, 'w')
    screen.onkeypress(press_down, 's')
    screen.onkeyrelease(release_down, 's')
    screen.onkeypress(press_left, 'a')
    screen.onkeyrelease(release_left, 'a')
    screen.onkeypress(press_right, 'd')
    screen.onkeyrelease(release_right, 'd')
    screen.onclick(click_cords)
    screen.onkey(player_cor, 'q')
    Tbutten.onclick(startgame)
    move_game()
    screen.mainloop()