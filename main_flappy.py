import pygame
import random


pygame.init()
# screen
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 30)
font_bigger=font = pygame.font.Font("freesansbold.ttf", 28)
font2 = pygame.font.Font("freesansbold.ttf", 15)
font4 = pygame.font.Font("freesansbold.ttf", 17)
font3 = pygame.font.Font("freesansbold.ttf", 20)
dimension= 64


d_height = 512
d_width = 288
game_over = True
hasOccured = False
collision = False
passed1 = False
passed2 = False
passed3 = False
in_customize = False

score=0
high_score=0
current = (0,0)
clicked =(0,0,0)
# 510, 288
screen = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption("FLAPPY BIRD")


# items
background = pygame.image.load('background-day.png').convert()
background_day_preview = pygame.transform.scale(background, (70, 100))
background_night = pygame.image.load('background-night.png').convert()
background_night_preview = pygame.transform.scale(background_night, (70, 100))
curr_back= background

base = pygame.image.load('base.png').convert()
base_x1 = 0
base_x2 = d_width

# bird
bird = pygame.image.load('bluebird-midflap.png').convert()
bird_up = pygame.transform.rotate(bird, 30)
bird_down = pygame.transform.rotate(bird, -45)
bird_rect = bird_up.get_rect(center = (50, 216))
bird_height = d_height/2
bird_width = d_width/2
bird_position = bird
bird_movement = 0

bird_yellow = pygame.image.load('yellowbird-upflap.png').convert()
bird_up_yellow = pygame.transform.rotate(bird_yellow, 30)
bird_down_yellow = pygame.transform.rotate(bird_yellow, -45)

bird_red = pygame.image.load('redbird-upflap.png').convert()
bird_up_red = pygame.transform.rotate(bird_red, 30)
bird_down_red = pygame.transform.rotate(bird_red, -45)

#bird_blue = pygame.image.load('bluebird-upflap.png').convert()
#bird_up_blue = pygame.transform.rotate(bird_blue, 30)
#bird_down_blue = pygame.transform.rotate(bird_blue, -45)

bird_blue = pygame.image.load('bluebird-upflap.png').convert()
# bird_blues.set_colorkey((0, 0, 0))
# bird_blue = pygame.transform.scale(bird_blues, (55, 55))
bird_up_blue = pygame.transform.rotate(bird_blue, 30)
bird_down_blue = pygame.transform.rotate(bird_blue, -45)
# pipe
pipe = pygame.image.load('pipe-green.png')
pipe_down = pygame.image.load('pipe-green.png').convert()
pipe_down = pygame.transform.rotate(pipe_down, 180)
pipeX = 350
pipeX2 = pipeX + 180
pipeX3 = pipeX2 + 180
pipeY_atas = -180
pipeY = 300

height1 = 150
height2 = 200
height3 = 160


def gameOver():
    game_over = True
    text = font.render("GAME OVER", True, (0, 100, 100))
    text2 = font2.render("press any key to start over", True, (100, 100, 100))
    text_rect = text.get_rect(center=(144, (d_height/2)-50))
    text2_rect = text2.get_rect(center=(144, (d_height / 2)-20))
    pygame.draw.rect(screen, (0, 0, 0), [20, 20, 248, 400], 5)
    pygame.draw.rect(screen, (200, 200, 200), [20, 20, 248, 400])
    pygame.draw.rect(screen, (0, 150, 100), [70, 285, 150, 50])
    pygame.draw.rect(screen, (0, 0, 0), [70, 285, 150, 50], 2)
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)

def restart_button(current, clicked):
    if ((current[0] > 70 and current[0] < 220) and (current[1]>285 and current[1]<335)):
        start_again = font3.render("Main Menu", True, (0, 0, 0))
        start_again_rect = start_again.get_rect(center=(145, 310))
        screen.blit(start_again, start_again_rect)
        if click[0] == 1:
            main_menu()
            return False
    else:
        start_again = font4.render("Main Menu", True, (0, 0, 0))
        start_again_rect = start_again.get_rect(center=(145, 310))
        screen.blit(start_again, start_again_rect)


def main_menu():

    in_main_menu = True
    game_over = True
    current = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (0, 0, 0), [20, 20, 248, 400], 5)
    pygame.draw.rect(screen, (200, 200, 200), [20, 20, 248, 400])
    text = font_bigger.render("Flappy Bird", True, (0, 100, 100))
    text2 = font3.render("by Brandon", True, (0, 100, 100))
    text_rect = text.get_rect(center=(144, 100))
    text2_rect = text2.get_rect(center=(144, 130))


    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)

    screen.blit(bird, ((130, 206)))
    if check_presses(current, click) == True:
        return "play"
    if check_customize(current, click) == True:
        return "customize"
    if check_quit(current, click)== True:
        return "quit"

def check_quit(current, click):
    text5 = font3.render("Quit", True, (0, 100, 100))
    text5_rect = text5.get_rect(center=(194, 280))
    if ((current[0] > 177 and current[0] < 213) and (current[1]>273 and current[1]<285)):
        text5 = font.render("Quit", True, (0, 100, 100))
        text5_rect = text5.get_rect(center=(194, 280))
        if click[0] == 1:
            screen.blit(text5, text5_rect)
            return True
    screen.blit(text5, text5_rect)
    return False

def customize():
    pygame.draw.rect(screen, (0, 0, 0), [20, 20, 248, 400], 5)
    pygame.draw.rect(screen, (200, 200, 200), [20, 20, 248, 400])
    day = font2.render("Day", True, (0, 100, 100))
    day_rect = day.get_rect(center=(102, 110))
    screen.blit(day, day_rect)

    night = font2.render("Night", True, (0, 100, 100))
    night_rect = day.get_rect(center=(183, 110))
    screen.blit(night, night_rect)

    birds = font2.render("Birds", True, (0, 100, 100))
    birds_rect = birds.get_rect(center=(144, 300))
    screen.blit(birds, birds_rect)
    bird_yellow_rect = bird_yellow.get_rect(center=(84, 340))
    bird_red_rect = bird_red.get_rect(center=(144, 340))
    bird_blue_rect = bird_blue.get_rect(center=(204, 340))
    screen.blit(bird_yellow, bird_yellow_rect)
    screen.blit(bird_red, bird_red_rect)
    screen.blit(bird_blue, bird_blue_rect)


def check_presses(current, click):
    play = font3.render("Play", True, (0, 100, 100))
    if ((current[0] > 64 and current[0] < 124) and (current[1]>268 and current[1]<295)):
        play = font.render("Play", True, (0, 100, 100))
        if click[0] == 1:
            play_rect = play.get_rect(center=(94, 280))
            screen.blit(play, play_rect)
            return True

    play_rect = play.get_rect(center=(94, 280))
    screen.blit(play, play_rect)
    return False

def check_customize(current, click):
    customize = font3.render("Customize", True, (0, 100, 100))
    customize_rect = customize.get_rect(center=(144, 340))
    if ((current[0] > 93 and current[0] < 195) and (current[1]>330 and current[1]<344)):
        customize = font.render("Customize", True, (0, 100, 100))
        customize_rect = customize.get_rect(center=(144, 340))
        if click[0] == 1:
            screen.blit(customize, customize_rect)
            return True
    screen.blit(customize, customize_rect)
    return False

def check_customize_screen(current, click):
    back = font2.render("Back", True, (0, 100, 100))
    back_rect = back.get_rect(topleft=(30, 50))
    screen.blit(background_day_preview, (70, 120))
    screen.blit(background_night_preview, (150, 120))

    if ((current[0] > 30 and current[0] < 60) and (current[1]>50 and current[1]<60)):
        back = font3.render("Back", True, (0, 100, 100))
        back_rect = back.get_rect(topleft=(30, 50))
        if click[0] == 1:
            screen.blit(back, back_rect)
            return "back"
    screen.blit(back, back_rect)

    if ((current[0] > 72 and current[0] < 144) and (current[1]>120 and current[1]<220)):
        pygame.draw.rect(screen, (0, 0, 0), [70, 120, 70, 100], 2)
        if click[0] == 1:
            return "day"
    if ((current[0] > 144 and current[0] < 212) and (current[1]>120 and current[1]<220)):
        pygame.draw.rect(screen, (0, 0, 0), [150, 120, 70, 100], 2)
        if click[0] == 1:
            return "night"
    if ((current[0] > 64 and current[0] < 104) and (current[1]>320 and current[1]<360)):
        pygame.draw.rect(screen, (0, 0, 0), [64, 320, 40, 40], 2)
        if click[0] == 1:
            return "yellow"
    if ((current[0] > 124 and current[0] < 164) and (current[1]>320 and current[1]<360)):
        pygame.draw.rect(screen, (0, 0, 0), [124, 320, 40, 40], 2)
        if click[0] == 1:
            return "red"
    if ((current[0] > 184 and current[0] < 224) and (current[1]>320 and current[1]<360)):
        pygame.draw.rect(screen, (0, 0, 0), [184, 320, 40, 40], 2)
        if click[0] == 1:
            return "blue"


def pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3):
    difference = 460
    screen.blit(pipe, ((pipeX, 440-height1)))
    screen.blit(pipe_down, ((pipeX, -height1)))

    screen.blit(pipe, ((pipeX2, 440-height2)))
    screen.blit(pipe_down, ((pipeX2, -height2)))

    screen.blit(pipe, ((pipeX3, 440-height3)))
    screen.blit(pipe_down, ((pipeX3, -height3)))

def base_movement(base_x1, base_x2):
    screen.blit(base, (base_x1, 450))
    screen.blit(base, (base_x2, 450))

def bird_move(bird_position, x, y):
    screen.blit(bird_position, ((x, y)))

def score_display(score):
    score_surface = font.render('Score: ' + str(score), True, (0,0,0))
    score_rect = score_surface.get_rect(center= (144, 50))
    screen.blit(score_surface, score_rect)

def high_score_d(high_score):
    score_surface = font2.render('High Score: ' + str(high_score), True, (100,100,100))
    score_rect = score_surface.get_rect(center= (144, 90))
    screen.blit(score_surface, score_rect)

def current_background(curr_back):
    screen.blit(curr_back, (0, 0))
    
running = True
in_main_menu = True

while running:
    screen.fill((0, 0, 0))
    current_background(curr_back)
    for event in pygame.event.get():
        current = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if game_over == False:
            bird_position = bird_up
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = 0
                    bird_movement -= 10
        else:
            if in_main_menu == False and in_customize == False:
                if event.type == pygame.KEYDOWN:
                    passed1 = False
                    passed2 = False
                    passed3 = False
                    score = 0
                    game_over = False
                    collision= False
                    # start over game
                    bird_rect.centery = 216
                    bird_rect.centerx = 50
                    bird_movement = 0
                    pipeX = 350
                    pipeX2 = 350 + 180
                    pipeX3=pipeX2+ 180
                    height1 = random.randint(100, 250)
                    height2 = random.randint(100, 250)
                    height3 = random.randint(100, 250)
                    pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)

    if game_over == False:
        bird_movement += 1
        bird_rect.centery += bird_movement
        screen.blit(bird_position, bird_rect)

    # game over
    if game_over and collision:
        game_over = True
        pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)
        bird_rect.centery += 20
        base_movement(base_x1, base_x2)
        screen.blit(bird_down, bird_rect)
        if bird_rect.centery > 430:
            bird_rect.centery = 430

    if bird_rect.centery >= 430 and not collision:
        game_over = True
        bird_rect.centery = 430
        pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)
        screen.blit(bird_down, (bird_rect))
        base_movement(base_x1, base_x2)
 

    # pipe movement
    if game_over == False:
        pipeX -= 3.8
        pipeX2 -= 3.8
        pipeX3 -= 3.8
        if pipeX <= -270:
            height1 = random.randint(100, 250)
            height2 = random.randint(100, 250)
            pipeX = 300
            pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)
            passed1= False
        elif pipeX2 <= -270:
            pipeX2 = 300
            height2 = random.randint(100, 250)
            pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)
            passed2 = False
        elif pipeX3 <= -270:
            pipeX3 = 300
            height3 = random.randint(100, 250)
            pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)
            passed3 = False
        else:
            pipe_movement(pipeX, pipeX2, pipeX3, height1, height2, height3)

        # checking collisions
        pipe_rect = pipe.get_rect(topleft=(pipeX, 440 - height1))
        pipe_rect2 = pipe_down.get_rect(topleft=(pipeX, -height1))
        pipe_rect3 = pipe.get_rect(topleft=(pipeX2, 440 - height2))
        pipe_rect4 = pipe_down.get_rect(topleft=(pipeX2, -height2))
        pipe_rect5 = pipe.get_rect(topleft=(pipeX3, 440 - height3))
        pipe_rect6 = pipe_down.get_rect(topleft=(pipeX3, -height3))

        if (bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(pipe_rect2)
                or bird_rect.colliderect(pipe_rect3) or bird_rect.colliderect(pipe_rect4)
                or bird_rect.colliderect(pipe_rect5) or bird_rect.colliderect(pipe_rect6)):
            game_over = True
            collision = True

    base_movement(base_x1, base_x2)


    if game_over == False:
        # base movement
        base_x1 -= 3.8
        base_x2 -= 3.8
        if base_x2 <= -288:
            base_x2 = 288
        if base_x1 <= -288:
            base_x1 = 288
        # counting scores
        if bird_rect.centerx > pipe_rect.centerx and passed1 == False:
            score += 1
            passed1 = True
        if bird_rect.centerx > pipe_rect3.centerx and passed2 == False:
            score += 1
            passed2 = True
        if bird_rect.centerx > pipe_rect5.centerx and passed3 == False:
            score+=1
            passed3= True


    score_display(score)

    if score > high_score:
        high_score = score
    if game_over == True:
        if in_main_menu == True:
            if main_menu()== "quit":
                running = False
            if main_menu() == "customize":
                in_main_menu= False
                in_customize = True
            elif main_menu() == "play":
                game_over= False
                in_main_menu= False
                game_over = False
                in_main_menu = False
                passed1 = False
                passed2 = False
                passed3 = False
                score = 0
                collision = False
                # start over game
                bird_rect.centery = 216
                bird_rect.centerx = 50
                bird_movement = 0
                pipeX = 350
                pipeX2 = pipeX + 180
                pipeX3 = pipeX2+ 180
                height1 = random.randint(100, 250)
                height2 = random.randint(100, 250)
                height3 = random.randint(100, 250)
                pipe_movement(pipeX, pipeX2, pipeX3,height1, height2, height3)


        elif in_customize== True:
            customize()
            pygame.draw.rect(screen, (0, 0, 0), [dimension, 320, 40, 40], 2)
            if check_customize_screen(current, click) == "back":
                in_customize = False
                in_main_menu= True
                main_menu()
            if check_customize_screen(current, click) == "day":
                curr_back= background
            if check_customize_screen(current, click) == "night":
                curr_back= background_night
            if check_customize_screen(current, click) == "yellow":
                dimension = 64
                bird = bird_yellow
                bird_up = bird_up_yellow
                bird_down = bird_down_yellow
            if check_customize_screen(current, click) == "red":
                dimension = 124
                bird = bird_red
                bird_up = bird_up_red
                bird_down = bird_down_red
            if check_customize_screen(current, click) == "blue":
                dimension = 184
                bird = bird_blue
                bird_up = bird_up_blue
                bird_down = bird_down_blue
        elif in_main_menu == False and in_customize == False:
            gameOver()
            high_score_d(high_score)
            score_display(score)
            if restart_button(current, click) == False:
                in_main_menu = True

    pygame.display.update()
    clock.tick(150)
