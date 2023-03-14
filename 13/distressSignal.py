import sys, re, os, copy, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        c=0
        sumind=0
        pair=0
        for i in inp :
            if i!="\n" :
                if c==0 :
                    p1=eval(i[:-1])
                    c+=1
                    continue
                elif c==1 :
                    p2=eval(i[:-1])
                    c+=1
                pair+=1
                c=0
                ind=flattenner3000(p1,p2)
                if ind==1 :
                    sumind+=pair
    return sumind

def flattenner3000(l1,l2) :
    if not l1 and l2 :
        return 1
    elif not l2 and l1 :
        return 0
    while len(l1)<len(l2) :
        l1.append(None)
    while len(l2)<len(l1) :
        l2.append(None)
    for i,j in zip(l1,l2) :
        if i==None and j :
            return 1
        elif i and j==None :
            return 0
        if isinstance(i,list) and isinstance(j,list) :
            ind=flattenner3000(i,j)
            if ind!=None :
                return ind
        elif isinstance(i,int) and isinstance(j,list) :
            ind=flattenner3000([i],j)
            if ind!=None :
                return ind
        elif isinstance(i,list) and isinstance(j,int) :
            ind=flattenner3000(i,[j])
            if ind!=None :
                return ind
        elif isinstance(i,int) and isinstance(j,int) :
            if i<j :
                return 1
            elif i>j :
                return 0


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        sumind=[]
        count=1
        p2=[[[2]],[[6]]]
        for j in p2 : 
            for i in inp :
                if i!="\n" :
                    p1=eval(i[:-1])
                    ind=flattenner4000(p1,j)
                    if ind==1 :
                        count+=1
            sumind.append(count)
            inp.seek(0)
            count=1
    return sumind[0]*(sumind[1]+1)

def flattenner4000(l1,l2) :
    if not l1 and l2 :
        return 1
    elif not l2 and l1 :
        return 0
    while len(l1)<len(l2) :
        l1.append(None)
    while len(l2)<len(l1) :
        l2.append(None)
    for i,j in zip(l1,l2) :
        if i==None and j :
            return 1
        elif i and j==None :
            return 0
        if isinstance(i,list) and isinstance(j,list) :
            ind=flattenner4000(i,j)
            if ind!=None :
                return ind
        elif isinstance(i,int) and isinstance(j,list) :
            ind=flattenner4000([i],j)
            if ind!=None :
                return ind
        elif isinstance(i,list) and isinstance(j,int) :
            ind=flattenner4000(i,[j])
            if ind!=None :
                return ind
        elif isinstance(i,int) and isinstance(j,int) :
            if i<j :
                return 1
            elif i>j :
                return 0

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

