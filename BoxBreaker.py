
import pygame as py
import random

HEIGHT = 62 * 8 + 50
WHITE = (255, 255, 255)
BACKGROUND = (3,3,3)
BALL_SIZE = 7
UNIT_SIZE = 45
MAX_LEVEL_NUMBER = 11
OFFSET = 2
BLOCK_SIZE = UNIT_SIZE - OFFSET
BAR_WIDTH = 100
BAR_HEIGHT = 10
BAR_Y = HEIGHT - BAR_HEIGHT - 10
BALL_START_Y = BAR_Y - 100
BALL_START_SPEED_X = 1
BALL_START_SPEED_Y = 2
WIDTH = 4 + ((BLOCK_SIZE + OFFSET) * 10)  
BAR_X = (WIDTH / 2) - (BAR_WIDTH / 2)
BALL_START_X = BAR_X + (BAR_WIDTH / 2)

class Ball():
    def __init__(self, x, y, speed_x, speed_y, value):
        super().__init__()
        
        self.x = x 
        self.y = y 
        self.value = value
        self.speed_x = speed_x
        self.speed_y = speed_y


    def draw(self, screen):
        
        py.draw.circle(screen, WHITE, (self.x, self.y), BALL_SIZE)

    def move(self, vel):
        self.x += self.speed_x * vel
        self.y += self.speed_y * vel

    def increment(self):
        self.value += 1

    
    
       
class Bar():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def draw(self, screen):
        py.draw.rect(screen, (0, 0, 250), (self.x, self.y, BAR_WIDTH, BAR_HEIGHT))
    

class Block():
    
    def __init__(self, x, y, value, width, height, is_ball_block):
        super().__init__()
        self.value = value
        self.x = x * UNIT_SIZE + 2 
        self.y = y * UNIT_SIZE + 52
        self.width = width
        self.height = height
        self.is_ball_block = is_ball_block


    def draw(self, screen):
        color = ()
        if not self.is_ball_block:
            font = py.font.Font('freesansbold.ttf', 15)
            text = font.render(str(self.value), True, WHITE)
            
            if not self.value * 10 >= 240:
                color = (self.value * 10, 40 ,150)
            else:
                color = (240, 40 ,150)
            py.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            
                
            screen.blit(text, (self.x + (self.width / 2) - text.get_rect().width / 2, self.y + (self.height / 2) - text.get_rect().height / 2))
        else:
            font = py.font.Font('freesansbold.ttf', 15)
            text = font.render("+ ", True, WHITE)

            py.draw.rect(screen, (249, 233, 110), (self.x, self.y, self.width, self.height))
            py.draw.circle(screen, WHITE, ((self.x + self.width / 2) + 10 , self.y + self.height / 2), BALL_SIZE)
            screen.blit(text, (self.x + (self.width / 2) - text.get_rect().width / 2, self.y + (self.height / 2) - text.get_rect().height / 2))


    def decrement(self, value):
        if self.value > 0:
            self.value -= value

    def moveDown(self):
        self.y += UNIT_SIZE
    



def InitBlocks(level_num):
    x = 0
    y = 0
    blocks = []
    with open("/Users/caleb/Box Breaker/Level_" + str(level_num) + ".txt") as f:
        for line in f:
            for char in line:
                value = random.randint(0 + level_num, GetMaxValue(level_num))              
                if char == "1":
                    
                    blocks.append(Block(x, y, value, BLOCK_SIZE, BLOCK_SIZE, False))
                elif char == "2":
                    
                    blocks.append(Block(x, y, value, BLOCK_SIZE * 10 + 20, BLOCK_SIZE, False))
                elif char == "3":
                    blocks.append(Block(x, y, value, BLOCK_SIZE * 3 + 4, BLOCK_SIZE, False))
                
                elif char == "4":
                    blocks.append(Block(x, y, value, BLOCK_SIZE * 4 + 6, BLOCK_SIZE, False))
                elif char == "5":
                    blocks.append(Block(x, y, value, BLOCK_SIZE * 5 + 8, BLOCK_SIZE, False))
                                        
                elif char == "b":

                    blocks.append(Block(x, y, 1, BLOCK_SIZE, BLOCK_SIZE, True))

                x+= 1
            y += 1
            x = 0

    return blocks





def GetMaxValue(level_num):
    max = 0
    if level_num == 1:
        max = 2
    if level_num == 2:
        max = 4
    if level_num == 3:
        max = 6
    if level_num == 4:
        max = 10
    if level_num == 5:
        max = 15
    if level_num == 6:
        max = 10
    if level_num == 7:
        max = 20
    if level_num == 8:
        max = 40
    if level_num == 9:
        max = 50
    if level_num >= 10:
        max = 100
    return max




def GetVelocity(level_num):
    velocity = 1
    
    if level_num == 1:
        velocity = 2
    elif level_num == 2:
        velocity = 2
    elif level_num == 3:
        velocity = 2.5
    elif level_num == 4:
        velocity = 3
    elif level_num == 5:
        velocity = 3.5
    elif level_num >= 6:
        velocity = 5
    
    
    return velocity


def DrawHUD(screen, level_num, ball_value):
    py.draw.rect(screen, (25, 25, 25), (0, 0, WIDTH, 50))
    DrawBallValue(screen, ball_value)
    DrawLevelNumber(screen, level_num)
    


def DrawLevelNumber(screen, level_num):
    font = py.font.Font('freesansbold.ttf', 20)
    level_text = font.render("Level " + str(level_num), True, WHITE)
    
    screen.blit(level_text, ((WIDTH / 2) - level_text.get_rect().width / 2, 10))  
            
def DrawBallValue(screen, ball_value):
    py.draw.circle(screen, WHITE, (45, 20), BALL_SIZE )
    font = py.font.Font('freesansbold.ttf', 20)
    ball_number_text = font.render("x " + str(ball_value), True, WHITE)
    
    screen.blit(ball_number_text, (50, 10))  

def StartGame(screen, level_num, ball, bar, blocks, timer ):
        
    
    restart = False
    game_over = False
    fast_forward = False
    moveDown = False

    while not restart:

        for event in py.event.get():
        
            if(event.type == py.QUIT):
                py.quit()

              
            if(event.type == py.MOUSEMOTION):
                bar.x = py.mouse.get_pos()[0] - BAR_WIDTH / 2
                    
            keys = py.key.get_pressed()
            
            if keys[py.K_r]:
                restart = True
                
            if keys[py.K_SPACE]:
                fast_forward = True
            else:
                fast_forward = False

        screen.fill(BACKGROUND)
        
        DrawBlocks(screen, blocks)
        
        if(IsGameOver(blocks)):
            DrawGameOver(screen)
            game_over = True
        
        if IsLevelWon(blocks):
            if  level_num < MAX_LEVEL_NUMBER:
                level_num += 1

                blocks = InitBlocks(level_num)
            else:
                DrawWinScreen(screen)
                game_over = True


        if not game_over:
            
            ball.draw(screen)

            velocity = GetVelocity(level_num)

            
            
            ResolvePaddleBarCollisions(ball, bar)
            ResolveWallCollisions(ball)
            
            if(ball.y + BALL_SIZE > HEIGHT + 50 ):
                
                ball.x = bar.x + BAR_WIDTH / 2
                ball.y = bar.y - 30
                ball.speed_x = BALL_START_SPEED_X
                ball.speed_y =  BALL_START_SPEED_Y

                moveDown = True
 

            if not fast_forward:
                ball.move(velocity)
            
            else:
                ball.move(10)
            
            UpdateBlocks(screen, ball, blocks, moveDown)
            moveDown = False
            bar.draw(screen)


            DrawHUD(screen, level_num, ball.value)

           
        timer.tick(60)
        py.display.update()
   
def DrawWinScreen(screen):
    font = py.font.Font('freesansbold.ttf', 20)
    win_text = font.render("YOU CLEARED ALL THE LEVELS!!", True, WHITE)
    
    screen.blit(win_text, ((WIDTH / 2) - win_text.get_rect().width / 2, HEIGHT / 2))    
            
    font = py.font.Font('freesansbold.ttf', 20)
    replay_text = font.render("PRESS R TO RESTART", True, WHITE)
    screen.blit(replay_text, (WIDTH / 2- win_text.get_rect().width / 2 + 50 , (HEIGHT / 2) + 50 ))    


def ResolveWallCollisions(ball):
    if(ball.y - BALL_SIZE <= 50):
        ball.speed_y *= -1
                    
    if ball.x - BALL_SIZE<= 0:
                ball.speed_x *= -1

                        
    if ball.x + BALL_SIZE >= WIDTH:
        ball.speed_x *= -1


def ResolvePaddleBarCollisions(ball, bar):

    
            
    # top left corner of paddle bar collision when coming from right
    if ball.speed_x < 0 and ball.speed_y > 0:
        if ball.x + BALL_SIZE /2 >= bar.x + BAR_WIDTH and ball.x <= bar.x + BAR_WIDTH:
            if ball.y + BALL_SIZE >= bar.y and ball.y + BALL_SIZE <= bar.y + BAR_HEIGHT:
            
                ball.speed_y *= -1
                ball.speed_x *= -1
    
    
    
    # middle of the paddle bar collision
    if ball.x + BALL_SIZE / 2 >= bar.x and ball.x + BALL_SIZE / 2 <= bar.x + BAR_WIDTH:
        if(ball.y + BALL_SIZE   >= bar.y and ball.y + BALL_SIZE  <= bar.y + BAR_HEIGHT):
            ball.speed_y *= -1


    
    #top left corner of paddle bar collision when ball is coming from the right
    if ball.speed_x < 0 and ball.speed_y > 0:
        if ball.x <= bar.x and ball.x  +BALL_SIZE >= bar.x  :
            if ball.y + BALL_SIZE >= bar.y and ball.y <= bar.y + BAR_HEIGHT:
                ball.speed_y *= -1

    # collision of top left corner of paddle bar when ball is coming from the left
    if ball.speed_x > 0 and ball.speed_y > 0:
        if ball.x + BALL_SIZE / 2 <= bar.x and ball.x + BALL_SIZE > bar.x:
            if ball.y + BALL_SIZE >= bar.y and ball.y + BALL_SIZE <= bar.y + BAR_HEIGHT:
                ball.speed_x *= -1
                ball.speed_y *= -1
                print("top left corner coming from left")

           
##############################################
def Main():
    
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    timer = py.time.Clock()
    level_num = 11
    bar = Bar(BAR_X, BAR_Y)
    ball_start_value = 10
    keep_going = True

    while keep_going:  
        blocks = InitBlocks(level_num)
        ball = Ball(BALL_START_X, BALL_START_Y, BALL_START_SPEED_X, BALL_START_SPEED_Y, ball_start_value)
        StartGame(screen, level_num, ball, bar, blocks, timer)
########################################
        




              
def IsLevelWon(blocks):
    block_count = 0
    
    for block in blocks:
        if not block.is_ball_block:
            block_count += 1 
    
    if block_count == 0:
        return True
    
    return False


def IsGameOver(blocks):
    for block in blocks:

        if( block.y // UNIT_SIZE == HEIGHT // UNIT_SIZE - 1 ):
            return True
    return False

        

def DrawGameOver(screen):
    font = py.font.Font('freesansbold.ttf', 50)
    game_over_text = font.render("GAME OVER", True, WHITE)
    
    screen.blit(game_over_text, ((WIDTH / 2) - game_over_text.get_rect().width / 2, HEIGHT / 2))    
            
    font = py.font.Font('freesansbold.ttf', 20)
    replay_text = font.render("PRESS R TO RESTART", True, WHITE)
    screen.blit(replay_text, (WIDTH / 2- replay_text.get_rect().width / 2, HEIGHT / 2 + 50 ))    


def DrawBlocks(screen, blocks):
    for block in blocks:
        block.draw(screen)
        
def DrawBalls(screen, balls):
    for ball in balls:
        ball.draw(screen)


def UpdateBlocks(screen, ball, blocks, moveDown):
    
    for block in blocks:
        
        
        ResolveBlockCollision(ball, block)
        
        #if the block's value is 0 or less, then clear it 
        if block.value <= 0:
            blocks.remove(block)
        
        if moveDown:
            block.moveDown()
        
        
        
        

        
       

def ResolveBlockCollision(ball, block):
    
    collision = GetBlockCollision(ball, block)

    if(collision == "BOTTOM" or collision == "TOP"):
                    
        if block.is_ball_block:
        
            ball.increment()
        
        block.decrement(ball.value)
        ball.speed_y *= -1

            
    if(collision == "LEFT" or collision == "RIGHT" ):
        
        if block.is_ball_block:
        
            ball.increment()
        
        block.decrement(ball.value)
 
        ball.speed_x *= -1 
            



def GetBlockCollision(ball, block):
        # bottom side collision
        if(ball.speed_x > 0 and ball.speed_y < 0) or (ball.speed_x < 0 and ball.speed_y < 0):
            if(ball.x  >= block.x and ball.x <= block.x + block.width ):
                if(ball.y - BALL_SIZE >= block.y and ball.y - BALL_SIZE <= block.y + block.height):
                    return "BOTTOM"
        
        # right side collision
        if(ball.speed_x < 0 and ball.speed_y < 0) or (ball.speed_x < 0 and ball.speed_y > 0):  
            if(ball.x - BALL_SIZE >= block.x and ball.x  - BALL_SIZE <= block.x + block.width ):
                if(ball.y >= block.y and ball.y <= block.y + block.height):
                    return "RIGHT"

        
        if(ball.speed_x > 0 and ball.speed_y > 0) or (ball.speed_x < 0 and ball.speed_y > 0):
            if(ball.x >= block.x and ball.x <= block.x + block.width ):
                if(ball.y + BALL_SIZE + 5  >= block.y and ball.y <= block.y + block.height):
                    return "TOP"

            
        if(ball.speed_x > 0 and ball.speed_y > 0) or (ball.speed_x > 0 and ball.speed_y < 0):
            if(ball.x + BALL_SIZE >= block.x and ball.x + BALL_SIZE <= block.x + BALL_SIZE):
                if(ball.y >= block.y and ball.y <= block.y + block.height):
                    return "LEFT"
        
       
Main()