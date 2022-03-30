import time
from copy import deepcopy as dc
from datetime import datetime as dt
import os

def readFile(filename) -> list:
# I.S. filename terdefinisi, format benar
# F.S. mengembalikan representasi struktur data matrix dari bacaan file
    with open(filename) as f:
        return [list(map(int, line.strip('\n').split())) for line in f]

def printMatrix(m) -> None:
# I.S. m terdefinisi
# F.S. menampilkan matrix m
    print("-"*21)
    for i in m:
        print("|",end="")
        for j in i:
            if j == 0:
                print("    ",end="|")
            else:
                if j < 10:
                    print(" 0%d " % j, end="|")
                else:
                    print(" %d " % j, end="|")
        print()
        print("-"*5 + "+" + "-"*4 + "+" + "-"*4 + "+" + "-"*5)

def move(m, x,y, dirs):
    if dirs == "u":  # up
        m[x][y], m[x-1][y] = m[x-1][y], m[x][y]
    elif dirs == "r":
        m[x][y], m[x][y+1] = m[x][y+1], m[x][y]
    elif dirs == "d":
        m[x][y], m[x+1][y] = m[x+1][y], m[x][y]
    else:
        m[x][y], m[x][y-1] = m[x][y-1], m[x][y]
    return m

def moveType(x,y):
    if x > 0 and x < 3:
        if y == 0:
            return "urd" 
        elif y == 3:
            return "uld"
        else:
            return "urdl"
    elif x == 0:
        if y == 0:
            return "rd" 
        elif y == 3:
            return "ld" 
        else:
            return "rdl" 
    else:
        if y == 0:
            return "ur" 
        elif y == 3:
            return "ul" 
        else:
            return "url"

def getX(m) -> int:
# I.S. m terdefinisi, selalu mengandung 0
# F.S. mengembalikan 1 apabila posisi 0 di matrix m (i,j) memenuhi (i+j) mod 2 != 0
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 0:
                return int((i+j) % 2 != 0)

def posisi(num,m) -> int:
    pos = 0
    for i in m:
        for j in i:
            if j == num:
                return pos
            pos += 1

def koordinat(m, num) -> (int,int):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == num:
                return i,j

def kurang(num,m) -> int:
    count = 0
    for i in m:
        for j in i:
            if num == 0:
                count += int(j < 16 and posisi(j,m) > posisi(num, m))
            else:
                count += int(j < num and posisi(j,m) > posisi(num, m) and j != 0)
    return count

def totalKurang(m) -> int:
    total = 0
    for i in m:
        for j in i:
            total += kurang(j,m)
    return total

def isValidProblem(m):
    return (totalKurang(m) + getX(m)) % 2 == 0


def getCost(m):
    correct_num = 1
    count = 0
    for i in m:
        for j in i:
            if j != correct_num and j != 0:
                count += 1
            correct_num += 1
    return count 

def isSolution(m):
    num = 1
    for i in m:
        for j in i:
            if j != num and j != 0:
                return False
            num += 1
    return True


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data, cost):
        self.queue.append((cost, data))
        self.queue.sort(reverse=True)

    def remove(self):
        return self.queue.pop()[1]

    def size(self):
        return len(self.queue)

    