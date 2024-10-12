import itertools
import time
import os 

os.system("")
########## itertools test
# list1 = [2,3,4,5,6,7]
# list2 = [11,23,44,55]

# for a,b in itertools.zip_longest(list2,list1):
    # print(a,b)
    
class spritesheet():
    def __init__(self, path, color, zlevel = 0, frames = 0, dx = 0, dy = 0):
        self.path = path
        self.color = color ##escape code
        self.zlevel = zlevel
        self.frames = frames
        self.dx = dx
        self.dy = dy

#"""path, escape code color, z-level, frames att for looping purposes
outline = spritesheet("bg","\033[94m", zlevel = 22, frames = 5)
circle = spritesheet("circle","\033[31m", zlevel = 6, frames = 5)
square = spritesheet("square","\033[32m", zlevel = 8, frames = 5)
# lightning = spritesheet("lightning","\033[32m", zlevel = 5, frames = 5)

def get_zlevels(argstuple):
    z_dict = {}
    for ss_obj in argstuple:
        z_dict[ss_obj] = ss_obj.zlevel
        z_greatest = next(iter(z_dict))
    return z_dict
    
def get_colors(argstuple):
    pass

def tuple_into_list(argstuple):
    argslist = []
    for arg in argstuple:
        argslist.append(arg)
    return argslist

def obj_frameslist_dict(argstuple):
    sprite_dict = {}
    for ss_obj in argstuple: ## ss_obj = spritesheet object
        sprite_dict[ss_obj] = []
        for frame in range(1,ss_obj.frames+1):
            path = os.path.join("{0}".format(ss_obj.path), "txt", "{0}.txt".format(frame)) ## os.path.join works regardless of OS
            file = open(path, "r", encoding="utf-8")
            # sprite_dict[ss_obj].append(file.read()+"{0}".format(ss_obj.color)) ## If I encounter color issues, this might be a hint
            sprite_dict[ss_obj].append(file.read())
    return sprite_dict

def grab_sprite_dict(argslist, sprite_dict): # Grabs sprite_dict locations according to argslist, sends back list [ [frame1, frame2..], [frame1, frame2, frame3], [... ]
    locations = []
    print(argslist)
    for i in argslist:
        locations += [sprite_dict[i]]
    return locations
    
def run_animation(*args): #First arg should be edge/bg
    argslist = tuple_into_list(args) # tuple into ss_obj list
    sprite_dict = obj_frameslist_dict(args) # {ss_obj: [frame1, frame2,..],...}
    z_dict = get_zlevels(args) # {ss_obj: zlevel,...}
    locations = grab_sprite_dict(argslist, sprite_dict) ## to be used with zip()
    base = sprite_dict[argslist[0]] # dude wtf was I going to do with this
    for objs in zip(*locations): # * unpacks locations list into n different lists (objs)
        for chars in zip(*objs): # objs unpacked into n different characters
            char_zlevel = {}
            compare = []
            color = " "
            if all(" " in t for t in chars): # if all 3 chars are " " 
                print(" ", end="")
                continue
            for i in range(len(chars)):
                char_zlevel[chars[i]] = z_dict[argslist[i]]
            for i in chars:
                if i != " ":
                    compare.append(i)
            to_print=compare[0]
            for i in compare:
                if char_zlevel[i] > char_zlevel[to_print]:
                    to_print = i
            print(to_print, end="")
        print("\033[34A\033[2K", end="")
        time.sleep(0.5)

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
        
run_animation(outline, circle, square)
print("end")


