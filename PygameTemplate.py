#import pip
#pip.main(['install']+['pygame'])
import pygame
pygame.init()
screenwidth = 1000
screenheight = 500
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Land Game")
run = True
# load images
object_img =  pygame.image.load('Fannel.png')
object_x=250
object_y=100
object_cur_pos = [object_x,object_y]
bg_img = pygame.image.load('HawaiiBeach.jpg')
scale_bg_img = pygame.transform.scale(bg_img,(screenwidth,screenheight))
                                      

while run:
    screen.blit(scale_bg_img,(0,0))
    screen.blit(object_img,(object_x,object_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# Read keys
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_a:
                object_x -=20
                
            if event.key== pygame.K_d:
                object_x +=20
                
            if event.key== pygame.K_s:
                
                object_y +=20
            if event.key== pygame.K_w:
                
                object_y -=20
# read Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            Object_cur_pos =pygame.mouse.get_pos()
            #print(Object_cur_pos)
            object_x=Object_cur_pos[0]
            object_y=Object_cur_pos[1]
            
    pygame.display.update()
    

pygame.quit()
