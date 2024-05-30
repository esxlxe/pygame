import pygame
import sys

pygame.init()  # Инициализация Pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 2000, 800  # Размеры экрана
SKY_COLOR = (135, 206, 235)  # Цвет неба
GROUND_COLOR = (34, 139, 34)  # Цвет земли
FPS = 60  # Кадров в секунду
moving_left = False
moving_right = False
moving_jump = False
moving_jump_1 = False
main_font = pygame.font.Font("fonts/main_font.otf", 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Установка экрана
pygame.display.set_caption("Капибара собирает монеты")  # Заголовок игры
clock = pygame.time.Clock()  # Для отслеживания времени
counter_coins = 0

# Загрузка изображений
hero_img = pygame.image.load('graphics/hero.png').convert_alpha()
coin_img = pygame.image.load('graphics/coin.png').convert_alpha()

GROUND_HEIGHT = 45  # Высотка земли
# Позиции героя и монеты
hero_x, hero_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - GROUND_HEIGHT
coin_x, coin_y = 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - GROUND_HEIGHT

# Создание rect ("прямоугольников") для обнаружения столкновений
hero_rect = hero_img.get_rect(midbottom=(hero_x, hero_y))
coin_rect = coin_img.get_rect(midbottom=(coin_x, coin_y))
coin_rect_1 = coin_img.get_rect(midbottom=(coin_x + 1000, coin_y - 100))
# Основной цикл

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Выход из Pygame
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Клавиша 'A' была нажата!")
                moving_left = True
            if event.key == pygame.K_d:
                print("Клавиша 'D' была нажата!")
                moving_right = True
            if event.key == pygame.K_w:
                moving_jump = True
            if event.key == pygame.K_s:
                moving_jump_1 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("Клавиша 'A' была отпущена!")
                moving_left = False
            if event.key == pygame.K_d:
                print("Клавиша 'D' была отпущена!")
                moving_right = False
            if event.key == pygame.K_w:
                print("Клавиша 'SPACE' была нажата!")
                moving_jump = False
            if event.key == pygame.K_s:
                moving_jump_1 = False

    if moving_left == True:
        hero_rect.x -= 5
    if moving_right == True:
        hero_rect.x += 5
    if moving_jump == True:
        hero_rect.y -= 10
    if moving_jump_1 == True:
        hero_rect.y += 10

    coin_rect.x -= 4 # Каждую итерацию монета смещается
    coin_rect_1.x -= 4 # Каждую итерацию монета смещается

    if hero_rect.colliderect(coin_rect):
        counter_coins += 1
        coin_rect.x = 10
        if hero_rect.colliderect(coin_rect_1):
            counter_coins += 1
            coin_rect.x = 10
    text_coins = main_font.render(f"Собрано монет: {counter_coins}", False, "mintcream")
    screen.fill(SKY_COLOR)  # Заливка фона цветом неба

    # Рисование земли
    pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

    # Рисование героя и монеты
    screen.blit(coin_img, coin_rect)
    screen.blit(coin_img, coin_rect_1)
    screen.blit(hero_img, hero_rect)
    screen.blit(text_coins, (400, 30))
    # Обновление экрана
    pygame.display.flip()
    # Верхняя граница обновления, чтобы обновлялось не слишком часто
    clock.tick(FPS)
