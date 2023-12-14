import pygame
import Button

pygame.init()

#create game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load Button images
resume_img = pygame.image.load("images/Button_resume.png").convert_alpha()
options_img = pygame.image.load("images/Button_options.png").convert_alpha()
quit_img = pygame.image.load("images/Button_quit.png").convert_alpha()
video_img = pygame.image.load('images/Button_video.png').convert_alpha()
audio_img = pygame.image.load('images/Button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/Button_keys.png').convert_alpha()
back_img = pygame.image.load('images/Button_back.png').convert_alpha()


Background_Main = pygame.image.load('Image/background_G.png')
Background_Family = pygame.image.load('Image/Background_Family.png')
Background_Uninformed = pygame.image.load('Image/Background_Uninformed.png')
Background_informed = pygame.image.load('Image/Background_informed.png')
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

Btn_Gready_img = pygame.image.load('Image\Btn_gready.png').convert_alpha()
Btn_A_img = pygame.image.load('Image\Btn_A.png').convert_alpha()


Exit_Button = Button.Button(510, 400, Btn_Exit_img, 1)
Info_Button = Button.Button(510, 335, Btn_Info_img, 1)
Start_Button = Button.Button(510, 270, Btn_Start_img, 1)

Home_Button = Button.Button(510, 400, Btn_home_img, 1)
informed_Button = Button.Button(510, 270, Btn_informed_img, 1)
uninformed_Button = Button.Button(510, 335, Btn_uninformed_img, 1)

BFS_Button = Button.Button(450, 160, Btn_BFS_img, 1)
DFS_Button = Button.Button(450, 245, Btn_DFS_img, 1)
DLS_Button = Button.Button(450, 330, Btn_DLS_img, 1)
ID_Button = Button.Button(450, 420, Btn_ID_img, 1)
UCS_Button = Button.Button(450, 505, Btn_UCS_img, 1)

Gready_Button = Button.Button(510, 270, Btn_Gready_img, 1)
A_Button = Button.Button(510, 370, Btn_A_img, 1)


#create Button instances
resume_Button = Button.Button(304, 125, resume_img, 1)
options_Button = Button.Button(297, 250, options_img, 1)
quit_Button = Button.Button(336, 375, quit_img, 1)
video_Button = Button.Button(226, 75, video_img, 1)
audio_Button = Button.Button(225, 200, audio_img, 1)
keys_Button = Button.Button(246, 325, keys_img, 1)
back_Button = Button.Button(332, 450, back_img, 1)





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
#menu_state = "SelectFamily"

while run:
    
  #  screen.blit(Background_Main,(0,0))
    print(menu_state)
    if menu_state == "main":
        screen.blit(Background_Main,(0,0))
        if Start_Button.draw(screen):
            menu_state = "SelectFamily"
        if Info_Button.draw(screen):
            menu_state = "options"
        if Exit_Button.draw(screen):
            run = False            
    elif menu_state == "SelectFamily":
          screen.blit(Background_Family,(0,0))
          if uninformed_Button.draw(screen):
              menu_state = "Uninformed"
          if informed_Button.draw(screen):
              menu_state = "informed"
          if Exit_Button.draw(screen):
             run = False    

    elif menu_state == "Uninformed":
          screen.blit(Background_Uninformed,(0,0))
          if DFS_Button.draw(screen):
             Algorithm_Name="DFS"
          if BFS_Button.draw(screen):
             Algorithm_Name="BFS"
          if ID_Button.draw(screen):
             Algorithm_Name="ID"
          if UCS_Button.draw(screen):
             Algorithm_Name="UCS"
          if DLS_Button.draw(screen):
             Algorithm_Name="DLS"
    elif menu_state == "informed":
          screen.blit(Background_informed,(0,0))
          if Gready_Button.draw(screen):
             Algorithm_Name="Gready"
          if A_Button.draw(screen):
             Algorithm_Name="A"
         

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
    for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            game_paused = True
    if event.type == pygame.QUIT:
        run = False
    clock.tick(10)
    pygame.display.update()

pygame.quit()