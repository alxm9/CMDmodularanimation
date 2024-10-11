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
    def __init__(self, path, color, zlevel, frames, dx = 0, dy = 0):
        self.path = path
        self.color = color ##escape code
        self.zlevel = zlevel
        self.frames = frames
        self.dx = dx
        self.dy = dy

#"""path, escape code color, z-level, frames att for looping purposes
background = spritesheet("bg\\txt","\033[94m", 5, 1)
circle = spritesheet("circle\\txt","\033[31m", 1, 5)
square = spritesheet("square\\txt","\033[32m", 2, 5)

def run_animation(*args):
    # while True:  
    sprite_dict = {}
    for ss_obj in args:
        sprite_dict[ss_obj] = []
        for frame in range(1,ss_obj.frames+1):
            file = open("{0}\\{1}.txt".format(ss_obj.path,frame), "r", encoding="utf-8")
            sprite_dict[ss_obj].append(file.read()+"{0}".format(ss_obj.color))
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
                
    while True: #modifying above to print one char at a time which will then be used to crossref
        for list in sprite_dict:
            for frame in sprite_dict[list]:
                for char in frame:
                    print("{0}".format(char), end="") # this seems to work so far
                print("")
                print("\033[35A\033[2K", end="")
                time.sleep(0.2)
    

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
        
run_animation(background, circle, square)


