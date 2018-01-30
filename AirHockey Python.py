import pygame
import math

pygame.init()

name = "Air Hockey"
pygame.display.set_caption(name)

size = (600, 700)
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (11, 174, 224)
YELLOW = (255, 255, 0)

yellow_x = 300
yellow_y = 500
red_x = 300
red_y = 200
puck_x= 300
puck_y= 350

yellow_change_x = 0
yellow_change_y = 0
red_change_x = 0
red_change_y = 0
puck_change_x = -2
puck_change_y = 1

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    '''if((yellow_y - 40 == puck_y + 30 and yellow_x == puck_x) or (yellow_x + 40 == puck_x - 30 and yellow_y == puck_x) or (yellow_y + 40 == puck_y - 30 and yellow_x == puck_x) or (yellow_x - 40 == puck_x + 30 and yellow_y == puck_y)):
        puck_change_x = yellow_change_x
        puck_change_y = yellow_change_y
        
    if((yellow_x + 40 == puck_x - 30 and yellow_y + 5 == puck_y) or (yellow_x - 5 == puck_x and yellow_y + 5 == puck_y) or (yellow_x + 5 == puck_x and yellow_y - 5 == puck_y) or (yellow_x - 5 == puck_x and yellow_y - 5 == puck_y)):
                puck_change_x = yellow_change_x
                puck_change_y = yellow_change_y
    elif((red_x + 5 == puck_x and red_y + 5 == puck_y) or (red_x - 5 == puck_x and red_y + 5 == puck_y) or (red_x + 5 == puck_x and red_y - 5 == puck_y) or (red_x - 5 == puck_x and red_y - 5 == puck_y)):
                puck_change_x = red_change_x
                puck_change_y = red_change_y'''
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            yellow_change_x = -5
        elif event.key == pygame.K_d:
            yellow_change_x = 5
        elif event.key == pygame.K_w:
            yellow_change_y = -5
        elif event.key == pygame.K_s:
            yellow_change_y = 5
        elif event.key == pygame.K_LEFT:
            red_change_x = -5
        elif event.key == pygame.K_RIGHT:
            red_change_x = 5
        elif event.key == pygame.K_UP:
            red_change_y = -5
        elif event.key == pygame.K_DOWN:
            red_change_y = 5

    if(puck_x > 540 - 30 or puck_x < 60 + 30):
        puck_change_x *= -1
    if(puck_y > 700 - 30 or puck_y < 0 + 30):
        puck_change_y *= -1
            
    if(((puck_x - yellow_x)**2 + (puck_y - yellow_y)**2)**(0.5) <= 70):
        puck_change_x = (puck_x - yellow_x) + yellow_change_x/100
        puck_change_y = (puck_y - yellow_y) + yellow_change_y/100
    if(((puck_x - red_x)**2 + (puck_y - red_y)**2)**(0.5) <= 70):
        puck_change_x = red_change_x
        puck_change_y = red_change_y
    
    #movement
    yellow_x += yellow_change_x
    yellow_y += yellow_change_y
    red_x += red_change_x
    red_y += red_change_y
    puck_x += puck_change_x
    puck_y += puck_change_y

    
    '''elif(puck_x < 95 and puck_y > 670):
        puck_change_x = 5;
        puck_change_y = 5;
    elif(puck_x > 695 and puck_y > 670):
        puck_change_x = -5;
        puck_change_y = 5;
    elif(puck_x < 95 and puck_y < 30):
        puck_change_x = 5;
        puck_change_y = -5;
    elif(puck_x > 695 and puck_y < 30):
        puck_change_x = -5;
        puck_change_y = -5;'''
    
    if red_x > 530 - 40 :
        red_x = 489
        red_x_change = 0
    if red_x < 70 + 40:
        red_x = 111
        red_x_change = 0
    if red_y > 280 + 40: 
        red_y = 321
        red_y_change = 0
    if red_y < 75 - 40:
        red_y = 34
        red_y_change = 0
        
    if yellow_x > 530 - 40:
        yellow_x = 489
        yellow_change_x = 0
    if yellow_x < 70 + 40:
        yellow_x = 111
        yellow_change_x = 0
    if yellow_y > 620 + 40:
        yellow_y = 659
        yellow_change_y = 0
    if yellow_y < 420 - 40:
        yellow_y = 379
        yellow_change_y = 0



#puck bounce

    if(puck_x >= 165 and puck_x <= 435 and puck_y >= -20 and puck_y <= 30):
        print("Player 1 scored!")
        yellow_x = 300
        yellow_change_x = 0
        yellow_change_y = 0
        yellow_y = 500
        red_x = 300
        red_change_x = 0
        red_change_y = 0
        red_y = 200
        puck_x = 300
        puck_y = 350
        puck_change_x = 0
        puck_change_y = 5;
        
    elif(puck_x >= 165 and puck_x <= 435 and puck_y >= 670 and puck_y <= 720):
        print("Player 2 scored!")
        yellow_x = 300
        yellow_change_x = 0
        yellow_change_y = 0
        yellow_y = 500
        red_x = 300
        red_change_x = 0
        red_change_y = 0
        red_y = 200
        puck_x = 300
        puck_y = 350
        puck_change_x = 0
        puck_change_y = -5;

    screen.fill(BLUE)
    
    #BORDERS
    pygame.draw.circle(screen, WHITE, [125, 50], 50)
    pygame.draw.circle(screen, WHITE, [475, 50], 50)
    pygame.draw.circle(screen, WHITE, [125, 650], 50)
    pygame.draw.circle(screen, WHITE, [475, 650], 50)
    pygame.draw.rect(screen, WHITE, ((75, 50), (450, 600)))
    pygame.draw.polygon(screen, WHITE, ((125, 0), (175, 0), (175, 50)), 0)
    pygame.draw.polygon(screen, WHITE, ((425, 0), (475, 0), (425, 50)), 0)
    pygame.draw.polygon(screen, WHITE, ((125, 700), (175, 700), (175, 650)), 0)
    pygame.draw.polygon(screen, WHITE, ((425, 700), (475, 700), (425, 650)), 0)

    #CREASE UP
    pygame.draw.rect(screen, RED, ((175, 0), (10, 100)))
    pygame.draw.rect(screen, RED, ((415, 0), (10, 100)))
    pygame.draw.rect(screen, RED, ((185, 90), (230, 10)))
    pygame.draw.rect(screen, LIGHT_BLUE, ((185, 10), (230, 80)))
    pygame.draw.rect(screen, BLACK, ((185, 0), (230, 10)))
    
    #CREASE DOWN
    pygame.draw.rect(screen, RED, ((175, 600), (10, 100)))
    pygame.draw.rect(screen, RED, ((415, 600), (10, 100)))
    pygame.draw.rect(screen, RED, ((185, 600), (230, 10)))
    pygame.draw.rect(screen, LIGHT_BLUE, ((185, 610), (230, 80)))
    pygame.draw.rect(screen, BLACK, ((185, 690), (230, 10)))

    #CIRCLES
    pygame.draw.circle(screen, RED, (300, 350), 60, 10)
    pygame.draw.circle(screen, RED, (300, 350), 8, 0)
    pygame.draw.circle(screen, RED, (175, 500), 50, 10)
    pygame.draw.circle(screen, RED, (175, 500), 4, 0)
    pygame.draw.circle(screen, RED, (425, 500), 50, 10)
    pygame.draw.circle(screen, RED, (425, 500), 4, 0)
    pygame.draw.circle(screen, RED, (175, 200), 50, 10)
    pygame.draw.circle(screen, RED, (175, 200), 4, 0)
    pygame.draw.circle(screen, RED, (425, 200), 50, 10)
    pygame.draw.circle(screen, RED, (425, 200), 4, 0)

    #LINES
    pygame.draw.line(screen, RED, (75, 350), (240, 350), 10)
    pygame.draw.line(screen, RED, (360, 350), (525, 350), 10)
    pygame.draw.line(screen, LIGHT_BLUE, (75, 430), (525, 430), 10)
    pygame.draw.line(screen, LIGHT_BLUE, (75, 270), (525, 270), 10)

    #HANDLES
    pygame.draw.circle(screen, YELLOW, (yellow_x, yellow_y), 40, 0)
    pygame.draw.circle(screen, RED, (red_x, red_y), 40, 0)

    pygame.draw.circle(screen, BLACK, (puck_x, puck_y), 30, 0)

    #scoreboard
    pygame.draw.rect(screen,YELLOW,[15,350,60,75],3)
    pygame.draw.rect(screen,RED,[15,275,60,75],3)


    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
pygame.quit()
