import turtle
import random
from Screen_Init import screen, Canvas, backround
class Turtle_Game:
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
    Game_story = {   'playing_story':False, 'current_Act': 'none', 'current_phase': 'none', 'current_Scene': 'none',
                    'pause_Game': False,'MacGuffin': 'None', 'Re_MacGuffin': False, 'transition_timer': -1,
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
    def set_map_speed():
        # 1. Define the master speed
        speed = Turtle_Game.map_settings['speed']
        for key in ['UPS', 'DPS', 'LPS', 'RPS']:
            Turtle_Game.map_settings[key] = speed
    def move_objects(direction):
        all_entitys = entity.all_entity_objects
        for enti in all_entitys:
            if enti != Charcter.active_player:
                if direction == 'up' and Turtle_Game.map_settings['up'] == True: enti.actor.sety(enti.actor.ycor()-Turtle_Game.map_settings['UPS'])
                if direction == 'down' and Turtle_Game.map_settings['down'] == True: enti.actor.sety(enti.actor.ycor()+Turtle_Game.map_settings['DPS'])
                if direction == 'left' and Turtle_Game.map_settings['left'] == True: enti.actor.setx(enti.actor.xcor()+Turtle_Game.map_settings['LPS'])
                if direction == 'right' and Turtle_Game.map_settings['right'] == True: enti.actor.setx(enti.actor.xcor()-Turtle_Game.map_settings['RPS'])
        if Generate_boss_mazes.current_maze != None: Generate_boss_mazes.current_maze.move_walls(backround.xcor(), backround.ycor())
        health_system.track_player()

class entity:
    all_entity_names = []
    all_entity_objects = []
    directions = ('up', 'down', 'left', 'right')
    def __init__(self, name = "None", shape = "PT_FR.gif", hide = False):
        entity.all_entity_names.append(name)
        entity.all_entity_objects.append(self)
        self.name = name
        self.actor = turtle.Turtle()
        self.actor.shape(shape)
        if hide: self.actor.hideturtle()
        self.actor.speed(0)
        self.actor.penup()

        self.default_shape = 'None'

        self.active = False
        self.direction = 'up'
        self.default_direction = 'up'

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.print_type = 'None'
        self.conversable = False

        self.active_collisions = []

        self.speed = 5
        self.LPS, self.RPS, self.UPS, self.DPS = 5, 5, 5, 5

        self.animation_enabled = False
        self.lock_Animation = False
        self.lock = False
        self.Oscillate_ani = True
        self.move_timer = -4
    # def maintain_z_order(self):
    #     active_player = Charcter.active_player
    #     stack = Canvas.find_all()
    #     curr_layer = stack.index(active_player.actor.turtle._item)
    #     other_layer = stack.index(self.actor.turtle._item)
    #     if  curr_layer < other_layer and self.actor.ycor() > active_player.actor.ycor():
    #         Canvas.tag_raise(active_player.actor.turtle._item, self.actor.turtle._item) 
    #     elif curr_layer > other_layer and self.actor.ycor() <= active_player.actor.ycor():
    #         Canvas.tag_lower(active_player.actor.turtle._item, self.actor.turtle._item)
    def get_enti_direction(self, enti2):
        angel = self.actor.towards(enti2)
        if 315 < angel <= 360 or 0 <= angel <= 45:
            return 'right'
        elif 45 < angel <= 135:
            return 'up'
        elif 135 < angel <= 225:
            return 'left'
        elif 225 < angel <= 315:
            return 'down'
    def set_movement_permissions(self):
        direction = self.direction
        actor = self.actor
        if direction == 'up' and self.up == True: actor.sety(actor.ycor() + self.UPS)
        if direction == 'down' and self.down == True: actor.sety(actor.ycor() - self.DPS)
        if direction == 'left' and self.left == True: actor.setx(actor.xcor() - self.LPS)
        if direction == 'right' and self.right == True: actor.setx(actor.xcor() + self.RPS)    
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

class health_system:
    bars = []
    def __init__(self, type = "player", health = 100):
        self.current_health = health
        self.max_health = health
        self.current_shift = 0
        self.damege_bar = turtle.Turtle()
        self.health_bar = turtle.Turtle()
        self.damege_bar.penup()
        self.health_bar.penup()
        self.damege_bar.shape('square')
        self.health_bar.shape('square')
        self.damege_bar.color('black', 'red')
        self.health_bar.color('black', 'green')
        self.base_width = 1
        self.base_length = 1
        if type == 'player': self.base_length, self.base_width = 0.5, 4
        self.damege_bar.turtlesize(self.base_length, self.base_width)
        self.health_bar.turtlesize(self.base_length, self.base_width)
        health_system.bars.append(self)
    def track_player():
        for player in health_system.bars:
            player.damege_bar.goto(player.actor.xcor(), player.actor.ycor()+30)
            player.health_bar.goto(player.actor.xcor() - player.current_shift, player.actor.ycor()+30)
            stack = Canvas.find_all()
            if stack.index(player.health_bar.turtle._item) != stack.index(player.actor.turtle._item)-1:
                Canvas.tag_lower(player.health_bar.turtle._item, player.actor.turtle._item)
                Canvas.tag_lower(player.health_bar.turtle._item, player.actor.turtle._item)

    def damege_calc(self, damage):
        self.current_health -= damage
        if self.current_health < 0: self.current_health = 0
        percent_remaining = self.current_health / self.max_health
        new_width = percent_remaining * self.base_width
        if self.current_health <= 0:
            new_width = 0.01
        self.current_shift = (self.base_width - new_width) * 10
        
        self.health_bar.turtlesize(0.5, new_width)
        print(f'Current Health: {self.current_health}')
    def restore_calc(self, restored):
        self.current_health += restored
        percent_remaining = self.current_health / self.max_health
        if self.current_health <= 100:
            new_width = percent_remaining * self.base_width
        else:
            new_width = 0.01
        self.current_shift = (self.base_width - new_width) * 10
        
        self.health_bar.turtlesize(0.5, new_width)
        print(f'Current Health: {self.current_health}')

class Charcter(Turtle_Game, entity, health_system):
    charcters = [] # stores the names of all charcters
    charcters_objects = [] # stores the turtle all charcters
    active_player = 'None'
    Int_Direction = ['down', 'up', 'right', 'left']
    def __init__(self, name = "None", sprite = "None"):
        entity.__init__(self, name, shape=sprite + '_FR.gif')
        health_system.__init__(self, 'player', 200)
        Charcter.charcters.append(name)
        Charcter.charcters_objects.append(self)
        

        self.canInteract = False
        self.vision_range = 55
        self.Collision_range = 40

        self.up_ani = {'frame1':sprite+'_BL.gif','frame2':sprite+'_BS.gif','frame3':sprite+'_BR.gif'}
        self.down_ani = {'frame1':sprite+'_FL.gif','frame2':sprite+'_FS.gif','frame3':sprite+'_FR.gif'}
        self.left_ani = {'frame1':sprite+'_LL.gif','frame2':sprite+'_LS.gif','frame3':sprite+'_LR.gif'}
        self.right_ani = {'frame1':sprite+'_RL.gif','frame2':sprite+'_RS.gif','frame3':sprite+'_RR.gif'}
        self.entity_sprites = [self.up_ani, self.down_ani, self.left_ani, self.right_ani]
    def activate_chacters():
        if not Charcter.map_settings['lock_map']:
            Charcter.active_player.activate_player_ani()
            # print(Generate_Maze.current_maze)
            # if (Generate_Maze.current_maze != None):
            #     Generate_Maze.wall_collsions(Charcter.active_player)
            #     Generate_Maze.maintain_z_order(Charcter.active_player)
            # Charcter.active_player.hit_box()
        # for enti in Charcter.charcters_objects:
        #     if enti != Charcter.active_player or Turtle_Game.map_settings['lock_map']:
        #         enti.set_direction()
        #         enti.animate_entity()
                # enti.maintain_z_order()
                # enti.Observe_Player()
        #         enti.set_movement_permissions()
    def set_direction(self):
        if self.up: self.direction  = 'up'
        elif self.down: self.direction  = 'down'
        elif self.left: self.direction  = 'left'
        elif self.right: self.direction  = 'right'
    def activate_player_ani(self):
        index =self.directions.index(self.map_settings['direction'])
        locks = [self.map_settings['up'], self.map_settings['down'], self.map_settings['left'], self.map_settings['right']]
        self.animate_entity(index , locks)
    def animate_entity(self, index = -1, locks = []):
        current_lock = False
        if index == -1:
            locks = [self.up, self.down, self.left, self.right]
            index = self.directions.index(self.direction)
        for lock in locks:
                    if lock == True: current_lock = lock
        if self == Charcter.active_player or True in [self.up, self.down, self.left, self.right]:
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
    def Observe_Player(self):
        active_only = Charcter.active_player.actor.distance(self.actor) <= self.vision_range
        locks = [self.up, self.down, self.left, self.right]
        if not active_only and (not self.map_settings['lock_map'] or True not in locks):
            for enti in Charcter.charcters_objects:
                actor = enti.actor
                if actor.isvisible() and enti != self:
                    if actor.distance(self.actor) <= self.vision_range:
                        direction = self.get_enti_direction(actor)
                        index = self.directions.index(direction)
                        direction_sprites = self.entity_sprites[index]
                        self.actor.shape(direction_sprites['frame2'])
        elif not self.map_settings['lock_map'] and active_only:
            direction = self.get_enti_direction(Charcter.active_player.actor)
            index = self.directions.index(direction)
            direction_sprites = self.entity_sprites[index]
            self.actor.shape(direction_sprites['frame2'])             
    def hit_box(self):
        if self == Charcter.active_player:
            speed = Turtle_Game.map_settings['speed']
            for PS in ['UPS', 'DPS', 'LPS', 'RPS']:
                if Turtle_Game.map_settings[PS] == 0: Turtle_Game.map_settings[PS] = speed
        for enti in Charcter.charcters_objects:
            if enti.actor.isvisible() and  enti != self:
                if enti not in self.active_collisions:
                    if enti.actor.distance(self.actor) <= self.Collision_range:
                        self.active_collisions.append(enti)
                elif enti in self.active_collisions:
                    if enti.actor.distance(self.actor) > self.Collision_range:
                        self.active_collisions.remove(enti)
        for enti in self.active_collisions:
            direction = self.get_enti_direction(enti.actor)
            index = self.directions.index(direction)
            if self == Charcter.active_player:
                dir = Turtle_Game.map_settings['Dir_speeds'][index]
                Turtle_Game.map_settings[dir] = 0  

class static_entity(Turtle_Game, entity):
    static_entity_names = []
    static_entity_objects = []
    def __init__(self = "None", name = "None", sprite = "None", hide = False):
        super().__init__(name, 'tempWall (1).gif', hide)

        static_entity.static_entity_names.append(name)
        static_entity.static_entity_objects.append(self)
    
        moveable = False

        static_antimation = {}

class Generate_Maze:
    current_maze = None
    start_marker = None
    end_marker = None
    def __init__(self, length, width, start_location = -1, size_of_start = 1):

        self.wall_dict = {}
        self.Nodes_dict = {}

        self.length = length
        self.width = width
        self.maze_size = length * width
        self.start_location =start_location
        self.cords = None
        self.num_walls = 0
        if Generate_Maze.start_marker == None:
            Generate_Maze.start_marker = turtle.Turtle()
            Generate_Maze.start_marker.penup()
            Generate_Maze.start_marker.shape('circle')
            Generate_Maze.start_marker.color('red')

            Generate_Maze.end_marker = turtle.Turtle()
            Generate_Maze.end_marker.shape('circle')
            Generate_Maze.end_marker.color('green')
            Generate_Maze.end_marker.penup()

        self.end_location = None

        self.actual_wdith = 0
        self.acutal_length = 0

        if (width%2 == 0): self.actual_wdith = - ((width+1) * 100)
        elif (width%2 == 1): self.actual_wdith = - (width * 100)
        if (length%2 == 0): self.acutal_length = ((length+1) * 100)
        elif (length%2 == 1): self.acutal_length = (length * 100)

        V_start = self.acutal_length
        H_start = self.actual_wdith
        for i in range((width*2)+1):
            V_start = self.acutal_length 
            for j in range((length*2)+1):
                if (i%2 == 0 or j%2 == 0):
                    newWall = wall_section(H_start, V_start, self.num_walls)
                    self.num_walls += 1
                    self.wall_dict[(H_start, V_start)] = newWall
                else:
                    newNode = Node_section(H_start, V_start)
                    self.Nodes_dict[(H_start, V_start)] = newNode
                V_start -= 100
            H_start += 100

        self.link_Nodes()
        self.link_walls()
        self.set_start()
        self.carve_maze()
        self.set_end()

    def set_start(self):
        # if 
        x, y = self.actual_wdith, self.acutal_length
        if (self.start_location == 'center'):
            self.start_location = self.Nodes_dict.get((0,0))
        elif (self.start_location == 'top right'):
            self.start_location = self.Nodes_dict.get((x,y))
        elif (self.start_location == 'bottem right'):
            self.start_location = self.Nodes_dict.get((x,-y))
        elif (self.start_location == 'top left'):
            x, y = self.actual_wdith + 100, self.acutal_length - 100
            print(x, y)
            self.start_location = self.Nodes_dict.get((x,y))
        elif (self.start_location == 'bottem left'):
            self.start_location = self.Nodes_dict.get((-x,-y))
        else:
            self.start_location = self.Nodes_dict[random.choice(list(self.Nodes_dict))]
        self.type = "start"
        Generate_Maze.start_marker.goto(self.start_location.xcor, self.start_location.ycor)

    def set_end(self):
        max_dist = -1
        furthest_node = self.start_location
        for node in self.Nodes_dict.values():
            if max_dist < node.nodes_from_start:
                max_dist = node.nodes_from_start
                furthest_node = node
        self.end_location = furthest_node
        Generate_Maze.end_marker.goto(self.end_location.xcor, self.end_location.ycor)

    def carve_maze(self):
        currNode = self.start_location
        self.start_location.nodes_from_start = 0
        stack = [currNode]
        visited = {currNode}
        dist = 0
        while stack:
            dist = currNode.nodes_from_start
            neighbors = []
            if currNode.up_node and currNode.up_node not in visited:
                neighbors.append(('up', currNode.up_node, currNode.up_wall))
            if currNode.down_node and currNode.down_node not in visited:
                neighbors.append(('down', currNode.down_node, currNode.down_wall))
            if currNode.left_node and currNode.left_node not in visited:
                neighbors.append(('left', currNode.left_node, currNode.left_wall))
            if currNode.right_node and currNode.right_node not in visited:
                neighbors.append(('right', currNode.right_node, currNode.right_wall))
            if neighbors:
                direction, nextNode, wall = random.choice(neighbors)
                wall.active = False
                wall.wall_turtle.hideturtle()
                visited.add(nextNode)
                stack.append(nextNode)
                currNode = nextNode
                currNode.nodes_from_start = dist + 1
            else:
                stack.pop()
                if stack:
                    currNode = stack[-1]

    def get_closest_node(enti):
        logic_y = (enti.actor.ycor() - backround.ycor())
        logic_x = (enti.actor.xcor() - backround.xcor())

        snap_x = round(logic_x / 200) * 200
        snap_y = round(logic_y / 200) * 200

        Closest_Node = Generate_Maze.current_maze.Nodes_dict.get((snap_x, snap_y))
        
        return Closest_Node

    def wall_collsions(enti):
        Closest_Node =  Generate_Maze.get_closest_node(enti)
        V_BUF = 55
        H_BUF = 70
        VW_BUF = 60
        HW_BUF = 50
        conditions = {
            'up': {
                'walls': [Closest_Node.up_wall, Closest_Node.top_left_wall, Closest_Node.top_right_wall],
                'check': lambda w: (w.ycor() - V_BUF <= enti.actor.ycor() <= w.ycor()) and \
                                (w.xcor() - VW_BUF <= enti.actor.xcor() <= w.xcor() + VW_BUF)
            },
            'down': {
                'walls': [Closest_Node.down_wall, Closest_Node.lower_left_wall, Closest_Node.lower_right_wall],
                'check': lambda w: (w.ycor() <= enti.actor.ycor() <= w.ycor() + V_BUF) and \
                                (w.xcor() - VW_BUF <= enti.actor.xcor() <= w.xcor() + VW_BUF)
            },
            'right': {
                'walls': [Closest_Node.right_wall, Closest_Node.top_right_wall, Closest_Node.lower_right_wall],
                'check': lambda w: (w.xcor() - H_BUF <= enti.actor.xcor() <= w.xcor()) and \
                                (w.ycor() - HW_BUF <= enti.actor.ycor() <= w.ycor() + HW_BUF)
            },
            'left': {
                'walls': [Closest_Node.left_wall, Closest_Node.top_left_wall, Closest_Node.lower_left_wall],
                'check': lambda w: (w.xcor() <= enti.actor.xcor() <= w.xcor() + H_BUF) and \
                                (w.ycor() - HW_BUF <= enti.actor.ycor() <= w.ycor() + HW_BUF)
            }
        }
        data = conditions.get(enti.direction)
        if data:
            for wall_obj in data['walls']:
                if wall_obj and wall_obj.active:
                    # 'data['check']' is the lambda function. 
                    # We pass 'wall_obj.wall_turtle' as 'w'
                    if data['check'](wall_obj.wall_turtle):
                        # Stop the movement for that direction
                        setting_key = f"{enti.direction[0].upper()}PS" # Result: 'UPS', 'DPS', etc.
                        Turtle_Game.map_settings[setting_key] = 0
                        break

    def maintain_z_order(enti):
        Closest_Node =  Generate_Maze.get_closest_node(enti)

        if (Closest_Node == None): return
    
        stack = Canvas.find_all()
        enti_data = enti.actor.turtle._item
        enti_index = stack.index(enti_data)

        left_wall = Closest_Node.left_wall
        if (left_wall != None and enti_index > stack.index(left_wall.wall_turtle.turtle._item)):
            Canvas.tag_raise(left_wall.wall_turtle.turtle._item, enti_data)
        right_wall = Closest_Node.right_wall
        if (right_wall != None and enti_index > stack.index(right_wall.wall_turtle.turtle._item)):
            Canvas.tag_raise(right_wall.wall_turtle.turtle._item, enti_data)
        up_wall = Closest_Node.up_wall
        if (up_wall != None and enti_index < stack.index(up_wall.wall_turtle.turtle._item)):
            Canvas.tag_lower(up_wall.wall_turtle.turtle._item, enti_data)
        down_wall = Closest_Node.down_wall
        if (down_wall != None and enti_index > stack.index(down_wall.wall_turtle.turtle._item)):
            Canvas.tag_raise(down_wall.wall_turtle.turtle._item, enti_data)
        top_right_wall = Closest_Node.top_right_wall


        if (top_right_wall != None and enti_index < stack.index(top_right_wall.wall_turtle.turtle._item)):
            Canvas.tag_lower(top_right_wall.wall_turtle.turtle._item, enti_data)
        top_left_wall = Closest_Node.top_left_wall
        if (top_left_wall != None and enti_index < stack.index(top_left_wall.wall_turtle.turtle._item)):
            Canvas.tag_lower(top_left_wall.wall_turtle.turtle._item, enti_data)
        lower_right_wall = Closest_Node.lower_right_wall
        if (lower_right_wall != None and enti_index > stack.index(lower_right_wall.wall_turtle.turtle._item)):
            Canvas.tag_raise(lower_right_wall.wall_turtle.turtle._item, enti_data)
        lower_left_wall = Closest_Node.lower_left_wall
        if (lower_left_wall != None and enti_index > stack.index(lower_left_wall.wall_turtle.turtle._item)):
            Canvas.tag_raise(lower_left_wall.wall_turtle.turtle._item, enti_data)

    def move_walls(self, back_x, back_y):
        # Only update walls that are on-screen or very close to the viewport.
        max_x = 1200 / 2 + 40  # Screen width / 2 + buffer
        min_x = -max_x
        max_y = 900 / 2 + 40  # Screen height / 2 + buffer
        min_y = -max_y
        
        Generate_Maze.start_marker.goto(self.start_location.xcor + back_x, self.start_location.ycor + back_y)
        Generate_Maze.end_marker.goto(self.end_location.xcor + back_x, self.end_location.ycor + back_y)

        for wall in self.wall_dict.values():
            if not wall.active:
                if wall.wall_turtle.isvisible():
                    wall.wall_turtle.hideturtle()
                continue
            x = wall.setlocation[0] + back_x
            y = wall.setlocation[1] + back_y
            if x < min_x or x > max_x or y < min_y or y > max_y:
                if wall.wall_turtle.isvisible():
                    wall.wall_turtle.hideturtle()
            else:
                wall.wall_turtle.goto(x, y)
                if not wall.wall_turtle.isvisible():
                    wall.wall_turtle.showturtle()
        
    def link_Nodes(self):
        for (x, y), node in self.Nodes_dict.items():
            node.left_wall = self.wall_dict.get((x - 100, y))
            node.right_wall = self.wall_dict.get((x + 100, y))
            node.up_wall = self.wall_dict.get((x, y + 100))
            node.down_wall = self.wall_dict.get((x, y - 100))
            
            node.left_node = self.Nodes_dict.get((x - 200, y))
            node.right_node = self.Nodes_dict.get((x + 200, y))
            node.up_node = self.Nodes_dict.get((x, y + 200))
            node.down_node = self.Nodes_dict.get((x, y - 200))

            node.top_right_wall = self.wall_dict.get((x + 100, y + 100))
            node.top_left_wall = self.wall_dict.get((x - 100, y + 100))
            node.lower_right_wall = self.wall_dict.get((x + 100, y - 100))
            node.lower_left_wall = self.wall_dict.get((x - 100, y - 100))

    def link_walls(self):
        for (x, y), wall in self.wall_dict.items():
            wall.left_wall = self.wall_dict.get((x - 100, y))
            wall.right_wall = self.wall_dict.get((x + 100, y))
            wall.up_wall = self.wall_dict.get((x, y + 100))
            wall.down_wall = self.wall_dict.get((x, y - 100))

    def shift_map():
        x, y = Generate_Maze.start_marker.xcor(), Generate_Maze.end_marker.ycor()
        print(x,y)
        backround.goto(backround.xcor() - x, backround.ycor() - y)
        Generate_Maze.start_marker.goto(Generate_Maze.start_marker.xcor() - x, Generate_Maze.start_marker.ycor() - y)
        Generate_Maze.end_marker.goto(Generate_Maze.end_marker.xcor() - x, Generate_Maze.end_marker.ycor() - y)
        for wall in Generate_Maze.current_maze.wall_dict.values():
            # Subtract start location to center maze at 0,0
            wall_turtle = wall.wall_turtle
            wall_turtle.goto(wall_turtle.xcor() + backround.xcor(), wall_turtle.ycor() + backround.ycor())

class Node_section:
    floor_tiles = []
    def __init__(self, x, y):
        self.left_wall = None
        self.right_wall = None
        self.up_wall = None
        self.down_wall = None
        self.xcor = x
        self.ycor = y
        self.left_node = None
        self.right_node = None
        self.up_node = None
        self.down_node = None

        self.top_right_wall = None
        self.top_left_wall = None
        self.lower_right_wall = None
        self.lower_left_wall = None

        self.nodes_from_start = 0
        print(f"Node created atn {x, y}")
        
class wall_section:
    wall_dict = {}
    walls = []
    total_Walls = 0
    def __init__(self, x, y, num_Walls):
        if num_Walls < wall_section.total_Walls:
            self.wall_turtle = wall_section.walls[num_Walls]
        else:
            self.wall_turtle = turtle.Turtle()
            # self.wall_turtle.hideturtle()
            wall_section.walls.append(self.wall_turtle)
            wall_section.total_Walls += 1
            # print(f"Wall created at {x}, {y}")
        self.wall_turtle.shape('tempWall (1).gif')
        self.wall_turtle.penup()
        self.wall_turtle.goto(x, y)
        self.setlocation = (x, y)

        wall_section.wall_dict[(x, y)] = self
        
        self.active = True
        self.lock = False
        self.type = None

        self.left_wall = None
        self.right_wall = None
        self.up_wall = None
        self.down_wall = None

    def maintain_z_order(self, enti):
        if enti.direction == 'up':
            Canvas.tag_raise(self.up_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
            Canvas.tag_lower(self.down_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
        if enti.direction == 'down':
            Canvas.tag_raise(self.up_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
            Canvas.tag_raise(self.down_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
        if enti.direction == 'left':
            Canvas.tag_raise(self.up_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
            Canvas.tag_raise(self.down_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
        if enti.direction == 'right':
            Canvas.tag_raise(self.up_wall.wall_turtle.turtle._item, enti.actor.turtle._item)
            Canvas.tag_raise(self.down_wall.wall_turtle.turtle._item, enti.actor.turtle._item)

class Generate_boss_mazes:
    all_mazes = []
    all_boss_mazes = []
    current_boss_mazes = None
    current_maze = None

    def __init__(self, numMazes=1, length=3, width=3, start=-1, sprite_sheet='Karel_wall'):
        self.current_maze = None
        self.mazes = []
        for i in range(numMazes):
            maze = Generate_Maze(length, width)
            self.mazes.append(maze)
            Generate_boss_mazes.all_mazes.append(maze)
        
        # Add this specific boss set instance to the master list
        Generate_boss_mazes.all_boss_mazes.append(self)
    @classmethod
    def reset_maze(cls):
        # Loop 1: The "View" (The physical Turtles)
        # Goal: Make sure only the walls for the current maze are visible
        for wall in wall_section.walls:
            if wall in cls.current_maze.wall_dict:
                wall.showturtle()
            else:
                wall.hideturtle()

        # Loop 2: The "Model" (The Information Nodes)
        # Goal: Disable the logic/collisions for walls that aren't here
        for wallNode in wall_section.wall_dict:
            if wallNode not in cls.current_maze.wall_dict:
                # If the information node isn't in our current maze, lock it
                # wall_section.wall_dict[wallNode] likely gets the actual object
                wall_section.wall_dict[wallNode].lock = True
            else:
                # If it IS in our maze, make sure it's unlocked
                wall_section.wall_dict[wallNode].lock = False
        Generate_Maze.shift_map()

    @classmethod
    def load_next_maze(cls):
        # 1. Handle Game Start
        if cls.current_boss_mazes is None:
            if not cls.all_boss_mazes:
                print("No boss mazes exist to load!")
                return
            cls.current_boss_mazes = cls.all_boss_mazes[0]
            # Set BOTH the instance-level and class-level pointers
            cls.current_boss_mazes.current_maze = cls.current_boss_mazes.mazes[0]
            cls.current_maze = cls.current_boss_mazes.current_maze
            Generate_Maze.current_maze = cls.current_maze

        else:
            # 2. Check current progress
            current_set = cls.current_boss_mazes
            try:
                index = current_set.mazes.index(current_set.current_maze)
            except ValueError:
                index = -1

            # 3. Move to next maze in set
            if index + 1 < len(current_set.mazes):
                current_set.current_maze = current_set.mazes[index + 1]
                # Update the Class-level master pointer
                cls.current_maze = current_set.current_maze
                Generate_Maze.current_maze = current_set.current_maze
                print(f"Moving to Maze {index + 2}...")
                
            else:
                # 4. Switch to next Boss Set
                boss_index = cls.all_boss_mazes.index(current_set)
                
                if boss_index + 1 < len(cls.all_boss_mazes):
                    cls.current_boss_mazes = cls.all_boss_mazes[boss_index + 1]
                    # Reset pointers for the new set
                    cls.current_boss_mazes.current_maze = cls.current_boss_mazes.mazes[0]
                    cls.current_maze = cls.current_boss_mazes.current_maze
                    Generate_Maze.current_maze = current_set.current_maze
                    print(f"Moving to Boss Set {boss_index + 2}.")
                else:
                    print("Victory! All boss sets cleared.")
                    # cls.current_maze = None # Game is over
        cls.reset_maze()


        
        
        