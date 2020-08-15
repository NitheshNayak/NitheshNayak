#Created by Nithesh Nayak on 22nd Feb 2020

#The follwing code works as follows:

#Developeda balloon shooting game using Python, the player goal is to shoot the balloon down.
#The player can move the cannon up and down using the arrow keys. To fire a bullet the player will press the space key.
#1.The Balloon should move up and down randomly.
#2.The player can shoot one bullet at a time. Only when the bullet is out of the game then the player can shoot again.
#3.The game ends when the balloon is shot down, display the number of missed shots.
#4.The bullet speed is 1.5 times the speed of the balloon.
#5.The balloon changes directions (up or down) at any time.

import random
import math
import pygame

pygame.init() #Intialization
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Balloon ShootOut")
icon=pygame.image.load('pistol-gun.png')
pygame.display.set_icon(icon)

#Cannon
gunImg=pygame.image.load('cannon.png') # load Cannon Imgae
gunPosX=650 
gunPosY=236 # [600/2 - 64] = middle of Y-axis 
gunPosY_change=0

#Balloon
# 1.The Balloon should move up and down randomly.
balloonImg=pygame.image.load('balloon.png') # load Balloon Imgae
balloonPosX=0
balloonPosY=random.randint(0,472) # 472 = 600-128 (128px is size of the balloon)
balloonPosY_change=0.30 #4.The bullet speed is 1.5 times the speed of the balloon.

#Bullet
bulletImg=pygame.image.load('bullet.png') # load bullet Imgae
bulletPosX=650
bulletPosY=0 # 472 = 600-128 (128px is size of the bullet)
bulletPosX_change=0.45 #4.The bullet speed is 1.5 times the speed of the balloon.
bullet_state = "ready"  #Bullet is hidden, can't see on screen

#Counting the missed shots
missed_shots= 0
score=0
font = pygame.font.Font('freesansbold.ttf',32)
textX =10
textY =10

def display_shots(x,y):  #3.The game ends when the balloon is shot down, display the number of missed shots.
    score=font.render("Missed shots : "+str(missed_shots),True,(0,0,0)) 
    screen.blit(score,(x,y))

def gun(x,y):
    screen.blit(gunImg,(x,y))    
    
def balloon(x,y):
    screen.blit(balloonImg,(x,y)) 
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire" # bullet is currently in motion
    screen.blit(bulletImg,(x-32,y+40))
    
def balloonStrike (balloonPosX,balloonPosY,bulletPosX,bulletPosY):
    distance = math.sqrt((math.pow(balloonPosX-bulletPosX,2)) + (math.pow(balloonPosY-bulletPosY,2)))  #Mathematical formaula for calculating distance between two points
    if distance <60: # 64+16 =80 : Balloon is 128px and bullet is 32px , by adding mid point of both will give 80
        return True
    else:
        return False
    
running = True #screen Stays
while running:
    
    screen.fill((255,255,255)) #RGB for White
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            
    #Key Board interface
    if event.type ==pygame.KEYDOWN:
        if event.key==pygame.K_DOWN: #Moving Down
            gunPosY_change = +0.3
        if event.key==pygame.K_UP: # Moving Up
            gunPosY_change = -0.3
        if event.key==pygame.K_SPACE: # Firing the bullet
            if bullet_state is "ready":
                bulletPosY=gunPosY #Current co-ordinates of the cannon
                fire_bullet(bulletPosX,bulletPosY)
            
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_DOWN or event.key==pygame.K_UP: # Key Released
            gunPosY_change= 0

#Updating Cannon and balloon co-ordinates
    gunPosY += gunPosY_change
    balloonPosY += balloonPosY_change
    
#Defining the Boundary
    # for the player 
    if gunPosY <=0:  
        gunPosY = 0
    elif gunPosY >=472: # 600-128( 128px is size of the cannon)
        gunPosY = 472
        
    #for the target
    if balloonPosY <=0: 
        balloonPosY_change = 0.3
        balloonPosY = random.randint(0,472)  #5.The balloon change directions (up or down) at any time.
    elif balloonPosY >=472: # 600-128( 128px is size of the balloon)
        balloonPosY_change = -0.3
        balloonPosY = random.randint(0, 472) #5.The balloon change directions (up or down) at any time.
        
    #bullet_path
    # 2.The player can shoot one bullet at a time. Only when the bullet is out of the game then the player can shoot again.
    if bulletPosX <=0: 
        missed_shots += 1
        bulletPosX= 650
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletPosX,bulletPosY)
        bulletPosX -= bulletPosX_change
     
    # Balloon strike
    strike = balloonStrike(balloonPosX,balloonPosY,bulletPosX,bulletPosY)

    if strike:
       print("Total missed Shots are:", missed_shots) #3.The game ends when the balloon is shot down, display the number of missed shots.
       print("kudos, Well Played")
       print("Game Over")
       break

    else:
        None
          
    gun(gunPosX,gunPosY)   
    balloon(balloonPosX,balloonPosY)
    display_shots(textX,textY)
    pygame.display.update()