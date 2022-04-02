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

def getKurang(m):
# I.S. arr merupakan matrix puzzle terdefinisi
# F.S. mengembalikan nilai sum of KURANG(i) dengan i merupakan setiap elemen dari arr (1,2,3,...,15)
    m1=[]
    for y in m:
        for x in y:
            m1.append(x)
    m = m1
    count = 0
    for i in range(15):
        for j in range(i + 1,16):
            if (m[j] and m[i] and m[i] > m[j]):
                count+=1
    return count
 
 
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
    return (getKurang(m) + getX(m)) % 2 == 0


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


N=4
def getInvCount(arr):
    arr1=[]
    for y in arr:
        for x in y:
            arr1.append(x)
    arr=arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1,N * N):
            # count pairs(arr[i], arr[j]) such that
            # i < j and arr[i] > arr[j]
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count+=1
         
     
    return inv_count
 
 
# find Position of blank from bottom
def findXPosition(puzzle):
    # start from bottom-right corner of matrix
    for i in range(N - 1,-1,-1):
        for j in range(N - 1,-1,-1):
            if (puzzle[i][j] == 0):
                return N - i
 
 
# This function returns true if given
# instance of N*N - 1 puzzle is solvable
def isSolvable2(puzzle):
    # Count inversions in given puzzle
    invCount = getInvCount(puzzle)
 
    # If grid is odd, return true if inversion
    # count is even.
    if (N & 1):
        return ~(invCount & 1)
 
    else:    # grid is even
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1