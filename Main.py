import pygame
import random
import pyautogui 
import time
pygame.mixer.init()
pygame.init() 

#Game window
screen_width = 900
screen_height = 600       
gameWindow = pygame.display.set_mode((screen_width,screen_height))

bg_img = pygame.image.load("Media/bg.png")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0 ,255)
green = (0, 153, 0)
grey = (104,104,104)

clock = pygame.time.Clock()
large_font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 25)

def screen_text_large(text, color, x, y): # Dispplay text on game screen
    screen_text = large_font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def screen_text_small(text, color, x, y): # Dispplay text on game screen
    screen_text = small_font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list: 
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome(): # Game start's
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        screen_text_large("Welcome To Snakes", black, 260, 250)
        screen_text_large("Press Space Bar To Play", red, 230, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("Media/back.mp3")
                    pygame.mixer.music.play()
                    Game_loop()
                # if event.key == pygame.
        
        pygame.display.update()
        clock.tick(60)

# Game loop
def Game_loop():  
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 2
    food_x = random.randint(20, 890)
    food_y = random.randint(53, 600)
    score = 0
    snake_size = 15
    snake_list = []
    snake_length = 1
    fps = 60

    # Starting of the loop 
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            screen_text_large("Game Over! Press Enter to continue", red, 100, 270)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0
                        
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0 

                    if event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_ESCAPE:
                        pyautogui.alert("Click OK to RESUME")

            snake_x = snake_x + velocity_x 
            snake_y = snake_y + velocity_y

            #Increasing score and giving food 
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                pygame.mixer.music.load("Media/bite.mp3")
                pygame.mixer.music.play()
                score = score+10
                food_x = random.randint(20, 880)
                food_y = random.randint(53, 580)
                snake_length = snake_length + 15

            gameWindow.fill(white)
            screen_text_large("Score: " + str(score) , blue, 5, 5)
            pygame.draw.rect(gameWindow,red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, black, [0,50], [0,52], 1800)
            screen_text_small("Settings", black,815,5)
            pygame.draw.circle(gameWindow, black, [850,33], 10)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:# Every element excluding last element of snake_list
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<50 or snake_y>screen_height:
                game_over = True
        plot_snake(gameWindow, green, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps) 

    pygame.quit
    quit()
welcome()
