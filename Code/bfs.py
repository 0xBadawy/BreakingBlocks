from collections import deque
from sys import exit
import copy
import random

sz=10
pth=[]
check = [[False] * sz for _ in range(sz)]
newcur = []
cur = []
rr=[0,0,1,-1]
cc=[1,-1,0,0]
start = [[0] * sz for _ in range(sz)]
mp = {}
def print_list(v):
    for i in range(sz):
        for j in range(sz):
            print(v[i][j],end='')
        print(' ')
    print("-------------------------------------")

def finish(v):
    for j in range(sz):
        if v[sz-1][j] != 0:
            return False
    return True

def floodfill(i, j,v,c):
    if v[i][j] == c:
        v[i] = list(v[i])   # Convert the string to a list of characters
        v[i][j] = 0            # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < sz and 0 <= jj < sz:
                floodfill(ii, jj,v, c)

def fall(v):
    for i in range(sz-2, -1, -1):
        for j in range(sz):
            if v[i + 1][j] == 0 and v[i][j] != 0:
                k = i
                while k < sz-1 and v[k + 1][j] == 0:
                    v[k + 1][j] = v[k][j]  # Reassign the value in the list
                    v[k][j] = 0  # Reassign the value in the list
                    k += 1

    for i in range(sz-1):
        if v[sz-1][i] == 0 and v[sz-1][i + 1] != 0:
            k = i
            while k > -1 and v[sz-1][k] == 0:
                for j in range(sz):
                    v[j][k] = v[j][k + 1]
                    v[j][k + 1] = 0
                k -= 1

for i in range(sz):
    for j in range(sz):
        start[i][j]=random.randint(1,2)
# Using deque for the queue
q = deque([(start, 0,[])])
while q:
    cur, x , path = q.popleft()
    if finish(cur):
        pth=path
        break
    for i in range(sz):
        for j in range(sz):
            check[i][j] = 0 if cur[i][j] == 0 else 1

    for i in range(sz):
        for j in range(sz):
            if check[i][j] == 1:
                newcur=copy.deepcopy(cur)
                floodfill(i,j,newcur,newcur[i][j])
                fall(newcur)
                newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                if newcur_tuple not in mp:
                    mp[tuple(map(tuple, newcur))] = 1
                    q.append((newcur, x + 1,path+[i,j]))
# Reconstruct the path
ans = []
a=0
nw=copy.deepcopy(start)
ans.append(nw)
while not finish(start):
    floodfill(pth[a],pth[a+1],start,start[pth[a]][pth[a+1]])
    nw=copy.deepcopy(start)
    ans.append(nw)
    fall(start)
    nw=copy.deepcopy(start)
    ans.append(nw)
    a+=2
ans.pop()
for i in ans:
    print_list(i)