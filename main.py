import itertools
import time
import os 
from operator import attrgetter

clear = lambda: os.system('cls')

os.system("")

class spritesheet():
    def gather_framelist(self):
        frameslist = []
        for frame in range(1,self.frames+1):
            path = os.path.join("{0}".format(self.path), "txt", "ascii-art ({0}).txt".format(frame)) ## os.path.join works regardless of OS
            file = open(path, "r", encoding="utf-8")
            frameslist.append(file.read())
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
###################### path, escape code color, z-level, frames
outline = spritesheet("bg","\033[94m", zlevel = 22, frames = 1)
circle = spritesheet("circle","\033[94m", zlevel = 6, frames = 5)
square = spritesheet("square","\033[32m", zlevel = 4, frames = 5)
lightning = spritesheet("lightning","\033[32m", zlevel = 5, frames = 5)
dude = spritesheet("dude", "\033[32m", zlevel= 3, frames = 28)
frontpillars = spritesheet("frontpillars","\033[31m", zlevel = 8, frames = 28)
backpillars = spritesheet("backpillars","\033[31m", zlevel = 2, frames = 28)
outline1 = spritesheet("outline1", "\033[94m", zlevel = 99, frames = 1)

def obj_frameslist_dict(argstuple, max_frame):
    sprite_dict = {}
    for ss_obj in argstuple: ## ss_obj = spritesheet object
        sprite_dict[ss_obj] = []
        for frame in range(1,ss_obj.frames+1):
            path = os.path.join("{0}".format(ss_obj.path), "txt", "ascii-art ({0}).txt".format(frame)) ## os.path.join works regardless of OS
            file = open(path, "r", encoding="utf-8")
            sprite_dict[ss_obj].append(file.read())
        # print(max_frame, len(sprite_dict[ss_obj]))
        if ss_obj.frames < max_frame: # extends frames by last frame
            sprite_dict[ss_obj].extend([sprite_dict[ss_obj][-1]] * (max_frame - ss_obj.frames))
    return sprite_dict

def adjust_to_max(list_framelists, max_frame): # adjusts to max frame
    for list in list_framelists:
        if len(list) < max_frame: # extends frames by last frame
            list.extend([list[-1]]*(max_frame - len(list)))
    return list_framelists
        
    
def run_animation(*args): #First arg should be edge/bg.
    max_frame = max(args, key=attrgetter('frames')).frames
    # sprite_dict = obj_frameslist_dict(args, max_frame) # {ss_obj: [frame1, frame2,..],...} # OBSOLETE
    # z_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("zlevel").items()} ## key:vvalue (output) for x in y (first loop) (for k,v..) (second loop)
    # color_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("color").items()} # WOW wtf was I thinking. CATASTROPHICALLY BAD.
    list_framelists = [i.frameslist for i in args]
    list_framelists = adjust_to_max(list_framelists, max_frame)
    for framelist in zip(*list_framelists): # * unpacks list_framelists into n different lists (objs)
        for chars in zip(*framelist): # framelist unpacked into char number of different characters
            z_char_color = {}
            compare = []
            if all(" " in t for t in chars): # if all 3 chars are " " 
                print(" ", end="")
                continue
            for i in range(len(chars)): # zlevel: [char, color]
                # z_char_color[z_dict[args[i]]] = [chars[i], color_dict[args[i]]] ### I walked in a circle. CATASTROPHICALLY BAD.
                z_char_color[args[i].zlevel] = [chars[i], args[i].color]
            for i in z_char_color:
                if z_char_color[i][0] != " ":
                    compare.append(i)
            to_print=compare[0]
            for i in compare:
                if i > to_print:
                    to_print = i
            color = z_char_color[to_print][1]
            print(color+z_char_color[to_print][0], end="")
        print("\033[38A\033[2K", end="")
        time.sleep(0.05)
        
def print_stillshot(framenumlist, *args): # [1,4], dude, backpillars
    max_frame = max(args, key=attrgetter('frames')).frames 
    sprite_dict = obj_frameslist_dict(args, max_frame) # {ss_obj: [frame1, frame2,..],...}
    z_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("zlevel").items()} ## key:vvalue (output) for x in y (first loop) (for k,v..) (second loop)
    color_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("color").items()}
    list_framelists = [sprite_dict[i] for i in args]

clear()
while True:
    run_animation(dude, frontpillars, backpillars, outline)


