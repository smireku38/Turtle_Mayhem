from Turtle_Game_Data import Game_story, entity, static_entity,map_settings, Game_dialogue
from Procces_Game_Dio import manual_print, auto_print, set_dialouges, word_space
from Screen_Init import backround
def phase1():
    phase1_entitys = entity.entity_pool
    props = static_entity.entity_pool
    if Game_story['Act1']['phase1']['Scene1'] == 'inactive':
        if phase1_entitys[0].actor.ycor() > 0 or phase1_entitys[0].down == False:
            if phase1_entitys[0].direction != 'down' and not phase1_entitys[0].down:
                map_settings['lock_map'] = True
                Game_story['playing_story'] = True
                phase1_entitys[0].actor.goto(0,300)
                phase1_entitys[1].actor.goto(50,340)
                phase1_entitys[2].actor.goto(-35,320)
                phase1_entitys[0].adjust_entity(direction = 'down', default = 'down', down = True)
                phase1_entitys[1].adjust_entity(direction = 'down', default = 'down', down = True)
                phase1_entitys[2].adjust_entity(direction = 'down', default = 'down', down = True)
                phase1_entitys[0].actor.showturtle()
                phase1_entitys[1].actor.showturtle()
                phase1_entitys[2].actor.showturtle()
        else:
            Game_dialogue['currAct'] = 'Act1'
            Game_dialogue['currSce'] = 'Scene1'
            Game_dialogue['currPhs'] = 'Phase1'
            set_dialouges()
            Game_story['Act1']['phase1']['Scene1'] = 'pending'
            phase1_entitys[0].adjust_entity()
            phase1_entitys[1].adjust_entity()
            phase1_entitys[2].adjust_entity()
            auto_print(Game_dialogue['Enti_W_Dio']['General'])
            return
    elif Game_story['Act1']['phase1']['Scene1'] == 'pending' and Game_story['Act1']['phase1']['Scene2'] == 'inactive':
        Game_story['Act1']['phase1']['Scene1'] = 'complete'
        phase1_entitys[0].adjust_entity(direction = 'down')
        return
    elif Game_story['Act1']['phase1']['Scene2'] == 'inactive':
        if phase1_entitys[0].actor.ycor() < 400:
            if phase1_entitys[0].direction != 'up' and not phase1_entitys[0].up:
                phase1_entitys[0].adjust_entity(direction = 'up', up = True)
                phase1_entitys[1].adjust_entity(direction = 'up', up = True)
                phase1_entitys[2].adjust_entity(direction = 'up', up = True)
        else:
            Game_story['Act1']['phase1']['Scene2'] = 'pending'
            return
    elif Game_story['Act1']['phase1']['Scene2'] == 'pending' and Game_story['Act1']['phase1']['Scene3'] == 'inactive':
        phase1_entitys[0].actor.goto(0,-440)
        phase1_entitys[1].actor.goto(50,-400)
        phase1_entitys[2].actor.goto(-35,-420)
        Game_story['Act1']['phase1']['Scene2'] = 'complete'
        return
    elif Game_story['Act1']['phase1']['Scene3'] == 'inactive':
        if phase1_entitys[0].actor.ycor() > -100:
            if phase1_entitys[0].direction == 'up' and  phase1_entitys[0].up:
                phase1_entitys[0].adjust_entity()
        if phase1_entitys[1].actor.ycor() > 200 and phase1_entitys[1].actor.xcor() <=100:
            if phase1_entitys[1].direction == 'up' and  phase1_entitys[1].up:
                phase1_entitys[1].adjust_entity(direction = 'right', right = True)
        elif phase1_entitys[1].actor.xcor() > 100 and phase1_entitys[1].actor.isvisible():
            if phase1_entitys[1].direction == 'right' and  phase1_entitys[1].right:
                phase1_entitys[1].adjust_entity()
                phase1_entitys[1].actor.hideturtle()
        if phase1_entitys[2].actor.ycor() > 200 and phase1_entitys[2].actor.xcor() <= 100:
            if phase1_entitys[2].direction == 'up' and  phase1_entitys[2].up:
                phase1_entitys[2].adjust_entity(direction = 'right', right = True)
        elif phase1_entitys[2].actor.xcor() > 100 and phase1_entitys[2].actor.isvisible():
            if phase1_entitys[1].direction == 'right' and  phase1_entitys[2].right:
                phase1_entitys[2].adjust_entity()
                phase1_entitys[2].actor.hideturtle()
        if not phase1_entitys[1].actor.isvisible() and not phase1_entitys[2].actor.isvisible():
            Game_story['playing_story'] = False
            map_settings['lock_map'] = False
            Game_story['Act1']['phase1']['Scene3'] = 'pending'
    elif Game_story['Act1']['phase1']['Scene3'] == 'pending':
        # print("Inside")
        U_y_bound = backround.ycor()+250
        L_y_bound = backround.ycor()+150
        U_x_bound = backround.xcor()+150
        L_x_bound = backround.xcor()+50
        if U_y_bound >= phase1_entitys[0].actor.ycor() >= L_y_bound and U_x_bound >= phase1_entitys[0].actor.xcor() >= L_x_bound:
            Game_story['Act1']['phase1']['Scene3'] = 'complete'
            return
    elif Game_story['Act1']['phase1']['Scene4'] == 'inactive':
        if phase1_entitys[1].conversant == False:
            x, y = backround.xcor(), backround.ycor()
            phase1_entitys[1].actor.goto(350 + x,50 + y)
            phase1_entitys[2].actor.goto(400 + x,50 + y)
            phase1_entitys[1].actor.showturtle()
            phase1_entitys[2].actor.showturtle()
            phase1_entitys[0].adjust_entity(direction = 'right')
            phase1_entitys[1].adjust_entity(direction = 'up')
            phase1_entitys[2].adjust_entity(direction = 'up')
            word_space['Can_print'] =  True
            phase1_entitys[1].conversant = True
            Game_story['MacGuffin'] = 'Bob'
        if Game_story['MacGuffin'] == 'none':
            print('starting Scene 4')
            phase1_entitys[1].conversant = False
            phase1_entitys[1].actor.hideturtle()
            phase1_entitys[2].actor.hideturtle()
            phase1_entitys[1].actor.goto(1000,1000)
            phase1_entitys[2].actor.goto(1000,1000)
            enti = entity.active_player
            speed = map_settings['speed']
            Game_story['Act1']['phase1']['Scene4'] = 'pending'
    elif Game_story['Act1']['phase1']['Scene4'] == 'pending':
        x, y = backround.xcor(), backround.ycor()
        if props[0].actor.isvisible() == False:
            Game_story['MacGuffin'] = 'Computer'
            props[0].actor.showturtle()
            props[0].actor.showturtle()
            props[0].actor.showturtle()
            props[0].has_text = True
            props[0].actor.goto(380 + x, 80 + y)
            props[0].conversant = True
        if Game_story['MacGuffin'] == 'none':
            phase1_entitys[0].actor.goto(0,300)
            props[0].conversant = False
            map_settings['lock_map'] = True
            Game_story['Act1']['phase1']['Scene4'] = 'complete'
    elif Game_story['Act1']['phase1']['Scene5'] == 'inactive':
        if Game_story['transition_timer'] == -1:
            Game_story['transition_timer'] = 20
            props[0].actor.shape('circle')
            props[1].actor.shape('circle')
            props[0].actor.color('red')
            props[1].actor.color('yellow')
            props[2].actor.shape("Cover(1).gif")
            props[3].actor.shape("Cover(1).gif")
            props[2].actor.goto(0, 200)
            props[3].actor.goto(0,-400)
            props[0].actor.goto(0,400)
            props[1].actor.goto(0,-10)
            props[0].actor.shapesize(stretch_wid=5, stretch_len=10) # Temp line
            props[1].actor.shapesize(stretch_wid=2, stretch_len=10) # Temp line
            props[0].actor.goto(0, 400)
            for turtle in [props[0].actor, props[1].actor, props[2].actor, props[3].actor] : turtle.showturtle()
        if Game_story['transition_timer'] > 0:
            for backdrop in [props[2].actor, props[3].actor]:
                if backdrop.ycor() <= 500:
                    backdrop.sety(backdrop.ycor()+40)
                else :
                    backdrop.sety(-500)
                    Game_story['transition_timer'] -= 1
                    print(Game_story['transition_timer'])
            if entity.active_player.actor.ycor() >= 0:
                entity.active_player.actor.sety(entity.active_player.actor.ycor()-5)
            else:
                props[0].actor.sety(props[0].actor.ycor()+2)
        elif (entity.active_player.actor.ycor() >= -300):
            entity.active_player.actor.sety(entity.active_player.actor.ycor()-5)
            # props[1].actor.hideturtle()
            # props[2].actor.hideturtle()
            # props[3].actor.hideturtle()
            props[1].actor.sety(props[1].actor.ycor()-5)
        else:
            Game_story['transition_timer'] = -1
            props[1].actor.hideturtle()
            Game_story['Act1']['phase1']['Scene5'] = 'pending'
      