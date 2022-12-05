import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        stack={}
        fullop=[]
        for i in inp :
            if i=="\n" or i[0:2]==" 1":
                continue
            elif i[0]!="m" :
                line=i[:-1].split(" ")
                c=0
                nline=[]
                for j in line :
                    if j=="" :
                        c+=1
                        if c==4 :
                            nline.append("")
                            c=0
                    else :
                        nline.append(j[1])
                c=0
                while c<len(nline) :
                    if c+1 in stack :
                        stack[c+1].append(nline[c])
                    else :
                        stack[c+1]=[nline[c]]
                    c+=1
            else :
                fullop.append([int(x) for x in re.findall("\d+",i)])
        for s in stack :
            while "" in stack[s] :
                stack[s].remove("")
            stack[s].reverse()
        
        for i in fullop :
            c=0
            while c<i[0]:
                c+=1
                stack[i[2]].append(stack[i[1]].pop())
        crate=""
        for i in stack :
            crate+=stack[i][-1]
    return crate


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        stack={}
        fullop=[]
        for i in inp :
            if i=="\n" or i[0:2]==" 1":
                continue
            elif i[0]!="m" :
                line=i[:-1].split(" ")
                c=0
                nline=[]
                for j in line :
                    if j=="" :
                        c+=1
                        if c==4 :
                            nline.append("")
                            c=0
                    else :
                        nline.append(j[1])
                c=0
                while c<len(nline) :
                    if c+1 in stack :
                        stack[c+1].append(nline[c])
                    else :
                        stack[c+1]=[nline[c]]
                    c+=1
            else :
                fullop.append([int(x) for x in re.findall("\d+",i)])
        for s in stack :
            while "" in stack[s] :
                stack[s].remove("")
            stack[s].reverse()
        
        for i in fullop :
            c=0
            stack[i[2]]+=stack[i[1]][len(stack[i[1]])-i[0]:]
            stack[i[1]]=stack[i[1]][:len(stack[i[1]])-i[0]]
        crate=""
        for i in stack :
            crate+=stack[i][-1]
    return crate


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


