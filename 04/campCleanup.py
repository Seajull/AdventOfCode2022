import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        tot=0
        for i in inp :
            p1=[int(x) for x in i.split(",")[0].split("-")]
            p2=[int(x) for x in i[:-1].split(",")[1].split("-")]
            p1s=p1[1]-p1[0]+1
            p2s=p2[1]-p2[0]+1
            if p1s < p2s : 
                mnp=p1
                mxp=p2
            else :
                mnp=p2
                mxp=p1
            rmi=list(range(mnp[0],mnp[1]+1))
            rma=list(range(mxp[0],mxp[1]+1))
            found=False
            for i in rmi :
                if i not in rma :
                    found=True
                    break
            if not found :
                tot+=1
    return tot 

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        tot=0
        for i in inp :
            p1=[int(x) for x in i.split(",")[0].split("-")]
            p2=[int(x) for x in i[:-1].split(",")[1].split("-")]
            p1s=p1[1]-p1[0]+1
            p2s=p2[1]-p2[0]+1
            if p1s < p2s : 
                mnp=p1
                mxp=p2
            else :
                mnp=p2
                mxp=p1
            rmi=list(range(mnp[0],mnp[1]+1))
            rma=list(range(mxp[0],mxp[1]+1))
            for i in rmi :
                if i in rma :
                    tot+=1
                    break
    return tot 

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


