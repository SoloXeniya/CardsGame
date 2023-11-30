import pygame
import random
import sys

# Инициализация Pygame
pygame.init()


# Размеры экрана
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 550

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

# Количество пар карточек
pairs = 5

# Список цветов для карточек
colors = [(148, 0, 211), (178, 34, 34), (240, 230, 140), (30, 144, 255), (0, 250, 154)] * 2

# Перемешивание цветов
random.shuffle(colors)

# Размеры карточек
CARD_WIDTH = 100
CARD_HEIGHT = 150

# Создание карточек
cards = []
for i in range(pairs * 2):
    cards.append({
        'color': colors[i],
        'jacket': pygame.Rect(i % 5 * (CARD_WIDTH + 10) + 100, (i // 5) * (CARD_HEIGHT + 10) + 100, CARD_WIDTH, CARD_HEIGHT),
        'flipped': False
    })


# Основной цикл игры
def main():
    global flipped_count 
    flipped_count = 0
    flipped_cards = []  # Хранит открытые карточки
    last_flip_time = 0 

    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():     # текущее время
            if event.type == pygame.QUIT:   
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and len(flipped_cards) < 2:
                for card in cards:
                    if card['jacket'].collidepoint(event.pos) and not card['flipped']:
                        card['flipped'] = True
                        flipped_cards.append(card)
                        last_flip_time = current_time
                        
                        

        # Отрисовка экрана
        screen.fill((255, 255, 255))
        draw_board()

        # Проверка на совпадение цветов
        if len(flipped_cards) == 2:
            if current_time - last_flip_time >= 500:    # Задержка для отображения карт
                if flipped_cards[0]['color'] == flipped_cards[1]['color']:   #dict  открытые карточки flipped_cards[номер открытой][dict]
                    
                    flipped_cards[0]['flipped'] = True
                    flipped_cards[1]['flipped'] = True
                    flipped_count += 1
                    print(flipped_count)
                    flipped_cards = []

                else:
                    pygame.time.delay(500)
                    flipped_cards[0]['flipped'] = False
                    flipped_cards[1]['flipped'] = False
                    flipped_cards = []
                    
        if flipped_count == 5:
            print("Игра завершена!")
            break


        pygame.display.flip()

def draw_board():
    for card in cards:
        if card['flipped']:
            pygame.draw.rect(screen, card['color'], card['jacket'])
        else:
            pygame.draw.rect(screen, (188, 143, 143), card['jacket'])

if __name__ == "__main__":
    main()
#В этом коде создается простая игра "Memory".
# Пользователь открывает карточки, и если они совпадают по цвету, 
# то они остаются открытыми. Если нет, то они возвращаются в начальное положение. 
# Игра продолжается до тех пор, пока все пары карточек не будут найдены.