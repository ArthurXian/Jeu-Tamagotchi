import pygame
import random
import time
from pygame.mixer import Sound

# Initialiser pygame
pygame.init()

# Définir la fenêtre de jeu
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tamagotchi Game")

# Définir la police
font = pygame.font.Font(None, 23)

# Charger et jouer la musique de fond
pygame.mixer.music.load(r"C:\Users\xianz\OneDrive\桌面\tamagotchi\背景音乐.mp3")
pygame.mixer.music.play(-1)  # Jouer la musique de fond en boucle

# Charger l'effet sonore de clic
click_sound = pygame.mixer.Sound(r"C:\Users\xianz\OneDrive\桌面\tamagotchi\clic.wav")

# Charger l'image de fond et ajuster la taille
background_image = pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\bg.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Charger l'image de l'écran de démarrage et ajuster la taille
start_image = pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\startgame.jpg")
start_image = pygame.transform.scale(start_image, (screen_width, screen_height))

# Charger les images des animaux
pet_images = {
    "Cat": {
        "awake": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\1_1.png"),
        "sleeping": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\1_2.png")
    },
    "Dog": {
        "awake": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\2_1.png"),
        "sleeping": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\2_2.png")
    },
    "Rabbit": {
        "awake": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\3_1.png"),
        "sleeping": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\3_2.png")
    },
    "Bird": {
        "awake": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\4_1.png"),
        "sleeping": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\4_2.png")
    },
    "Fish": {
        "awake": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\5_1.png"),
        "sleeping": pygame.image.load(r"C:\Users\xianz\OneDrive\桌面\游戏设计\5_2.png")
    }
}

# Ajuster la taille des images des animaux
for pet in pet_images.values():
    pet["awake"] = pygame.transform.scale(pet["awake"], (120, 120))
    pet["sleeping"] = pygame.transform.scale(pet["sleeping"], (120, 120))

# Initialiser la liste des animaux
def create_pet(name, images):
    return {
        "name": name,
        "images": images,
        "hunger": 200,
        "health": 200,
        "boredom": 200,
        "fatigue": 200,
        "sleeping": False,
        "sleep_timer": 0,
        "last_sleep_time": time.time(),
        "x": random.randint(0, screen_width),
        "y": random.randint(screen_height // 2, screen_height - 120),
        "speed_x": random.uniform(-0.5, 0.5),
        "speed_y": random.uniform(-0.5, 0.5)
    }

# Mettre à jour les statistiques de l'animal
def update_pet(pet, delta):
    current_time = time.time()
    if pet["sleeping"]:
        pet["sleep_timer"] -= delta
        if pet["sleep_timer"] <= 0:
            pet["sleeping"] = False
        pet["health"] = min(pet["health"] + 2 * delta, 200)
        pet["boredom"] = max(pet["boredom"] - 2 * delta, 0)
        pet["fatigue"] = min(pet["fatigue"] + 3 * delta, 200)
    else:
        pet["hunger"] = max(pet["hunger"] - 8 * delta, 0)
        pet["boredom"] = max(pet["boredom"] - 5 * delta, 0)
        pet["fatigue"] = min(pet["fatigue"] + 1 * delta, 200)
        if pet["boredom"] == 0:
            for p in pets:
                p["health"] = max(p["health"] - 8 * delta, 0)
            pet["health"] = max(pet["health"] - 10 * delta, 0)

        if current_time - pet["last_sleep_time"] > 10 and random.random() < 0.005:
            pet["sleeping"] = True
            pet["sleep_timer"] = random.randint(30, 60)
            pet["last_sleep_time"] = current_time

    pet["x"] += pet["speed_x"]
    pet["y"] += pet["speed_y"]

    if pet["x"] < 0 or pet["x"] > screen_width:
        pet["speed_x"] = -pet["speed_x"]
    if pet["y"] < screen_height // 2 or pet["y"] > screen_height - 120:
        pet["speed_y"] = -pet["speed_y"]

# Fonction pour nourrir l'animal
def pet_eat(pet, food_stock):
    if not pet["sleeping"] and pet["hunger"] < 200 and food_stock > 0:
        pet["hunger"] = min(pet["hunger"] + 50, 200)
        return True
    return False

# Fonction pour jouer avec l'animal
def pet_play(pet):
    if not pet["sleeping"]:
        pet["boredom"] = min(pet["boredom"] + 50, 200)
        pet["fatigue"] = max(pet["fatigue"] - 50, 0)

# Vérifier les conditions d'échec du jeu
def check_failure(pet):
    if pet["hunger"] == 0:
        return True, "Hunger reached zero"
    elif pet["health"] == 0:
        return True, "Health reached zero"
    elif pet["fatigue"] == 0:
        return True, "Fatigue reached zero"
    else:
        return False, ""

# Obtenir l'état de sommeil de l'animal
def get_sleep_status(pet):
    return "Sleeping" if pet["sleeping"] else "Awake"

# Dessiner l'animal à l'écran
def draw_pet(pet, screen, show_status=False, selected=False):
    size = 160 if selected else 120
    image = pet["images"]["sleeping"] if pet["sleeping"] else pet["images"]["awake"]
    image = pygame.transform.scale(image, (size, size))
    screen.blit(image, (pet["x"] - size // 2, pet["y"] - size // 2))

    if show_status:
        sleep_status_text = font.render(get_sleep_status(pet), True, (0, 0, 0))
        screen.blit(sleep_status_text, (pet["x"] - sleep_status_text.get_width() // 2, pet["y"] - 80))

        status_texts = [
            f"Hunger: {int(pet['hunger'])}",
            f"Health: {int(pet['health'])}",
            f"Boredom: {int(pet['boredom'])}",
            f"Fatigue: {int(pet['fatigue'])}"
        ]
        for index, status_text in enumerate(status_texts):
            text_surface = font.render(status_text, True, (0, 0, 0))
            text_y_position = pet["y"] + 50 + index * 15
            screen.blit(text_surface, (pet["x"] - text_surface.get_width() // 2, text_y_position))

# Réinitialiser le jeu
def reset_game():
    global pets, running, clock, game_time, days_passed, food_stock, selected_pet, game_over, game_over_reason
    pets = [
        create_pet("Cat", pet_images["Cat"]),
        create_pet("Dog", pet_images["Dog"]),
        create_pet("Rabbit", pet_images["Rabbit"]),
        create_pet("Bird", pet_images["Bird"]),
        create_pet("Fish", pet_images["Fish"])
    ]
    running = True
    clock = pygame.time.Clock()
    game_time = 180  # Temps de jeu par jour
    days_passed = 0
    food_stock = 50  # Stock de nourriture par jour
    selected_pet = None
    game_over = False
    game_over_reason = ""

# Boucle principale du jeu
reset_game()

# Écran de démarrage
def show_start_screen():
    screen.blit(start_image, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False

# Effet de transition en fondu
def fade_transition():
    fade = pygame.Surface((screen_width, screen_height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(background_image, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# Afficher l'écran de démarrage
show_start_screen()

# Effet de transition
fade_transition()

# Dessiner la scène
def draw_scene():
    screen.blit(background_image, (0, 0))

# Boucle principale du jeu
while running:
    delta = clock.tick(60) / 1000.0
    game_time -= delta

    if game_time <= 0:
        game_time = 180
        days_passed += 1
        food_stock = 50  # Réinitialiser le stock de nourriture chaque jour
        for pet in pets:
            pet["hunger"] = 200
            pet["health"] = 200
            pet["boredom"] = 200
            pet["fatigue"] = 200
            pet["sleeping"] = False

    draw_scene()

    if not game_over:
        timer_text = font.render(f"Time: {int(game_time)}s", True, (0, 0, 0))
        day_text = font.render(f"Days: {days_passed}", True, (0, 0, 0))
        food_text = font.render(f"Food Stock: {food_stock}", True, (0, 0, 0))
        screen.blit(timer_text, (10, 10))
        screen.blit(day_text, (10, 50))
        screen.blit(food_text, (10, 90))

        instructions = [
            "Click on a pet to select it",
            "Click 'Feed' or 'Play' to interact with the pet"
        ]
        for i, instruction in enumerate(instructions):
            instruction_text = font.render(instruction, True, (0, 0, 0))
            screen.blit(instruction_text, (10, 130 + i * 30))

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for pet in pets:
            update_pet(pet, delta)
            show_status = False
            if pygame.Rect(pet["x"] - 60, pet["y"] - 60, 120, 120).collidepoint(mouse_pos):
                show_status = True
                if mouse_clicked:
                    selected_pet = pet

            draw_pet(pet, screen, show_status=show_status, selected=(selected_pet == pet))

            if selected_pet == pet:
                # Dessiner les boutons d'interaction
                feed_button = pygame.Rect(pet["x"] - 50, pet["y"] + 90, 100, 30)
                play_button = pygame.Rect(pet["x"] - 50, pet["y"] + 130, 100, 30)
                pygame.draw.rect(screen, (255, 255, 255), feed_button)
                pygame.draw.rect(screen, (255, 255, 255), play_button)
                feed_text = font.render("Feed", True, (0, 0, 0))
                play_text = font.render("Play", True, (0, 0, 0))
                screen.blit(feed_text, (pet["x"] - feed_text.get_width() // 2, pet["y"] + 95))
                screen.blit(play_text, (pet["x"] - play_text.get_width() // 2, pet["y"] + 135))

                # Changer le curseur de la souris en forme de main
                if feed_button.collidepoint(mouse_pos) or play_button.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if feed_button.collidepoint(mouse_pos) and mouse_clicked:
                    click_sound.play()
                    if pet_eat(pet, food_stock):
                        food_stock -= 1
                if play_button.collidepoint(mouse_pos) and mouse_clicked:
                    click_sound.play()
                    pet_play(pet)

            # Vérifier les conditions d'échec du jeu
            failed, reason = check_failure(pet)
            if failed:
                game_over = True
                game_over_reason = f"Game Over: {reason}"
                pets = [pet]  # Ne garder que l'animal responsable de la fin du jeu
                break
    else:
        # Afficher le message de fin de jeu et la raison
        game_over_text = font.render(game_over_reason, True, (255, 0, 0))
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))

        # Dessiner l'animal responsable de la fin du jeu
        if pets:
            draw_pet(pets[0], screen, show_status=True, selected=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Réinitialiser le jeu et retourner à l'écran de démarrage
                    reset_game()
                    show_start_screen()
                    fade_transition()

    pygame.display.flip()

pygame.quit()
pygame.mixer.music.stop()

