from importlib.metadata import entry_points
from cv2 import pyrMeanShiftFiltering
import pygame
import numpy as np
import cv2
from lib.entity import entity
from lib.text import TextBox, GameOver, saveScore
from lib.scoreboard import scoreboard
import lib.load_files as file
import time

from lib.entity import Enemy, Bonus, Obstacle, player


white = (255, 255, 255)
black = (0, 0, 0)



class render:
    def __init__(self, window_size=(1920,1080)):
        self.__window = pygame.display.set_mode(window_size)
        # self.currenttime = int(round(time.time() * 1000))
        self.scoreboard = scoreboard(window_size)
        self.counter = 3
        self.images = {}
        boo1 = pygame.image.load("./resources/boo1.png").convert_alpha()
        self.images["coin"] = pygame.image.load("./sprite/bonus/Coin.png").convert_alpha()
        self.images["mario2"] = pygame.image.load("./resources/mario2.png").convert_alpha()
        self.images["boo1"] = pygame.transform.scale(boo1, (int(self.__window.get_height()/3), int(self.__window.get_height()/3)))


    def draw(self, state=0, img=[], entities=[], command=[], landmarks=[],debug="", bonus_val = 0, lives = 3, score = 0):
        enemies = []
        obstacles = []
        bonus = []

        feedback = ""
        for entity in entities:
            if entity.name == "Player":
                mario = entity
            elif entity.name == "Enemy":
                enemies.append(entity)
            elif entity.name == "Obstacle":
                obstacles.append(entity)
            elif entity.name == "Bonus":
                bonus.append(entity)
        if state == "game over":
            self.__render_camera(img)
            GameOver(self.__window)

        elif state == "save score?":
            scale_factor = self.__render_camera(img)
            # print(landmarks)
            correctedLandmark = (scale_factor[0]*landmarks[0][0],scale_factor[1]*landmarks[0][1])
            # print(correctedLandmark)

            sc = saveScore(self.__window, score, hand_pos=correctedLandmark)
            if (sc == 1):
                feedback = "yes score"
            elif (sc == 0):
                feedback = "no score"
                self.scoreboard.snapshot(self.__window, [correctedLandmark], score=score, save=0)
            self.__render_hand_command([correctedLandmark])

        elif state == "leaderboard":
            self.__render_camera(img)
            self.scoreboard.show(self.__window)

        elif state == "prepare pic":
            imgScale = self.__render_camera(img)

            for i in range(3):
                if landmarks[0][i] != (-1, -1):
                    landmarks[0][i] = (
                        imgScale[0]*landmarks[0][i][0],
                        imgScale[1]*landmarks[0][i][1]
                    )

            for i in range(2):
                if landmarks[1][i] != (-1, -1):
                    landmarks[1][i] = (
                        imgScale[0]*landmarks[1][i][0],
                        imgScale[1]*landmarks[1][i][1]
                    )


            boo1 = self.__window.blit(self.images["boo1"], [self.__window.get_width() - self.images["boo1"].get_width(),
                                                        self.__window.get_height() - self.images["boo1"].get_height()])

            font = pygame.font.Font("./resources/SuperMario256.ttf", 50, bold=False)
            text = font.render("Touch Boo when you're ready!", 1, (0,0,0))
            self.__window.blit(text, [self.__window.get_width()/2 - text.get_width()/2, 
                                      self.__window.get_height()/4 - text.get_height()/2])

            self.scoreboard.display(self.__window, landmarks) # Draw Square
            self.__render_hand_command([landmarks[1][0]])
            if (boo1.collidepoint(landmarks[1][0])):
                return "ok pic"

        elif state == "pic":
            imgScale = self.__render_camera(img)
            for i in range(3):
                if landmarks[0][i] != (-1, -1):
                    landmarks[0][i] = (
                        imgScale[0]*landmarks[0][i][0],
                        imgScale[1]*landmarks[0][i][1]
                    )

            for i in range(2):
                if landmarks[1][i] != (-1, -1):
                    landmarks[1][i] = (
                        imgScale[0]*landmarks[1][i][0],
                        imgScale[1]*landmarks[1][i][1]
                    )
            self.scoreboard.snapshot(self.__window, landmarks, 10000, 1)
            
        elif state == "game":
            self.__render_camera(img)
            self.redrawWindow(bonus_val, obstacles, enemies, mario, score, lives)
            self.check_BackGround()
            t = TextBox(self.__window, debug)
            t.display()

        elif(state == -11):
            self.__render_camera(img)
            self.__render_hand_command(landmarks)
        elif(state == -12):
            self.__render_camera(img)
            self.__render_face_command(landmarks)
        elif(state == -13):
            self.__render_camera(img)
            # print(command['landmarks'])
            # if command != [(-1,-1)]:
            if landmarks:
                self.__render_body_command(landmarks)
                mytext = TextBox(self.__window, size=20)
                mytext.updateText(debug)
                mytext.display()
        
        pygame.display.update()
        return feedback

    def __render_camera(self, img=[], size=(1920,1080)):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        priorSize = imgRGB.shape
        imgRGB = cv2.resize(imgRGB, (size[1],size[0]), interpolation = cv2.INTER_AREA)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        self.__window.blit(frame, (0,0))
        outputFactor = (imgRGB.shape[0]/priorSize[0],imgRGB.shape[1]/priorSize[1])
        return outputFactor

    def __render_hand_command(self,command = []):
        # if len(command) >= 2:
        for com in command:
            if com != (-1,-1):
                pygame.draw.circle(self.__window, (191, 39, 28), com, 15)

    def __render_face_command(self,command = []):
        if command != []:
            for com in command:
                if com != (-1,-1):
                    pygame.draw.circle(self.__window, (191, 39, 28), com, 15)
    
    def __render_body_command(self,command = []):
        if command:
            # print(command)
            for com in command:
                if com != (-1,-1):
                    pygame.draw.circle(self.__window, (191, 39, 28), (com.x,com.y), 15)

    def __render_HUD(self, window, lives, score, coins):
        HUD = pygame.Surface((window.get_width(), window.get_height()/8),  pygame.SRCALPHA, 32)

        font = pygame.font.Font("./resources/SuperMario256.ttf", HUD.get_height(), bold=False)
        font_s = pygame.font.Font("./resources/SuperMario256.ttf", int(HUD.get_height()*0.8), bold=False)
        
        score = font.render(str(score), 1, white)
        x = font_s.render("x", 1, white)
        coin = font.render("{:03}".format(coins), 1, white)
        
        lives = font.render("{:02}".format(lives), 1, white)
        self.images["mario2"] = pygame.transform.scale(self.images["mario2"], 
                                                      (int(HUD.get_height()), int(HUD.get_height())))
        self.images["coin"] = pygame.transform.scale(self.images["coin"], (int(HUD.get_height()), int(HUD.get_height())))
        HUD.blit(self.images["mario2"], (0,0))
        HUD.blit(x, ((HUD.get_height(), x.get_height()/3)))
        HUD.blit(lives, (HUD.get_height() + x.get_width(), 10))
        HUD.blit(score, (HUD.get_width()/2-score.get_width()/2, 10))
        HUD.blit(self.images["coin"], (HUD.get_width() - HUD.get_height() - x.get_width() - coin.get_width(),0))
        HUD.blit(x, (HUD.get_width() - coin.get_width() - x.get_width(), x.get_height()/3))
        HUD.blit(coin, (HUD.get_width() - coin.get_width(), 10))
        
        window.blit(HUD, (0,0))

    # Função Utilizada Durante o Jogo Para Desenhar HUD(Score e Vidas), Inimigos, Bónus, Mario e Obstáculos
    def redrawWindow(self,Movement_x, objects, bonus, runner, score, lives):
        

        self.__window.blit(file.BackGround, (file.BackGroundX, 0))  # draws our first BackGround image
        file.window.blit(file.BackGround, (file.BackGroundX2, 0))  # draws the second BackGround image

        self.__render_HUD(self.__window, lives, score, 0)

        # Objectos = Lista que Contém Inimigos/Obstáculos
        for x in objects:
            x.draw(file.window)

        # Bonus = Lista que Contém Bónus
        for y in bonus:
            y.draw(file.window)

        runner.draw(file.window, 95)  # NEW

        # Condição que Verifica se Mario Saiu Do Ecrã
        if Movement_x <= -70:
            file.window.blit(file.Loser_Text, file.LoserRect)


    # Atualiza BackGround
    def check_BackGround(self):
        file.BackGroundX -= 1  # Move both background images back
        file.BackGroundX2 -= 1

        # 1º BackGround Image starts at (0,0)
        if file.BackGroundX < file.BackGround.get_width() * -1:  # If our BackGround is at the -width then reset its position
            file.BackGroundX = file.BackGround.get_width()

        if file.BackGroundX2 < file.BackGround.get_width() * -1:
            file.BackGroundX2 = file.BackGround.get_width()

