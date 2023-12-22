import pygame
import Button
import total
import time
import random
import copy
import heapq
from collections import deque
pygame.init()


###############################################################################
###############################################################################
###############################################################################
###############################################################################

#-----------------------------------------------------------
sz = 10
check = [[False] * sz for _ in range(sz)]
rr = [0, 0, 1, -1]
cc = [1, -1, 0, 0]
pth = []
cur = []
newcur = []
start = [[0] * sz for _ in range(sz)]
elapsed_time_m=0
ansA = []

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
############################################################
############################################################
############################################################
############################################################
bb=0
sz=10
number_of_red = 0
number_of_blue = 0
TimeE=10
runT1=1

start = [[0] * sz for _ in range(sz)]

Red = pygame.image.load('Image/red.png') 
Yellow = pygame.image.load('Image/Yellow.png')
White = pygame.image.load('Image/trans_n.png') 


def print_list(v):
    for u in range(len(v)):
         temp=v[u]        
         for i in range(sz):
            for j in range(sz):
               print(temp[i][j], end='')
            print(' ')
         print("-------------------------------------")


def display():
      space=63
   #if runT1==1:
      for i in range(sz):
         for j in range(sz):
               if(start[i][j]==1):
                  screen.blit(Yellow, ( 520+(j*space)  ,  70 +(i*space)   )  )
               if(start[i][j]==2):
                  screen.blit(Red,    ( 520+(j*space)  ,  70 +(i*space)    ) )
               if(start[i][j]==0):
                  screen.blit(White,  ( 520+(j*space)  ,  70 +(i*space)    ) ) 
     # pygame.display.update()

def display_Algo():
   for u in range(len(ansA)):
        temp=ansA[u]
        
        space=63
        for i in range(sz):
            for j in range(sz):
                  if(temp[i][j]==1):
                     screen.blit(Yellow, ( 520+(j*space)  ,  70 +(i*space)   )  )
                  if(temp[i][j]==2):
                     screen.blit(Red,    ( 520+(j*space)  ,  70 +(i*space)    ) )
                  if(temp[i][j]==0):
                     screen.blit(White,  ( 520+(j*space)  ,  70 +(i*space)    ) ) 
      #  pygame.display.update()
      #  pygame.time.delay(1200)



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




def randomize():
   for i in range(sz):
      for j in range(sz):
         start[i][j]=random.randint(1,2)
   print_list(start)
   count_colors()


#create game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

TEXT_COL = (255, 255, 255)

Font_Main=pygame.font.Font('Font/Glue Gun.otf', 30)

Background_Main = pygame.image.load('Image/background_G.png')
Background_Family = pygame.image.load('Image/Background_Family.png')
Background_Uninformed = pygame.image.load('Image/Background_Uninformed.png')
Background_informed = pygame.image.load('Image/Background_informed.png')
Background_rundom = pygame.image.load('Image/Background_rundom.png')
Background_game = pygame.image.load('Image/Background_game.png')

Btn_Exit_img = pygame.image.load('Image/Btn_Exit.png').convert_alpha()
Btn_Info_img = pygame.image.load('Image/Btn_Info.png').convert_alpha()
Btn_Start_img = pygame.image.load('Image/Btn_Start.png').convert_alpha()

Btn_informed_img = pygame.image.load('Image/Btn_informed.png').convert_alpha()
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

Rundom_Button =  Button.Button(50, 470, Btn_rundom_img, 1)
Rundom_Start_Button =  Button.Button(50, 570, Btn_Start_algo_img, 1)



def draw_text(text, font, text_col, x, y):
   img = font.render(text, True, text_col)
   screen.blit(img, (x, y))

#game loop
run = True
Welcom_Window=True
Rundom_Window=False
Algorithm_Window=False
clock =pygame.time.Clock()

menu_state = "main"
Algorithm_Name = ""
delay=250
xyt=0

while run:
   
   if(xyt%10==0):
      print("menu state :: ",menu_state)
      print("Algorithm  :: ",Algorithm_Name)
      print("--------------------")
   xyt+=1
   print(number_of_red)
   if menu_state == "main":
         screen.blit(Background_Main,(0,0))
         if Start_Button.draw(screen):
            menu_state = "Rundom"
            pygame.time.delay(delay)
         if Info_Button.draw(screen):
            menu_state = "options"
            pygame.time.delay(delay)
         if Exit_Button.draw(screen):
            run = False   
            

   if menu_state == "Rundom":
         screen.blit(Background_rundom,(0,0))
         if Rundom_Start_Button.draw(screen):
            menu_state = "SelectFamily"            
            pygame.time.delay(delay)
         if Rundom_Button.draw(screen):
            runT1=1
            randomize()
            runT1=0
            pygame.time.delay(delay)
         print_list(start)
         display()
         text_red=Font_Main.render(str(number_of_red),False,'White')
         text_blue=Font_Main.render(str(number_of_blue),False,'White')
         screen.blit(text_red,(300,233))
         screen.blit(text_blue,(300,300))
         
         

         
                     
   elif menu_state == "SelectFamily":
         screen.blit(Background_Family,(0,0))
         if uninformed_Button.draw(screen):
            menu_state = "Uninformed"
            pygame.time.delay(delay)
         if Exit_Button.draw(screen):
            run = False    
         if informed_Button.draw(screen):
            menu_state = "informed"
            pygame.time.delay(delay)
         if Exit_1_Button.draw(screen):
            menu_state = "main"
            pygame.time.delay(delay)

   elif menu_state == "Uninformed":
         screen.blit(Background_Uninformed,(0,0))
         if DFS_Button.draw(screen):
            Algorithm_Name="DFS"
            menu_state="Algo"
            pygame.time.delay(delay)
         if BFS_Button.draw(screen):
            Algorithm_Name="BFS"
             
            pygame.time.delay(delay)
         if ID_Button.draw(screen):
            Algorithm_Name="ID"
             
            pygame.time.delay(delay)
         if UCS_Button.draw(screen):
            Algorithm_Name="UCS"
             
            pygame.time.delay(delay)
         if DLS_Button.draw(screen):
            Algorithm_Name="DLS"
             
            pygame.time.delay(delay)
         if Exit_2_Button.draw(screen):
            menu_state = "SelectFamily"
            Algorithm_Name=""
            pygame.time.delay(delay)

   elif menu_state == "informed":
      screen.blit(Background_informed,(0,0))
      if Gready_Button.draw(screen):
         Algorithm_Name="Gready"          
         pygame.time.delay(delay)
      if A_Button.draw(screen):          
         Algorithm_Name="A"
         pygame.time.delay(delay)
      if Exit_3_Button.draw(screen):
         menu_state = "SelectFamily"
         Algorithm_Name=""
         pygame.time.delay(delay)

   if Algorithm_Name=="DFS":     
      screen.blit(Background_game,(0,0))
      if Algorithm_Name=="DFS" and bb==0:
          start_time = time.time()
          ansA=total.dfs()
          #print_list(ansA)
          
          display_Algo()          
          end_time = time.time()
          elapsed_time_m = (end_time - start_time) * 1000
      bb+=1
          

   
         
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


'''

    #check if the options menu is open
    if menu_state == "options":
        #draw the different options Buttons
        if video_Button.draw(screen):
            print("Video Settings")
        if audio_Button.draw(screen):
            print("Audio Settings")
        if keys_Button.draw(screen):
          print("Change Key Bindings")
        if back_Button.draw(screen):
           menu_state = "main"


'''
  #event handler
   

pygame.quit()