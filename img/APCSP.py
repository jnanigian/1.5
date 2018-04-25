import pygame
import os
#Used Pygame as a module for code
#Also used os to import images
#Also got QR code image from online
stage=0
img_dir = os.path.join(os.path.dirname(__file__), "img")
WIDTH = 350
HEIGHT = 400
FPS = 30
size=1
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE=(255,165,0)
PURPLE=(160,32,240)
gamestart=1
score1=0
score2=0
game_folder=os.path.dirname(__file__)
img_folder= os.path.join(game_folder,"img")
img= img_folder
height = len(img)
width = len(img[0])


class QRTEXT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "qrtex.png")).convert()
        self.rect = self.image.get_rect()

        self.rect.center = (175, 300)


    def update(self):
        self.rect.center = (175, 300)


class QR(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "sample.png")).convert()
        self.rect = self.image.get_rect()

        self.rect.center = (175, 100)


    def update(self):
        global stage
        if stage==0:
            self.speedx=0
        if stage >0:
            self.speedx=30
        keystate = pygame.key.get_pressed()



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
background=pygame.image.load(os.path.join(img_dir, "unnamed.png")).convert()
background_rect=background.get_rect()
all_sprites = pygame.sprite.Group()
ballg=pygame.sprite.Group()
qr=QR()
qrtex=QRTEXT()
all_sprites.add(qr,qrtex)

# Game loop
running = True

while running==True:

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(WHITE)

    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

import time
codelist=[10000000,11000000,11100000,11110000,11111000]

games="No"


def start():
    print("This app is made to make it easier to add your friends in all your apps and games,")
    time.sleep(1)
    print("You insert a specific code of the person you would like to add and thern that person's phone number is added to your contacts,")
    time.sleep(1)
    print("You are also given the option to add these friends to your games")
    time.sleep(1)
    code=int(input("What is the code for the person you would like to add?"))
    if code==codelist[0]:
        print("This is a code for Mason Ross!")
        time.sleep(1)
        print("This person's number will be added to your contacts!")
        time.sleep(1)
        print("Mason Ross Contact Information")
        time.sleep(1)
        print("Phone Number:856-325-3392")
        time.sleep(1)
        print("Residence:California")
        time.sleep(1)
        game= str(input("Would you like to add this person to your games?"))
        if games=="yes" or "Yes":
            print("Great!")
            gamenum= int(input("How many games would you like to add this person to?"))
            for i in range(gamenum):
                game=str(input("What Game would you like to add this person to?"))
                print("Mason Ross has been added to " + game)
        else:
            print("Okay, Thanks for using this app!")
        print("This person is now on your phone")



    if code==codelist[1]:
        print("This is a code for Devin Patel!")
        time.sleep(1)
        print("This person's number will be added to your contacts!")
        time.sleep(1)
        print("Devin Patel Contact Information")
        time.sleep(1)
        print("Phone Number:852-322-3396")
        time.sleep(1)
        print("Residence:California")
        time.sleep(1)
        game= str(input("Would yo like to add this person to your games?"))
        if games=="yes" or "Yes":
            print("Great!")
            gamenum= int(input("How many games would you like to add this person to?"))
            for i in range(gamenum):
                game=str(input("What Game would you like to add this person to?"))
                print("Devin Patel has been added to " + game)
        else:
            print("Okay, Thanks for using this app!")
        print("This person is now on your phone")

















pygame.quit()
start()
