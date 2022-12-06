import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            data=i[:-1]
            c=0
            while c<len(data) :
                if c<4 :
                    c+=1
                    continue
                else :
                    if len(set(data[c-4:c]))==4 :
                        return(c)
                    c+=1


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            data=i[:-1]
            c=0
            while c<len(data) :
                if c<14 :
                    c+=1
                    continue
                else :
                    if len(set(data[c-14:c]))==14 :
                        return(c)
                    c+=1


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


