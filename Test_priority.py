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
    def move_objects(direction):
        all_entitys = entity.all_entity_objects
        for enti in all_entitys:
            if enti != Charcter.active_player:
                if direction == 'up' and Turtle_Game.map_settings['up'] == True: enti.actor.sety(enti.actor.ycor()-Turtle_Game.map_settings['UPS'])
                if direction == 'down' and Turtle_Game.map_settings['down'] == True: enti.actor.sety(enti.actor.ycor()+Turtle_Game.map_settings['DPS'])
                if direction == 'left' and Turtle_Game.map_settings['left'] == True: enti.actor.setx(enti.actor.xcor()+Turtle_Game.map_settings['LPS'])
                if direction == 'right' and Turtle_Game.map_settings['right'] == True: enti.actor.setx(enti.actor.xcor()-Turtle_Game.map_settings['RPS'])
        Generate_Maze.current_maze.move_walls(backround.xcor(), backround.ycor())

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
    def maintain_z_order(self):
        active_player = Charcter.active_player
        stack = Canvas.find_all()
        curr_layer = stack.index(active_player.actor.turtle._item)
        other_layer = stack.index(self.actor.turtle._item)
        if  curr_layer < other_layer and self.actor.ycor() > active_player.actor.ycor():
            Canvas.tag_raise(active_player.actor.turtle._item, self.actor.turtle._item) 
        elif curr_layer > other_layer and self.actor.ycor() <= active_player.actor.ycor():
            Canvas.tag_lower(active_player.actor.turtle._item, self.actor.turtle._item)
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

class Charcter(Turtle_Game, entity):
    charcters = [] # stores the names of all charcters
    charcters_objects = [] # stores the turtle all charcters
    active_player = 'None'
    Int_Direction = ['down', 'up', 'right', 'left']
    def __init__(self, name = "None", sprite = "None"):
        super().__init__(name, shape=sprite + '_FR.gif')
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
            Generate_Maze.wall_collision(Charcter.active_player)
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
    current_maze = 'none'

    def __init__(self, length, width, start_location = -1, size_of_start = 1):

        self.wall_dict = {}
        self.Nodes_dict = {}

        self.length = length
        self.width = width
        self.maze_size = length * width
        self.start_location =start_location
        
        self.start_marker = turtle.Turtle()
        self.start_marker.penup()
        self.start_marker.shape('circle')
        self.start_marker.shapesize(5, 5)
        self.start_marker.color('red')

        self.end_marker = turtle.Turtle()
        self.end_marker.shape('circle')
        self.end_marker.color('green')
        self.end_marker.shapesize(5, 5)
        self.end_marker.penup()

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
                    newWall = self.wall_section(H_start, V_start)
                    self.wall_dict[(H_start, V_start)] = newWall
                else:
                    newNode = self.Node_section(H_start, V_start)
                    self.Nodes_dict[(H_start, V_start)] = newNode
                V_start -= 100
            H_start += 100

        self.link_Nodes()
        self.link_walls()
        self.set_start()
        self.carve_maze()
        self.set_end()
        self.set_start()

    def set_start(self):
        x, y = self.actual_wdith, self.acutal_length
        if (self.start_location == 'center'):
            self.start_location = self.Nodes_dict.get((0,0))
        elif (self.start_location == 'top right'):
            self.start_location = self.Nodes_dict.get((x,y))
        elif (self.start_location == 'bottem right'):
            self.start_location = self.Nodes_dict.get((x,-y))
        elif (self.start_location == 'top left'):
            self.start_location = self.Nodes_dict.get((-x,y))
        elif (self.start_location == 'bottem left'):
            self.start_location = self.Nodes_dict.get((-x,-y))
        else:
            self.start_location = self.Nodes_dict[random.choice(list(self.Nodes_dict))]
        self.node_type = "start"

    def set_end(self):
        max_dist = -1
        furthest_node = self.start_location
        for node in self.Nodes_dict.values():
            if max_dist < node.nodes_from_start:
                max_dist = node.nodes_from_start
                furthest_node = node
        self.end_location = furthest_node
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

    def wall_collision(enti):
        if enti == Charcter.active_player and 0 in [enti.up, enti.down, enti.left, enti.right]:
            speed = Turtle_Game.map_settings['speed']
            for PS in ['UPS', 'DPS', 'LPS', 'RPS']:
                if Turtle_Game.map_settings[PS] == 0: Turtle_Game.map_settings[PS] = speed
        
        logic_x = (enti.actor.xcor() - backround.xcor())
        logic_y = (enti.actor.ycor() - backround.ycor())

        snap_x = round(logic_x / 100) * 100
        snap_y = round(logic_y / 100) * 100

        # print(logic_x, logic_y)
        # print(snap_x, snap_y)
        
        player_direction = Charcter.active_player.direction
        start = 0
        end = 0
        increment = 0

        Closest_Wall = Generate_Maze.wall_section.wall_dict.get((snap_x, snap_y))
        
        if Closest_Wall == None:
            if player_direction == 'up':
                Closest_Wall = Generate_Maze.wall_section.wall_dict.get((snap_x, snap_y + 100))
            elif player_direction == 'down':
                Closest_Wall = Generate_Maze.wall_section.wall_dict.get((snap_x, snap_y - 100))
            elif player_direction == 'left':
                Closest_Wall = Generate_Maze.wall_section.wall_dict.get((snap_x - 100, snap_y))
            elif player_direction == 'right':
                Closest_Wall = Generate_Maze.wall_section.wall_dict.get((snap_x + 100, snap_y))

        if Closest_Wall == None:
            return
        Closest_Wall.maintain_z_order(enti.actor)
        if Closest_Wall.active:
                    # Buffer: how many pixels 'thick' the collision zone is
                    Vertical_buffer = 50
                    Horizontal_buffer = 70

                    if player_direction == 'up':
                        # Check if Sam is in the X-lane AND between (Wall Bottom) and (Wall Center)
                        if Closest_Wall.wall_turtle.ycor() - Vertical_buffer <= enti.actor.ycor() <= Closest_Wall.wall_turtle.ycor() and \
                        Closest_Wall.wall_turtle.xcor() - 60 <= enti.actor.xcor() <= Closest_Wall.wall_turtle.xcor() + 60:
                            Turtle_Game.map_settings['UPS'] = 0

                        else:
                            Turtle_Game.map_settings['UPS'] = speed

                    elif player_direction == 'down':
                        # Check if Sam is between (Wall Center) and (Wall Top)
                        if Closest_Wall.wall_turtle.ycor() <= enti.actor.ycor() <= Closest_Wall.wall_turtle.ycor() + Vertical_buffer and \
                        Closest_Wall.wall_turtle.xcor() - 60 <= enti.actor.xcor() <= Closest_Wall.wall_turtle.xcor() + 60:
                            Turtle_Game.map_settings['DPS'] = 0
                        else:
                            Turtle_Game.map_settings['DPS'] = speed

                    elif player_direction == 'left':
                        # Check if Sam is between (Wall Center) and (Wall Right Edge)
                        if Closest_Wall.wall_turtle.xcor() <= enti.actor.xcor() <= Closest_Wall.wall_turtle.xcor() + Horizontal_buffer and \
                        Closest_Wall.wall_turtle.ycor() - 60 <= enti.actor.ycor() <= Closest_Wall.wall_turtle.ycor() + 60:
                            Turtle_Game.map_settings['LPS'] = 0
                        else:
                            Turtle_Game.map_settings['LPS'] = speed

                    elif player_direction == 'right':
                        # Check if Sam is between (Wall Left Edge) and (Wall Center)
                        if Closest_Wall.wall_turtle.xcor() - Horizontal_buffer <= enti.actor.xcor() <= Closest_Wall.wall_turtle.xcor() and \
                        Closest_Wall.wall_turtle.ycor() - 60 <= enti.actor.ycor() <= Closest_Wall.wall_turtle.ycor() + 60:
                            Turtle_Game.map_settings['RPS'] = 0
                        else:
                            Turtle_Game.map_settings['RPS'] = speed
        else:
            # If the wall is NOT active, ensure Sam can move freely
            Turtle_Game.map_settings['UPS'], Turtle_Game.map_settings['DPS'] = speed, speed
            Turtle_Game.map_settings['LPS'], Turtle_Game.map_settings['RPS'] = speed, speed

    def move_walls(self, back_x, back_y):
        # Only update walls that are on-screen or very close to the viewport.
        max_x = 1200 / 2 + 40  # Screen width / 2 + buffer
        min_x = -max_x
        max_y = 900 / 2 + 40  # Screen height / 2 + buffer
        min_y = -max_y
        
        self.start_marker.goto(self.start_location.xcor + back_x, self.start_location.ycor + back_y)
        self.end_marker.goto(self.end_location.xcor + back_x, self.end_location.ycor + back_y)

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
        print(f"All {len(self.Nodes_dict)} nodes Linked")

    def link_walls(self):
        for (x, y), wall in self.wall_dict.items():
            wall.left_wall = self.wall_dict.get((x - 100, y))
            wall.right_wall = self.wall_dict.get((x + 100, y))
            wall.up_wall = self.wall_dict.get((x, y + 100))
            wall.down_wall = self.wall_dict.get((x, y - 100))
        print(f"All {len(self.wall_dict)} walls Linked")

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

            self.nodes_from_start = 0
            

    class wall_section:
        wall_dict = {}
        def __init__(self, x, y):
            self.wall_turtle = turtle.Turtle()      
            self.wall_turtle.shape('tempWall (1).gif')
            self.wall_turtle.penup()
            self.wall_turtle.goto(x, y)
            self.setlocation = (x, y)
            print(f"Wall created at {x}, {y}")

            Generate_Maze.wall_section.wall_dict[(x, y)] = self
            
            self.active = True
            self.node_type = None

            self.left_wall = None
            self.right_wall = None
            self.up_wall = None
            self.down_wall = None
        def maintain_z_order(self, obj2):
            # stack = Canvas.find_all()
            # curr_layer = stack.index(obj2.turtle._item)
            # other_layer = stack.index(self.wall_turtle.turtle._item)
            # if  curr_layer < other_layer and self.wall_turtle.ycor() > obj2.ycor():
            Canvas.tag_raise(Charcter.active_player.actor.turtle._item, self.wall_turtle.turtle._item) 
            # elif curr_layer > other_layer and self.wall_turtle.ycor() <= obj2.ycor():
            #     Canvas.tag_lower(obj2.turtle.turtle._item, self.wall_turtle.turtle._item)
