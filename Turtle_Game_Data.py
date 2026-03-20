Game_settings = {'HitBoxes_on': False,'Talking_to': 'None', 'General_timer': -1}
Game_entities =  { 'turtles':{},
                    'characters':{'Sam', 'Bob', 'Pam', 'Computer'},
                    'enities':['Sam', 'Bob', 'Pam', 'Computer','paper','phone'],
                    'objects':{'Computer'},
                    
                    'current_turtle':'None', 'current_info':'backround',
                    'backround': {'turtle': 'None','direction': 'up','lock_Obj':False, 'set_turtle':False,
                           'switch': False, 'speed':5,'up':False,'down':False,'left':False,'right':False,
                           'LPS':5,'RPS':5,'UPS':5,'DPS':5,
                           },

                    'Sam': {'turtle': 'None', 'turtle2': 'None',
                            
                            'lock':False, 'set_turtle':False,

                            'print_type':'auto', 'Can_speak': False,

                            'animation_enabled':False,
                            'lock_Animation':False,
                            'Oscillate_ani': True,
                            'move_timer':-4,
                            
                            'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5,

                            'direction': 'up', 'default_direction':'up',
                            'up':False,'down':False,'left':False,'right':False,
                            'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                            'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                            'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                            'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'},
                           },

                    'Bob': {'turtle': 'None', 'turtle2': 'None',
                            
                            'lock':False, 'set_turtle':False,

                            'print_type':'auto', 'Can_speak': False,

                            'animation_enabled':False,
                            'lock_Animation':False,
                            'Oscillate_ani': True,
                            'move_timer':-4,
                            
                            'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5,

                            'direction': 'up', 'default_direction':'up',
                            'up':False,'down':False,'left':False,'right':False,
                            'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                            'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                            'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                            'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'},
                           },

                    'Pam': {'turtle': 'None', 'turtle2': 'None',
                            
                            'lock':False, 'set_turtle':False,

                            'print_type':'auto', 'Can_speak': False,

                            'animation_enabled':False,
                            'lock_Animation':False,
                            'Oscillate_ani': True,
                            'move_timer':-4,
                            
                            'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5,

                            'direction': 'up', 'default_direction':'up',
                            'up':False,'down':False,'left':False,'right':False,
                            'up_ani':{'frame1':'PT_BL.gif','frame2':'PT_BS.gif','frame3':'PT_BR.gif'},
                            'down_ani':{'frame1':'PT_FL.gif','frame2':'PT_FS.gif','frame3':'PT_FR.gif'},
                            'left_ani':{'frame1':'PT_LL.gif','frame2':'PT_LS.gif','frame3':'PT_LR.gif'},
                            'right_ani':{'frame1':'PT_RL.gif','frame2':'PT_RS.gif','frame3':'PT_RR.gif'},
                            },
                    'paper':{'turtle': 'None', 'turtle2': 'None',
                             'direction': 'down','state':False, 'set_turtle':False,'Can_speak': False,
                             'up':False,'down':False,'left':False,'right':False,'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5,
                            },
                    'phone':{'turtle': 'None', 'turtle2': 'None',
                             'direction': 'down','state':False, 'set_turtle':False,'Can_speak': False,
                             'up':False,'down':False,'left':False,'right':False,'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5},
                    'Computer':{'turtle': 'None', 'turtle2': 'None',
                             'direction': 'down','state':False, 'set_turtle':False,'print_type':'auto','Can_speak': False,'default_direction':'up',
                             'up':False,'down':False,'left':False,'right':False,'speed':5,'LPS':5,'RPS':5,'UPS':5,'DPS':5}
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