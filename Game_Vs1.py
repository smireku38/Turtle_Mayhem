import turtle

screen = turtle.Screen()
screen.setup(1300,700)

player = turtle.Turtle()
player.color('teal')
player.penup()
player.goto(-35,280)

Tbox = turtle.Turtle()
#Tbox.speed(0)

Tbutten = turtle.Turtle()
Tbutten.color("pink")
Tbutten.goto(300,100)

def test():
    pass

Playgame = True
currentbounds = "None"
currentmap = test

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
    Tbox.clear()
    # screen.bgpic(next_map)
    DrawBoxes(boundslist)

def mazemap(new_x, new_y):
    global currentbounds,currentmap
    if -39 <= new_x <= 39 and 312 <= new_y <= 350:
        player.goto(39,193)
        currentbounds = maze_cor
        print(currentmap)
        currentmap = lobbymap
        loadmap('map.gif', maze_cor)
        return True
    else:
        return False

def lobbymap(new_x, new_y):
    global currentbounds, currentmap, Playgame
    print('Start')
    if Playgame == True or 20 <= new_x <= 55 and 212 <= new_y <= 250:
        player.goto(2,278)
        currentbounds = lobby_cor
        currentmap = mazemap
        print(currentmap)
        loadmap("town.gif", lobby_cor)
        player.showturtle()
        Playgame = False
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
    for cor in range(0, len(currentbounds), 2):
        if currentbounds[cor][0] <= new_x <= currentbounds[cor+1][0] and currentbounds[cor][1] <= new_y <= currentbounds[cor+1][1]:
            return True
    if currentmap(new_x, new_y):
        return True
    return False

def playermove(new_x, new_y):
    if not is_collisions(new_x, new_y):
        player.goto(new_x, new_y)
    else:
        print('Hit Wall!')
def move_forward():
    #player.setheading(90)
    new_x, new_y = player.xcor(), player.ycor() + 15
    playermove(new_x, new_y)
def move_backword():
    #player.setheading(270)
    new_x, new_y = player.xcor(), player.ycor() - 15
    playermove(new_x, new_y)
def move_left():
    #player.setheading(180)
    new_x, new_y = player.xcor() - 15, player.ycor()
    playermove(new_x, new_y)
def move_right():
    #player.setheading(0)
    new_x, new_y = player.xcor() + 15, player.ycor()
    playermove(new_x, new_y)

def drag_player(x,y):
    player.goto(x,y)
    print(f"{x},{y}")


if __name__ == '__main__':
    proccesmaps()
    print(maze_cor)
    screen.listen()
    screen.onkeypress(move_forward, "Up")
    screen.onkeypress(move_backword, "Down")
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    player.ondrag(drag_player)
    Tbutten.onclick(startgame)
    screen.mainloop()