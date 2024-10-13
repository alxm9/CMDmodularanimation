import itertools
import time
import os 
from operator import attrgetter

clear = lambda: os.system('cls')

os.system("")

class spritesheet():
    def __init__(self, path, color, zlevel = 0, frames = 0, dx = 0, dy = 0, delay = 0):
        self.path = path
        self.color = color ##escape code
        self.zlevel = zlevel
        self.frames = frames
        self.dx = dx # not implemented
        self.dy = dy # not implemented
        self.delay = delay # not implemented
        
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
    
def run_animation(*args): #First arg should be edge/bg
    # obsolete # z_dict = get_zlevels(args) # {ss_obj: zlevel,...} # This wasn't ideal, why not just make use of the method?
    # obsolete # locations = grab_sprite_dict(argslist, sprite_dict) ## to be used with zip() ## made a simpler version
    max_frame = max(args, key=attrgetter('frames')).frames 
    sprite_dict = obj_frameslist_dict(args, max_frame) # {ss_obj: [frame1, frame2,..],...}
    z_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("zlevel").items()} ## key:vvalue (output) for x in y (first loop) (for k,v..) (second loop)
    color_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("color").items()}
    list_framelists = [sprite_dict[i] for i in args]
    base = sprite_dict[args[0]] # this is dumb
    for framelist in zip(*list_framelists): # * unpacks list_framelists into n different lists (objs)
        for chars in zip(*framelist): # framelist unpacked into char number of different characters
            z_char_color = {}
            compare = []
            if all(" " in t for t in chars): # if all 3 chars are " " 
                print(" ", end="")
                continue
            for i in range(len(chars)): # zlevel: [char, color]
                z_char_color[z_dict[args[i]]] = [chars[i], color_dict[args[i]]]
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
        time.sleep(0.02)
        
def print_stillshot(framenumlist, *args): # [1,4], dude, backpillars
    max_frame = max(args, key=attrgetter('frames')).frames 
    sprite_dict = obj_frameslist_dict(args, max_frame) # {ss_obj: [frame1, frame2,..],...}
    z_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("zlevel").items()} ## key:vvalue (output) for x in y (first loop) (for k,v..) (second loop)
    color_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("color").items()}
    list_framelists = [sprite_dict[i] for i in args]

# def tuple_into_list(argstuple): # WOW this was incredibly dumb
    # argslist = []
    # for arg in argstuple:
        # argslist.append(arg)
    # return argslist

# def get_zlevels(argstuple): # no longer in use
    # z_dict = {}
    # for ss_obj in argstuple:
        # z_dict = z_dict | ss_obj.get_whatever("zlevel")
    # return z_dict


    
# def grab_sprite_dict(argslist, sprite_dict): # Grabs sprite_dict locations according to argslist, sends back list [ [frame1, frame2..], [frame1, frame2, frame3], [... ]
    # locations = []
    # print(argslist)
    # for i in argslist:
        # locations += [sprite_dict[i]]
    # return locations
        
# def run_animation(*args): #First arg should be edge/bg #### THIS WORKS
    #obsolete # z_dict = get_zlevels(args) # {ss_obj: zlevel,...} # This wasn't ideal, why not just make use of the method?
    #obsolete # locations = grab_sprite_dict(argslist, sprite_dict) ## to be used with zip() ## made a simpler version
    # argslist = tuple_into_list(args) # tuple into ss_obj list. Probably not necessary. KEEP AS TUPLE?
    # sprite_dict = obj_frameslist_dict(args) # {ss_obj: [frame1, frame2,..],...}
    # z_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("zlevel").items()} ## key:vvalue (output) for x in y (first loop) (for k,v..) (second loop)
    # color_dict = {k:v for ss_obj in args for k,v in ss_obj.get_whatever("color").items()} ## not sure if ideal but don't wanna go through too many functions
    # list_framelists = [sprite_dict[i] for i in argslist]
    # base = sprite_dict[argslist[0]] # wtf was I going to do with this
    # for objs in zip(*list_framelists): # * unpacks locations list into n different lists (objs)
        # for chars in zip(*objs): # objs unpacked into n different characters
            # char_zlevel = {}
            # char_colors = {}
            # compare = []
            # if all(" " in t for t in chars): # if all 3 chars are " " 
                # print(" ", end="")
                # continue
            # for i in range(len(chars)):
                # char_zlevel[chars[i]] = z_dict[argslist[i]]
                # char_colors[chars[i]] = color_dict[argslist[i]]
            # for i in chars:
                # if i != " ":
                    # compare.append(i)
            # to_print=compare[0]
            # for i in compare:
                # if char_zlevel[i] > char_zlevel[to_print]:
                    # to_print = i
            # color = char_colors[to_print]
            # print(color+to_print, end="")
        # print("\033[34A\033[2K", end="")
        # time.sleep(0.5)


    #THIS WORKS
    # for objs in zip(*locations): # * unpacks locations list into n different lists (objs)
        # for chars in zip(*objs): # objs unpacked into n different characters
            # char_zlevel = {}
            # compare = []
            # color = " "
            # if all(" " in t for t in chars): # if all 3 chars are " " 
                # print(" ", end="")
                # continue
            # for i in range(len(chars)):
                # char_zlevel[chars[i]] = z_dict[argslist[i]]
            # for i in chars:
                # if i != " ":
                    # compare.append(i)
            # to_print=compare[0]
            # for i in compare:
                # if char_zlevel[i] > char_zlevel[to_print]:
                    # to_print = i
            # print(to_print, end="")
        # print("\033[34A\033[2K", end="")
        # time.sleep(0.5)
                
            
            
            
            # if char2 == " ":
                # print(argslist[2].color+char3, end="")
                # continue
            # if char3 == " ":
                # print(argslist[1].color+char2, end="")
                # continue
            # to_print = char2
            # if z_dict[argslist[1]] > z_dict[argslist[2]]:
                # to_print = char3
            # print(to_print, end="")
        # print("\033[35A\033[2K", end="")
        # time.sleep(1)
    
    # for obj2_frame, obj3_frame in zip(sprite_dict[argslist[1]], sprite_dict[argslist[2]]):
        # for char2, char3 in zip(obj2_frame, obj3_frame): #### THIS WORKS
            # if char2 == " " and char3 == " ":
                # print(" ", end="")
                # continue
            # if char2 == " ":
                # print(argslist[2].color+char3, end="")
                # continue
            # if char3 == " ":
                # print(argslist[1].color+char2, end="")
                # continue
            # to_print = char2
            # if z_dict[argslist[1]] > z_dict[argslist[2]]:
                # to_print = char3
            # print(to_print, end="")
        # print("\033[35A\033[2K", end="")
        # time.sleep(1)
        
    # print(sprite_dict)
    # print(sprite_dict[(list(sprite_dict)[0])])
    # while True: #this works, prints only the list of the circle
        # for i in sprite_dict[(list(sprite_dict)[1])]:
            # print("")
            # print("{0}".format(i))
            # print("\033[36A\033[2K", end="")
            # time.sleep(0.2)
            
    # while True: #loops through the entire dict and prints everything
        # for list in sprite_dict:
            # for frame in sprite_dict[list]:               
                # print("")
                # print("{0}".format(frame))
                # print("\033[36A\033[2K", end="")
                # time.sleep(0.2)
                
    # while True: #modifying above to print one char at a time which will then be used to crossref
        # for list in sprite_dict:
            # for frame in sprite_dict[list]:
                # for char in frame:
                    # print("{0}".format(char), end="") # this seems to work so far
                # print("")
                # print("\033[35A\033[2K", end="")
                # time.sleep(0.2)

    # while True:
        # zlevel_a = args[1].zlevel
        # zlevel_b = args[2].zlevel
        # for a,b in zip(sprite_dict[(list(sprite_dict)[1])],sprite_dict[(list(sprite_dict)[2])]):
            # if 
    # while True:
        # for x in base: #### this should be towards the end of the loop
            # print("")
            # print("\033[35A\033[2K", end="")
            # time.sleep(0.2)       

    # for i in framelist: reference from previous test
        # file = open("textsequence\\{0}.txt".format(i),"r", encoding="utf-8")
        # print("")
        # print(file.read()+"{0}".format(color_a))
        # print("\033[37A\033[2K", end="")
        # time.sleep(0.05)
        # counter += 1
        # if counter == 10:
            # color_a, color_b = color_b, color_a
            # counter = 0
        # file.close()
        
# run_animation(outline, circle, square)
clear()
while True:
    run_animation(outline1, dude, frontpillars, backpillars)


