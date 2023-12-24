import pygame
import Button
import total
import time
import random
import copy
import heapq
import math
import sys

from collections import deque
from decimal import Decimal, getcontext
pygame.init()


###############################################################################
###############################################################################
###############################################################################
###############################################################################



def print_list(v):
    for u in v:             
         for i in range(sz):
            for j in range(sz):
               print(u[i][j], end='')
            print(' ')
         print("-------------------------------------")


#-----------------------------------------------------------
sz = 10
check = [[False] * sz for _ in range(sz)]
rr = [0, 0, 1, -1]
cc = [1, -1, 0, 0]
pth = []
cur = []
newcur = []
start = [[0] * sz for _ in range(sz)]
MainArray=[]
elapsed_time_m=0
lengthof_selution=0
total_state=0
complet="NO"
optemal="YES"
Algo_Name="uniform_cost_search"
Ospace=10
TEXT_COL = (69, 43, 6)
bb=0
sz=10
number_of_red = 0
number_of_blue = 0
TimeE=10
runT1=1
start = [[0] * sz for _ in range(sz)]
ansA = []



#----------------------------------------------------------------------- heuristic function --------
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


#----------------------------------------------------------------------- finish function --------
def finish(v):
    for j in range(sz):
        if v[sz - 1][j] != 0:
            return False
    return True


#----------------------------------------------------------------------- floodfill function --------
def floodfill(i, j, v, c):
    if v[i][j] == c:
        v[i] = list(v[i])  # Convert the string to a list of characters
        v[i][j] = 0  # Reassign the value in the list
        check[i][j] = 0
        for k in range(4):
            ii, jj = i + rr[k], j + cc[k]
            if 0 <= ii < sz and 0 <= jj < sz:
                floodfill(ii, jj, v, c)


#----------------------------------------------------------------------- fall function --------
def fall(v):
    for i in range(sz - 2, -1, -1):
        for j in range(sz):
            if v[i + 1][j] == 0 and v[i][j] != 0:
                k = i
                while k < sz - 1 and v[k + 1][j] == 0:
                    v[k + 1][j] = v[k][j]  # Reassign the value in the list
                    v[k][j] = 0  # Reassign the value in the list
                    k += 1
                    
                    
#----------------------------------------------------------------------- fall function --------
def fall2(v):
    for i in range(sz - 1):
        if v[sz - 1][i] == 0 and v[sz - 1][i + 1] != 0:
            k = i
            while k > -1 and v[sz - 1][k] == 0:
                for j in range(sz):
                    v[j][k] = v[j][k + 1]
                    v[j][k + 1] = 0
                k -= 1


#----------------------------------------------------------------------- Sound initialize --------
Play_effect = pygame.mixer.Sound("Sound\\Game2.mp3")
Win_effect = pygame.mixer.Sound("Sound\\success.mp3")


#----------------------------------------------------------------------- Color initialize --------
Red = pygame.image.load('Image\\red.png') 
Yellow = pygame.image.load('Image\\Yellow.png')
White = pygame.image.load('Image\\trans_n.png') 





#----------------------------------------------------------------------- Display function --------
def display():
      space=63
      for i in range(sz):
         for j in range(sz):
               if(start[i][j]==1):
                  screen.blit(Yellow, ( 520+(j*space)  ,  70 +(i*space)   )  )
               if(start[i][j]==2):
                  screen.blit(Red,    ( 520+(j*space)  ,  70 +(i*space)    ) )
               if(start[i][j]==0):
                  screen.blit(White,  ( 520+(j*space)  ,  70 +(i*space)    ) )      

def display_Algo():
   currarray=[]
   for u in range(len(ansA)):
      screen.blit(Background_game,(0,0))
      if currarray!=ansA[u]:Play_effect.play()
      currarray=ansA[u]      
      temp=ansA[u]
      
      space=63
      for i in range(sz):
         for j in range(sz):
               if(temp[i][j]==1):
                  screen.blit(Yellow, ( 500+(j*space)  ,  65 +(i*space)   )  )
               if(temp[i][j]==2):
                  screen.blit(Red,    ( 500+(j*space)  ,  65 +(i*space)    ) )
               if(temp[i][j]==0):
                  screen.blit(White,  ( 500+(j*space)  ,  65 +(i*space)    ) )

      text_DFS_Time=Font_Main.render(str(elapsed_time_m)+" ms",False,'White')
      screen.blit(text_DFS_Time,(180,550)) 
      text_DFS_Time=Font_Main.render(str(Ospace)+" Kb",False,'White')
      screen.blit(text_DFS_Time,(180,590)) 
      text_DFS_Time=Font_Main.render(str(optemal)+" ",False,'White')
      screen.blit(text_DFS_Time,(250,497)) 
      text_DFS_Time=Font_Main.render(str(complet)+" ",False,'White')
      screen.blit(text_DFS_Time,(270,450)) 
      text_DFS_Time=Font_Main.render(str(lengthof_selution)+" ",False,'White')
      screen.blit(text_DFS_Time,(315,400)) 
      text_DFS_Time=Font_Main.render(str(total_state)+" ",False,'White')
      screen.blit(text_DFS_Time,(265,355))
      text_Algo=Font_Main.render(str(Algo_Name),False,TEXT_COL)
      screen.blit(text_Algo,(100,128))
      pygame.display.update()
      pygame.time.delay(1200)
   Win_effect.play()
   pygame.time.delay(2000)




#----------------------------------------------------------------------- count colors function --------
def count_colors():  
    global number_of_red, number_of_blue
    red=0
    blue=0
    for i in range(sz):
        for j in range(sz):
            if start[i][j] == 1:
               red += 1
            else:
               blue += 1
    number_of_blue=blue
    number_of_red=red

#----------------------------------------------------------------------- randomize function --------
def randomize():
   for i in range(sz):
      for j in range(sz):
         start[i][j]=random.randint(1,2)
   count_colors()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ai Project")

game_paused = False

Font_Main=pygame.font.Font('Font\\Glue Gun.otf', 30)

Background_Main = pygame.image.load('Image\\background_G.png')
Background_Family = pygame.image.load('Image\\Background_Family.png')
Background_Uninformed = pygame.image.load('Image\\Background_Uninformed.png')
Background_informed = pygame.image.load('Image\\Background_informed.png')
Background_rundom = pygame.image.load('Image\\Background_rundom.png')
Background_game = pygame.image.load('Image\\Background_game.png')

Btn_Exit_img = pygame.image.load('Image\\Btn_Exit.png').convert_alpha()
Btn_Info_img = pygame.image.load('Image\\Btn_Info.png').convert_alpha()
Btn_Start_img = pygame.image.load('Image\\Btn_Start.png').convert_alpha()

Btn_informed_img = pygame.image.load('Image\\Btn_informed.png').convert_alpha()
Btn_uninformed_img = pygame.image.load('Image\Btn_unInofrmed.png').convert_alpha()
Btn_home_img = pygame.image.load('Image\Btn_home.png').convert_alpha()

Btn_BFS_img = pygame.image.load('Image\Btn_BFS.png').convert_alpha()
Btn_DFS_img = pygame.image.load('Image\Btn_DFS.png').convert_alpha()
Btn_DLS_img = pygame.image.load('Image\Btn_DLS.png').convert_alpha()
Btn_UCS_img = pygame.image.load('Image\Btn_UCS.png').convert_alpha()
Btn_ID_img = pygame.image.load('Image\Btn_ID.png').convert_alpha()

Btn_rundom_img = pygame.image.load('Image\Btn_rundom.png').convert_alpha()
Btn_Start_algo_img = pygame.image.load('Image\Btn_StartAlgo.png').convert_alpha()

Btn_Gready_img = pygame.image.load('Image\Btn_gready.png').convert_alpha()
Btn_A_img = pygame.image.load('Image\Btn_A.png').convert_alpha()

Btn_Back_img = pygame.image.load('Image\Trans_n.png').convert_alpha()

Start_effect = pygame.mixer.Sound("Sound\\Start.wav")
Click_effect = pygame.mixer.Sound("Sound\\click.wav")
Dice_effect = pygame.mixer.Sound("Sound\dice.mp3")

Exit_Button = Button.Button(510, 400, Btn_Exit_img, 1)
Info_Button = Button.Button(510, 335, Btn_Info_img, 1)
Start_Button = Button.Button(510, 270, Btn_Start_img, 1)

Home_Button = Button.Button(510, 400, Btn_home_img, 1)
informed_Button = Button.Button(510, 273, Btn_informed_img, 1)
uninformed_Button = Button.Button(510, 335, Btn_uninformed_img, 1)

BFS_Button = Button.Button(450, 160, Btn_BFS_img, 1)
DFS_Button = Button.Button(450, 245, Btn_DFS_img, 1)
DLS_Button = Button.Button(450, 330, Btn_DLS_img, 1)
ID_Button = Button.Button(450, 420, Btn_ID_img, 1)
UCS_Button = Button.Button(450, 505, Btn_UCS_img, 1)

Gready_Button = Button.Button(510, 270, Btn_Gready_img, 1)
A_Button = Button.Button(510, 370, Btn_A_img, 1)

Exit_1_Button = Button.Button(590, 470, Btn_Back_img, 1)
Exit_2_Button = Button.Button(570, 640, Btn_Back_img, 1)
Exit_3_Button =  Button.Button(590, 470, Btn_Back_img, 1)
Exit_4_Button =  Button.Button(195, 640, Red, 1)

Rundom_Button =  Button.Button(50, 470, Btn_rundom_img, 1)
Rundom_Start_Button =  Button.Button(50, 570, Btn_Start_algo_img, 1)




def draw_text(text, font, text_col, x, y):
   img = font.render(text, True, text_col)
   screen.blit(img, (x, y))

run = True
Welcom_Window=True
Rundom_Window=False
Algorithm_Window=False
clock =pygame.time.Clock()
menu_state = "main"
Algorithm_Name = "None"
delay=250
xyt=0
mB=1


while run:   
   if(xyt%10==0):
      print("menu state :: ",menu_state)
      print("Algorithm  :: ",Algorithm_Name)
      print("--------------------")
   xyt+=1
   if menu_state == "main":
         if mB:
             Start_effect.play()
             mB-=1
         screen.blit(Background_Main,(0,0))
         if Start_Button.draw(screen):
            menu_state = "Rundom"
            Click_effect.play()
            pygame.time.delay(delay)
         if Info_Button.draw(screen):
            menu_state = "options"
            Click_effect.play()
            pygame.time.delay(delay)
         if Exit_Button.draw(screen):
            run = False   
            

   if menu_state == "Rundom":
         screen.blit(Background_rundom,(0,0))
         if Rundom_Start_Button.draw(screen):
            menu_state = "SelectFamily" 
            Click_effect.play()           
            pygame.time.delay(delay)
         if Rundom_Button.draw(screen):      
            runT1=1
            Dice_effect.play()
            randomize()
            MainArray=copy.deepcopy(start)
            runT1=0
            pygame.time.delay(delay)
         #print_list(start)
         display()
         text_red=Font_Main.render(str(number_of_red),False,'White')
         text_blue=Font_Main.render(str(number_of_blue),False,'White')
         screen.blit(text_red,(300,233))
         screen.blit(text_blue,(300,300))
         
         
         
                     
   elif menu_state == "SelectFamily":
         screen.blit(Background_Family,(0,0))
         if uninformed_Button.draw(screen):
            menu_state = "Uninformed"
            Click_effect.play()
            pygame.time.delay(delay)
         if Exit_Button.draw(screen):
            run = False    
         if informed_Button.draw(screen):
            menu_state = "informed"
            Click_effect.play()
            pygame.time.delay(delay)
         if Exit_1_Button.draw(screen):
            menu_state = "main"
            Click_effect.play()
            pygame.time.delay(delay)

   elif menu_state == "Uninformed":
         screen.blit(Background_Uninformed,(0,0))
         if DFS_Button.draw(screen):
            Algorithm_Name="DFS"
            Click_effect.play()
            pygame.time.delay(delay)
         if BFS_Button.draw(screen):
            Algorithm_Name="BFS"
            Click_effect.play()
             
            pygame.time.delay(delay)
         if ID_Button.draw(screen):
            Algorithm_Name="ID"
            Click_effect.play()
            pygame.time.delay(delay)
         if UCS_Button.draw(screen):
            Algorithm_Name="UCS"
            Click_effect.play()
            pygame.time.delay(delay)
         if DLS_Button.draw(screen):
            Algorithm_Name="DLS"
            Click_effect.play()
            pygame.time.delay(delay)
         if Exit_2_Button.draw(screen):
            menu_state = "SelectFamily"
            Algorithm_Name=""
            Click_effect.play()
            pygame.time.delay(delay)

   elif menu_state == "informed":
      screen.blit(Background_informed,(0,0))
      if Gready_Button.draw(screen):
         Algorithm_Name="Gready"    
         Click_effect.play()      
         pygame.time.delay(delay)
      if A_Button.draw(screen):          
         Algorithm_Name="A"
         Click_effect.play()
         pygame.time.delay(delay)
      if Exit_3_Button.draw(screen):
         menu_state = "SelectFamily"
         Click_effect.play()
         Algorithm_Name=""
         pygame.time.delay(delay)





   if Algorithm_Name!="None":     
      print("In Algorithm_Name : ")      
      screen.blit(Background_game,(0,0))
      start=copy.deepcopy(MainArray)
      if Algorithm_Name=="DFS":         
         print("IDFS")
         display()
         start_time = time.time()          
         ansA , total_state =total.dfs(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
        # 
         complet="NO"
         optemal="NO"
         Algo_Name="Depth First Search"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo() 
          
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
         
         
            
      elif Algorithm_Name=="A":
         print("As")
         display()
         start_time = time.time()          
         ansA , total_state=total.a_star(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="a star    algorithm"
         complet="YES"
         optemal="YES"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
             
      elif Algorithm_Name=="BFS":
         print("BFS")
         display()
         start_time = time.time()          
         ansA , total_state=total.bfs(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="Breadth First Search"
         complet="YES"
         optemal="YES"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()    
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
            
      elif Algorithm_Name=="DLS":
         print("DLS")

         display()
         start_time = time.time()          
         ansA , total_state=total.depth_limit_search(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="depth limit search"
         complet="NO"
         optemal="NO"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()         
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
            
      elif Algorithm_Name=="Gready":
         print("Geady")
         display()
         start_time = time.time()          
         ansA , total_state=total.greedy_best_first_search(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="greedy best first"
         complet="NO"
         optemal="No"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
            
      elif Algorithm_Name=="ID":
         print("ID")
         display()
         start_time = time.time()          
         ansA , total_state=total.itirative_depth_limit_search(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="itirative depth limit"
         complet="YES"
         optemal="YES"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
            
      elif Algorithm_Name=="UCS":
         print("UCS")
         display()
         start_time = time.time()          
         ansA , total_state=total.uniform_cost_search(start)
         print(len(ansA))
         end_time = time.time()
         elapsed_time_ms = (end_time - start_time) * 1000
         elapsed_time_m=math.trunc(elapsed_time_ms)          
         lengthof_selution= math.trunc (len(ansA)/3)
         Algo_Name="uniform cost search"
         complet="YES"
         optemal="YES"
         Ospace=math.trunc(total_state*400/1024)
         display_Algo()
         pygame.time.delay(1500)
         menu_state = "SelectFamily"
         Algorithm_Name="None"
      
          

   
         
   for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            game_paused = True
     if event.type == pygame.QUIT:
        run = False
     clock.tick(TimeE)
     pygame.display.update()
   pygame.display.update()
  #   display()

pygame.quit()