import turtle
import time

T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
screen = turtle.Screen()

screen.tracer(1)
word_space = {'A':20,'B':20,'C':22,'D':20,'E':20,'F':20,'G':25,'H':22,'I':8,'J':18,'K':22,'L':19,'M':26,
              'N':23,'O':26,'P':23,'Q':26,'R':24,'S':21,'T':21,'U':25,'V':23,'W':34,'X':24,'Y':22,'Z':22,
              'a':18,'b':19,'c':18,'d':18,'e':18,'f':10,'g':18,'h':18,'i':8,'j':7,'k':17,'l':7,'m':26,
              'n':18,'o':18,'p':19,'q':18,'r':12,'s':18,'t':10,'u':19,'v':17,'w':24,'x':16,'y':16,'z':20,
              ' ':10,'.':10,',':10,'!':11,'?':20,'-':11, '(':10,')':10, ':':10,
              'textbox_on':False, 'currline':0}


def procces_dialouge(dialouge_text): #open file and make it useable
    d_file= open(dialouge_text)
    d_text= d_file.readlines()
    box_text=[]
    for i in range(0,len(d_text)): # make sure it is the chr we want, get rid of /n
        box_text.append(d_text[i].strip())
    d_file.close() 
    return box_text
def set_turtle(turtleName, shape='turtle', color='black', width= 0, length=0, outline=0):
    turtleName.shape(shape)
    turtleName.color(color)
    turtleName.penup()
    if turtleName == T_box: turtleName.turtlesize(length, width, outline)
    # turtleName.hideturtle()
def set_textbox_turtles():
    word_space['currline'] = 0
    if word_space['textbox_on'] == False:
        set_turtle(line1, 'arrow', 'white')
        set_turtle(line2, 'arrow', 'white')
        set_turtle(line3, 'arrow', 'white')
        set_turtle(line4, 'arrow', 'white')
        set_turtle(T_box, 'square', 'black', length=10, width=40, outline=10)
    x, y= -390, -200 # where texts starts
    line1.goto(x,y)
    line2.goto(x,y-40)
    line3.goto(x,y-80)
    line4.goto(x,y-120)
    T_box.goto(0,-250)
    T_box.showturtle()
        
def print_Text(dialoge):
    current_turtle = line1
    x, y= -390, -200 # where texts starts
    for i in dialoge:
        current_turtle.goto(x,y)
        current_turtle.write(i, font =("Ariel", 25, "normal"))
        x+= word_space[i] # space between text
        time.sleep(0.01) #time between letter
        if i ==' ':
            word_len = 0
            while dialoge[dialoge.index(i)+word_len] != ' ':
                word_len += 1
            T_space = x
            for j in range(word_len):
                T_space += word_space[dialoge[j]]
            if T_space > 320: 
                print('break')
                x = -390 # start new line and continue
                y-=40 # New line
                if current_turtle == line1: current_turtle = line2
                elif current_turtle == line2: current_turtle = line3
                elif current_turtle == line3: current_turtle = line4
                elif current_turtle == line4: current_turtle = line1
    time.sleep(2)
set_turtle(T_box, 'square', 'black', length=10, width=40, outline=10)



game_txt = procces_dialouge('Game_D.txt')
screen.listen()
# screen.onkey(start_T, 'e')
screen.mainloop()