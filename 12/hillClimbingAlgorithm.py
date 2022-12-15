import sys, re, os, copy, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        grid=[]
        c=0
        for i in inp :
            line=[0 if x=="S" else ord(x)-96 for x in list(i[:-1])]
            if 0 in line :
                start=(c,line.index(0))
            if -27 in line :
                line[line.index(-27)]=27
                end=(c,line.index(27))
#            line=[[x,0] for x in line]
            grid.append(line)
            c+=1
    G={}
    x=0
    while x<len(grid) :
        y=0
        while y<len(grid[x]) :
            G[(x,y)]=getVoisin(grid,(x,y))
            y+=1
        x+=1
    """
    Stolen from https://math.univ-lyon1.fr/irem/Formation_ISN/formation_parcours_graphes/largeur/3_python1.html
    """
    P={start :None}
    Q=[start]
    while Q :
        u=Q.pop(0)
        for v in G[u] :
            if v in P : 
                continue
            P[v]=u
            Q.append(v)
    path=[]
    cur=end
    while start not in path :
        path.append(P[cur])
        cur=P[cur]
    return len(path)

def getVoisin(grid,coord) :
    x=coord[0]
    y=coord[1]
    maxx=len(grid)
    maxy=len(grid[x])
    cur=grid[x][y]
    if cur==0 :
        cur=1
    elif cur==27 :
        cur=26
    voisin=[]
    voisin.append((x,y+1))
    voisin.append((x,y-1))
    voisin.append((x-1,y))
    voisin.append((x+1,y))
    valid=[]
    for i in voisin :
        if -1 in i or i[0]>= maxx or i[1] >= maxy :
            continue
        else :
            if grid[i[0]][i[1]]>cur+1 :
                continue
            else :
                valid.append(i)
    return(valid)
        
            


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        grid=[]
        c=0
        start=[]
        for i in inp :
            line=[1 if x=="S" else ord(x)-96 for x in list(i[:-1])]
            if 1 in line : 
                y1=[k for k, x in enumerate(line) if x==1]
                start+=(list(itertools.product([c],y1)))
            if -27 in line :
                line[line.index(-27)]=27
                end=(c,line.index(27))
#            line=[[x,0] for x in line]
            grid.append(line)
            c+=1
    G={}
    x=0
    allpath=[]
    while x<len(grid) :
        y=0
        while y<len(grid[x]) :
            G[(x,y)]=getVoisin(grid,(x,y))
            y+=1
        x+=1
    for s in start : 
        """
        Stolen from https://math.univ-lyon1.fr/irem/Formation_ISN/formation_parcours_graphes/largeur/3_python1.html
        """
        P={s :None}
        Q=[s]
        while Q :
            u=Q.pop(0)
            for v in G[u] :
                if v in P : 
                    continue
                P[v]=u
                Q.append(v)
        path=[]
        cur=end
        if end not in P :
            continue
        while s not in path :
            path.append(P[cur])
            cur=P[cur]
        allpath.append(len(path))
    return min(allpath)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

