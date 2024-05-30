import pygame
import sys

pygame.init()  # Инициализация Pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Размеры экрана
SKY_COLOR = (135, 206, 235)  # Цвет неба
GROUND_COLOR = (34, 139, 34)  # Цвет земли
FPS = 60  # Кадров в секунду
moving_left = False
moving_right = False
moving_jump = False
main_font = pygame.font.Font("fonts/main_font.otf", 20)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Установка экрана
pygame.display.set_caption("Капибара собирает монеты")  # Заголовок игры
clock = pygame.time.Clock()  # Для отслеживания времени
counter_coins = 0

# Загрузка изображений
hero_img = pygame.image.load('graphics/hero.png').convert_alpha()
coin_img = pygame.image.load('graphics/coin.png').convert_alpha()

GROUND_HEIGHT = 35  # Высотка земли
# Позиции героя и монеты
hero_x, hero_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - GROUND_HEIGHT
coin_x, coin_y = 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - GROUND_HEIGHT
# Создание rect ("прямоугольников") для обнаружения столкновений
hero_rect = hero_img.get_rect(midbottom=(hero_x, hero_y))
coin_rect = coin_img.get_rect(midbottom=(coin_x, coin_y))

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("Клавиша 'A' была отпущена!")
                moving_left = False
            if event.key == pygame.K_d:
                print("Клавиша 'D' была отпущена!")
                moving_right = False

    if moving_left == True:
        hero_rect.x -= 1
    if moving_right == True:
        hero_rect.x += 1

    coin_rect.x -= 1 # Каждую итерацию монета смещается

    if hero_rect.colliderect(coin_rect):
        print("Коллизия")
        counter_coins += 0
    text_coins = main_font.render(f"Собрано монет: {counter_coins}", False, "mintcream")
    screen.fill(SKY_COLOR)  # Заливка фона цветом неба

    # Рисование земли
    pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

    # Рисование героя и монеты
    screen.blit(coin_img, coin_rect)
    screen.blit(hero_img, hero_rect)
    screen.blit(text_coins, (400, 30))
    # Обновление экрана
    pygame.display.flip()
    # Верхняя граница обновления, чтобы обновлялось не слишком часто
    clock.tick(FPS)
