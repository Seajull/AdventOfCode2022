import sys, re, os, shutil

def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp:
            isp=i[:-1].split(" ")
            if isp[0]=="$" :
                if isp[1]=="cd" :
                    if isp[2]=="/" :
                        try :
                            os.chdir("1")
                        except :
                            os.mkdir("1")
                            os.chdir("1")
                        continue
                    else :
                        try :
                            os.chdir(isp[2])
                        except :
                            os.mkdir(isp[2])
                            os.chdir(isp[2])
            else :
                if isp[0]!="dir" :
                    with open(isp[0],"w") as osef:
                        pass
                else :
                    try :
                        os.mkdir(isp[1])
                    except :
                        pass
    os.chdir("/home/admincbellot/dev/AOC22/07/1")
    lsum=[]
    for i in os.walk(".") :
        sumSub=0
        for j in os.walk(i[0]) :
            j=[int(x) for x in j[2]]
            sumSub+=sum(j)
        lsum.append(sumSub)
    os.chdir("/home/admincbellot/dev/AOC22/07/")
    try :
        shutil.rmtree("/home/admincbellot/dev/AOC22/07/1")
    except : 
        sys.exit("oskour")
    sublsum=[x for x in lsum if x <= 100000] 
    return sum(sublsum)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        for i in inp:
            isp=i[:-1].split(" ")
            if isp[0]=="$" :
                if isp[1]=="cd" :
                    if isp[2]=="/" :
                        try :
                            os.chdir("2")
                        except :
                            os.mkdir("2")
                            os.chdir("2")
                        continue
                    else :
                        try :
                            os.chdir(isp[2])
                        except :
                            os.mkdir(isp[2])
                            os.chdir(isp[2])
            else :
                if isp[0]!="dir" :
                    with open(isp[0],"w") as osef:
                        pass
                else :
                    try :
                        os.mkdir(isp[1])
                    except :
                        pass
    os.chdir("/home/admincbellot/dev/AOC22/07/2")
    lsum=[]
    for i in os.walk(".") :
        sumSub=0
        for j in os.walk(i[0]) :
            j=[int(x) for x in j[2]]
            sumSub+=sum(j)
        lsum.append(sumSub)
    os.chdir("/home/admincbellot/dev/AOC22/07/")
    try :
        shutil.rmtree("/home/admincbellot/dev/AOC22/07/2")
    except : 
        sys.exit("oskour")

    sizeToDel=(70000000-max(lsum)-30000000)*-1
    lsum.sort()
    for i in lsum :
        if i >=sizeToDel :
            return(i)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


