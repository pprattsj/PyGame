#import pip
#pip.main(['install']+['pygame'])
import pygame
pygame.init()
#create Screen
screenwidth = 1000
screenheight = 500
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Pallette Game")


# load images
object_img =  pygame.image.load('Fannel.png')
tile11=pygame.transform.scale(object_img,(40,40))
tile0= pygame.transform.scale(pygame.image.load('RedFieldTile.png'),(40,40))
tile2= pygame.transform.scale(pygame.image.load('BridgeTile.png'),(40,40))
tile3= pygame.transform.scale(pygame.image.load('MTile.png'),(40,40))

curr_tile = tile11
bg_img = pygame.image.load('PalletteBoard.png')
scale_bg_img = pygame.transform.scale(bg_img,(screenwidth,screenheight))

mouse_x=250
mouse_y=100
mouse_cur_pos = [mouse_x,mouse_y]
pallette=[['r','o'],['y','l'],['g','t'],['b','m'],['p','v'],['b','z']]
run = True
def get_pallette(mouse_pos,pallette,curr_tile):
    #print(mouse_pos)
    x=int((mouse_pos[0]-819)/72)
    y=int((mouse_pos[1]-34)/73)
    #print(x,y)
    #print( pallette[y][x])
    tile=curr_tile
    if pallette[y][x]=='r':
        tile=tile0
    if  pallette[y][x]=='p':
        tile=tile2
    if  pallette[y][x]=='m':
        tile=tile3
    if  pallette[y][x]=='o':
        tile=tile11
    return tile


def place_Tile(mouse_pos,curr_tile):
          #print( mouse_pos[0],mouse_pos[1])
          tile_x=int((mouse_pos[0]-35)/40)*40+35
          tile_y=int((mouse_pos[1]-34)/40)*40+34
          #print(tile_x,tile_y)
          screen.blit(curr_tile,(tile_x,tile_y))
          
screen.blit(scale_bg_img,(0,0))
#screen.blit(tile0,(41,28))
while run:

# read QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# read Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cur_pos =pygame.mouse.get_pos()
            #print(mouse_cur_pos)
            mouse_x=mouse_cur_pos[0]
            mouse_y=mouse_cur_pos[1]
            if mouse_y>=34 and mouse_y <467:
                if mouse_x >= 819 and mouse_x <962:
                    #print("Pallette Area")
                    curr_tile = get_pallette(mouse_cur_pos,pallette,curr_tile)
                    #print(curr_pallet)
                if mouse_x >= 35 and mouse_x <789:
                    #print("Canvas Area")
                    place_Tile(mouse_cur_pos,curr_tile)
                    pygame.display.update()

# Read keys
#            if event.key== pygame.K_a:
#                object_x -=20                
#            if event.key== pygame.K_d:
#                object_x +=20                
#            if event.key== pygame.K_s:                
#                object_y +=20
#            if event.key== pygame.K_w:                
#                object_y -=20
            
    pygame.display.update()
    

pygame.quit()
