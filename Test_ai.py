import time
from Turtle_Game_Data import Turtle_Game, Charcter, health_system
from Game_Turtles import*
from Player_controls import*
from Screen_Init import screen

def character_funct():
    Charcter.activate_chacters()
    
def set_maze():
    Generate_boss_mazes.load_next_maze()
    Generate_Maze.shift_map()
    Charcter.active_player.damege_calc(10)
def restore_health():
    Charcter.active_player.restor_calc(10)
    print(f'{10} points of health restored!')

def move_game():
    if Turtle_Game.Game_story['pause_Game'] == False:
        # phase1()
        Turtle_Game.set_map_speed()
        character_funct()
        move_backround()
        screen.update()
        screen.ontimer(move_game, 20)  # Use 16ms for ~60fps, or 20 for 50fps
screen.listen()
screen.onkeypress(press_up, 'w')
screen.onkeyrelease(release_up, 'w')
screen.onkeypress(press_down, 's')
screen.onkeyrelease(release_down, 's')
screen.onkeypress(press_left, 'a')
screen.onkeyrelease(release_left, 'a')
screen.onkeypress(press_right, 'd')
screen.onkeyrelease(release_right, 'd')
screen.onkey(set_maze, 'p')
screen.onkey(restore_health, '0')
move_game()
screen.mainloop()




