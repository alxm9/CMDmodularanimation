import itertools
import time
import os 
import curses
from curses import wrapper
from operator import attrgetter
import ctypes

def maximize_terminal(): # windows only
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, SW_MAXIMISE)

maximize_terminal()


clear = lambda: os.system('cls')

os.system("") # I need to remember why I put this here

class spritesheet():
    def gather_framelist(self):
        frameslist = []
        for frame in range(1,self.frames+1):
            path = os.path.join("spritesheets","{0}".format(self.path), "txt", "ascii-art ({0}).txt".format(frame)) ## os.path.join works regardless of OS
            file = open(path, "r", encoding="utf-8")
            frameslist.append(file.read())
            file.close()
        return frameslist
        
    def __init__(self, path, color, zlevel = 0, frames = 0, dx = 0, dy = 0, delay = 0):
        self.path = path
        self.color = color ##escape code
        self.zlevel = zlevel
        self.frames = frames
        self.dx = dx # not implemented
        self.dy = dy # not implemented
        self.delay = delay # not implemented
        self.frameslist = self.gather_framelist() # testing {self: [frame1, frame2,..],...}
        
    def get_whatever(self, attr): # pull attribute as object:attribute dict
        return {self: getattr(self, attr)}
    
    def get_flatvalue(self, attr):
        return getattr(self, attr)
        
# All txt frames should have the same amount of lines and same col at the end of a line. For now.
##################### path, escape code color, z-level, frames
outline = spritesheet("bg","\033[37m", zlevel = 22, frames = 1)
circle = spritesheet("circle","\033[94m", zlevel = 6, frames = 5)
square = spritesheet("square","\033[32m", zlevel = 4, frames = 5)
lightning = spritesheet("lightning","\033[32m", zlevel = 5, frames = 5)
dude = spritesheet("dude", "\033[32m", zlevel= 5, frames = 28)
frontpillars = spritesheet("frontpillars","\033[31m", zlevel = 8, frames = 28)
backpillars = spritesheet("backpillars","\033[31m", zlevel = 2, frames = 28)
outline = spritesheet("outline1", "\033[37m", zlevel = 99, frames = 1)

fire2 = spritesheet("fire2", "\033[31m", zlevel = 8, frames = 95)
building1 = spritesheet("building1", "\033[37m", zlevel = 7, frames = 95)
fire = spritesheet("fire", "\033[31m", zlevel = 6, frames = 95)
heli = spritesheet("heli", "\033[90m", zlevel = 5, frames = 95)
skyscraper = spritesheet("skyscraper", "\033[37m", zlevel = 4, frames = 95)
fire3 = spritesheet("fire3", "\033[31m", zlevel = 3, frames = 95)
citybg = spritesheet("citybg", "\033[37m", zlevel = 2, frames = 95)
pulse = spritesheet("pulse", "\033[31m", zlevel = 1, frames = 95)
climbers = spritesheet("climbers", "\033[32m", zlevel = 10, frames = 95)
dudeontop = spritesheet("dudeontop", "\033[94m", zlevel = 11, frames = 95)
moon = spritesheet("moon", "\033[31m", zlevel = 0.5, frames = 1)

intro_male_eyes = spritesheet("intro_male_eyes", "\033[37m", zlevel = 5, frames = 38)
intro_male_body = spritesheet("intro_male_body", "\033[94m", zlevel = 3, frames = 1)
intro_male_hair = spritesheet("intro_male_hair", "\033[90m", zlevel = 10, frames = 1)
bed = spritesheet("bed", "\033[90m", zlevel = 0.1, frames = 1)
pillow = spritesheet("pillow", "\033[37m", zlevel = 0.2, frames = 1)

def adjust_to_max(list_framelists, max_frame): # adjusts to max frame
    for list in list_framelists:
        if len(list) < max_frame: # extends frames by last frame
            list.extend([list[-1]]*(max_frame - len(list)))
    return list_framelists
        
#### CURSES #############################################################################
#### WIP
def run_animation_curses(win, *args): #First arg should be edge/bg.
    max_frame = max(args, key=attrgetter('frames')).frames
    list_framelists = [i.frameslist for i in args]
    list_framelists = adjust_to_max(list_framelists, max_frame)
    for framelist in zip(*list_framelists): # * unpacks list_framelists into n different lists (objs)
        print_frame_curses(framelist,win,args)
        win.move(0,0)
        win.refresh()
        time.sleep(0.05)
        
def print_stillshot_curses(framenumlist,win, *args): # [1,4], dude, backpillars
    max_frame = max(args, key=attrgetter('frames')).frames
    list_framelists = [i.frameslist for i in args]
    list_framelists = adjust_to_max(list_framelists, max_frame)
    frames_to_print = []
    counter = 0
    for i in range(len(args)):
        frames_to_print.append(list_framelists[i][framenumlist[counter]])
        counter += 1
    for framelist in zip(*frames_to_print): # * unpacks list_framelists into n different lists (objs)
        print_frame_curses(framelist,win,args)
        
def print_frame_curses(framelist,win, args):
    for chars in zip(*framelist): # framelist unpacked into char number of different characters
        z_char_color = {}
        compare = []
        if all(" " in t for t in chars): # if all 3 chars are " " 
            win.addstr(" ")
            continue
        for i in range(len(chars)): # zlevel: [char, color]
            z_char_color[args[i].zlevel] = [chars[i], args[i].color]
        for i in z_char_color:
            if z_char_color[i][0] != " ":
                compare.append(i)
        to_print=compare[0]
        for i in compare:
            if i > to_print:
                to_print = i
        win.addstr(z_char_color[to_print][0])

def main(stdscr): ### WIP
    # def maximizer():
        # while True:
            # key = stdscr.getch()
            # if key == curses.KEY_RESIZE:
                # maximize_terminal()
    # maximizer = threading.Thread(target=maximizer)
    # maximizer.start()
    maximize_terminal()
    terminal_height, terminal_width = stdscr.getmaxyx()
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.nodelay(True)
    height_1, width_1 = 52, 102
    display_win = curses.newwin(height_1, width_1, 0, 0)
    stdscr.scrollok(1)
    display_win.scrollok(1)
    current_scene = ([22,3,10],display_win, dude, backpillars, frontpillars)
    intro_2 = (display_win,intro_male_body,intro_male_hair,intro_male_eyes,outline, bed, pillow)
    intro_1 = (display_win,fire,fire2,fire3,skyscraper,building1,heli,citybg,pulse, climbers, dudeontop, moon, outline)
    # print_stillshot_curses(*current_scene) ## ([frames to print for each arg], curses window, unlimited args..)
    run_animation_curses(*intro_1)
    run_animation_curses(*intro_2)
    display_win.refresh()
    display_win.clear()
    # clear()
    # print_stillshot_curses(*current_scene)
    while True:
        # scene = copy.copy(current_scene)
        # display_win = curses.newwin(height_1, width_1, 0, 0)
        terminal_height, terminal_width = stdscr.getmaxyx()
        display_win.refresh()
        display_win.clear()
        display_win.scrollok(1)
        print_stillshot_curses(*current_scene) ## ([frames to print for each arg], curses window, unlimited args..)
        display_win.refresh()
        display_win.clear()
        time.sleep(0.2)
        stdscr.refresh()
        stdscr.clear()
        while (terminal_height < 50) or (terminal_width < 50):
            clear()

wrapper(main)
# screen = curses.initscr()
# display_win = curses.newwin(50, 103, 11, 75)
# print_stillshot_curses([22,3,10],display_win, dude, backpillars, frontpillars) ## ([frames to print for each arg], curses window, unlimited args..)
# display_win.getch()
clear()

# resize = curses.is_term_resized(y, x)

##### Prints a still frame. The list contains the frame of each argument you want to print. 22 - dude, 3 - backpillars, 10 - frontpillars
##### There is a curses version of this a few lines up
# print_stillshot([22,3,10], dude, backpillars, frontpillars)

# while True:
    #### Runs animation
    # run_animation(fire,fire2,fire3,skyscraper,building1,heli,citybg,pulse, climbers, dudeontop, moon, outline)
    # run_animation(intro_male_body,intro_male_hair,intro_male_eyes,outline, bed, pillow)