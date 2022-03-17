from mimetypes import init
import pygame

white = (255, 255, 255)

class TextBox:
    def __init__(self, surface, contents="Bla", position=[0,0], size=30, bgcolor=white, color=(0,0,0)):
        self.contents=[]
        if(contents.find("\n")!=-1):
            self.parse(contents)
        else:
            self.contents.append(contents)
        self.position = position
        self.surface = surface
        self.color = color
        self.bgcolor = bgcolor
        self.size = size
        self.font = pygame.font.SysFont("Calibri", size)
        self.Text = []
        self.renderText()
        self.updateBackground()
    
    def updateText(self, new_text):
        self.contents = []
        self.Text = []
        if new_text.find("\n")!=-1 :
            self.parse(new_text)
        else:
            self.contents.append(new_text)
        self.renderText()
        self.updateBackground()

    def renderText(self):
        for T in range(len(self.contents)):
            self.Text.append(self.font.render(self.contents[T], 1, self.color))

    def updateBackground(self, bgcolor = white):
        self.Background = pygame.Surface((self.size*len(max(self.contents, key=len)), self.size*len(self.Text)))
        self.Background.set_alpha(30)
        self.bgcolor = bgcolor
        self.Background.fill(self.bgcolor)

    def parse(self, text):
        aux = text.split("\n")
        for t in aux:
            self.contents.append(t)

    def display(self):
        self.surface.blit(self.Background, self.position)
        for T in range(len(self.Text)):
            self.surface.blit(self.Text[T], (self.position[0], self.position[1] + self.size*T))
