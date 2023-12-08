from collections import deque
import copy
import random
check = [[False] * 8 for _ in range(8)]
newcur = []
cur = []
rr=[0,0,1,-1]
cc=[1,-1,0,0]
start = [[''] * 8 for _ in range(8)]
end = ['........'] * 8
mp = {}

def print_list(v):
    for i in range(8):
        for j in range(8):
            print(v[i][j],end='')
        print(' ')
    print("-------------------------------------")

def finish():
    for j in range(8):
        if cur[7][j] != '.':
            return False
    return True

def floodfill2(i, j, c):
    if newcur[i][j] == c:
        newcur[i] = list(newcur[i])  # Convert the string to a list of characters
        newcur[i][j] = '.'  # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < 8 and 0 <= jj < 8:
                floodfill2(ii, jj, c)

def floodfill1(i, j):
    floodfill2(i, j, cur[i][j])

def fall():
    for i in range(6, -1, -1):
        for j in range(8):
            if newcur[i + 1][j] == '.' and newcur[i][j] != '.':
                k = i
                while k < 7 and newcur[k + 1][j] == '.':
                    newcur[k + 1] = list(newcur[k + 1])  # Convert the string to a list of characters
                    newcur[k + 1][j] = newcur[k][j]  # Reassign the value in the list
                    newcur[k] = list(newcur[k])  # Convert the string to a list of characters
                    newcur[k][j] = '.'  # Reassign the value in the list
                    k += 1
                    # Check if k + 1 is within the valid range
                    if k + 1 < 8:
                        newcur[k + 1] = ''.join(newcur[k + 1])
                    # Check if k is within the valid range
                    if k < 8:
                        newcur[k] = ''.join(newcur[k])


# Input for 'start'
'''
for i in range(8):
    start[i] = input()
'''
for i in range(8):
    for j in range(8):
        if random.randint(1,2) % 2 == 0:
            start[i][j]='r'
        else:
            start[i][j]='b'
# Using deque for the queue
q = deque([(start, 0)])

while q:
    cur, x = q.popleft()
    if finish():
        break

    for i in range(8):
        for j in range(8):
            check[i][j] = 0 if cur[i][j] == '.' else 1

    for i in range(8):
        for j in range(8):
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

