import random
import string
import time

class Evolve:
    def  __init__(self, sBase):
        self.sBase = sBase
        self.sShuffle =''

    def GenShuffle(self):
        self.sShuffle=''
        for i in self.sBase:
            self.sShuffle += random.choice(string.ascii_letters)

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
    

x= Evolve('Hello, world!')
x.GenShuffle()
a = x.f()
b = x.f2()
print(a)
print(b)
c = x.levdistI(a,b)
print(c)
d = x.hamdist(a,b)
print(d)
start_time = time.time()
for i in range(1000):
    x.GenShuffle()
    b = x.f2()
    print(b)
    c = x.levdistI(a,b)
    print(c)
print("--- %s seconds ---" % (time.time() - start_time))
