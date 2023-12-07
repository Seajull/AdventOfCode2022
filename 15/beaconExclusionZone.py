import sys, re, os, copy, itertools

def partOne(inpu,line) :
    with open(inpu,'r') as inp :
        sensor=[]
        beacon=[]
        occup=[]
        for i in inp :
            resx=re.findall("x=(-?\d+)",i)
            resy=re.findall("y=(-?\d+)",i)
            sensor.append((int(resx[0]),int(resy[0])))
            beacon.append((int(resx[1]),int(resy[1])))
        for i,j in zip(sensor,beacon) :
            distance=max(i[0],j[0])-min(i[0],j[0])+max(i[1],j[1])-min(i[1],j[1])
            if i[1]-distance<line<i[1]+distance :
                dl=abs(i[1]-line)
                dl=distance-dl
                poss=list(itertools.product(list(range(i[0]-dl,i[0]+dl+1)),[10]))
                for k in poss :
                    occup.append(k)
        c=0
        for i in set(beacon) :
            if i[1]==line :
                c+=1
    return len(set(occup))-c

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1],2000000))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        sensor=[]
        beacon=[]
        bound={}
        for i in inp :
            resx=re.findall("x=(-?\d+)",i)
            resy=re.findall("y=(-?\d+)",i)
            sensor.append((int(resx[0]),int(resy[0])))
            beacon.append((int(resx[1]),int(resy[1])))
        for i,j in zip(sensor,beacon) : 
            distance=max(i[0],j[0])-min(i[0],j[0])+max(i[1],j[1])-min(i[1],j[1])
            for k in findbound(i,distance) :
                if k in bound.keys() :
                    bound[k]+=1
                else :
                    bound[k]=1
        print(bound.values())


def findbound(coord,distance) :
    top=(coord[0],coord[1]-distance)
    bottom=(coord[0],coord[1]+distance)
    left=(coord[0]-distance,coord[1])
    right=(coord[0]+distance,coord[1])
    bo=[]
    bo+=[(i-1,j) for i,j in zip(list(range(left[0],top[0]+1)),list(reversed(range(top[1],left[1]+1))))]
    bo+=[(i,j-1) for i,j in zip(list(range(left[0],top[0]+1)),list(reversed(range(top[1],left[1]+1))))]

    bo+=[(i-1,j) for i,j in zip(list(range(left[0],bottom[0]+1)),list(range(left[1],bottom[1]+1)))]
    bo+=[(i,j+1) for i,j in zip(list(range(left[0],bottom[0]+1)),list(range(left[1],bottom[1]+1)))]

    bo+=[(i+1,j) for i,j in zip(list(range(bottom[0],right[0]+1)),list(reversed(range(right[1],bottom[1]+1))))]
    bo+=[(i,j+1) for i,j in zip(list(range(bottom[0],right[0]+1)),list(reversed(range(right[1],bottom[1]+1))))]

    bo+=[(i+1,j) for i,j in zip(list(range(top[0],right[0]+1)),list(range(top[1],right[1]+1)))]
    bo+=[(i,j-1) for i,j in zip(list(range(top[0],right[0]+1)),list(range(top[1],right[1]+1)))]
    return(set(bo))



print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

