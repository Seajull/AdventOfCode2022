import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        cycle=0
        value=1
        lval=[]
        for i in inp :
            cycle+=1
            if cycle in [20,60,100,140,180,220] :
                lval.append(value*cycle)
            if i[:-1] != "noop" :
                num=int(i[:-1].split(" ")[1])
                cycle+=1
                if cycle in [20,60,100,140,180,220] :
                    lval.append(value*cycle)
                value+=num
    return sum(lval)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        cycle=0
        value=1
        lcrt=[]
        crtpos=0
        crt=""
        for i in inp :
            sprite=[value-1,value,value+1]
            cycle+=1
            if crtpos in sprite :
                crt+="#"
            else :
                crt+="."
            crtpos+=1
            if crtpos%40==0 :
                lcrt.append(crt)
                crtpos=0
                crt=""
            if i[:-1] != "noop" :
                num=int(i[:-1].split(" ")[1])
                cycle+=1
                if crtpos in sprite :
                    crt+="#"
                else :
                    crt+="."
                crtpos+=1
                if crtpos%40==0 :
                    lcrt.append(crt)
                    crtpos=0
                    crt=""
                value+=num
        for i in lcrt:
            print(i)

print("==> PART TWO <==")
partTwo(sys.argv[1])

