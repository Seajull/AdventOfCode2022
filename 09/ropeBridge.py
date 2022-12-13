import sys, re, os, copy

def partOne(inpu) :
    with open(inpu,'r') as inp :
        pos=[0,0]
        tpos=["T","T"]
        tpos=[0,0]
        allpos=[]
        allposT=[]
        for i in inp :
            c=0
            isp=i[:-1].split(" ")
            cur=isp[0]
            if cur=="R" :
                while c<int(isp[1]) :
                    pos[1]+=1
                    cpos=copy.deepcopy(pos)
                    allpos.append(cpos)
                    c+=1
                    if abs(tpos[0]-allpos[-1][0]) == 2 or abs(tpos[1]-allpos[-1][1]) == 2: 
                        tpos=allpos[-2]
                        allposT.append(tpos)
            elif cur=="L" :
                while c<int(isp[1]) :
                    pos[1]-=1
                    cpos=copy.deepcopy(pos)
                    allpos.append(cpos)
                    c+=1
                    if abs(tpos[0]-allpos[-1][0]) == 2 or abs(tpos[1]-allpos[-1][1]) == 2: 
                        tpos=allpos[-2]
                        allposT.append(tpos)
            elif cur=="D" :
                while c<int(isp[1]) :
                    pos[0]+=1
                    cpos=copy.deepcopy(pos)
                    allpos.append(cpos)
                    c+=1
                    if abs(tpos[0]-allpos[-1][0]) == 2 or abs(tpos[1]-allpos[-1][1]) == 2: 
                        tpos=allpos[-2]
                        allposT.append(tpos)
            elif cur=="U" :
                while c<int(isp[1]) :
                    pos[0]-=1
                    cpos=copy.deepcopy(pos)
                    allpos.append(cpos)
                    c+=1
                    if abs(tpos[0]-allpos[-1][0]) == 2 or abs(tpos[1]-allpos[-1][1]) == 2: 
                        tpos=allpos[-2]
                        allposT.append(tpos)
        uni=[]
        for i in allposT :
            if i not in uni :
                uni.append(i)
    return len(uni)+1
                

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


"""
PART1 won't work for this, need to rewrite all this shit
OR MAYBE if i virtually move the head and loop 9 times
(1 (H) move, 2 move and become H, 3 move and become H, etc)
and keep only pos of tail
"""

"""
I can't explain how it works.
"""
def partTwo(inpu) :
    with open(inpu,'r') as inp :
        pos=[0,0]
        tpos=["T","T"]
        tpos=[0,0]
        rpos=[tpos]*10
        allpos=[[] for i  in range(10)]
        allposT=[]
        for i in inp :
            isp=i[:-1].split(" ")
            cur=isp[0]
            c=0
            if cur=="R" :
                while c<int(isp[1]) :
                    pos[1]+=1
                    rpos[0]=copy.deepcopy(pos)
                    allpos[0].append(copy.deepcopy(rpos[0]))
                    c+=1
                    r=0
                    for tpos in rpos : 
                        if r>0 :
                            if abs(tpos[0]-rpos[r-1][0]) == 2 or abs(tpos[1]-rpos[r-1][1]) == 2: 
                                if r== 1 :
                                    rpos[r]=allpos[r-1][-2]
                                    allpos[r].append(rpos[r])
                                else :
                                    if not (tpos[0]==rpos[r-1][0] or tpos[1]==rpos[r-1][1]) :
                                        if abs(tpos[0]-rpos[r-1][0]) == 2 and abs(tpos[1]-rpos[r-1][1]) == 2: 
                                            rpos[r]=allpos[r-1][-2]
                                            allpos[r].append(rpos[r])
                                        else : 
#                                            rpos[r]=allpos[r-1][-2]
#                                            rpos[r][1]+=1
                                            if allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]-1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]-1]
                                            allpos[r].append(rpos[r])
                                    else :
                                        if tpos[0]==rpos[r-1][0] :
                                            if tpos[1]>rpos[r-1][1] :
                                                rpos[r]=[tpos[0],tpos[1]-1]
                                            else :
                                                rpos[r]=[tpos[0],tpos[1]+1]
                                        elif tpos[1]==rpos[r-1][1] :
                                            if tpos[0]>rpos[r-1][0] :
                                                rpos[r]=[tpos[0]-1,tpos[1]]
                                            else :
                                                rpos[r]=[tpos[0]+1,tpos[1]]
#                                        rpos[r]=allpos[r-1][-2]
                                        allpos[r].append(rpos[r])
                                    if r==9 :
                                        allposT.append(rpos[r])
                        r+=1
            elif cur=="L" :
                while c<int(isp[1]) :
                    pos[1]-=1
                    rpos[0]=copy.deepcopy(pos)
                    allpos[0].append(rpos[0])
                    c+=1
                    r=0
                    for tpos in rpos : 
                        if r>0 :
                            if abs(tpos[0]-rpos[r-1][0]) == 2 or abs(tpos[1]-rpos[r-1][1]) == 2: 
                                if r== 1 :
                                    rpos[r]=allpos[r-1][-2]
                                    allpos[r].append(rpos[r])
                                else :
                                    if not (tpos[0]==rpos[r-1][0] or tpos[1]==rpos[r-1][1]) :
                                        if abs(tpos[0]-rpos[r-1][0]) == 2 and abs(tpos[1]-rpos[r-1][1]) == 2: 
                                            rpos[r]=allpos[r-1][-2]
                                            allpos[r].append(rpos[r])
                                        else : 
#                                            rpos[r]=allpos[r-1][-2]
                                            if allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]-1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]-1]
#                                            rpos[r][1]-=1
                                            allpos[r].append(rpos[r])
                                    else :
                                        if tpos[0]==rpos[r-1][0] :
                                            if tpos[1]>rpos[r-1][1] :
                                                rpos[r]=[tpos[0],tpos[1]-1]
                                            else :
                                                rpos[r]=[tpos[0],tpos[1]+1]
                                        elif tpos[1]==rpos[r-1][1] :
                                            if tpos[0]>rpos[r-1][0] :
                                                rpos[r]=[tpos[0]-1,tpos[1]]
                                            else :
                                                rpos[r]=[tpos[0]+1,tpos[1]]
                                        allpos[r].append(rpos[r])
                                    if r==9 :
                                        allposT.append(rpos[r])
                        r+=1

            elif cur=="D" :
                while c<int(isp[1]) :
                    pos[0]+=1
                    rpos[0]=copy.deepcopy(pos)
                    allpos[0].append(rpos[0])
                    c+=1
                    r=0
                    for tpos in rpos : 
                        if r>0 :
                            if abs(tpos[0]-rpos[r-1][0]) == 2 or abs(tpos[1]-rpos[r-1][1]) == 2: 
                                if r== 1 :
                                    rpos[r]=allpos[r-1][-2]
                                    allpos[r].append(rpos[r])
                                else :
                                    if not (tpos[0]==rpos[r-1][0] or tpos[1]==rpos[r-1][1]) :
                                        if abs(tpos[0]-rpos[r-1][0]) == 2 and abs(tpos[1]-rpos[r-1][1]) == 2: 
                                            rpos[r]=allpos[r-1][-2]
                                            allpos[r].append(rpos[r])
                                        else : 
#                                            rpos[r]=allpos[r-1][-2]
#                                            rpos[r]=[rpos[r][0]+1,allpos[r-1][-2][1]]
                                            if allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]-1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]-1]
#                                            rpos[r][0]+=1
                                            allpos[r].append(rpos[r])
                                    else :
                                        if tpos[0]==rpos[r-1][0] :
                                            if tpos[1]>rpos[r-1][1] :
                                                rpos[r]=[tpos[0],tpos[1]-1]
                                            else :
                                                rpos[r]=[tpos[0],tpos[1]+1]
                                        elif tpos[1]==rpos[r-1][1] :
                                            if tpos[0]>rpos[r-1][0] :
                                                rpos[r]=[tpos[0]-1,tpos[1]]
                                            else :
                                                rpos[r]=[tpos[0]+1,tpos[1]]
#                                        rpos[r]=allpos[r-1][-2]
                                        allpos[r].append(rpos[r])
                                    if r==9 :
                                        allposT.append(rpos[r])
                        r+=1

            elif cur=="U" :
                while c<int(isp[1]) :
                    pos[0]-=1
                    rpos[0]=copy.deepcopy(pos)
                    allpos[0].append(rpos[0])
                    c+=1
                    r=0
                    for tpos in rpos : 
                        if r>0 :
                            if abs(tpos[0]-rpos[r-1][0]) == 2 or abs(tpos[1]-rpos[r-1][1]) == 2: 
                                if r==1 :
                                    rpos[r]=allpos[r-1][-2]
                                    allpos[r].append(rpos[r])
                                else :
                                    if not (tpos[0]==rpos[r-1][0] or tpos[1]==rpos[r-1][1]) :
                                        if abs(tpos[0]-rpos[r-1][0]) == 2 and abs(tpos[1]-rpos[r-1][1]) == 2: 
                                            rpos[r]=allpos[r-1][-2]
                                            allpos[r].append(rpos[r])
                                        else : 
#                                            rpos[r]=allpos[r-1][-2]
                                            if allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]>rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]+1,rpos[r][1]-1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]>rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]+1]
                                            elif allpos[r-1][-1][0]<rpos[r][0] and allpos[r-1][-1][1]<rpos[r][1] :
                                                rpos[r]=[rpos[r][0]-1,rpos[r][1]-1]
#                                            rpos[r][0]-=1
                                            allpos[r].append(rpos[r])
                                    else :
                                        if tpos[0]==rpos[r-1][0] :
                                            if tpos[1]>rpos[r-1][1] :
                                                rpos[r]=[tpos[0],tpos[1]-1]
                                            else :
                                                rpos[r]=[tpos[0],tpos[1]+1]
                                        elif tpos[1]==rpos[r-1][1] :
                                            if tpos[0]>rpos[r-1][0] :
                                                rpos[r]=[tpos[0]-1,tpos[1]]
                                            else :
                                                rpos[r]=[tpos[0]+1,tpos[1]]
#                                        rpos[r]=allpos[r-1][-2]
                                        allpos[r].append(rpos[r])
                                    if r==9 :
                                        allposT.append(rpos[r])
                        r+=1
        uni=[]
        for i in allposT :
            if i not in uni :
                uni.append(i)
    return len(uni)+1

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


