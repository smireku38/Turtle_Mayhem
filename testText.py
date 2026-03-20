import turtle
import time

T_box = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()
line4 = turtle.Turtle()
line1.color('red')
screen = turtle.Screen()


screen.tracer(0)
word_space = {'A':20,'B':20,'C':22,'D':20,'E':20,'F':20,'G':25,'H':22,'I':8,'J':18,'K':22,'L':19,'M':26,
              'N':23,'O':26,'P':23,'Q':26,'R':24,'S':21,'T':21,'U':25,'V':23,'W':34,'X':24,'Y':22,'Z':22,
              'a':18,'b':19,'c':18,'d':18,'e':18,'f':10,'g':18,'h':18,'i':8,'j':7,'k':17,'l':7,'m':26,
              'n':18,'o':18,'p':19,'q':18,'r':12,'s':18,'t':10,'u':19,'v':17,'w':24,'x':16,'y':16,'z':20,
              '0':10,'1':10,'2':10,'3':10,'4':10,'5':10,'6':10,'7':10,'8':10,'9':10,
              ' ':10,'.':10,',':10,'!':11,'?':20,'-':11, '(':10,')':10, ':':10, '\'':11,'=':10,'+':10,
              'printing_text':'case1','textbox_on':False, 'currline':0, 'spam_lock':False}

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
game_txt = procces_dialouge('Game_D.txt')
def manage_printing(dialoge = game_txt):
    if word_space['printing_text'] == 'case3':
        word_space['printing_text'] = 'case1'
        line1.clear()
        line2.clear()
        line3.clear()
        line4.clear()
        if word_space['currline'] < len(game_txt)-1:word_space['currline'] += 1

    if word_space['printing_text'] == 'case1':
        set_textbox_turtles()
        word_space['printing_text'] = 'case2'
        screen.tracer(1)
        print_Text(dialoge[word_space['currline']])
        screen.tracer(0)

    elif word_space['printing_text'] == 'case2':
        word_space['spam_lock'] = False
        screen.tracer(0)
        print_Text(dialoge[word_space['currline']])
        if word_space['currline'] < len(game_txt)-2: word_space['printing_text'] = 'case3'
        else:word_space['printing_text'] = 'case4' # end of text
        word_space['spam_lock'] = True

    if word_space['printing_text'] == 'case4':
        T_box.hideturtle()
        word_space['printing_text'] = 'case1'
        word_space['currline'] = 0
        word_space['textbox_on'] = False
        screen.update()
def manual_print():
    manage_printing(game_txt)

def auto_print():
    while word_space['currline'] < len(game_txt)-1:
        manage_printing(game_txt)
        if word_space['currline'] < len(game_txt)-2: time.sleep(1.5)
    word_space['printing_text'] = 'case4'
    manage_printing(game_txt)

#====================================================================

#
screen.listen()
if word_space['spam_lock'] == False: screen.onkey(auto_print, 'e')
screen.mainloop()
    