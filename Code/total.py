import copy
import random
import heapq
from collections import deque
#-----------------------------------------------------------
sz = 10
check = [[False] * sz for _ in range(sz)]
rr = [0, 0, 1, -1]
cc = [1, -1, 0, 0]
pth = []
cur = []
newcur = []
start = [[0] * sz for _ in range(sz)]
#----------------------------------------------------------
def heuristic_function(v):
    blue=0
    red=0
    for i in range(sz):
        for j in range(sz):
            if v[i][j]==1:
                red=1
            elif v[i][j]==2:
                blue=1
    return red+blue

def print_list(v):
    for i in range(sz):
        for j in range(sz):
            print(v[i][j], end='')
        print(' ')
    print("-------------------------------------")

def finish(v):
    for j in range(sz):
        if v[sz - 1][j] != 0:
            return False
    return True

def floodfill(i, j, v, c):
    if v[i][j] == c:
        v[i] = list(v[i])  # Convert the string to a list of characters
        v[i][j] = 0  # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < sz and 0 <= jj < sz:
                floodfill(ii, jj, v, c)

def fall(v):
    for i in range(sz - 2, -1, -1):
        for j in range(sz):
            if v[i + 1][j] == 0 and v[i][j] != 0:
                k = i
                while k < sz - 1 and v[k + 1][j] == 0:
                    v[k + 1][j] = v[k][j]  # Reassign the value in the list
                    v[k][j] = 0  # Reassign the value in the list
                    k += 1

def fall2(v):
    for i in range(sz - 1):
        if v[sz - 1][i] == 0 and v[sz - 1][i + 1] != 0:
            k = i
            while k > -1 and v[sz - 1][k] == 0:
                for j in range(sz):
                    v[j][k] = v[j][k + 1]
                    v[j][k + 1] = 0
                k -= 1
#------------------------------------------------------------------------
def a_star():
    mp = {}
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)

    # Using heapq for the priority queue
    q = [(heuristic_function(start), (start, []))]
    while q:
        x , (cur, path) = heapq.heappop(q)
        if finish(cur):
            pth = path
            break
        for i in range(sz):
            for j in range(sz):
                check[i][j] = 0 if cur[i][j] == 0 else 1

        for i in range(sz):
            for j in range(sz):
                if check[i][j] == 1:
                    newcur = copy.deepcopy(cur)
                    floodfill(i, j, newcur, newcur[i][j])
                    fall(newcur)
                    fall2(newcur)
                    newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                    if newcur_tuple not in mp:
                        mp[tuple(map(tuple, newcur))] = 1
                        heapq.heappush(q, (x + 1 +heuristic_function(newcur), (newcur, path + [i, j])))
    # Reconstruct the path
    ans = []
    a = 0
    nw = copy.deepcopy(start)
    ans.append(nw)
    while not finish(start):
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2

    ans.pop()
    return ans

def bfs():
    sz=10
    pth=[]
    newcur = []
    cur = []
    start = [[0] * sz for _ in range(sz)]
    mp = {}
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
                    fall2(newcur)
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
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans

def depth_limit_search():
    limit=5
    pth=[]
    mp = {}
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)
    # Using deque for the queue
    q = deque([(start, 0,[])])
    while q:
        cur, x , path = q.pop()
        if finish(cur):
            pth=path
            break

        if limit==x:
            continue
        for i in range(sz):
            for j in range(sz):
                check[i][j] = 0 if cur[i][j] == 0 else 1

        for i in range(sz):
            for j in range(sz):
                if check[i][j] == 1:
                    newcur=copy.deepcopy(cur)
                    floodfill(i,j,newcur,newcur[i][j])
                    fall(newcur)
                    fall2(newcur)
                    newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                    if newcur_tuple not in mp:
                        mp[tuple(map(tuple, newcur))] = 1
                        q.append((newcur, x + 1,path+[i,j]))
    # Reconstruct the path
    if len(pth)==0:
        print("no answer found")
        exit()
    ans = []
    a=0
    nw=copy.deepcopy(start)
    ans.append(nw)
    while not finish(start):
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans

def dfs():
    mp = {}
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)
    # Using deque for the queue
    q = deque([(start, 0,[])])
    while q:
        cur, x , path = q.pop()
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
                    fall2(newcur)
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
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans

def greedy_best_first_search():
    mp = {}
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)

    # Using heapq for the priority queue
    q = [(heuristic_function(start), (start, []))]
    while q:
        x , (cur, path) = heapq.heappop(q)
        if finish(cur):
            pth = path
            break
        for i in range(sz):
            for j in range(sz):
                check[i][j] = 0 if cur[i][j] == 0 else 1

        for i in range(sz):
            for j in range(sz):
                if check[i][j] == 1:
                    newcur = copy.deepcopy(cur)
                    floodfill(i, j, newcur, newcur[i][j])
                    fall(newcur)
                    fall2(newcur)
                    newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                    if newcur_tuple not in mp:
                        mp[tuple(map(tuple, newcur))] = 1
                        heapq.heappush(q, (heuristic_function(newcur), (newcur, path + [i, j])))
    # Reconstruct the path
    ans = []
    a = 0
    nw = copy.deepcopy(start)
    ans.append(nw)
    while not finish(start):
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans

def itirative_depth_limit_search():
    b=0
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)

    # Using deque for the queue
    for limit in range(100):
        q = deque([(start, 0,[])])
        while q:
            cur, x , path = q.pop()
            if finish(cur):
                pth=path
                b=1
                break

            if limit==x:
                continue
            for i in range(sz):
                for j in range(sz):
                    check[i][j] = 0 if cur[i][j] == 0 else 1

            for i in range(sz):
                for j in range(sz):
                    if check[i][j] == 1:
                        newcur=copy.deepcopy(cur)
                        floodfill(i,j,newcur,newcur[i][j])
                        fall(newcur)
                        fall2(newcur)
                        q.append((newcur, x + 1,path+[i,j]))
        if b:
            break

    # Reconstruct the path
    ans = []
    a=0
    nw=copy.deepcopy(start)
    ans.append(nw)
    while not finish(start):
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans

def uniform_cost_search():
    mp = {}
    for i in range(sz):
        for j in range(sz):
            start[i][j]=random.randint(1,2)

    # Using heapq for the priority queue
    q = [(0, (start, []))]

    while q:
        x , (cur, path) = heapq.heappop(q)
        if finish(cur):
            pth = path
            break
        for i in range(sz):
            for j in range(sz):
                check[i][j] = 0 if cur[i][j] == 0 else 1

        for i in range(sz):
            for j in range(sz):
                if check[i][j] == 1:
                    newcur = copy.deepcopy(cur)
                    floodfill(i, j, newcur, newcur[i][j])
                    fall(newcur)
                    fall2(newcur)
                    newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                    if newcur_tuple not in mp:
                        mp[tuple(map(tuple, newcur))] = 1
                        heapq.heappush(q, (x + 1, (newcur, path + [i, j])))
    # Reconstruct the path
    ans = []
    a = 0
    nw = copy.deepcopy(start)
    ans.append(nw)
    while not finish(start):
        floodfill(pth[a], pth[a + 1], start, start[pth[a]][pth[a + 1]])
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        fall2(start)
        nw = copy.deepcopy(start)
        ans.append(nw)
        a += 2
    ans.pop()
    return ans





#dfs()
#bfs()
#uniform_cost_search()
#depth_limit_search()
#itirative_depth_limit_search()
#a_star()
#greedy_best_first_search()



