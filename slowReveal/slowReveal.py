from __future__ import print_function
import random
import time
import numpy
import os





with open("smiley.txt") as f:
    content = f.read().splitlines()
    #print(content)

numOfShow = 0
notShown = []
#print(len(content[0]))
#print(len(content))
exs = []
exs.append(["throw"])
for rows in range(0, len(content)-1):
    exs.append([])
    for cols in range(0, len(content[rows])-1):
        #print(exs[rows])
        #print(exs[rows+1])
        exs[rows+1].append([False, content[rows][cols]])
        #print(y)
        if(exs[rows+1][cols][1] == " "):
            exs[rows+1][cols][0] = True
            numOfShow += 1
        else:
            notShown.append([rows, cols])
    #print(exs[rows])
    #print (len(content[rows]))
    #print (rows)
exs.pop(0)

print(exs[0])
random.shuffle(notShown)

print("here 1")
def show(exs):
    os.system("clear")
    for x in exs:
        for y in x:
            if(y[0]):
                print(y[1], sep="", end="")
            else:
                print(" ", sep="", end="")

        print(" ")

    print("\n"*2)

print("here 2")

length = len(exs)*len(exs[0])
done = False


while(not done):
    
    
    for i in range(8):
        if(len(notShown) == 0):
            break
        x, y = notShown.pop()
        #print(exs[x][y])
        exs[x][y][0]=True
        numOfShow += 1
    

        #print("here 3")
        #num = random.randint(0, len(exs)-1)
        #num2 = random.randint(0, len(exs[0])-1)
        #if(not exs[num][num2]):
        #    print(exs[num][num2][0])
        #    exs[num][num2][0]=True
        #    numOfShow += 1
        #    picked = True

    show(exs)
    time.sleep(.01)

    if(numOfShow >= length):
        done = True

