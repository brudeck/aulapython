import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("ex23.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()