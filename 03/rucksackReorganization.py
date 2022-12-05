import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        tot=0
        for i in inp :
            i=i[:-1]
            li=len(i)
            c1=i[:int(li/2)] 
            c2=i[int(li/2):]
            diff=(set(c1)^set(c2))
            same=[]
            for j,k in zip(c1,c2) :
                if j not in diff :
                    same.append(j)
                if k not in diff :
                    same.append(k)
            for m in list(set(same)) :
                if ord(m) >= 97 :
                    tot+=(ord(m)-96)
                else:
                    tot+=(ord(m)-38)
    return tot 

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        c=0
        group=[]
        common=[]
        tot=0
        for i in inp :
            ruck=i[:-1]
            group.append(ruck)
            c+=1
            if c==3 :
                for j in group[0] :
                    if j in group[1] and j in group[2]:
                        common.append(j)
                c=0
                for m in list(set(common)) :
                    if ord(m) >= 97 :
                        tot+=(ord(m)-96)
                    else:
                        tot+=(ord(m)-38)
                group=[]
                common=[]
    return tot

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


