import pygame
import time 
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Ghost: coasting along")

BG = pygame.transform.scale(pygame.image.load("sgctc.jpg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 60
GHOST_WIDTH = 50
GHOST_HEIGHT = 60

PLAYER_VEL = 5
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
BULLET_VEL = 3
FONT = pygame.font.SysFont("Calibri", 40)

def draw(player1, elapsed_time, bullets):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, ("orange"), player1)
    

    for bullet in bullets:
        pygame.draw.rect(WIN, "red", bullet)

    pygame.display.update()

def main():
    run = True
    player1 = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    bullet_add_increment = 2000
    bullet_count = 0

    bullets = []
    hit = False

    while run:
        bullet_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if bullet_count > bullet_add_increment:
            for _ in range(5):  
                bullet_x = random.randint(0, WIDTH - BULLET_WIDTH)
                bullet = pygame.Rect(bullet_x, -BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

            bullet_add_increment = max(200, bullet_add_increment - 50)
            bullet_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keyboard= pygame.key.get_pressed()
        if keyboard[pygame.K_LEFT] and player1.x - PLAYER_VEL >= 0:
            player1.x -= PLAYER_VEL
        if keyboard[pygame.K_RIGHT] and player1.x + PLAYER_VEL + player1.width <= WIDTH:
            player1.x += PLAYER_VEL

        for bullet in bullets[:]:
            bullet.y += BULLET_VEL
            if bullet.y > HEIGHT:
                bullets.remove(bullet)
            elif bullet.y + bullet.height >= player1.y and bullet.colliderect(player1):
                bullets.remove(bullet)
                hit = True
                break
        if hit: 
            lost_text = FONT.render("YOU LOSE HAHA", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            break

        draw(player1, elapsed_time, bullets)
    
    pygame.quit()

if __name__ == "__main__":
    main()

