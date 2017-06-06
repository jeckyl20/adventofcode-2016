def direction(current, new):
    ''' Figure out which direction I'm going '''
    mydir = current 
    newdir = new[0]
    ## test to see what current direction is and which way we'll turn
#    print mydir
#    print newdir
    if newdir == "L":
        if mydir == "n":
            return "w"
        elif mydir == "e":
            return "n"
        elif mydir == "s":
            return "e"
        else:
            return "s"
    else:
        if mydir == "n":
            return "e"
        elif mydir == "e":
            return "s"
        elif mydir == "s":
            return "w"
        else:
            return "n"

def findhq(start, *args):
    ''' We don't know how many steps we'll have so we'll use *args '''
    curdir = start
    orig = {"x":0, "y":0}
    for step in args:
#        print "here is an arg from args: ", step
#        print "here is the first char of arg from args: ", step[0]
#        print "here are the rest of the chars of arg from args: ", step[1:]
#        print curdir
        curdir = direction(curdir, step)
#        print curdir
#        print orig
        if curdir == "n":
            # add to x in orig dictionary
            orig["x"] += int(step[1:])
        elif curdir == "s":
            # subtract from x in orig dictionary
            orig["x"] -= int(step[1:])
        elif curdir == "e":
            orig["y"] += int(step[1:])
        else:
            orig["y"] -= int(step[1:])
#        print orig
    
    ## some test prints and addition of the coordinates to find dist
    print "Value of X coordinate: ", abs(orig["x"])
    print "Value of Y coordinate: ", abs(orig["y"])
    print abs(orig["x"]) + abs(orig["y"])

## tests for direction function
#test = direction("n", "L2")
#print test
#test2 = direction(test, "L3")
#print test2
#test3 = direction(test2, "L2")
#print test3

## test for finding hq function
findhq("n", "L2", "L3", "L4", "L100", R"20")

# real input here
#findhq("n", "R4","R3","L3","L2","L1","R1","L1","R2","R3","L5","L5","R4","L4","R2","R4","L3","R3","L3","R3","R4","R2","L1","R2","L3","L2","L1","R3","R5","L1","L4","R2","L4","R3","R1","R2","L5","R2","L189","R5","L5","R52","R3","L1","R4","R5","R1","R4","L1","L3","R2","L2","L3","R4","R3","L2","L5","R4","R5","L2","R2","L1","L3","R3","L4","R4","R5","L1","L1","R3","L5","L2","R76","R2","R2","L1","L3","R189","L3","L4","L1","L3","R5","R4","L1","R1","L1","L1","R2","L4","R2","L5","L5","L5","R2","L4","L5","R4","R4","R5","L5","R3","L1","L3","L1","L1","L3","L4","R5","L3","R5","R3","R3","L5","L5","R3","R4","L3","R3","R1","R3","R2","R2","L1","R1","L3","L3","L3","L1","R2","L1","R4","R4","L1","L1","R3","R3","R4","R1","L5","L2","R2","R3","R2","L3","R4","L5","R1","R4","R5","R4","L4","R1","L3","R1","R3","L2","L3","R1","L2","R3","L3","L1","L3","R4","L4","L5","R3","R5","R4","R1","L2","R3","R5","L5","L4","L1","L1")
