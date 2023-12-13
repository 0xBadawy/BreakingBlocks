from collections import deque
from sys import exit
import copy
import random
import pygame

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

def floodfill(i, j,v,c):
    if v[i][j] == c:
        v[i] = list(v[i])   # Convert the string to a list of characters
        v[i][j] = '.'            # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < sz and 0 <= jj < sz:
                floodfill(ii, jj,v, c)

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
                floodfill(i,j,newcur,newcur[i][j])
                fall()
                newcur_tuple = tuple(map(tuple, newcur))  # Convert the list to a tuple of tuples
                if newcur_tuple not in mp:
                    mp[tuple(map(tuple, newcur))] = tuple(map(tuple, cur))
                    q.append((newcur, x + 1))

# Reconstruct the path
anss = []
ans = []
while tuple(map(tuple, end)) in mp:
    anss.append(list(map(list, end)))
    end = list(map(list, mp[tuple(map(tuple, end))]))

anss.append(start)
anss.reverse()

anss2=copy.deepcopy(anss)
for i in range(0,len(anss)-1):
    b=0
    ans.append(anss[i])
    for j in range(sz-1,-1,-1):
        for k in range(sz):
            if anss2[i][j][k]!=anss2[i+1][j][k]:
                floodfill(j,k,anss2[i],anss2[i][j][k])
                ans.append(anss2[i])
                b=1
                break
        if b==1:
            break

# Print the result
for i in range(len(ans)):
    print_list(ans[i])


############################################################################################
############################################################################################


ccc=0
pygame.init()
screen = pygame.display.set_mode((1200,750))
pygame.display.set_caption('8 puzzle')
clock =pygame.time.Clock()

Red = pygame.image.load('Image/red.png').convert_alpha()
Background = pygame.image.load('Image/background.png')
Yellow = pygame.image.load('Image/Yellow.png').convert_alpha()
Background = pygame.image.load('Image/background.png')
White = pygame.image.load('Image/white.png').convert_alpha()

while True:
    for u in range(len(ans)):
        screen.blit(Background,(0,0))
        temp=ans[u]
        print(u)
        print("   ********** *******")
        space=63
        for i in range(sz):
            for j in range(sz):
                if(temp[i][j]=='b'):
                    screen.blit(Yellow, ( 465+(j*space)  ,  60 +(i*space)   )  )
                if(temp[i][j]=='r'):
                    screen.blit(Red,    ( 465+(j*space)  ,  60 +(i*space)    ) )
                if(temp[i][j]=='.'):
                    screen.blit(White,  ( 465+(j*space)  ,  60 +(i*space)    ) )  
        pygame.display.update()
        clock.tick(0.9)
    break