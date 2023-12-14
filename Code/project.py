from collections import deque
import copy
import random
sz=10
check = [[False] * sz for _ in range(sz)]
newcur = []
cur = []
rr=[0,0,1,-1]
cc=[1,-1,0,0]
start = [[''] * sz for _ in range(sz)]
end = ['.'*sz] * sz
mp = {}
def print_list(v):
    for i in range(sz):
        for j in range(sz):
            print(v[i][j],end='')
        print(' ')
    print("-------------------------------------")


def finish():
    for j in range(sz):
        if cur[sz-1][j] != '.':
            return False
    return True

def floodfill2(i, j, c):
    if newcur[i][j] == c:
        newcur[i] = list(newcur[i])   # Convert the string to a list of characters
        newcur[i][j] = '.'            # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < sz and 0 <= jj < sz:
                floodfill2(ii, jj, c)

def floodfill1(i, j):
    floodfill2(i, j, cur[i][j])

def fall():
    for i in range(sz-2, -1, -1):
        for j in range(sz):
            if newcur[i + 1][j] == '.' and newcur[i][j] != '.':
                k = i
                while k < sz-1 and newcur[k + 1][j] == '.':
                    newcur[k + 1] = list(newcur[k + 1])  # Convert the string to a list of characters
                    newcur[k + 1][j] = newcur[k][j]  # Reassign the value in the list
                    newcur[k] = list(newcur[k])  # Convert the string to a list of characters
                    newcur[k][j] = '.'  # Reassign the value in the list
                    k += 1
                    # Check if k + 1 is within the valid range
                    if k + 1 < sz:
                        newcur[k + 1] = ''.join(newcur[k + 1])
                    # Check if k is within the valid range
                    if k < sz:
                        newcur[k] = ''.join(newcur[k])
    
    for i in range(sz-1):
        if newcur[sz-1][i] == '.' and newcur[sz-1][i + 1] != '.':
            k = i
            while k > -1 and newcur[sz-1][k] == '.':
                for j in range(sz):
                    newcur[j] = list(newcur[j])
                    newcur[j][k] = newcur[j][k + 1]
                    newcur[j][k + 1] = '.'
                    newcur[j] = ''.join(newcur[j])
                k -= 1


# Input for 'start'
'''
for i in range(8):
    start[i] = input()
'''
for i in range(sz):
    for j in range(sz):
        p=random.randint(1,2) % 2
        if p == 0:
            start[i][j]='r'
        elif p==1 :
            start[i][j]='b'
# Using deque for the queue
q = deque([(start, 0)])

while q:
    cur, x = q.popleft()
    if finish():
        break
    for i in range(sz):
        for j in range(sz):
            check[i][j] = 0 if cur[i][j] == '.' else 1

    for i in range(sz):
        for j in range(sz):
            if check[i][j] == 1:
                newcur=copy.deepcopy(cur)
                floodfill1(i,j)
                fall()
                newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                if newcur_tuple not in mp:
                    mp[tuple(map(tuple, newcur))] = tuple(map(tuple, cur))
                    q.append((newcur, x + 1))

# Reconstruct the path
ans = []
while tuple(map(tuple, end)) in mp:
    ans.append(list(map(list, end)))
    end = list(map(list, mp[tuple(map(tuple, end))]))

ans.append(start)
ans.reverse()

# Print the result
for i in range(len(ans)):
    print_list(ans[i])

