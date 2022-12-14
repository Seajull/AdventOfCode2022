import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        c=0
        listMonk=[]
        for i in inp :
            if c==0 :
                num=int(i[:-2].split(" ")[1])
                listMonk.append(monkey(num))
            elif c==1 :
                item=i[:-1].split(": ")[1].split(", ")
                listMonk[num].item=item
            elif c==2 :
                op=i[:-1].split(": ")[-1][6:]
                listMonk[num].op=op
            elif c==3 :
                test=[]
                test.append("new%"+i[:-1].split(": ")[-1].split(" ")[-1])
            elif c==4 :
                test.append(int(i[:-1].split(": ")[-1].split(" ")[-1]))
            elif c==5 :
                test.append(int(i[:-1].split(": ")[-1].split(" ")[-1]))
                listMonk[num].test=test
            elif c==6 :
                c=0
                continue
            c+=1
    nround=20
    monkeyBusiness=[]
    for n in range(nround) :
        for m in listMonk :
            for item in m.item :
                old=int(item)
                new=int(eval(m.op)/3)
                if not(eval(m.test[0])) :
                    listMonk[m.test[1]].item.append(new)
                else :
                    listMonk[m.test[2]].item.append(new)
                m.ins+=1
            m.item=[]
    for m in listMonk :
        monkeyBusiness.append(m.ins)
    monkeyBusiness.sort()
    return monkeyBusiness[-2]*monkeyBusiness[-1]

class monkey : 
    def __init__(self,num,item=[],op="",test=[],ins=0,diff=[]): 
        self.num=num
        self.item=item
        self.op=op
        self.test=test
        self.ins=ins
        self.diff=diff


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        c=0
        listMonk=[]
        for i in inp :
            if c==0 :
                num=int(i[:-2].split(" ")[1])
                listMonk.append(monkey(num))
            elif c==1 :
                item=i[:-1].split(": ")[1].split(", ")
                listMonk[num].item=item
            elif c==2 :
                op=i[:-1].split(": ")[-1][6:]
                listMonk[num].op=op
            elif c==3 :
                test=[]
                test.append("new%"+i[:-1].split(": ")[-1].split(" ")[-1])
            elif c==4 :
                test.append(int(i[:-1].split(": ")[-1].split(" ")[-1]))
            elif c==5 :
                test.append(int(i[:-1].split(": ")[-1].split(" ")[-1]))
                listMonk[num].test=test
            elif c==6 :
                c=0
                continue
            c+=1
    nround=10000
    monkeyBusiness=[]
    mod=1
    for m in listMonk :
        mod=mod*int(m.test[0].split("%")[1])
    for n in range(nround) :
        for m in listMonk :
            for item in m.item :
                old=int(item)
                new=int(eval(m.op))%mod
                if not(eval(m.test[0])) :
                    listMonk[m.test[1]].item.append(new)
                else :
                    listMonk[m.test[2]].item.append(new)
                m.ins+=1
            if m.num ==0 :
                m.diff.append(m.ins)
            m.item=[]
#        print()
#        print(n)
#    for m in listMonk :
#        print("Monkey " +str(m.num))
#        print(m.ins)
    for m in listMonk :
        monkeyBusiness.append(m.ins)
    monkeyBusiness.sort()
    return monkeyBusiness[-2]*monkeyBusiness[-1]

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

