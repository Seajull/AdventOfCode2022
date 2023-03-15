import sys, re, os, copy, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        occu=[]
        maxdepth=0
        left=None
        right=None
        for i in inp :
            res=re.findall("\d+",i)
            coord=[int(x) for x in res]
            coord=[coord[j:j+2] for j in range(0, len(coord),2)]
#            print(coord)
            c=0
            while c<len(coord)-1 :
                mic0=min([coord[c][0],coord[c+1][0]])
                mac0=max([coord[c][0],coord[c+1][0]])
                mic1=min([coord[c][1],coord[c+1][1]])
                mac1=max([coord[c][1],coord[c+1][1]])
                ir=list(range(mic0,mac0+1))
                jr=list(range(mic1,mac1+1))
                for r in list(itertools.product(ir,jr)) :
                    if r not in occu :
                        occu.append(r)
                    if r[1]>maxdepth:
                        maxdepth=r[1]
                    if left==None :
                        left=r[0]
                    elif r[0]<left :
                        left=r[0]
                    if right==None :
                        right=r[0]
                    elif r[0]>right :
                        right=r[0]
                c+=1
        x=list(range(left,right+1))
        y=list(range(0,maxdepth+1))
        poss=list(itertools.product(x,y))
        grain=0
        lost=False
        while True :
            start=(500,0)
            while True :
                if start[1]+1>maxdepth or start[0]-1<left or start[0]+1>right :
                    lost=True
                    break
                down=(start[0],start[1]+1)
                le=(start[0]-1,start[1]+1)
                ri=(start[0]+1,start[1]+1)
                if down in occu and le in occu and ri in occu :
                    break
                if down not in occu and down in poss :
                    start=down
                elif down in occu and down in poss:
                    if le not in occu and le in poss :
                        start=le
                    elif le not in poss :
                        break
                    elif le in occu and le in poss :
                        if ri not in occu and ri in poss :
                            start=ri
                        elif ri not in poss :
                            lost=True
                            break
            
            if start not in occu and start in poss and not lost:
                occu.append(start)
                lost=False
                grain+=1
            else :
                break
    return grain

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        occu=[]
        maxdepth=0
        for i in inp :
            res=re.findall("\d+",i)
            coord=[int(x) for x in res]
            coord=[coord[j:j+2] for j in range(0, len(coord),2)]
#            print(coord)
            c=0
            while c<len(coord)-1 :
                mic0=min([coord[c][0],coord[c+1][0]])
                mac0=max([coord[c][0],coord[c+1][0]])
                mic1=min([coord[c][1],coord[c+1][1]])
                mac1=max([coord[c][1],coord[c+1][1]])
                ir=list(range(mic0,mac0+1))
                jr=list(range(mic1,mac1+1))
                for r in list(itertools.product(ir,jr)) :
                    if r not in occu :
                        occu.append(r)
                    if r[1]>maxdepth:
                        maxdepth=r[1]
                c+=1
        grain=0
        floor=maxdepth+2
        while True :
            start=(500,0)
            while True :
                if start[1]+1>=floor :
                    break
                down=(start[0],start[1]+1)
                le=(start[0]-1,start[1]+1)
                ri=(start[0]+1,start[1]+1)
                if down not in occu :
                    start=down
                elif le not in occu :
                    start=le
                elif ri not in occu :
                    start=ri
                else :
                    break
            if start not in occu :
                occu.append(start)
                grain+=1
            else :
                break
    return grain

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

