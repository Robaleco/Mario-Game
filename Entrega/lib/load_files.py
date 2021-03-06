import pygame
from pygame import *
import random

# Script que Guarda Variáveis estáticas(Imagens, Sons, Tipo de Texto) e Funções as Quais Lidam Com Transformação
# Destes Dados

Screen_Width = 1920
Screen_Height =  1080
#pyautogui.size()
pygame.init()
window_size=(1920,1080)
window = pygame.display.set_mode(window_size, flags=pygame.FULLSCREEN)
window_size = (Screen_Width, Screen_Height)

pygame.display.set_caption("Interactive Mario Game")
clock = pygame.time.Clock()

# Sons
mixer.init()
Jump = mixer.Sound("Sounds/Jump (Small Mario).wav")
Coin_Sound = mixer.Sound("Sounds/Coin.wav")
Game_Over = mixer.Sound("Sounds/Game Over.wav")
Bump = mixer.Sound("Sounds/Bump.mp3")
Duck = mixer.Sound("Sounds/Fire Works.wav")
Mario_Dies = mixer.Sound("Sounds/Mario Dies.wav")

# BackGround Music
mixer.music.load("Sounds/BackGroundMusic.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.05)

font = pygame.font.Font("resources/SuperMario256.ttf", 64)
Loser_Text = font.render('Loser', True, (255, 255, 255), (0, 0, 0))
LoserRect = Loser_Text.get_rect()
LoserRect.center = (Screen_Width // 2, Screen_Height // 2)

# Load BackGround
BackGround = pygame.image.load("Sprite/BackGround/BackGround.jpg").convert()
BackGround = pygame.transform.scale(BackGround, (Screen_Width, Screen_Height))

# Mover BackGround
BackGroundX = 0
BackGroundX2 = BackGround.get_width()


# Load Imagens Lives
Hearts_3 = pygame.image.load("Sprite/Lives/noback.png").convert_alpha()
Hearts_3 = pygame.transform.scale(Hearts_3, (Screen_Width / 6, Screen_Height / 10))
Hearts_2 = pygame.image.load("Sprite/Lives/noback1.png").convert_alpha()
Hearts_2 = pygame.transform.scale(Hearts_2, (Screen_Width / 6, Screen_Height / 10))
Hearts_1 = pygame.image.load("Sprite/Lives/noback2.png").convert_alpha()
Hearts_1 = pygame.transform.scale(Hearts_1, (Screen_Width / 6, Screen_Height / 10))

# Load das Imagens Bonus
# Bónus Aéreos e Terrestres
Coin = pygame.image.load("Sprite/Bonus/Coin.png").convert_alpha()
Coin = pygame.transform.scale(Coin, (Screen_Width / 15, Screen_Height / 10))
#RedCoin = pygame.image.load("Sprite/Bonus/RedCoin.png").convert_alpha()
#BlueCoin = pygame.image.load("Sprite/Bonus/BlueCoin.png").convert_alpha()
#PurpleCoin = pygame.image.load("Sprite/Bonus/PurpleCoin.png").convert_alpha()
#GreenCoin = pygame.image.load("Sprite/Bonus/GreenCoin.png").convert_alpha()

#BigPrincessCoin = pygame.image.load("Sprite/Bonus/BigPrincessCoin.png").convert_alpha()
BigYoshiCoin = pygame.image.load("Sprite/Bonus/BigYoshiCoin.png").convert_alpha()
BigYoshiCoin = pygame.transform.scale(BigYoshiCoin, (Screen_Width / 15, Screen_Height / 8))

BigACoin = pygame.image.load("Sprite/Bonus/BigACoin.png").convert_alpha()
BigACoin = pygame.transform.scale(BigACoin, (Screen_Width / 15, Screen_Height / 8))

#PinkApple = pygame.image.load("Sprite/Bonus/PinkApple.png").convert_alpha()
#PurpleApple = pygame.image.load("Sprite/Bonus/PurpleApple.png").convert_alpha()
RedApple = pygame.image.load("Sprite/Bonus/RedApple.png").convert_alpha()
RedApple = pygame.transform.scale(RedApple, (Screen_Width / 18, Screen_Height / 12))
#YellowApple = pygame.image.load("Sprite/Bonus/YellowApple.png").convert_alpha()

Star = pygame.image.load("Sprite/Bonus/Star.png").convert_alpha()
Star = pygame.transform.scale(Star, (Screen_Width / 20, Screen_Height / 12))

RedStar = pygame.image.load("Sprite/Bonus/RedStar.png").convert_alpha()
RedStar = pygame.transform.scale(RedStar, (Screen_Width / 20, Screen_Height / 12))


#BlackStar = pygame.image.load("Sprite/Bonus/BlackStar.png").convert_alpha()
#BlackStar = pygame.transform.scale(BlackStar, (Screen_Width / 30, Screen_Height / 20))

#GreenStar = pygame.image.load("Sprite/Bonus/GreenStar.png").convert_alpha()
#GreenStar = pygame.transform.scale(GreenStar, (Screen_Width / 30, Screen_Height / 20))

#PurpleStar = pygame.image.load("Sprite/Bonus/PurpleStar.png").convert_alpha()
#PurpleStar = pygame.transform.scale(PurpleStar, (Screen_Width / 30, Screen_Height / 20))

#MoonBonus = pygame.image.load("Sprite/Bonus/MoonBonus.png").convert_alpha()

# Bónus Terrestres
RedMushroom = pygame.image.load("Sprite/Bonus/RedMushroom.png").convert_alpha()
RedMushroom = pygame.transform.scale(RedMushroom, (Screen_Width / 20, Screen_Height / 12))

ExtendedMushroom = pygame.image.load("Sprite/Bonus/ExtendedMushroom.png").convert_alpha()
ExtendedMushroom = pygame.transform.scale(ExtendedMushroom, (Screen_Width / 15, Screen_Height / 12))
#BlueMushroom = pygame.image.load("Sprite/Bonus/BlueMushroom.png").convert_alpha()
#PurpleMushroom = pygame.image.load("Sprite/Bonus/PurpleMushroom.png").convert_alpha()

#YellowFlowerBonus = pygame.image.load("Sprite/Bonus/YellowFlowerBonus.png").convert_alpha()
Red_YellowFlowerBonus = pygame.image.load("Sprite/Bonus/Red_YellowFlowerBonus.png").convert_alpha()
Red_YellowFlowerBonus = pygame.transform.scale(Red_YellowFlowerBonus, (Screen_Width / 17, Screen_Height / 10))
#BlueFlowerBonus = pygame.image.load("Sprite/Bonus/BlueFowerBonus.png").convert_alpha()

#HappyBonusPlant = pygame.image.load("Sprite/Bonus/HappyBonusPlant.png").convert_alpha()
#HappyBonusPlant = pygame.transform.scale(HappyBonusPlant, (Screen_Width / 25, Screen_Height / 15))

# Load das Imagens Enemies
FatTurtle = pygame.image.load("Sprite/Enemies/FatTurtle.png")
FatTurtle = pygame.transform.scale(FatTurtle, (Screen_Width / 20, Screen_Height / 7))

Gumba = pygame.image.load("Sprite/Enemies/Gumba.png")
Gumba = pygame.transform.scale(Gumba, (Screen_Width / 15, Screen_Height / 9))

LeftBullet = pygame.image.load("Sprite/Enemies/LeftBullet.png")
LeftBullet = pygame.transform.scale(LeftBullet, (Screen_Width / 14, Screen_Height / 7))

RedGhost = pygame.image.load("Sprite/Enemies/RedGhost.png")
RedGhost = pygame.transform.scale(RedGhost, (Screen_Width / 13, Screen_Height / 7))

#RedTurtleSpikes = pygame.image.load("Sprite/Enemies/RedTurtleSpikes.png")
#RedTurtleSpikes = pygame.transform.scale(RedTurtleSpikes, (Screen_Width / 25, Screen_Height / 15))

#Animal = pygame.image.load("Sprite/Enemies/Animal.png")
#Animal = pygame.transform.scale(Animal, (Screen_Width / 25, Screen_Height / 13))

BlackFlower = pygame.image.load("Sprite/Enemies/BlackFlower.png")
BlackFlower = pygame.transform.scale(BlackFlower, (Screen_Width / 14, Screen_Height / 8))
#BlueSpikeTurtle = pygame.image.load("Sprite/Enemies/BlueSpikeTurtle.png")

FlowerLeftObstacle = pygame.image.load("Sprite/Enemies/FlowerLeftObstacle.png")
FlowerLeftObstacle = pygame.transform.scale(FlowerLeftObstacle, (Screen_Width / 17, Screen_Height / 7))

ScaredRedFish = pygame.image.load("Sprite/Enemies/ScaredRedFish.png")
ScaredRedFish = pygame.transform.scale(ScaredRedFish, (Screen_Width / 14, Screen_Height / 8))

SmallBowser = pygame.image.load("Sprite/Enemies/SmallBowser.png")
SmallBowser = pygame.transform.scale(SmallBowser, (Screen_Width / 18, Screen_Height / 6))

#SurprisedFish = pygame.image.load("Sprite/Enemies/SurprisedFish.png")
#SurprisedFish = pygame.transform.scale(SurprisedFish, (Screen_Width / 25, Screen_Height / 15))

AngryGhost = pygame.image.load("Sprite/Enemies/AngryGhost.png")
AngryGhost = pygame.transform.scale(AngryGhost, (Screen_Width / 14, Screen_Height / 7))

#TurtleGhost = pygame.image.load("Sprite/Enemies/TurtleGhost.png")
TurtleShell = pygame.image.load("Sprite/Enemies/TurtleShell.png")
TurtleShell = pygame.transform.scale(TurtleShell, (Screen_Width / 14, Screen_Height / 10))

#TurtleWithSpike = pygame.image.load("Sprite/Enemies/TurtleWithSpike.png")

# Load Obstacles
FirePipe = pygame.image.load("Sprite/Obstacle/FirePipe.png")
FirePipe = pygame.transform.scale(FirePipe, (Screen_Width / 25, Screen_Height / 11))

DarkFirePipe = pygame.image.load("Sprite/Obstacle/DarkFirePipe.png")
DarkFirePipe = pygame.transform.scale(DarkFirePipe, (Screen_Width / 25, Screen_Height / 11))

Vine = pygame.image.load("Sprite/Obstacle/Vine.png")
Vine = pygame.transform.scale(Vine, (Screen_Width / 25, Screen_Height / 15))

run_string = ["Sprite/Mario/WalkingArmsUp.png", "Sprite/Mario/StandingArmsUp.png"]
jump_string = ["Sprite/Mario/JumpVictorius.png", "Sprite/Mario/JumpVictorius.png",
               "Sprite/Mario/JumpVictorius.png", "Sprite/Mario/JumpVictorius.png",
               "Sprite/Mario/JumpingArmsUp.png", "Sprite/Mario/JumpingArmsUp.png",
               "Sprite/Mario/JumpingArmsUp.png", "Sprite/Mario/JumpingArmsUp.png"]
duck_string = ["Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png",
               "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png",
               "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png",
               "Sprite/Mario/Duck.png", "Sprite/Mario/Duck.png"]
fall_string = ["Sprite/Mario/Scared.png"]
scale = [10, 10]

jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
            -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
            -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

# Código Associado Às Animações
def create_anim(image, scale, number_images):
    animation = []
    for i in range(number_images):
        animation.append(pygame.image.load(image[i]))
        animation[i] = pygame.transform.scale(animation[i], (Screen_Width / scale[0], Screen_Width / scale[1]))
        animation[i] = pygame.transform.flip(animation[i], True, False)

    return animation


def flip_anim(image, number_images):
    animation = []
    for i in range(number_images):
        animation.append(image[i])
        animation[i] = pygame.transform.flip(animation[i], True, False)
    return animation


run_anim = create_anim(run_string, scale, 2)
jump = create_anim(jump_string, scale, 8)
duck = create_anim(duck_string, [15,15], 11)
fall = create_anim(fall_string, scale, 1)

flip_run_anim = flip_anim(run_anim, 2)
flip_jump = flip_anim(jump, 8)
flip_duck = flip_anim(duck, 11)
flip_fall = flip_anim(fall, 1)


def pick_enemie(pick, x, y, width, height):
    # Enemie, (x, y, width, height)
    if pick == 0:
        Enemie = FatTurtle
        y = Screen_Height / 1.32
        hitbox = (x - Screen_Width / 200, y + Screen_Height / 200, width - Screen_Width / 150, height - Screen_Height / 20)

    if pick == 1:
        Enemie = Gumba
        y = Screen_Height / 1.26
        hitbox = (x, y + Screen_Height / 150, width - Screen_Width / 60, height - Screen_Height / 15)

    if pick == 2:
        Enemie = BlackFlower
        y = Screen_Height / 1.28
        hitbox = (x, y, width, height - Screen_Height / 20)

    if pick == 3:
        Enemie = FlowerLeftObstacle
        y = Screen_Height / 1.3
        hitbox = (x, y, width - Screen_Width / 100, height - Screen_Height / 40)

    if pick == 4:
        Enemie = SmallBowser
        y = Screen_Height / 1.35
        hitbox = (x, y + Screen_Height / 100, width - Screen_Width / 100, height - Screen_Height / 20)

    if pick == 5:
        Enemie = TurtleShell
        y = Screen_Height / 1.24
        hitbox = (x, y, width - Screen_Width / 100, height - Screen_Height / 20)

    if pick == 6:
        Enemie = LeftBullet
        y = Screen_Height / 1.52
        hitbox = (x, y, width - Screen_Width / 150, height - Screen_Height / 30)

    if pick == 7:
        Enemie = RedGhost
        y = Screen_Height / 1.52
        hitbox = (x, y, width - Screen_Width / 250, height - Screen_Height / 30)

    if pick == 8:
        Enemie = ScaredRedFish
        y = Screen_Height / 1.52
        hitbox = (x, y, width - Screen_Width / 100, height - Screen_Height / 20)

    if pick == 9:
        Enemie = AngryGhost
        y = Screen_Height / 1.52
        hitbox = (x, y, width - Screen_Width / 100, height - Screen_Height / 20)

    return Enemie, y, hitbox


def pick_obstacle(pick, x, y, width, height):
    if pick == 0:
        Obstacle = FirePipe
        y = Screen_Height / 1.23
        hitbox = (x + Screen_Width / 350, y, width, height - Screen_Height / 30)

    if pick == 1:
        Obstacle = DarkFirePipe
        y = Screen_Height / 1.23
        hitbox = (x + Screen_Width / 350, y, width, height - Screen_Height / 30)

    if pick == 2:
        Obstacle = Vine
        y = + Screen_Height / 1.19
        hitbox = (x + Screen_Width / 350, y, width, height - Screen_Height / 30)
    return Obstacle, y, hitbox


def pick_bonus(pick, x, y, width, height,random_height):
    if pick == 0:
        Bonus = Coin
        if random_height == 0: # Terrestre
            y = Screen_Height / 1.24
        else:
            y = Screen_Height / 1.6
        score = 10
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 40, height - Screen_Height / 20)

    if pick == 1:
        Bonus = BigYoshiCoin
        score = 50
        if random_height == 0: # Terrestre
            y = Screen_Height / 1.28
        else:
            y = Screen_Height / 1.6
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 50, height - Screen_Height / 50)

    if pick == 2:
        Bonus = BigACoin
        score = 100
        if random_height == 0:  # Terrestre
            y = Screen_Height / 1.28
        else:
            y = Screen_Height / 1.6
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 50, height - Screen_Height / 50)

    if pick == 3:
        Bonus = RedApple
        score = 40
        if random_height == 0:  # Terrestre
            y = Screen_Height / 1.215
        else:
            y = Screen_Height / 1.6
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 40, height - Screen_Height / 18)

    if pick == 4:
        Bonus = Star
        score = 150
        if random_height == 0:  # Terrestre
            y = Screen_Height / 1.215
        else:
            y = Screen_Height / 1.6
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 40, height - Screen_Height / 18)

    if pick == 5:
        Bonus = RedStar
        score = 200
        if random_height == 0:  # Terrestre
            y = Screen_Height / 1.215
        else:
            y = Screen_Height / 1.6
        hitbox = (x + Screen_Width / 350, y, width - Screen_Width / 40, height - Screen_Height / 18)

    if pick == 6:
        Bonus = RedMushroom
        score = 250
        y = Screen_Height / 1.22
        hitbox = (x, y + Screen_Height / 200, width - Screen_Width / 80, height - Screen_Height / 18)

    if pick == 7:
        Bonus = ExtendedMushroom
        score = 300
        y = Screen_Height / 1.22
        hitbox = (x, y + Screen_Height / 200, width + Screen_Width / 400, height - Screen_Height / 18)

    if pick == 8:
        Bonus = Red_YellowFlowerBonus
        score = 500
        y = Screen_Height / 1.235
        hitbox = (x, y + Screen_Height / 200, width - Screen_Width / 80, height - Screen_Height / 18)


    return Bonus, y, hitbox, score
