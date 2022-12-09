import sys, re, os, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        grid=[]
        for i in inp :
            grid.append([int(x) for x in list(i[:-1])])
        x=0
        totVisi=0
        while x<len(grid) :
            y=0
            while y<len(grid) :
                if isVisible(grid,(x,y)) :
                    totVisi+=1
                y+=1
            x+=1
    return totVisi

def isVisible(grid,coord) :
    if coord[0]==0 or coord[0]==len(grid)-1 or coord[1]==0 or coord[1]==len(grid[coord[0]])-1 :
        return(True)
    else :
        hori=list(itertools.product([coord[0]],list(range(0,len(grid[coord[1]])))))
        verti=list(itertools.product(list(range(0,len(grid[coord[0]]))),[coord[1]]))
        left=hori[:hori.index(coord)]
        right=hori[hori.index(coord)+1:]
        up=verti[:verti.index(coord)]
        down=verti[verti.index(coord)+1:]

        left=[grid[x[0]][x[1]] for x in left] 
        right=[grid[x[0]][x[1]] for x in right] 
        up=[grid[x[0]][x[1]] for x in up] 
        down=[grid[x[0]][x[1]] for x in down] 
        alldir=[left,right,up,down]

        c=0
        for i in alldir :
            for j in i :
                if j >= grid[coord[0]][coord[1]] :
                    c+=1
                    break
        if c<4 :
            return True
        else :
            return False
                

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        grid=[]
        for i in inp :
            grid.append([int(x) for x in list(i[:-1])])
        x=0
        score=[]
        while x<len(grid) :
            y=0
            while y<len(grid) :
                score.append(scenic(grid,(x,y)))
                y+=1
            x+=1
    return max(score)

def scenic(grid,coord) :
    if coord[0]==0 or coord[0]==len(grid)-1 or coord[1]==0 or coord[1]==len(grid[coord[0]])-1 :
        return(0)
    else :
        hori=list(itertools.product([coord[0]],list(range(0,len(grid[coord[1]])))))
        verti=list(itertools.product(list(range(0,len(grid[coord[0]]))),[coord[1]]))
        left=hori[:hori.index(coord)]
        left=left[::-1]
        right=hori[hori.index(coord)+1:]
        up=verti[:verti.index(coord)]
        up=up[::-1]
        down=verti[verti.index(coord)+1:]

        left=[grid[x[0]][x[1]] for x in left] 
        right=[grid[x[0]][x[1]] for x in right] 
        up=[grid[x[0]][x[1]] for x in up] 
        down=[grid[x[0]][x[1]] for x in down] 
        alldir=[left,right,up,down]
        found=False
        sco=1
        for i in alldir :
            c=0
            for j in i :
                if j >= grid[coord[0]][coord[1]] :
                    c+=1
                    break
                else :
                    c+=1
            sco=sco*c
        return sco

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


