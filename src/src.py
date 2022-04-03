import time
from copy import deepcopy as dc
from datetime import datetime as dt
import os
import heapq as hq

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
# I.S. m, x, y, dirs terdefinisi
# F.S. mengembalikan matrix m yang telah ditempuh dengan perpindahan dari (x,y) terhadap arah dirs
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
# I.S. x dan y terdefinisi
# F.S. mengembalikan string yang menunjukkan arah perpindahan yang memungkinkan dari koordinat (x,y)
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

def posisi(num,m) -> int:
# I.S. num dan m terdefinisi
# F.S. mengembalikan posisi dari num pada m, berupa angka dari 0..15
    pos = 0
    for i in m:
        for j in i:
            if j == num:
                return pos
            pos += 1

def koordinat(m, num) -> (int,int):
# I.S. m terdefinisi, num terdefinisi
# F.S. mengembalikan koordinat (i,j) dari num
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == num:
                return i,j

def getX(m) -> int:
# I.S. m terdefinisi, selalu mengandung 0
# F.S. mengembalikan 1 apabila posisi 0 di matrix m (i,j) memenuhi (i+j) mod 2 != 0
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 0:
                return int((i+j) % 2 != 0)


def getCost(m):
# I.S. m terdefinisi
# F.S. mengembalikan nilai cost dari m, cost didapatkan dengan pendekatan banyak ubin non-kosong
#      yang berada pada susunan solusi akhir
    correct_num = 1
    count = 0
    for i in m:
        for j in i:
            if j != correct_num and j != 0:
                count += 1
            correct_num += 1
    return count 


def isSolution(m):
# I.S. m terdefinisi
# F.S. mengembalikan True apabila m merupakan solusi, False apabila tidak
    num = 1
    for i in m:
        for j in i:
            if j != num and j != 0:
                return False
            num += 1
    return True

def Kurang(m,i):
# I.S. m dan i terdefinisi
# F.S. mengembalikan nilai KURANG(i), banyaknya ubin bernomor j
#      sedemikian sehingga j < i dan POSISI(j) > POSISI(i).
    count = 0
    for arr in m:
        for j in arr:
            if j == 0:
                j = 16
            if i == 0:
                if j != i and j < 16 and posisi(j,m) > posisi(i,m):
                    count += 1
            else:
                if j!=i and j < i and posisi(j,m) > posisi(i,m):
                    count += 1
    return count

def sigmaKurang(m):
# I.S. m terdefinisi
# F.S. mengembalikan nilai total KURANG(i) untuk i pada range [0..15]
    sigma = 0
    for i in range(16):
        sigma += Kurang(m,i)
    return sigma
 
 
def getX(m):
# I.S. m terdefinisi, selalu mengandung 0
# F.S. mengembalikan True apabila (i+j) mod 2 != 0 , sebaliknya False
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 0:
                return int((i+j) % 2 != 0)
 
 
def isSolvable(m):
# I.S. m terdefinisi
# F.S. mengembalikan True apabila puzzle terdefinisi memiliki solusi, False apabila tidak
    return (sigmaKurang(m) + getX(m)) % 2 == 0

def printInitInfo(m):
# I.S. m terdefinisi
# F.S. menampilkan informasi awal, mengenai solvable / tidak
    print("0 refers to block 16")
    for i in range(16):
        print(i,":",Kurang(m, i))
    print("X :",getX(m))
    print("---------------")
    print("SIGMA KURANG + X = ", sigmaKurang(m) + getX(m))
    print()


def gatherSolvedPath(m,routes):
# I.S. m terdefinisi, routes terdefinisi yang merupakan map dari pasangan  (child , parent) dari tiap puzzle nodes
# F.S. mengembalikan list of puzzle yang merupakan rute solusi unik yang tercapai
    result = [(m,'None')]
    temp = routes[str(m)]
    while str(temp[0]) != 'root':
        result.append(temp)
        temp = routes[str(temp[0])]
    return result


def printSolvedPath(result):
# I.S. result terdefinisi, berupa list berisi puzzle yang merupakan rute solusi unik yang tercapai
# F.S. mencetak rute solusi unik yang tercapai
    for idx in range(len(result)-1,-1,-1):
        printMatrix(result[idx][0])   
        if idx == 0:
            print("PROBLEM SOLVED!!")
        else:
            move = ''
            if result[idx][1] == 'u':
                move = 'DOWN'
            elif result[idx][1] == 'd':
                move = 'UP'
            elif result[idx][1] == 'r':
                move = 'LEFT'
            else:
                move = 'RIGHT'
            print("STEP {}: MOVE {}".format(len(result)- idx , move))
