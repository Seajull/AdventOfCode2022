import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        elv=[]
        s=0
        for i in inp :
            if i!="\n":
                s+=int(i[:-1])
            else :
                elv.append(s)
                s=0
        elv.append(s)
    return max(elv)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        elv=[]
        s=0
        for i in inp :
            if i!="\n":
                s+=int(i[:-1])
            else :
                elv.append(s)
                s=0
        elv.append(s)
        elv.sort(reverse=True)
    return sum(elv[0:3])

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


