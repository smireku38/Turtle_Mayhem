import turtle
from Screen_Init import screen, Canvas
class entity:
    entitys = []
    entity_pool = []
    collidabl_turtles = []
    active_player = 'None'
    Int_Direction = ['down', 'up', 'right', 'left']
    def __init__(self = "None", name = "None", sprite = "None"):
        entity.entitys.append(name)
        entity.entity_pool.append(self)
        self.name = name
        self.actor = turtle.Turtle()

        self.actor.speed(0)
        self.actor.penup()

        self.canInteract = False
        self.vision_range = 55
        self.Collision_range = 40
        self.active_collisions = []

        self.lock = False

        self.speed = 5
        self.direction = 'up'
        self.default_direction = 'up'
        self.default_shape = 'None'
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        self.LPS, self.RPS, self.UPS, self.DPS = 5, 5, 5, 5

        self.animation_enabled = False
        self.lock_Animation = False
        self.Oscillate_ani = True
        self.move_timer = -4

        self.print_type = 'manual'
        self.conversant = False
        self.up_ani = {'frame1':sprite+'_BL.gif','frame2':sprite+'_BS.gif','frame3':sprite+'_BR.gif'}
        self.down_ani = {'frame1':sprite+'_FL.gif','frame2':sprite+'_FS.gif','frame3':sprite+'_FR.gif'}
        self.left_ani = {'frame1':sprite+'_LL.gif','frame2':sprite+'_LS.gif','frame3':sprite+'_LR.gif'}
        self.right_ani = {'frame1':sprite+'_RL.gif','frame2':sprite+'_RS.gif','frame3':sprite+'_RR.gif'}
        self.directions = ['up', 'down', 'left', 'right']
        self.entity_sprites = [self.up_ani, self.down_ani, self.left_ani, self.right_ani]
    def activate_entitys():
        if not map_settings['lock_map']:
            entity.active_player.activate_player_ani()
            # entity.active_player.hit_box()
        for enti in entity.entity_pool:
            if enti != entity.active_player or map_settings['lock_map']:
                enti.set_direction()
                enti.animate_entity()
                enti.maintain_z_order()
                enti.Observe_Player()
                enti.set_movement_permissions()
    def adjust_entity(self, name = 'None', obj = 'None', direction = 'None', default = 'None', up = False, down = False, left = False, right = False):
        if name != 'None': self.name = name 
        if obj != 'None': self.actor = obj 
        if direction != 'None': self.direction = direction
        if default != 'None': self.default_direction = default
        if True in [up, down, left, right]:
            self.up, self.down = up, down
            self.left, self.right = left, right
        else:
            self.up, self.down = False, False
            self.left, self.right = False, False
    def set_direction(self):
        if self.up: self.direction  = 'up'
        elif self.down: self.direction  = 'down'
        elif self.left: self.direction  = 'left'
        elif self.right: self.direction  = 'right'
    def activate_player_ani(self):
        index =self.directions.index(map_settings['direction'])
        locks = [map_settings['up'], map_settings['down'], map_settings['left'], map_settings['right']]
        self.animate_entity(index , locks)
    def animate_entity(self, index = -1, locks = []):
        current_lock = False
        if index == -1:
            locks = [self.up, self.down, self.left, self.right]
            index = self.directions.index(self.direction)
        for lock in locks:
                    if lock == True: current_lock = lock
        if self == entity.active_player or True in [self.up, self.down, self.left, self.right]:
            direction_sprites = self.entity_sprites[index]
            if current_lock:
                    if self.move_timer == -4: self.actor.shape(direction_sprites['frame1'])
                    elif self.move_timer == 0: self.actor.shape(direction_sprites['frame2'])
                    elif self.move_timer == 4: self.actor.shape(direction_sprites['frame3'])
            else:self.actor.shape(direction_sprites['frame2'])
        elif self.canInteract == False:
            if self.actor.shape() != self.default_shape:
                index = self.directions.index(self.default_direction)
                direction_sprites = self.entity_sprites[index]
                self.actor.shape(direction_sprites['frame2'])
        self.animation_timer(current_lock)
    def animation_timer(self, current_lock = False):
        if current_lock == True:
            if self.Oscillate_ani==True:
                if self.move_timer!=4:
                    self.move_timer+=1
                else:self.Oscillate_ani=False
            elif self.Oscillate_ani==False:
                if self.move_timer!=-4:
                    self.move_timer-=1
                else:self.Oscillate_ani=True
        elif self.move_timer != -4: self.move_timer = -4
    def get_player_direction(self, enti2):
        angel = self.actor.towards(enti2)
        if 315 < angel <= 360 or 0 <= angel <= 45:
            return 'right'
        elif 45 < angel <= 135:
            return 'up'
        elif 135 < angel <= 225:
            return 'left'
        elif 225 < angel <= 315:
            return 'down'
    def Observe_Player(self):
        active_only = entity.active_player.actor.distance(self.actor) <= self.vision_range
        locks = [self.up, self.down, self.left, self.right]
        if not active_only and (not map_settings['lock_map'] or True not in locks):
            for enti in self.entity_pool:
                actor = enti.actor
                if actor.isvisible() and enti != self:
                    if actor.distance(self.actor) <= self.vision_range:
                        direction = self.get_player_direction(actor)
                        index = self.directions.index(direction)
                        direction_sprites = self.entity_sprites[index]
                        self.actor.shape(direction_sprites['frame2'])
        elif not map_settings['lock_map'] and active_only:
            direction = self.get_player_direction(entity.active_player.actor)
            index = self.directions.index(direction)
            direction_sprites = self.entity_sprites[index]
            self.actor.shape(direction_sprites['frame2'])       
    def hit_box(self):
        if self == entity.active_player:
            speed = map_settings['speed']
            for PS in ['UPS', 'DPS', 'LPS', 'RPS']:
                if map_settings[PS] == 0: map_settings[PS] = speed
        for enti in entity.entity_pool:
            if enti.actor.isvisible() and  enti != self:
                if enti not in self.active_collisions:
                    if enti.actor.distance(self.actor) <= self.Collision_range:
                        self.active_collisions.append(enti)
                elif enti in self.active_collisions:
                    if enti.actor.distance(self.actor) > self.Collision_range:
                        self.active_collisions.remove(enti)
        for enti in self.active_collisions:
            direction = self.get_player_direction(enti.actor)
            index = self.directions.index(direction)
            if self == entity.active_player:
                dir = map_settings['Dir_speeds'][index]
                map_settings[dir] = 0
            


            
        
        # if not enti.actor.isvisible() and  enti == self:
        #     return
            # if enti.actor.distance(self.actor)<= self.Collision_range:
            #         direction = enti.direction
            #         if enti == entity.active_player:
            #             index = map_settings['controls'].index(direction)
            #             dir = map_settings['Dir_speeds'][index]
            #             map_settings[dir] = 0
                # else:
                #     if enti == entity.active_player:
                #         speed = map_settings['speed']
                #         for PS in ['UPS', 'DPS', 'LPS', 'RPS']:
                #             if map_settings[PS] == 0:
                #                 map_settings[PS] = speed

                        # if direction == 'up': map_settings['UPS'], map_settings['DPS'] = 0, 5
                        # if direction == 'down': map_settings['DPS'], map_settings['UPS'] = 0, 5
                        # if direction == 'left': map_settings['LPS'], map_settings['RPS'] = 0, 5
                        # if direction == 'right': map_settings['RPS'], map_settings['LPS'] = 0, 5          
    def maintain_z_order(self):
        active_player = entity.active_player
        stack = Canvas.find_all()
        curr_layer = stack.index(active_player.actor.turtle._item)
        other_layer = stack.index(self.actor.turtle._item)
        if  curr_layer < other_layer and self.actor.ycor() > active_player.actor.ycor():
            Canvas.tag_raise(active_player.actor.turtle._item, self.actor.turtle._item) 
        elif curr_layer > other_layer and self.actor.ycor() <= active_player.actor.ycor():
            Canvas.tag_lower(active_player.actor.turtle._item, self.actor.turtle._item)
    def set_movement_permissions(self):
        direction = self.direction
        actor = self.actor
        if direction == 'up' and self.up == True: actor.sety(actor.ycor() + self.UPS)
        if direction == 'down' and self.down == True: actor.sety(actor.ycor() - self.DPS)
        if direction == 'left' and self.left == True: actor.setx(actor.xcor() - self.LPS)
        if direction == 'right' and self.right == True: actor.setx(actor.xcor() + self.RPS)
class static_entity:
    entitys = []
    entity_pool = []
    def __init__(self = "None", name = "None", sprite = "None", hide = False):
        self.name = name
        self.actor = turtle.Turtle()

        self.entitys.append(name)
        self.entity_pool.append(self)
    
        self.actor.speed(0)
        self.actor.penup()
        if hide: self.actor.hideturtle()
        moveable = False

        has_text = False

        static_shape = sprite+'_FS.gif'
        self.actor.shape(static_shape)
        static_antimation = {}

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        self.LPS, self.RPS, self.UPS, self.DPS = 5, 5, 5, 5


map_settings = {'direction': 'up',
                'lock_map':False,
                'set_turtle':False,
                'switch': False,
                'speed':5,
                'up':False,'down':False,'left':False,'right':False,
                'LPS':5,'RPS':5,'UPS':5,'DPS':5,
                'controls':['up', 'down', 'left', 'right'],
                'Dir_speeds':['UPS', 'DPS', 'LPS', 'RPS']
                }
Game_story = {   'playing_story':False, 'current_Act': 'none', 'current_phase': 'none', 'current_Scene': 'none', 'current_turtle': 'none',
                  'pause_Game': False,'MacGuffin': 'None', 'Re_MacGuffin': False,
                'Act1':{'phase1':{
                                'Scene1':'inactive', 'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive',},
                        'phase2':{
                               'Scene1':'inactive', 'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive',},
                        'phase3':{
                               'Scene1':'inactive', 'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive',}
                    }
            }
Game_dialogue = {    'currAct':'none', 'currPhs': 'none', 'currSce':'none', 'current_name':'none',
                    'Enti_W_Dio':{'Bob': '','Sam': '','Pam': '','Computer': ''},
                'Act1':{
                    'Phase1':{
                            'Scene1':{
                                'General': [],'Bob':[],'Computer':[]},
                            'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive'},
                    'Phase2':{
                            'Scene1':'inactive', 'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive'},
                    'Phase3':{
                            'Scene1':'inactive', 'Scene2':'inactive', 'Scene3':'inactive','Scene4':'inactive','Scene5':'inactive',}}
            }
