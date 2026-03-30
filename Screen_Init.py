import turtle

screen = turtle.Screen()
Canvas = screen.getcanvas()
screen.setup(width=900, height=900)
screen.tracer(0)
screen.register_shape('Cover(1).gif')
backround = turtle.Turtle()
backround.shape('Cover(1).gif')
backround.penup()
images = ['PT_FR.gif', 'PT_FL.gif', 'PT_FS.gif', 'PT_BR.gif', 'PT_BL.gif', 'PT_BS.gif',
          'PT_LR.gif', 'PT_LL.gif', 'PT_LS.gif', 'PT_RR.gif', 'PT_RL.gif', 'PT_RS.gif',
          'Cover(1).gif'
         ]
for image in images:
    screen.register_shape(image)
