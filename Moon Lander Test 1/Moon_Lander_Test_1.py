import pygame
pygame.init()
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)

screen = pygame.display.set_mode((700, 1000))

pygame.display.set_caption("Lunar Lander Simulation")

backround = pygame.image.load("C:/Users/768588/Downloads/astrophotography-tips-stars-night-sky-milky-way-crater-lake-national-park-oregon-1.jpg")



doExit = False
clock = pygame.time.Clock()

#CONSTANTS
Fuel = 1000

xPos = 350
yPos = 500

xVel = 0
yVel = -10/60

kup = False
kright = False
kleft = False

isOnGround = False
RocketOn = False
crashed = False

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity: ', False, (0,200, 200))
text2 = font.render(str(int(yVel)), 1, (0, 200, 200))
text3 = font.render('You Crashed', False, (200, 50, 50))
text4 = font.render('Vertical velocity: ', False, (200, 20, 20))
text5 = font.render(str(int(yVel)), 1, (200, 20, 20))
text6 = font.render('Height: ', False, (20,20,200))
text7 = font.render(str(int(yPos)), 1, (20, 20, 200))
text8 = font.render('Fuel: ', False, (20,20,200))
text9 = font.render(str(int(Fuel)), 1, (20, 20, 200))




while doExit == False:

    clock.tick(60)
    kup = False
    kright = False
    kleft = False
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            doExit = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                kleft = True
            if event.key == pygame.K_UP:
                kup = True
            if event.key == pygame.K_RIGHT:
                kright = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kleft = False
            if event.key == pygame.K_UP:
                kup = False
            if event.key == pygame.K_RIGHT:
                kright = False


#input-------------------------------------------------------
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        xVel -= 1/60
         
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        xVel += 1/60

    else:
        xVel = 0

    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        yVel -= .417/60
        isOnGround = False
        RocketOn = True
        Fuel -= 2
  
 
    else:
        if isOnGround == False:
            yVel += 1.62/60
        RocketOn = False

#physics------------------------------------------------------------

    if isOnGround == True and abs(yVel) >.5:
        crashed = True
        xPos = 350
        yPos = 0
        xVel = 0
        yVel = 0
        isOnGround = False

    if isOnGround == True and abs(yVel) <.5:
        crashed = False
        xVel = 0
        yVel = 0
    print("yVel is", yVel)

    if yPos > 950:
        isOnGround = True
        yPos = 950

    if Fuel < 0:
        doExit = True
        print("You ran out of fuel and crashed")

#update-------------------------------------

    xPos += xVel
    yPos += yVel


    text2 = font.render(str("%.2f" %(yVel*-1)), 1, (0,200,200))
    text5 = font.render(str("%.2f" %(yVel*-1)), 1, (200,20,20))

    text6 = font.render('Height:', False, (20,20,200))
    text7 = font.render(str(int(1000-yPos)), 1, (0,200,200))

    text8 = font.render('Fuel:', False, (20,20,200))
    text9 = font.render(str(int(Fuel)), 1, (0,200,200))
        
#render---------------------------------------------------------
    screen.fill((0,0,0))

    screen.blit(backround, (0,0))
    if crashed == True:
        screen.blit(text3, (200,500))
        pygame.display.flip()
        pygame.time.wait(1000)

    if abs(yVel) < .5:
        screen.blit(text1,(10,10))
        screen.blit(text2,(250,10))
    else:
        screen.blit(text4, (20,10))
        screen.blit(text5, (250,10))

    screen.blit(text6,(10,60))
    screen.blit(text7,(150,60))
    screen.blit(text8,(10,100))
    screen.blit(text9,(150,100))

    pygame.draw.rect(screen, (250, 250, 250), (xPos, yPos, 40, 40))
    pygame.draw.rect(screen, (128, 128, 128), (350, 990, 1000, 10))
    pygame.draw.rect(screen, (128, 128, 128), (0, 990, 1000, 10))

    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
        pygame.draw.rect(screen, (255, 255, 0), (xPos, yPos+40, 40, 10))
        pygame.draw.rect(screen, (255, 255, 0), (xPos+5, yPos+50, 30, 10))
        pygame.draw.rect(screen, (255, 255, 0), (xPos+10, yPos+60, 20, 10))
        pygame.draw.rect(screen, (255, 255, 0), (xPos+15, yPos+70, 10, 10))
    print(xPos,yPos)
              
    pygame.display.flip()
#end game loop###################################

pygame.quit()



            
