import pygame                       
from pygame import transform
from random import randint
from time import time as timer

from pygame.version import PygameVersion 

pygame.init()           
pygame.font.init()

font2 = pygame.font.SysFont("Arial", 25)    
font1 = pygame.font.SysFont("Arial", 80)    

win_width = 850        
win_height = 700       


BLACK = (0, 0 ,0)          
WHITE = (255, 255, 255)
YELLOW = (255,211,67)
RED = (255, 0, 0)

img_backg = "flappy_back.jpg"      
img_hero = "Bird.png"
img_finish = "finish.png"



win = font1.render("YOU WON!", True, (YELLOW))   
lose = font1.render("YOU LOST!", True, (RED))   
        
score = 0  
life = 1

FPS = 60       

clock = pygame.time.Clock()


window = pygame.display.set_mode((win_width, win_height))       
pygame.display.set_caption("FlappyBird 2D game")       

background = transform.scale(pygame.image.load(img_backg), (win_width, win_height))        

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):       
    pass
class Player(GameSprite):      
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.y > 5: 
            hero.rect.y -= 10
        
            
        

        
        

hero = Player(img_hero, 5, win_height - 450, 80, 90, 10)            

heros = pygame.sprite.Group()
heros.add(hero)
borders = pygame.sprite.Group()            

border = Enemy("border2.png", 300, 470, 50, 250, 10)                   
border2 = Enemy("border2_down.png", 300, 0, 50, 200, 10)
border3 = Enemy("border2.png", 550, 420, 50, 280, 10)
border4 = Enemy("border2_down.png", 550, 0, 50, 200, 10)
border5 = Enemy("border2.png", 800, 380, 50, 330, 10)
border6 = Enemy("border2_down.png", 800, -100, 50, 280, 10)
border7 = Enemy("border2.png", 1050, 470, 50, 250, 10)
border8 = Enemy("border2_down.png", 1050, 0, 50, 200, 10)
border9 = Enemy("border2_down.png", 1280, 0, 50, 250, 10)
border10 = Enemy("border2.png", 1280, 540, 50, 250, 10)
border11 = Enemy("border2.png", 1500, 470, 50, 250, 10)                    
border12 = Enemy("border2_down.png", 1500, 0, 50, 200, 10)
border13 = Enemy("border2.png", 1750, 400, 50, 330, 10)
border14 = Enemy("border2_down.png", 1750, -100, 50, 300, 10)
border15 = Enemy("border2.png", 2000, 350, 50, 370, 10)
border16 = Enemy("border2_down.png", 2000, -130, 50, 280, 10)
border17 = Enemy("border2.png", 2250, 470, 50, 250, 10)              
border18 = Enemy("border2_down.png", 2250, 0, 50, 200, 10)
border19 = Enemy("border2_right.png", 2300, 100, 250, 50, 10)
border20 = Enemy("border2_right.png", 2300, 500, 250, 50, 10)


coin = Enemy("coin.png", 300, 360, 35, 35, 1)
coin2 = Enemy("coin.png", 800, 285, 35, 35, 1)
coin3 = Enemy("coin.png", 1280, 400, 35, 35, 1)
coin4 = Enemy("coin.png", 2000, 230, 35, 35, 1)
coin5 = Enemy("coin.png", 2250, 375, 35, 35, 1)
coins = pygame.sprite.Group()


coins.add(coin)
coins.add(coin2)
coins.add(coin3)
coins.add(coin4)
coins.add(coin5)



borders.add(border)    
borders.add(border2)
borders.add(border3)
borders.add(border4)
borders.add(border5)
borders.add(border6)
borders.add(border7)
borders.add(border8)
borders.add(border9)
borders.add(border10)
borders.add(border11)
borders.add(border12)
borders.add(border13)
borders.add(border14)
borders.add(border15)
borders.add(border16)
borders.add(border17)
borders.add(border18)
borders.add(border19)
borders.add(border20)


game_finish = Enemy(img_finish, 2500, 150, 75, 350, 1)
game_finish_gr = pygame.sprite.Group()
game_finish_gr.add(game_finish)

playing = True
finish = False

while playing:                              
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        
        
    

    if not finish:
        window.blit(background, (0, 0))
        hero.update()
        hero.reset()
        borders.update()
        borders.draw(window)
        coins.update()
        coins.draw(window)
        game_finish.update()
        game_finish.reset()
        
    

        if pygame.sprite.spritecollide(hero, borders, False):
            pygame.sprite.spritecollide(hero, borders, True)
            life -= 1
        
        if pygame.sprite.spritecollide(hero, coins, False):
            pygame.sprite.spritecollide(hero, coins, True)
            score += 10

        if pygame.sprite.spritecollide(hero, game_finish_gr, False):
            pygame.sprite.spritecollide(hero, game_finish_gr, True)
            finish = True
            window.blit(win, (200, 200))
       

            
            

        border.rect.x -= 2
        border2.rect.x -= 2 
        border3.rect.x -= 2
        border4.rect.x -= 2
        border5.rect.x -= 2          
        border6.rect.x -= 2
        border7.rect.x -= 2
        border8.rect.x -= 2
        border9.rect.x -= 2
        border10.rect.x -= 2
        border11.rect.x -=  2
        border12.rect.x -= 2
        border13.rect.x -= 2
        border14.rect.x -= 2
        border15.rect.x -= 2
        border16.rect.x -= 2
        border17.rect.x -= 2
        border18.rect.x -= 2
        border19.rect.x -= 2
        border20.rect.x -= 2

        coin.rect.x -= 2
        coin2.rect.x -= 2
        coin3.rect.x -= 2
        coin4.rect.x -= 2
        coin5.rect.x -= 2
        
        game_finish.rect.x -= 2

        hero.rect.y += 3 
        
        
        score_number = font2.render("Score: " + str(score), 1, (WHITE))
        window.blit(score_number, (10, 5))                            

        life_number = font2.render("Lifes: " + str(life), 1, (WHITE))
        window.blit(life_number, (10, 30))                         

        if border.rect.x >= win_width:
            window.blit(win, (200, 200))

        if life == 0:
            finish = True
            window.blit(lose, (200, 280))

       
        if hero.rect.y > 600:
            window.blit(lose, (200, 280))
            hero.rect.y = 610
            finish = True
        
    else:                      
        finish = False
        score = 0
        life = 1

        pygame.time.delay(4000)

        hero.rect.x = 5
        hero.rect.y = win_height - 450

        for b in borders:
            b.kill() 
        border = Enemy("border2.png", 300, 470, 50, 250, 10)                    #створення стін
        border2 = Enemy("border2_down.png", 300, 0, 50, 200, 10)
        border3 = Enemy("border2.png", 550, 420, 50, 280, 10)
        border4 = Enemy("border2_down.png", 550, 0, 50, 200, 10)
        border5 = Enemy("border2.png", 800, 380, 50, 330, 10)
        border6 = Enemy("border2_down.png", 800, -100, 50, 280, 10)
        border7 = Enemy("border2.png", 1050, 470, 50, 250, 10)
        border8 = Enemy("border2_down.png", 1050, 0, 50, 200, 10)
        border9 = Enemy("border2_down.png", 1280, 0, 50, 250, 10)
        border10 = Enemy("border2.png", 1280, 540, 50, 250, 10)
        border11 = Enemy("border2.png", 1500, 470, 50, 250, 10)                    
        border12 = Enemy("border2_down.png", 1500, 0, 50, 200, 10)
        border13 = Enemy("border2.png", 1750, 400, 50, 330, 10)
        border14 = Enemy("border2_down.png", 1750, -100, 50, 300, 10)
        border15 = Enemy("border2.png", 2000, 350, 50, 370, 10)
        border16 = Enemy("border2_down.png", 2000, -130, 50, 280, 10)
        border17 = Enemy("border2.png", 2250, 470, 50, 250, 10)                    #створення стін
        border18 = Enemy("border2_down.png", 2250, 0, 50, 200, 10)
        border19 = Enemy("border2_right.png", 2300, 100, 250, 50, 10)
        border20 = Enemy("border2_right.png", 2300, 500, 250, 50, 10)

        borders.add(border)
        borders.add(border2)
        borders.add(border3)
        borders.add(border4)
        borders.add(border5)
        borders.add(border6)
        borders.add(border7)
        borders.add(border8)
        borders.add(border9)
        borders.add(border10)
        borders.add(border11)
        borders.add(border12)
        borders.add(border13)
        borders.add(border14)
        borders.add(border15)
        borders.add(border16)
        borders.add(border17)
        borders.add(border18)
        borders.add(border19)
        borders.add(border20)

        coin = Enemy("coin.png", 300, 360, 35, 35, 1)
        coin2 = Enemy("coin.png", 800, 285, 35, 35, 1)
        coin3 = Enemy("coin.png", 1280, 400, 35, 35, 1)
        coin4 = Enemy("coin.png", 2000, 230, 35, 35, 1)
        coin5 = Enemy("coin.png", 2250, 375, 35, 35, 1)
        coins = pygame.sprite.Group()


        coins.add(coin)
        coins.add(coin2)
        coins.add(coin3)
        coins.add(coin4)
        coins.add(coin5)

        game_finish = Enemy(img_finish, 2500, 150, 75, 350, 1)
        game_finish_gr = pygame.sprite.Group()
        game_finish_gr.add(game_finish)

    
    pygame.display.update()
    clock.tick(FPS)
