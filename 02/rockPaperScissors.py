import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        rule={"A":(1,["C","Z"]),"B":(2,["A","X"]),"C":(3,["B","Y"]),"X":(1,["C","Z"]),"Y":(2,["A","X"]),"Z":(3,["B","Y"])}
        tot=0
        for i in inp :
            isp=i[:-1].split(" ")
            tot+=rule[isp[1]][0]
            if isp[0] in rule[isp[1]][1]:
                tot+=6
            elif rule[isp[0]][0]==rule[isp[1]][0] :
                tot+=3
    return tot

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        rule={"A":(1,["C","B"]),"B":(2,["A","C"]),"C":(3,["B","A"])}
        tot=0
        for i in inp :
            isp=i[:-1].split(" ")
            if isp[1]=="X" :
                tot+=rule[rule[isp[0]][1][0]][0]
            elif isp[1]=="Y":
                tot+=rule[isp[0]][0]+3
            else :
                tot+=rule[rule[isp[0]][1][1]][0]+6
    return tot


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


