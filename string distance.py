import random
import string
import time
import psutil

iCount = 100

class StringEvolution:
    def  __init__(self, sBase):
        self.sBase = sBase
        self.sShuffle =''
        self.arrS = ['' for x in range(iCount)]
        self.arrD = [100 for x in range(iCount)]
        self.sLen = len(sBase)
        self.iGen = 0
        self.iMinDist = 0
        

    def Shuffle(self):
        self.sShuffle=''
        for i in self.sBase:
            self.sShuffle += random.choice(string.ascii_letters)
        for i in range(iCount):
            self.arrS[i] = self.sShuffle

    def f(self):
        return self.sBase

    def f2(self):
        return self.sShuffle

    def levdistR(self, s1, s2, l1, l2):
        if l1==0: return l2
        if l2==0: return l1
        if s1[l1-1] == s2[l2-1]: cost = 0
        else: cost = 1
        return min(self.levdistR(s1, s2, l1-1, l2) +1,
                   self.levdistR(s1, s2, l1  ,l2-1)+1,
                   self.levdistR(s1, s2, l1-1,l2-1)+cost)

    def levdistI(self, s1, s2):
        m = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]
        for x in range(1, len(s1)+1):
            m[x][0] = x
        for y in range(1, len(s2)+1):
            m[0][y] = y
        for y in range(1,len(s2)+1):
            for x in range(1,len(s1)+1):
                if s1[x-1] == s2[y-1]:
                    subCost = 0
                else:
                    subCost = 1
                m[x][y] = min(m[x-1][y] +1,
                              m[x][y-1] +1,
                              m[x-1][y-1] +subCost)
        return m[len(s1)][len(s2)]

    def hamdist(self, s1, s2):
        return sum(el1 != el2 for el1, el2 in zip(s1, s2))

    def evolve(self, s):
        #iRandAmount = random.randint(1, self.sLen)
        sOut = ''
        for i in s:
            iRand = random.randint(0, 100)
            if iRand == 0:
                sOut += random.choice(string.ascii_letters)
            else:
                sOut +=i
        return sOut

    def evolveAll(self):
        iMinInd =0
        iMin = 10000
        for i in range(iCount):
            self.arrS[i] = self.evolve(self.arrS[i])
            self.arrD[i] = self.hamdist(self.sBase, self.arrS[i])
            if self.arrD[i] < iMin:
                iMin = self.arrD[i]
                iMinInd = i
        return iMinInd

    def nextGen(self, iBase):
        for i in range(iCount):
            self.arrS[i] = self.arrS[iBase]
        if self.iMinDist > self.arrD[iBase] or self.iGen == 0:
            self.iMinDist = self.arrD[iBase]
            print('Generation: ', self.iGen,' best: ',self.arrS[iBase],'distance: ',self.arrD[iBase])
        self.iGen += 1
    

x= StringEvolution('LetsTrySomeLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongStringLongerThanThisForSure')
x.Shuffle()
x.iMinDist = x.hamdist(x.sBase, x.sShuffle)
#a = x.f()
#b = x.f2()
print(x.f())
print(x.f2())
#c = x.levdistI(a,b)
#print(c)
#d = x.hamdist(a,b)
#print(d)
start_time = time.time()
#for i in range(1000):
#    x.GenShuffle()
#    b = x.f2()
#    print(b)
#    c = x.levdistI(a,b)
#    print(c)
#s = x.evolve(x.f())
print(min(x.arrD)) 
while min(x.arrD) != 0:
    iInd = x.evolveAll()
    #print(iInd)
    #print(x.arrS[iInd])
    #print(x.arrD[iInd])
    x.nextGen(iInd)

print("--- %s seconds ---" % (time.time() - start_time))
