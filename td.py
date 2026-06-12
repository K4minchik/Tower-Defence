import pgzrun, random, pygame, json
from pgzero.builtins import *
from pgzhelper import *


hide_mouse()

WIDTH = 1600 # Ширина окна
HEIGHT = 900 # Высота окна

TITLE = "Tower Defence" # Заголовок окна игры
FPS = 60 # Количество кадров в секунду

version = "BETA 1.6"

mode = "menu"

data = {'money': 100, 'wave': 0, "house_hp": 100, "wave_enemies": 1, "boss_health_max": 50, "health_max": 100, "counter": 1, "shield_hp": 10, "shield_hp_max": 10}
sound_data = {"volume1": 1, "sound_switch": True, "mob_switch": True, "language": "eng", "texture_mode": "normal"}
shop_data =  {"health_small": 0, "shield_switch": False}
upgrade_data = {"house_level": 1, "house_count": 500, "turret_left_level": 0, "turret_left_count": 100, "couldown_turret_left": 100, "turret_right_level": 0, "turret_right_count": 100, "couldown_turret_right": 100, "cursor_level": 1, "cursor_count": 2500, "shield_level": 1, "shield_count": 100}
achievements_data = {"achievement1": False, "achievement_counter": 0, "achievements_animate": False, "achievement2": False, "achievement2_counter": 0, "achievement3": False, "achievement4": False, "achievement5": False}

time1 = 0
real_time = 0
couldown = 0
timer = False

time1_turret_left = 0
real_time_turret_left = 0
couldown_turret_left = 0
timer_turret_left = False

time1_turret_right = 0
real_time_turret_right = 0
couldown_turret_right = 0
timer_turret_right = False

time1_animate = 0
real_time_animate = 0
couldown_animate = 0
timer_animate = False

time1_end = 0
real_time_end = 0
couldown_end = 0
timer_end = False

button_press = 0
info_str = 1

setting_mode = "music"

exitt = Actor("arrow_back.png", (1500, 800))
logo_game = Actor("logo_game.png", (1000, 200))
logo_game.images = ["logo_game_idle2.png", "logo_game.png"]
logo_game.fps = 2

fon1 = Actor("fon1.png")
fon2 = Actor("fon2.png")
game_over = Actor("end.png")
play = Actor("empty_button.png", (250, 190)) 
shop = Actor("empty_button.png", (350, 120)) 
updateb = Actor("empty_button.png", (700, 120))
settings = Actor("empty_button.png", (250, 360))
titles = Actor("empty_button.png", (250, 530))
start = Actor("button9.png", (1400, 120))
achievements = Actor("button9.png", (250, 700))
play1 = Actor('play.png', play.pos)
updateb1 = Actor('updateb.png', updateb.pos)
shop1 = Actor('shop.png', shop.pos)
settings1 = Actor('settings.png', settings.pos)
titles1 = Actor("credits.png", titles.pos)
start1 = Actor("start.png", start.pos)
achievements1 = Actor("achievements.png", achievements.pos)

flag_menu = Actor('flag_idle1.png', center = (1150, 500))
flag_menu.images = ['flag_idle1.png', 'flag_idle2.png', 'flag_idle3.png', 'flag_idle4.png']
flag_menu.fps = 8

flag_menu_patriot = Actor('flag_idle1_patriot.png', center = (1140, 380))
flag_menu_patriot.images = ['flag_idle1_patriot.png', 'flag_idle2_patriot.png', 'flag_idle3_patriot.png', 'flag_idle4_patriot.png']
flag_menu_patriot.fps = 8

info = Actor("info.png", (1500, 800))
arrow = Actor("arrow_back", (80, 80))
empty_fon1 = Actor("empty_fon1", (800, 450))
empty_fon2 = Actor("empty_fon2", (800, 450))
volume_line1 = Actor("volume_line", (1000, 220))
arrow_music_l = Actor("volume_arrow_left", (730, 220))
arrow_music_r = Actor("volume_arrow_right", (1270, 220))
arrow_language_l = Actor("volume_arrow_left", (730, 220))
arrow_language_r = Actor("volume_arrow_right", (1270, 220))
arrow_info_l = Actor("volume_arrow_left", (300, 450))
arrow_info_r = Actor("volume_arrow_right", (1300, 450))
arrow_setting_l = Actor("setting_arrow_left", (510, 130))
arrow_setting_r = Actor("setting_arrow_right", (1090, 130))
music_cursor =  Actor("volume_cursor", (1205, 220))
switch1 = Actor("switch_on", (950, 320))
switch2 = Actor("switch_on", (950, 420))
switch3 = Actor("switch_off", (950, 320))
health_shop = Actor("health_shop.png", (300, 150))
health_shop_button = Actor("empty_button.png", (400, 150))
health_small_shop = Actor("health_small_shop.png", (300, 350))
health_small_shop_button = Actor("empty_button.png", (400, 350))
health_game = Actor("health_game.png", (100, 100))
house_upgrade = Actor("house_upgrade.png", (310, 150))
house_upgrade_button = Actor("empty_button.png", (400, 150))
shield_r = Actor("shield_r.png", (3000, 600))
shield_l = Actor("shield_l.png", (3000, 600))
shield_shop = Actor("shield_shop.png", (1105, 150))
shield_shop_button = Actor("empty_button.png", (1200, 150))
shield_upgrade = Actor("shield_upgrade.png", (1105, 150))
shield_upgrade_button = Actor("empty_button.png", (1200, 150))
shield_game = Actor("shield_game.png", (300, 100))
turret_left = Actor("turret_left.png", (600, 630))
turret_right = Actor("turret_right.png", (1000, 630))
turret_left_upgrade_button = Actor("empty_button.png", (800, 150))
turret_right_upgrade_button = Actor("empty_button.png", (800, 350))
turret_left_upgrade = Actor("turret_left_upgrade", (710, 150))
turret_right_upgrade = Actor("turret_right_upgrade", (710, 350))
turret_left_shop_button = Actor("empty_button.png", (800, 150))
turret_right_shop_button = Actor("empty_button.png", (800, 350))
turret_left_shop = Actor("turret_left_shop", (710, 150))
turret_right_shop = Actor("turret_right_shop", (710, 350))
cursor_shop = Actor("cursor_shop.png", (310, 350))
cursor_shop_button = Actor("empty_button.png", (400, 350))
info_tab = Actor("info1.png")

boss1_side = random.randint(1,2)
if boss1_side == 1:
    boss1 = Actor("boss1_r_idle2.png", (-100, 570))
    boss1.images = ["boss1_r_idle2.png", "boss1_r_idle3.png"]
elif boss1_side == 2:
    boss1 = Actor("boss1_l_idle2.png", (1700, 570))
    boss1.images = ["boss1_l_idle2.png", "boss1_l_idle3.png"]
boss1.fps = 2
boss1_hp = data["boss_health_max"]

ban = Actor("ban.png")
ban_hand = Actor("ban_hand1.png")
ban_hand.images = ["ban_hand1.png", "ban_hand2.png"]
ban_hand.fps = 2

cursor = Actor("cursor.png") # Курсор мыши

house = Actor("house1", (800, 600))

achievement_game = Actor("achievement1.png", (1950, 120))
achievement1 = Actor("achievement_lock.png", (450, 120))
achievement2 = Actor("achievement_lock.png", (1150, 120))
achievement3 = Actor("achievement_lock.png", (450, 330))
achievement4 = Actor("achievement_lock.png", (450, 530))
achievement5 = Actor("achievement_lock.png", (450, 730))
achievements_animate = False

en_time = 0

bullets_left = []
bullets_right = []

enemies_r = []
enemies_l = []
for i in range(data["wave_enemies"]):
    skin_r = 1
    if skin_r == 1:
        enemy_r = Actor("slime_r", (-100, 650))
        enemy_r.speed = random.uniform(2,3)
    enemies_r.append(enemy_r)
    break
for i in range(data["wave_enemies"]):
    skin_l = 1
    if skin_l == 1:
        enemy_l = Actor("slime_l", (1700, 650))
        enemy_l.speed = random.uniform(2,3)
    enemies_r.append(enemy_l)
    break

if mode != "ban":
    with open('data.txt') as dataa:
        data = json.load(dataa)
    with open('sound_data.txt') as dataaa:
        sound_data = json.load(dataaa)
    with open('shop_data.txt') as dataaaa:
        shop_data = json.load(dataaaa)
    with open('upgrade_data.txt') as dataaaaa:
        upgrade_data = json.load(dataaaaa)
    with open('achievements_data.txt') as dataaaaaa:
        achievements_data = json.load(dataaaaaa)
    

if data["money"] < 99999 or shop_data["health_small"] < 99 and sound_data["texture_mode"] == "normal":
    music.play('lobby')  
if data["money"] > 99999 or shop_data["health_small"] > 99 and sound_data["texture_mode"] == "normal":
    sound_data["volume1"] = 1
    music.play("lobby_ban")
if sound_data["texture_mode"] == "patriot":
    music.play("patriot")

if sound_data["volume1"] == 1:
    music_cursor.x = 1205
    music.set_volume(1)
elif sound_data["volume1"] == 0.75:
    music_cursor.x = 1105
    music.set_volume(0.75)
elif sound_data["volume1"] == 0.5:
    music_cursor.x = 1005
    music.set_volume(0.5)
elif sound_data["volume1"] == 0.25:
    music_cursor.x = 905
    music.set_volume(0.25)
elif sound_data["volume1"] == 0:
    music_cursor.x = 795
    music.set_volume(0)

# Отрисовка
def draw(): 
    if sound_data["language"] == "eng": # Проверка языка (английская отрисовка)
        if mode == "menu":
            fon1.draw()
            play.draw()
            settings.draw()
            play1.draw()
            settings1.draw()
            if sound_data["texture_mode"] == "normal":
                flag_menu.draw()
            elif sound_data["texture_mode"] == "patriot":
                flag_menu_patriot.draw()
            titles.draw()
            titles1.draw()
            achievements.draw()
            achievements1.draw()
            logo_game.draw()
        
        
        elif mode == "settings":
            fon1.draw()

            flag_menu.draw()
            empty_fon2.draw()

            arrow.draw()
            arrow_setting_l.draw()
            arrow_setting_r.draw()
            
            if setting_mode == "music":
                screen.draw.text("Sound settings", fontsize = 50, center = (800, 130), color = 'black', fontname = 'pixel.ttf')
                screen.draw.text("Music volume", fontsize = 40, center = (500, 220), color = 'black', fontname = 'pixel.ttf')
                arrow_music_l.draw()
                arrow_music_r.draw()
                volume_line1.draw()
                music_cursor.draw()

                screen.draw.text("Other sounds", fontsize = 40, center = (500, 320), color = 'black', fontname = 'pixel.ttf')
                switch1.draw()
                if sound_data["sound_switch"] == True:
                    switch1.image = "switch_on"
                    screen.draw.text("ON", fontsize = 50, center = (1055, 325), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["sound_switch"] == False:
                    switch1.image = "switch_off"
                    screen.draw.text("OFF", fontsize = 50, center = (1065, 325), color = 'black', fontname = 'pixel.ttf')

                screen.draw.text("Mob sounds", fontsize = 40, center = (500, 420), color = 'black', fontname = 'pixel.ttf')
                switch2.draw()
                if sound_data["mob_switch"] == True:
                    switch2.image = "switch_on"
                    screen.draw.text("ON", fontsize = 50, center = (1055, 425), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["mob_switch"] == False:
                    switch2.image = "switch_off"
                    screen.draw.text("OFF", fontsize = 50, center = (1065, 425), color = 'black', fontname = 'pixel.ttf') 

            elif setting_mode == "grafic":
                screen.draw.text("Graphics settings", fontsize = 50, center = (800, 130), color = 'black', fontname = 'pixel.ttf')

                screen.draw.text("Language", fontsize = 40, center = (500, 220), color = 'black', fontname = 'pixel.ttf')
                arrow_language_l.draw()
                arrow_language_r.draw()
                if sound_data["language"] == "eng":
                    screen.draw.text("English", fontsize = 40, center = (1000, 220), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["language"] == "rus":
                    screen.draw.text("Русский", fontsize = 40, center = (1000, 220), color = 'black', fontname = 'pixel.ttf')
                
                screen.draw.text("Patriot mode", fontsize = 40, center = (500, 320), color = 'black', fontname = 'pixel.ttf')
                switch3.draw()
                if sound_data["texture_mode"] == "patriot":
                    switch3.image = "switch_on"
                    screen.draw.text("ON", fontsize = 50, center = (1055, 325), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["texture_mode"] == "normal":
                    switch3.image = "switch_off"
                    screen.draw.text("OFF", fontsize = 50, center = (1065, 325), color = 'black', fontname = 'pixel.ttf') 

            
        elif mode == "titles":
            fon1.draw()

            flag_menu.draw()

            empty_fon1.draw()
            arrow.draw()
            screen.draw.text("Developed by:", fontsize = 50, center = (800, 170), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Alisa Orlovskaia (K4minchik)", fontsize = 50, center = (800, 220), color = 'orange', fontname = 'pixel.ttf')
            screen.draw.text("Contacts:", fontsize = 50, center = (800, 300), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Discord - k4minchik\nEmail - orlovskayau17@gmail.com", fontsize = 50, center = (800, 380), color = 'orange', fontname = 'pixel.ttf')
            screen.draw.text("Special Thanks To:", fontsize = 50, center = (800, 490), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Semyon Pavonskiy (4unduck);\n Alisa Mironova; You.", fontsize = 50, center = (800, 570), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(f"Made ENTIRELY on PyGame Zero\nVersion - {version}", fontsize = 50, center = (800, 730), color = 'black', fontname = 'pixel.ttf')
        
        
        elif mode == "play":
            fon2.draw()
            house.draw()
            shop.draw()
            updateb.draw()
            start.draw()
            shop1.draw()
            updateb1.draw()
            start1.draw()
            arrow.draw()
            info.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()
            screen.draw.text("House HP", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Money", fontsize = 40, midleft = (655, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (820, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("Shield HP", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')


        elif mode == "shop":
            fon2.draw()
            house.draw()
            arrow.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()
            
            screen.draw.text("House HP", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Money", fontsize = 40, midleft = (655, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (820, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("Shield HP", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')

            health_shop_button.draw()
            health_shop.draw()
            screen.draw.text("Count : 1000", fontsize = 25, center = (435, 195), color = 'Orange', fontname = 'pixel.ttf')
            screen.draw.text("NOT STORED", fontsize = 23, center = (435, 165), color = 'RED', fontname = 'pixel.ttf')
            screen.draw.text("Fully restores \nhealth", fontsize = 23, center = (435, 120), color = 'Black', fontname = 'pixel.ttf')

            health_small_shop_button.draw()
            health_small_shop.draw()
            screen.draw.text("Count : 50", fontsize = 25, center = (435, 390), color = 'Orange', fontname = 'pixel.ttf')
            screen.draw.text("In storage :", fontsize = 23, center = (415, 355), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text(str(shop_data["health_small"]), fontsize = 23, midleft = (500, 355), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text("Restores 10 HP", fontsize = 23, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')

            turret_left_shop_button.draw()
            turret_left_shop.draw()
            if upgrade_data["turret_left_level"] == 0:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret", fontsize = 25, center = (845, 130), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("SALES", fontsize = 40, center = (845, 150), color = 'RED', fontname = 'pixel.ttf')
            turret_right_shop_button.draw()
            turret_right_shop.draw()
            if upgrade_data["turret_right_level"] == 0:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret", fontsize = 25, center = (845, 330), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("SALES", fontsize = 40, center = (845, 350), color = 'RED', fontname = 'pixel.ttf')

            shield_shop_button.draw()
            shield_shop.draw()
            if shop_data["shield_switch"] == False:
                screen.draw.text("Count : 500", fontsize = 25, center = (1245, 175), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Shield\n with hp", fontsize = 25, center = (1245, 130), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("SALES", fontsize = 40, center = (1245, 150), color = 'RED', fontname = 'pixel.ttf')
        
        
        elif mode == "upgrade":
            fon2.draw()
            house.draw()
            arrow.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()

            house_upgrade_button.draw()
            house_upgrade.draw()
            if upgrade_data["house_level"] != 4:
                screen.draw.text("Count :", fontsize = 25, center = (435, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["house_count"]), fontsize = 25, center = (435, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("+max HP for \nhouse", fontsize = 23, center = (435, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("MAX LEVEL", fontsize = 25, center = (445, 145), color = 'RED', fontname = 'pixel.ttf')

            turret_left_upgrade_button.draw()
            turret_left_upgrade.draw()
            if upgrade_data["turret_left_level"] == 0:
                screen.draw.text("NOT\n AVAILABLE", fontsize = 27, center = (845, 150), color = 'RED', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 1:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret fires \nbullets every \n0.8 second", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 2:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret fires \nbullets every \n0.5 second", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 3:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret fires \nbullets every \n0.2 second", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 4:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret fires \nbullets every \n0.08 second", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 5:
                screen.draw.text("Count :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Left turret fires \nbullets every \n0.05 second", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("MAX LEVEL", fontsize = 25, center = (850, 145), color = 'RED', fontname = 'pixel.ttf')

            turret_right_upgrade_button.draw()
            turret_right_upgrade.draw()
            if upgrade_data["turret_right_level"] == 0:
                screen.draw.text("NOT\n AVAILABLE", fontsize = 27, center = (845, 350), color = 'RED', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 1:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret fires \nbullets every \n0.8 second", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 2:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret fires \nbullets every \n0.5 second", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 3:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret fires \nbullets every \n0.2 second", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 4:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret fires \nbullets every \n0.08 second", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 5:
                screen.draw.text("Count :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Right turret fires \nbullets every \n0.05 second", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("MAX LEVEL", fontsize = 25, center = (850, 345), color = 'RED', fontname = 'pixel.ttf')

            cursor_shop_button.draw()
            cursor_shop.draw()
            if upgrade_data["cursor_level"] == 1:
                screen.draw.text("Count :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("2 damage & coin\nper click", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 2:
                screen.draw.text("Count :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("4 damage & coin\nper click", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 3:
                screen.draw.text("Count :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("6 damage & coin\nper click", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 4:
                screen.draw.text("Count :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("8 damage & coin\nper click", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 5:
                screen.draw.text("Count :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("10 damage & coin\nper click", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("MAX LEVEL", fontsize = 25, center = (445, 345), color = 'RED', fontname = 'pixel.ttf')

            shield_upgrade_button.draw()
            shield_upgrade.draw()
            if upgrade_data["shield_count"] != 6400:
                screen.draw.text("Count :", fontsize = 25, center = (1245, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["shield_count"]), fontsize = 25, center = (1245, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("+max HP for\nshield", fontsize = 23, center = (1245, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("MAX LEVEL", fontsize = 25, center = (1245, 145), color = 'RED', fontname = 'pixel.ttf')
            

            screen.draw.text("House HP", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Money", fontsize = 40, midleft = (655, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (820, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("Shield HP", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')

            
        elif mode == "go": 
            fon2.draw()
            for i in range(len(enemies_r)):
                enemies_r[i].draw()
            for i in range(len(enemies_l)):
                enemies_l[i].draw()
            house.draw()
            
            screen.draw.text("Wave", fontsize = 40, midleft = (720, 350), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text(str(data["wave"]), fontsize = 40, midleft = (870, 350), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text("Time left", fontsize = 40, midleft = (640, 300), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text(f"{couldown}", fontsize = 40, midleft = (875, 300), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text("House HP", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Money", fontsize = 40, midleft = (655, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (820, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("Shield HP", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')
            health_game.draw()
            screen.draw.text("Q", fontsize = 50, midleft = (30, 55), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text(str(shop_data["health_small"]), fontsize = 50, center = (100, 150), color = 'Black', fontname = 'pixel.ttf')
            
            if upgrade_data["turret_left_level"] >= 1:
                # Отрисовка пуль
                for i in range(len(bullets_left)):
                    bullets_left[i].draw()
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                for i in range(len(bullets_right)):
                    bullets_right[i].draw()
                turret_right.draw()
            if data["wave"]%2 == 0 and couldown <= 20 and boss1_hp > 0:
                boss1.draw()
                screen.draw.text(f"LENG HP : {boss1_hp}\nTHE SHIELD WON'T PROTECT", fontsize = 40, center = (800, 120), color = 'RED', fontname = 'pixel.ttf')
            shield_l.draw()
            shield_r.draw()
            
            
        elif mode == "achievements":
            fon1.draw()
            flag_menu.draw()
            arrow.draw()
            achievement1.draw()
            achievement2.draw()
            achievement3.draw()
            achievement4.draw()
            achievement5.draw()


        elif mode == "info":
            fon2.draw()
            arrow.draw()
            info_tab.draw()
            arrow_info_r.draw()
            arrow_info_l.draw()


        elif mode == "game_over":
            game_over.draw()


        elif mode == "ban":
            ban.draw()
            ban_hand.draw()
        achievement_game.draw()  
        cursor.draw() # курсор мыши

    if sound_data["language"] == "rus": # Проверка языка (русская отрисовка)
        if mode == "menu":
            fon1.draw()
            play.draw()
            settings.draw()
            play1.draw()
            settings1.draw()
            if sound_data["texture_mode"] == "normal":
                flag_menu.draw()
            elif sound_data["texture_mode"] == "patriot":
                flag_menu_patriot.draw()
            titles.draw()
            titles1.draw()
            achievements.draw()
            achievements1.draw()
            logo_game.draw()
        
        
        elif mode == "settings":
            fon1.draw()

            flag_menu.draw()
            empty_fon2.draw()

            arrow.draw()
            arrow_setting_l.draw()
            arrow_setting_r.draw()
            
            if setting_mode == "music":
                screen.draw.text("Настройки звука", fontsize = 50, center = (800, 130), color = 'black', fontname = 'pixel.ttf')
                screen.draw.text("Громкость музыки", fontsize = 36, center = (500, 220), color = 'black', fontname = 'pixel.ttf')
                arrow_music_l.draw()
                arrow_music_r.draw()
                volume_line1.draw()
                music_cursor.draw()

                screen.draw.text("Другие звуки", fontsize = 40, center = (500, 320), color = 'black', fontname = 'pixel.ttf')
                switch1.draw()
                if sound_data["sound_switch"] == True:
                    switch1.image = "switch_on"
                    screen.draw.text("ВКЛ", fontsize = 50, center = (1068, 325), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["sound_switch"] == False:
                    switch1.image = "switch_off"
                    screen.draw.text("ВЫКЛ", fontsize = 50, center = (1095, 325), color = 'black', fontname = 'pixel.ttf')

                screen.draw.text("Звуки существ", fontsize = 40, center = (500, 420), color = 'black', fontname = 'pixel.ttf')
                switch2.draw()
                if sound_data["mob_switch"] == True:
                    switch2.image = "switch_on"
                    screen.draw.text("ВКЛ", fontsize = 50, center = (1068, 425), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["mob_switch"] == False:
                    switch2.image = "switch_off"
                    screen.draw.text("ВЫКЛ", fontsize = 50, center = (1095, 425), color = 'black', fontname = 'pixel.ttf') 

            elif setting_mode == "grafic":
                screen.draw.text("Настройки графики", fontsize = 44, center = (800, 130), color = 'black', fontname = 'pixel.ttf')

                screen.draw.text("Язык", fontsize = 40, center = (500, 220), color = 'black', fontname = 'pixel.ttf')
                arrow_language_l.draw()
                arrow_language_r.draw()
                if sound_data["language"] == "eng":
                    screen.draw.text("English", fontsize = 40, center = (1000, 220), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["language"] == "rus":
                    screen.draw.text("Русский", fontsize = 40, center = (1000, 220), color = 'black', fontname = 'pixel.ttf')
                
                screen.draw.text("Режим патриота", fontsize = 40, center = (500, 320), color = 'black', fontname = 'pixel.ttf')
                switch3.draw()
                if sound_data["texture_mode"] == "patriot":
                    switch3.image = "switch_on"
                    screen.draw.text("ВКЛ", fontsize = 50, center = (1068, 325), color = 'black', fontname = 'pixel.ttf')
                elif sound_data["texture_mode"] == "normal":
                    switch3.image = "switch_off"
                    screen.draw.text("ВЫКЛ", fontsize = 50, center = (1095, 325), color = 'black', fontname = 'pixel.ttf') 


        elif mode == "titles":
            fon1.draw()

            flag_menu.draw()

            empty_fon1.draw()
            arrow.draw()
            screen.draw.text("Создала:", fontsize = 50, center = (800, 170), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Алиса Орловская (K4minchik)", fontsize = 50, center = (800, 220), color = 'orange', fontname = 'pixel.ttf')
            screen.draw.text("Контакты:", fontsize = 50, center = (800, 300), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Дискорд - k4minchik\nПочта - orlovskayau17@gmail.com", fontsize = 50, center = (800, 380), color = 'orange', fontname = 'pixel.ttf')
            screen.draw.text("Специальное Спасибо:", fontsize = 50, center = (800, 490), color = 'black', fontname = 'pixel.ttf')
            screen.draw.text("Семён Павонский (4unduck);\nАлиса Миронова.", fontsize = 50, center = (800, 570), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(f"Сделано ПОЛНОСТЬЮ на PyGame Zero\nВерсия - {version}", fontsize = 46, center = (800, 730), color = 'black', fontname = 'pixel.ttf')
        

        elif mode == "play":
            fon2.draw()
            house.draw()
            shop.draw()
            updateb.draw()
            start.draw()
            shop1.draw()
            updateb1.draw()
            start1.draw()
            arrow.draw()
            info.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()
            screen.draw.text("ХП Дома", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Деньги", fontsize = 40, midleft = (675, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (860, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("ХП Щита", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')
            

        elif mode == "shop":
            fon2.draw()
            house.draw()
            arrow.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()
            
            screen.draw.text("ХП Дома", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Деньги", fontsize = 40, midleft = (675, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (860, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("ХП Щита", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')

            health_shop_button.draw()
            health_shop.draw()
            screen.draw.text("Цена : 1000", fontsize = 25, center = (435, 195), color = 'Orange', fontname = 'pixel.ttf')
            screen.draw.text("НЕ ХРАНИТСЯ", fontsize = 22, center = (435, 165), color = 'RED', fontname = 'pixel.ttf')
            screen.draw.text("Полное \nвосстановление \nздоровья", fontsize = 20, center = (435, 120), color = 'Black', fontname = 'pixel.ttf')

            health_small_shop_button.draw()
            health_small_shop.draw()
            screen.draw.text("Цена : 50", fontsize = 25, center = (435, 390), color = 'Orange', fontname = 'pixel.ttf')
            screen.draw.text("В хранении : ", fontsize = 22, center = (415, 355), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text(str(shop_data["health_small"]), fontsize = 23, midleft = (500, 355), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text("Восстанавливает \n10 ХП", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')

            turret_left_shop_button.draw()
            turret_left_shop.draw()
            if upgrade_data["turret_left_level"] == 0:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая\n турель", fontsize = 27, center = (845, 125), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("ПРОДАНО", fontsize = 27, center = (845, 150), color = 'RED', fontname = 'pixel.ttf')
            turret_right_shop_button.draw()
            turret_right_shop.draw()
            if upgrade_data["turret_right_level"] == 0:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая\n турель", fontsize = 27, center = (845, 325), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("ПРОДАНО", fontsize = 27, center = (845, 350), color = 'RED', fontname = 'pixel.ttf')

            shield_shop_button.draw()
            shield_shop.draw()
            if shop_data["shield_switch"] == False:
                screen.draw.text("Цена : 500", fontsize = 25, center = (1245, 175), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Щит с ХП", fontsize = 27, center = (1245, 130), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("ПРОДАНО", fontsize = 27, center = (1245, 150), color = 'RED', fontname = 'pixel.ttf')
        

        elif mode == "upgrade":
            fon2.draw()
            house.draw()
            arrow.draw()
            if upgrade_data["turret_left_level"] >= 1:
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                turret_right.draw()
            shield_l.draw()
            shield_r.draw()

            house_upgrade_button.draw()
            house_upgrade.draw()
            if upgrade_data["house_level"] != 4:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["house_count"]), fontsize = 25, center = (435, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("+макс ХП \nдля дома", fontsize = 23, center = (435, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("МАКСИМАЛЬНЫЙ", fontsize = 16, center = (445, 135), color = 'RED', fontname = 'pixel.ttf')
                screen.draw.text("ЛВЛ", fontsize = 16, center = (445, 155), color = 'RED', fontname = 'pixel.ttf')

            turret_left_upgrade_button.draw()
            turret_left_upgrade.draw()
            if upgrade_data["turret_left_level"] == 0:
                screen.draw.text("НЕТ В\n НАЛИЧИИ", fontsize = 27, center = (845, 150), color = 'RED', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 1:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая турель\n стреляет каждую\n 0.8 секунду", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 2:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая турель\n стреляет каждую\n 0.5 секунду", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 3:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая турель\n стреляет каждую\n 0.2 секунду", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 4:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая турель\n стреляет каждую\n 0.08 секунду", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_left_level"] == 5:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_left_count"]), fontsize = 25, center = (835, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Левая турель\n стреляет каждую\n 0.05 секунду", fontsize = 20, center = (835, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("МАКСИМАЛЬНЫЙ", fontsize = 16, center = (850, 135), color = 'RED', fontname = 'pixel.ttf')
                screen.draw.text("ЛВЛ", fontsize = 16, center = (850, 155), color = 'RED', fontname = 'pixel.ttf')

            turret_right_upgrade_button.draw()
            turret_right_upgrade.draw()
            if upgrade_data["turret_right_level"] == 0:
                screen.draw.text("НЕТ В\n НАЛИЧИИ", fontsize = 27, center = (845, 350), color = 'RED', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 1:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая турель\n стреляет каждую\n 0.8 секунду", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 2:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая турель\n стреляет каждую\n 0.5 секунду", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 3:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая турель\n стреляет каждую\n 0.2 секунду", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 4:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая турель\n стреляет каждую\n 0.08 секунду", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["turret_right_level"] == 5:
                screen.draw.text("Цена :", fontsize = 25, center = (835, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["turret_right_count"]), fontsize = 25, center = (835, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("Правая турель\n стреляет каждую\n 0.05 секунду", fontsize = 20, center = (835, 320), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("МАКСИМАЛЬНЫЙ", fontsize = 16, center = (850, 335), color = 'RED', fontname = 'pixel.ttf')
                screen.draw.text("ЛВЛ", fontsize = 16, center = (850, 355), color = 'RED', fontname = 'pixel.ttf')

            cursor_shop_button.draw()
            cursor_shop.draw()
            if upgrade_data["cursor_level"] == 1:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("2 урона & монет\nза клик", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 2:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("4 урона & монет\nза клик", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 3:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("6 урона & монет\nза клик", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 4:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("8 урона & монет\nза клик", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            elif upgrade_data["cursor_level"] == 5:
                screen.draw.text("Цена :", fontsize = 25, center = (435, 370), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["cursor_count"]), fontsize = 25, center = (435, 395), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("10 урона & монет\nза клик", fontsize = 21, center = (435, 320), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("МАКСИМАЛЬНЫЙ", fontsize = 16, center = (445, 335), color = 'RED', fontname = 'pixel.ttf')
                screen.draw.text("ЛВЛ", fontsize = 16, center = (445, 355), color = 'RED', fontname = 'pixel.ttf')

            shield_upgrade_button.draw()
            shield_upgrade.draw()
            if upgrade_data["shield_count"] != 6400:
                screen.draw.text("Цена :", fontsize = 25, center = (1245, 170), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text(str(upgrade_data["shield_count"]), fontsize = 25, center = (1245, 195), color = 'Orange', fontname = 'pixel.ttf')
                screen.draw.text("+макс ХП \nдля щита", fontsize = 23, center = (1245, 120), color = 'Black', fontname = 'pixel.ttf')
            else:
                screen.draw.text("МАКСИМАЛЬНЫЙ", fontsize = 16, center = (1245, 135), color = 'RED', fontname = 'pixel.ttf')
                screen.draw.text("ЛВЛ", fontsize = 16, center = (1245, 155), color = 'RED', fontname = 'pixel.ttf')
            

            screen.draw.text("ХП Дома", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Деньги", fontsize = 40, midleft = (675, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (860, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("ХП Щита", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')

            
        elif mode == "go":
            fon2.draw()
            for i in range(len(enemies_r)):
                enemies_r[i].draw()
            for i in range(len(enemies_l)):
                enemies_l[i].draw()
            house.draw()
            
            screen.draw.text("Волна", fontsize = 40, midleft = (720, 350), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text(str(data["wave"]), fontsize = 40, midleft = (870, 350), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text("Оставшееся время", fontsize = 40, midleft = (540, 300), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text(f"{couldown}", fontsize = 40, midleft = (995, 300), color = 'white', fontname = 'pixel.ttf')
            screen.draw.text("ХП Дома", fontsize = 40, midleft = (640, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text(str(data["house_hp"]), fontsize = 40, midleft = (875, 750), color = 'Green', fontname = 'pixel.ttf')
            screen.draw.text("Деньги", fontsize = 40, midleft = (675, 800), color = 'Yellow', fontname = 'pixel.ttf')
            screen.draw.text(str(data["money"]), fontsize = 40, midleft = (860, 800), color = 'Yellow', fontname = 'pixel.ttf')
            if shop_data["shield_switch"] == True:
                screen.draw.text("ХП Щита", fontsize = 40, midleft = (655, 850), color = '#38f0e0', fontname = 'pixel.ttf')
                screen.draw.text(str(data["shield_hp"]), fontsize = 40, midleft = (890, 850), color = '#38f0e0', fontname = 'pixel.ttf')
            health_game.draw()
            screen.draw.text("Q", fontsize = 50, midleft = (30, 55), color = 'Black', fontname = 'pixel.ttf')
            screen.draw.text(str(shop_data["health_small"]), fontsize = 50, center = (100, 150), color = 'Black', fontname = 'pixel.ttf')
            
            if upgrade_data["turret_left_level"] >= 1:
                # Отрисовка пуль
                for i in range(len(bullets_left)):
                    bullets_left[i].draw()
                turret_left.draw()
            if upgrade_data["turret_right_level"] >= 1:
                for i in range(len(bullets_right)):
                    bullets_right[i].draw()
                turret_right.draw()
            if data["wave"]%2 == 0 and couldown <= 20 and boss1_hp > 0:
                boss1.draw()
                screen.draw.text(f"ЛЕНГ ХП : {boss1_hp}\nЩИТ НЕ ЗАЩИТИТ", fontsize = 40, center = (800, 120), color = 'RED', fontname = 'pixel.ttf')
            shield_l.draw()
            shield_r.draw()
            
            
        elif mode == "achievements":
            fon1.draw()
            flag_menu.draw()
            arrow.draw()
            achievement1.draw()
            achievement2.draw()
            achievement3.draw()
            achievement4.draw()
            achievement5.draw()


        elif mode == "info":
            fon2.draw()
            arrow.draw()
            info_tab.draw()
            arrow_info_r.draw()
            arrow_info_l.draw()


        elif mode == "game_over":
            game_over.draw()


        elif mode == "ban":
            ban.draw()
            ban_hand.draw()
        achievement_game.draw()  
        cursor.draw() # курсор мыши
        
# Проигрывание музыки в игре
def music1():
    if mode == "go":
        if sound_data["texture_mode"] == "normal":
            music.play("game")
        elif sound_data["texture_mode"] == "patriot":
            music.play("patriot")
    elif mode == "menu" or mode == "setting" or mode == "titles" or mode == "upgrade" or mode == "shop" or mode == "play" or mode == "achievements":
        if sound_data["texture_mode"] == "normal":
            music.play("lobby")
        elif sound_data["texture_mode"] == "patriot":
            music.play("patriot")
    elif mode == "game_over":
        music.stop()
        if sound_data["sound_switch"] == True:
            sounds.end.play()

# Таймер до конца раунда
def timer1():
    if timer == True:
        # Таймер
        global time1, real_time, couldown
        time1 += 1
        if time1 > 100:
            real_time = time1//100
        if real_time == 1:
            real_time = 0
            time1 = 0
            couldown -= 1
    elif timer == False:
        time1 = 0
        real_time = 0
        couldown = 30

# Таймер выстрелов левой турели
def timer1_turret_left():
    if timer_turret_left == True:
        # Таймер
        global time1_turret_left, real_time_turret_left, couldown_turret_left
        time1_turret_left += 1
        if time1_turret_left >= 1:
            real_time_turret_left = time1_turret_left//1
        if real_time_turret_left == upgrade_data["couldown_turret_left"]:
            real_time_turret_left = 0
            time1_turret_left = 0
            couldown_turret_left -= 100
    elif timer_turret_left == False or mode == "play":
        time1_turret_left = 0
        real_time_turret_left = 0
        couldown_turret_left = upgrade_data["couldown_turret_left"]

# Таймер выстрелов правой турели
def timer1_turret_right():
    if timer_turret_right == True:
        # Таймер
        global time1_turret_right, real_time_turret_right, couldown_turret_right
        time1_turret_right += 1
        if time1_turret_right >= 1:
            real_time_turret_right = time1_turret_right//1
        if real_time_turret_right == upgrade_data["couldown_turret_right"]:
            real_time_turret_right = 0
            time1_turret_right = 0
            couldown_turret_right -= 100
    elif timer_turret_right == False or mode == "play":
        time1_turret_right = 0
        real_time_turret_right = 0
        couldown_turret_right = upgrade_data["couldown_turret_right"]

# Таймер анимации достижений
def timer1_animate():
    if timer_animate == True:
        # Таймер
        global time1_animate, real_time_animate, couldown_animate
        time1_animate += 1
        if time1_animate > 100:
            real_time_animate = time1_animate//100
        if real_time_animate == 1:
            real_time_animate = 0
            time1_animate = 0
            couldown_animate -= 1
    elif timer_animate == False or mode == "play":
        time1_animate = 0
        real_time_animate = 0
        couldown_animate = 2

# Таймер экрана смерти
def timer1_end():
    if timer_end == True:
        # Таймер
        global time1_end, real_time_end, couldown_end
        time1_end += 1
        if time1_end > 100:
            real_time_end = time1_end//100
        if real_time_end == 1:
            real_time_end = 0
            time1_end = 0
            couldown_end -= 1
    elif timer_end == False:
        time1_end = 0
        real_time_end = 0
        couldown_end = 2

# Сброс положения кнопок
def restart(): 
    play.pos = (250, 190)
    shop.pos = (350, 120)
    updateb.pos = (700, 120)
    settings.pos = (250, 360)
    titles.pos = (250, 530)
    start.pos = (1400, 120)
    achievements.pos = (250, 700)
    info.pos = (1500, 800)
    play1.pos = play.pos
    updateb1.pos = updateb.pos
    shop1.pos = shop.pos
    settings1.pos = settings.pos
    titles1.pos = titles.pos
    start1.pos = start.pos 
    achievements1.pos = achievements.pos

# Новый враг
# Создание нового врага слева
def new_enemy_r():
    skin_r = random.randint(1,2)
    if skin_r == 1:
        enemy_r = Actor("slime_r", (-100, 650))
        enemy_r.speed = random.uniform(2,3)
    elif skin_r == 2:
        enemy_r = Actor("slime_r2", (-100, 650))
        enemy_r.speed = random.uniform(2,3)
    enemies_r.append(enemy_r)
# Создание нового врага справа
def new_enemy_l():
    skin_l = random.randint(1,2)
    if skin_l == 1:
        enemy_l = Actor("slime_l", (1700, 650))
        enemy_l.speed = random.uniform(2,3)
    elif skin_l == 2:
        enemy_l = Actor("slime_l2", (1700, 650))
        enemy_l.speed = random.uniform(2,3)
    enemies_l.append(enemy_l)

# Движение врагов
# Движение левых врагов
def enemy_r_ship():
    global wave_enemies
    for i in range(len(enemies_r)):
        enemies_r[i].x += enemies_r[i].speed
# Движение правых врагов
def enemy_l_ship():
    global wave_enemies
    for i in range(len(enemies_l)):
        enemies_l[i].x -= enemies_l[i].speed

# Дом умирает 😭 (Кароче данные откатываются)
def house_die():
    global data, mode, shop_data, upgrade_data, enemies_l, enemies_r,  bullets_left, bullets_right, boss1_hp, timer_end, couldown_end
    if data["house_hp"] <= 0 and timer_end == False:
        mode = "game_over"
        timer_end = True
        music1()
        bullets_left = []
        bullets_right = []
        enemies_r = []
        enemies_l = []
        data = {'money': 100, 'wave': 0, "house_hp": 100, "wave_enemies": 1, "boss_health_max": 50, "health_max": 100, "counter": 1, "shield_hp": 10, "shield_hp_max": 10}
        shop_data =  {"health_small": 0, "shield_switch": False}
        upgrade_data = {"house_level": 1, "house_count": 500, "turret_left_level": 0, "turret_left_count": 200, "couldown_turret_left": 100, "turret_right_level": 0, "turret_right_count": 200, "couldown_turret_right": 100, "cursor_level": 1, "cursor_count": 2500, "shield_level": 1, "shield_count": 100}
        if boss1_side == 1:
            boss1.x = -100
        elif boss1_side == 2:
            boss1.x = 1700
        with open('data.txt', 'w') as dataa:
            json.dump(data, dataa)
        with open('sound_data.txt', 'w') as dataaa:
            json.dump(sound_data, dataaa)
        with open('shop_data.txt', 'w') as dataaaa:
            json.dump(shop_data, dataaaa)
        with open('upgrade_data.txt', 'w') as dataaaaa:
            json.dump(upgrade_data, dataaaaa)
        with open('achievements_data.txt', 'w') as dataaaaaa:
            json.dump(achievements_data, dataaaaaa)

    if couldown_end <= 0 and mode == "game_over":
        timer_end = False
        mode = "menu"
        music1()

# Проверка текстур
def texture():
    if sound_data["texture_mode"] == "normal":
        fon1.image = "fon1.png"
        fon2.image = "fon2.png"
    elif sound_data["texture_mode"] == "patriot":
        fon1.image = "fon1_patriot.png"
        fon2.image = "fon2_patriot.png"

# Проверка языка
def language():
    if sound_data["language"] == "eng": # Русский
        play1.image = 'play.png'
        updateb1.image = 'updateb.png'
        shop1.image = 'shop.png'
        settings1.image = 'settings.png'
        titles1.image = "credits.png"
        start1.image = "start.png"
        achievements1.image = "achievements.png"
        ban.image = "ban.png"
        game_over.image = "end.png"

        if info_str == 1: #Обучение
            info_tab.image = "info1.png"
        elif info_str == 2:
            info_tab.image = "info2.png"
        elif info_str == 3:
            info_tab.image = "info3.png"
        elif info_str == 4:
            info_tab.image = "info4.png"
        elif info_str == 5:
            info_tab.image = "info5.png"
        elif info_str == 6:
            info_tab.image = "info6.png"
    elif sound_data["language"] == "rus": # Английский
        play1.image = 'play_rus.png'
        updateb1.image = 'updateb_rus.png'
        shop1.image = 'shop_rus.png'
        settings1.image = 'settings_rus.png'
        titles1.image = "credits_rus.png"
        start1.image = "start_rus.png"
        achievements1.image = "achievements_rus.png"
        ban.image = "ban_rus.png"
        game_over.image = "end_rus.png"

        if info_str == 1: #Обучение
            info_tab.image = "info1_rus.png"
        elif info_str == 2:
            info_tab.image = "info2_rus.png"
        elif info_str == 3:
            info_tab.image = "info3_rus.png"
        elif info_str == 4:
            info_tab.image = "info4_rus.png"
        elif info_str == 5:
            info_tab.image = "info5_rus.png"
        elif info_str == 6:
            info_tab.image = "info6_rus.png"

# Проверка стоимостей и установка нужных значений
def check():
    # Установка хп и стоимости прокачки дома
    if data["house_hp"] > data["health_max"]:
        data["house_hp"] = data["health_max"]
    if upgrade_data["house_level"] == 1:
        if sound_data["texture_mode"] == "normal": # Проверка на тектуры
            house.image = "house1.png"
        elif sound_data["texture_mode"] == "patriot":
            house.image = "house1_patriot.png"
        upgrade_data["house_count"] = 750
        data["health_max"] = 100
        house.pos = (800, 600)
    elif upgrade_data["house_level"] == 2:
        if sound_data["texture_mode"] == "normal": # Проверка на тектуры
            house.image = "house2.png"
        elif sound_data["texture_mode"] == "patriot":
            house.image = "house2_patriot.png"
        upgrade_data["house_count"] = 1500
        data["health_max"] = 250
        house.pos = (800, 570)
    elif upgrade_data["house_level"] == 3:
        if sound_data["texture_mode"] == "normal": # Проверка на тектуры
            house.image = "house3.png"
        elif sound_data["texture_mode"] == "patriot":
            house.image = "house3_patriot.png"
        upgrade_data["house_count"] = 3000
        data["health_max"] = 700
        house.pos = (800, 510)
    elif upgrade_data["house_level"] == 4:
        if sound_data["texture_mode"] == "normal": # Проверка на тектуры
            house.image = "house4.png"
        elif sound_data["texture_mode"] == "patriot":
            house.image = "house4_patriot.png"
        upgrade_data["house_count"] = 6000
        data["health_max"] = 1000
        house.pos = (800, 430)
    # Установка стоимости прокачки левой турели
    if upgrade_data["turret_left_level"] == 0:
        upgrade_data["turret_left_count"] = 100
    elif upgrade_data["turret_left_level"] == 1:
        turret_left.image = "turret_left"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 200
        upgrade_data["couldown_turret_left"] = 100
    elif upgrade_data["turret_left_level"] == 2:
        turret_left.image = "turret_left2"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 400
        upgrade_data["couldown_turret_left"] = 80
    elif upgrade_data["turret_left_level"] == 3:
        turret_left.image = "turret_left3"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 800
        upgrade_data["couldown_turret_left"] = 50
    elif upgrade_data["turret_left_level"] == 4:
        turret_left.image = "turret_left4"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 1600
        upgrade_data["couldown_turret_left"] = 20
    elif upgrade_data["turret_left_level"] == 5:
        turret_left.image = "turret_left5"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 3200
        upgrade_data["couldown_turret_left"] = 8
    elif upgrade_data["turret_left_level"] == 6:
        turret_left.image = "turret_left6"
        turret_left.pos = (600, 630)
        upgrade_data["turret_left_count"] = 6400
        upgrade_data["couldown_turret_left"] = 5
    # Установка стоимости прокачки правой турели
    if upgrade_data["turret_right_level"] == 0:
        upgrade_data["turret_right_count"] = 100
    elif upgrade_data["turret_right_level"] == 1:
        turret_right.image = "turret_right"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 200
        upgrade_data["couldown_turret_right"] = 100
    elif upgrade_data["turret_right_level"] == 2:
        turret_right.image = "turret_right2"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 400
        upgrade_data["couldown_turret_right"] = 80
    elif upgrade_data["turret_right_level"] == 3:
        turret_right.image = "turret_right3"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 800
        upgrade_data["couldown_turret_right"] = 50
    elif upgrade_data["turret_right_level"] == 4:
        turret_right.image = "turret_right4"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 1600
        upgrade_data["couldown_turret_right"] = 20
    elif upgrade_data["turret_right_level"] == 5:
        turret_right.image = "turret_right5"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 3200
        upgrade_data["couldown_turret_right"] = 8
    elif upgrade_data["turret_right_level"] == 6:
        turret_right.image = "turret_right6"
        turret_right.pos = (1000, 630)
        upgrade_data["turret_right_count"] = 6400
        upgrade_data["couldown_turret_right"] = 5
    # Установка хп и стоимости прокачик щита
    if upgrade_data["shield_level"] == 1:
        data["shield_hp_max"] = 10
        upgrade_data["shield_count"] = 100
    elif upgrade_data["shield_level"] == 2:
        data["shield_hp_max"] = 20
        upgrade_data["shield_count"] = 200
    elif upgrade_data["shield_level"] == 3:
        data["shield_hp_max"] = 40
        upgrade_data["shield_count"] = 400
    elif upgrade_data["shield_level"] == 4:
        data["shield_hp_max"] = 80
        upgrade_data["shield_count"] = 800
    elif upgrade_data["shield_level"] == 5:
        data["shield_hp_max"] = 160
        upgrade_data["shield_count"] = 1600
    elif upgrade_data["shield_level"] == 6:
        data["shield_hp_max"] = 320
        upgrade_data["shield_count"] = 3200
    elif upgrade_data["shield_level"] == 7:
        data["shield_hp_max"] = 640
        upgrade_data["shield_count"] = 6400
    # Установка силы и стоимости прокачки курсора
    if upgrade_data["cursor_level"] == 1:
        cursor.image = "cursor"
        data["counter"] = 1
        upgrade_data["cursor_count"] = 500
    elif upgrade_data["cursor_level"] == 2:
        cursor.image = "cursor2"
        data["counter"] = 2
        upgrade_data["cursor_count"] = 2000
    elif upgrade_data["cursor_level"] == 3:
        cursor.image = "cursor3"
        data["counter"] = 4
        upgrade_data["cursor_count"] = 4000
    elif upgrade_data["cursor_level"] == 4:
        cursor.image = "cursor4"
        data["counter"] = 6
        upgrade_data["cursor_count"] = 8000
    elif upgrade_data["cursor_level"] == 5:
        cursor.image = "cursor5"
        data["counter"] = 8
        upgrade_data["cursor_count"] = 16000
    elif upgrade_data["cursor_level"] == 6:
        cursor.image = "cursor6"
        data["counter"] = 10

# Анимация достижений
def achievements_animation():
    global timer_animate
    #Анимация достижения 1
    # Если выполняется достижение, то оно становится навсегда True
    if achievements_data["achievement_counter"] == 1:
        achievements_data["achievements_animate"] = True
        if sound_data["language"] == "eng": # Проверка языка
            achievement_game.image = "achievement1"
        elif sound_data["language"] == "rus":
            achievement_game.image = "achievement1_rus"
        achievements_data["achievement_counter"] += 1
    # Если оно = True, то картинка меняется
    if achievements_data["achievement1"] == True:
        if sound_data["language"] == "eng": # Проверка языка
            achievement1.image = "achievement1"
        elif sound_data["language"] == "rus":
            achievement1.image = "achievement1_rus"
    else:
        achievement1.image = "achievement_lock"
    # Ну и анимация при выполнении достижения
    if achievements_data["achievements_animate"] == True and achievements_data["achievement1"] == False:
        if timer_animate == False:
            animate(achievement_game, tween='decelerate', duration=1, x = 1350)
            timer_animate = True
        elif timer_animate == True and couldown_animate <= 0:
            animate(achievement_game, tween='decelerate', duration=1, x = 1950)
            achievements_data["achievement1"] = True
            achievements_data["achievements_animate"] = False
            timer_animate = False

    #Анимация достижения 2
    # Если выполняется достижение, то оно становится навсегда True
    if achievements_data["achievement2_counter"] == 1:
        achievements_data["achievements_animate"] = True
        if sound_data["language"] == "eng": # Проверка языка
            achievement_game.image = "achievement2"
        elif sound_data["language"] == "rus":
            achievement_game.image = "achievement2_rus"
        achievements_data["achievement2_counter"] += 1
    # Если оно = True, то картинка меняется
    if achievements_data["achievement2"] == True:
        if sound_data["language"] == "eng": # Проверка языка
            achievement2.image = "achievement2"
        elif sound_data["language"] == "rus":
            achievement2.image = "achievement2_rus"
    else:
        achievement2.image = "achievement_lock"
    # Ну и анимация при выполнении достижения
    if achievements_data["achievements_animate"] == True and achievements_data["achievement2"] == False:
        if timer_animate == False:
            animate(achievement_game, tween='decelerate', duration=1, x = 1350)
            timer_animate = True
        elif timer_animate == True and couldown_animate <= 0:
            animate(achievement_game, tween='decelerate', duration=1, x = 1950)
            achievements_data["achievement2"] = True
            achievements_data["achievements_animate"] = False
            timer_animate = False

    #Анимация достижения 3
    # Если выполняется достижение, то оно становится навсегда True
    if achievements_data["achievement_counter"] == 1000:
        achievements_data["achievements_animate"] = True
        if sound_data["language"] == "eng": # Проверка языка
            achievement_game.image = "achievement3"
        elif sound_data["language"] == "rus":
            achievement_game.image = "achievement3_rus"
        achievements_data["achievement_counter"] += 1
    # Если оно = True, то картинка меняется
    if achievements_data["achievement3"] == True:
        if sound_data["language"] == "eng": # Проверка языка
            achievement3.image = "achievement3"
        elif sound_data["language"] == "rus":
            achievement3.image = "achievement3_rus"
    else:
        achievement3.image = "achievement_lock"
    # Ну и анимация при выполнении достижения
    if achievements_data["achievements_animate"] == True and achievements_data["achievement3"] == False:
        if timer_animate == False:
            animate(achievement_game, tween='decelerate', duration=1, x = 1350)
            timer_animate = True
        elif timer_animate == True and couldown_animate <= 0:
            animate(achievement_game, tween='decelerate', duration=1, x = 1950)
            achievements_data["achievement3"] = True
            achievements_data["achievements_animate"] = False
            timer_animate = False

    #Анимация достижения 4
    # Если выполняется достижение, то оно становится навсегда True
    if achievements_data["achievement_counter"] == 100000:
        achievements_data["achievements_animate"] = True
        if sound_data["language"] == "eng": # Проверка языка
            achievement_game.image = "achievement4"
        elif sound_data["language"] == "rus":
            achievement_game.image = "achievement4_rus"
        achievements_data["achievement_counter"] += 1
    # Если оно = True, то картинка меняется
    if achievements_data["achievement4"] == True:
        if sound_data["language"] == "eng": # Проверка языка
            achievement4.image = "achievement4"
        elif sound_data["language"] == "rus":
            achievement4.image = "achievement4_rus"
    else:
        achievement4.image = "achievement_lock"
    # Ну и анимация при выполнении достижения
    if achievements_data["achievements_animate"] == True and achievements_data["achievement4"] == False:
        if timer_animate == False:
            animate(achievement_game, tween='decelerate', duration=1, x = 1350)
            timer_animate = True
        elif timer_animate == True and couldown_animate <= 0:
            animate(achievement_game, tween='decelerate', duration=1, x = 1950)
            achievements_data["achievement4"] = True
            achievements_data["achievements_animate"] = False
            timer_animate = False

    #Анимация достижения 5
    # Если выполняется достижение, то оно становится навсегда True
    if achievements_data["achievement_counter"] == 1000000:
        achievements_data["achievements_animate"] = True
        if sound_data["language"] == "eng": # Проверка языка
            achievement_game.image = "achievement5"
        elif sound_data["language"] == "rus":
            achievement_game.image = "achievement5_rus"
        achievements_data["achievement_counter"] += 1
    # Если оно = True, то картинка меняется
    if achievements_data["achievement5"] == True:
        if sound_data["language"] == "eng": # Проверка языка
            achievement5.image = "achievement5"
        elif sound_data["language"] == "rus":
            achievement5.image = "achievement5_rus"
    else:
        achievement5.image = "achievement_lock"
    # Ну и анимация при выполнении достижения
    if achievements_data["achievements_animate"] == True and achievements_data["achievement5"] == False:
        if timer_animate == False:
            animate(achievement_game, tween='decelerate', duration=1, x = 1350)
            timer_animate = True
        elif timer_animate == True and couldown_animate <= 0:
            animate(achievement_game, tween='decelerate', duration=1, x = 1950)
            achievements_data["achievement5"] = True
            achievements_data["achievements_animate"] = False
            timer_animate = False


# Колизия
def collision():
    global boss1_hp, couldown_shield
    # В режиме раунда
    if mode == "go":
        # Босс
        if house.colliderect(boss1): # если сталкивается с домом
            data["house_hp"] -= boss1_hp
            if boss1_side == 1:
                boss1.x = -100
            elif boss1_side == 2:
                boss1.x = 1700
            boss1_hp = 0
        for j in range(len(bullets_left)): # если сталкивается с пулями слева
            if bullets_left[j].colliderect(boss1):
                if data["money"] < 99999:
                    data["money"] += 1
                    achievements_data["achievement_counter"] += 1
                boss1_hp -= 1
                if sound_data["mob_switch"] == True:
                    sounds.die_boss1.play()
                bullets_left.pop(j)
                break
        for j in range(len(bullets_right)): # если сталкивается справа
            if bullets_right[j].colliderect(boss1):
                if data["money"] < 99999:
                    data["money"] += 1
                    achievements_data["achievement_counter"] += 1
                boss1_hp -= 1
                if sound_data["mob_switch"] == True:
                    sounds.die_boss1.play()
                bullets_right.pop(j)
                break
        # Враги слева
        for i in range(len(enemies_r)):
            if house.colliderect(enemies_r[i]): # если сталкиваются с домом
                data["house_hp"] -= 1
                enemies_r.pop(i)
                new_enemy_r()
                break
            if shield_l.colliderect(enemies_r[i]): # если сталкиваются с левым щитом
                if data["money"] < 99999:
                    data["money"] += 1
                    achievements_data["achievement_counter"] += 1
                data["shield_hp"] -= 1
                enemies_r.pop(i)
                if sound_data["mob_switch"] == True:
                    sounds.die.play()
                new_enemy_r()
                break
            for j in range(len(bullets_left)): # если сталкиваются с пулями слева
                if bullets_left[j].colliderect(enemies_r[i]):
                    if data["money"] < 99999:
                        data["money"] += 1
                        achievements_data["achievement_counter"] += 1
                    enemies_r.pop(i)
                    if sound_data["mob_switch"] == True:
                        sounds.die.play()
                    bullets_left.pop(j)
                    new_enemy_r()
                    break  
        # Враги справа
        for i in range(len(enemies_l)):
            if house.colliderect(enemies_l[i]): # если сталкиваются с домом
                data["house_hp"] -= 1
                enemies_l.pop(i)
                new_enemy_l()
                break
            if shield_r.colliderect(enemies_l[i]): # если сталкиваются с правым щитом
                if data["money"] < 99999:
                    data["money"] += 1
                    achievements_data["achievement_counter"] += 1
                data["shield_hp"] -= 1   
                enemies_l.pop(i)
                if sound_data["mob_switch"] == True:
                    sounds.die.play()
                new_enemy_l()
                break
            for j in range(len(bullets_right)): # если сталкиваются с пулями справа
                if bullets_right[j].colliderect(enemies_l[i]):
                    if data["money"] < 99999:
                        data["money"] += 1
                        achievements_data["achievement_counter"] += 1
                    enemies_l.pop(i)
                    if sound_data["mob_switch"] == True:
                        sounds.die.play()
                    bullets_right.pop(j)
                    new_enemy_l()
                    break
     
            
# Обновление
def update(dt):
    global mode, enemies_l, enemies_r, bullet_right, bullet_left, achievements_animate, bullets_right, bullets_left
    global play1, updateb1, shop1, settings1, titles1, start1, achievements1, ban, game_over
    global timer, boss1_hp,  couldown_shield, timer_turret_left, timer_turret_right, couldown_turret_left, couldown_turret_right, timer_animate
    # Функции которые должны работать постоянно
    house_die()
    language()
    texture()
    achievements_animation()
    check()
    collision()
    timer1()
    timer1_turret_left()
    timer1_turret_right()
    timer1_animate()
    timer1_end()
    # Анимация флага
    if mode == "menu" or mode == "settings" or mode == "titles" or mode == "achievements":
        if sound_data["texture_mode"] == "normal":
            flag_menu.animate()
        elif sound_data["texture_mode"] == "patriot":
            flag_menu_patriot.animate()
        logo_game.animate()
    # Анимация в режиме раунда
    elif mode == "go":
        boss1.animate()
        enemy_r_ship()
        enemy_l_ship()
        # Проверка существования турелей
        if upgrade_data["turret_left_level"] >= 1:
            timer_turret_left = True
            # Движение пули 
            for i in range(len(bullets_left)):
                if bullets_left[i].x < -100:
                    bullets_left.pop(i)
                    break
                else:
                    bullets_left[i].x -= 10
        if upgrade_data["turret_right_level"] >= 1:
            timer_turret_right = True
            # Движение пули 
            for i in range(len(bullets_right)):
                if bullets_right[i].x > 1700:
                    bullets_right.pop(i)
                    break
                else:
                    bullets_right[i].x += 10
        # Проверка волны для босса
        if data["wave"]%2 == 0 and couldown <= 20 and boss1_hp > 0:
            if boss1_side == 1:
                boss1.x += 0.5
            else:
                boss1.x -= 0.5
        elif boss1_hp <= 0:
            if boss1_side == 1:
                boss1.x = -100
            elif boss1_side == 2:
                boss1.x = 1700
            if achievements_data["achievement2"] == False:
                achievements_data["achievement2_counter"] += 1

    # Если таймер раунда закончился
    if couldown <= 0:
        mode = "play"
        music1()
        data["wave_enemies"] += 1
        data["boss_health_max"] += 25
        boss1_hp = data["boss_health_max"]
        timer = False
        enemies_r = []
        enemies_l = []
        bullets_right = []
        bullet_left = []

        # Я не знаю зачем это тут, так надо :D

        #for i in range(len(enemies_r)):
            #enemies_r.pop(i)
            #new_enemy_r()
            #enemies_r[i].x = -100
        #for i in range(len(enemies_l)):
            #enemies_l.pop(i)
            #new_enemy_l()
            #enemies_l[i].x = 1700

        with open('data.txt', 'w') as dataa:
            json.dump(data, dataa)
        with open('sound_data.txt', 'w') as dataaa:
            json.dump(sound_data, dataaa)
        with open('shop_data.txt', 'w') as dataaaa:
            json.dump(shop_data, dataaaa)
        with open('upgrade_data.txt', 'w') as dataaaaa:
            json.dump(upgrade_data, dataaaaa)
        with open('achievements_data.txt', 'w') as dataaaaaa:
            json.dump(achievements_data, dataaaaaa)

    # Смерть щита
    if data["shield_hp"] <= 0:
        shop_data["shield_switch"] = False
        shield_r.pos = (3000, 600)
        shield_l.pos = (3000, 600)
        if mode == "go":
            if sound_data["sound_switch"] == True:
                sounds.shield_down.play()
        data["shield_hp"] = data["shield_hp_max"]
    if shop_data["shield_switch"] == True: # возвращение в магазин
        shield_l.pos = (650, 600)
        shield_r.pos = (950, 600)

    # Проверка значений по режиму
    if mode == "play":
        couldown_shield = 0
        timer = False
        boss1_hp = data["boss_health_max"]

    # Выстрел пуль
    if mode == "go" and couldown_turret_left <= 0:
        bullet_left = Actor("bullet_left.png")
        bullet_left.pos = turret_left.pos
        bullets_left.append(bullet_left)
        couldown_turret_left = upgrade_data["couldown_turret_left"]
    if mode == "go" and couldown_turret_right <= 0:
        bullet_right = Actor("bullet_right.png")
        bullet_right.pos = turret_right.pos
        bullets_right.append(bullet_right)
        couldown_turret_right = upgrade_data["couldown_turret_right"]

    # Проверка бана или тип того (Понятия не имею зачем его добавила)
    if data["money"] > 99999 or shop_data["health_small"] > 99:
        mode = "ban"
    if mode == "ban":
        ban_hand.animate()


# Курсор мыши
def on_mouse_move(pos): 
    cursor.pos = pos
    global button_press
    # Кнопки в меню
    if mode == "menu": 
        # если курсор на кнопке Играть
        if play.collidepoint(pos) and button_press == 0: 
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(play, tween="decelerate", duration=0.25, y = 190 - 10)
            animate(play1, tween="decelerate", duration=0.25, y = 190 - 10)
            button_press = 'play'
        elif button_press == 'play' and not play.collidepoint(pos): # если НЕТ
            animate(play, tween='decelerate', duration=0.25, y = 180 + 10)
            animate(play1, tween='decelerate', duration=0.25, y = 180 + 10)
            button_press = 0
        # если курсор на кнопке Настройки
        if settings.collidepoint(pos) and button_press == 0: 
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(settings, tween="decelerate", duration=0.25, y = 360 - 10)
            animate(settings1, tween="decelerate", duration=0.25, y = 360 - 10)
            button_press = 'settings'
        elif button_press == 'settings' and not settings.collidepoint(pos): # если НЕТ
            animate(settings, tween='decelerate', duration=0.25, y = 350 + 10)
            animate(settings1, tween='decelerate', duration=0.25, y = 350 + 10)
            button_press = 0
        # если курсор на кнопке Кредиты
        if titles.collidepoint(pos) and button_press == 0: 
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(titles, tween="decelerate", duration=0.25, y = 530 - 10)
            animate(titles1, tween="decelerate", duration=0.25, y = 530 - 10)
            button_press = 'titles'
        elif button_press == 'titles' and not titles.collidepoint(pos): # если НЕТ
            animate(titles, tween='decelerate', duration=0.25, y = 520 + 10)
            animate(titles1, tween='decelerate', duration=0.25, y = 520 + 10)
            button_press = 0
        # если курсор на кнопке Достижения 
        if achievements.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(achievements, tween="decelerate", duration=0.25, y = 700 - 10)
            animate(achievements1, tween="decelerate", duration=0.25, y = 700 - 10)
            button_press = 'achievements'
        elif button_press == 'achievements' and not achievements.collidepoint(pos): # если НЕТ
            animate(achievements, tween='decelerate', duration=0.25, y = 690 + 10)
            animate(achievements1, tween='decelerate', duration=0.25, y = 690 + 10)
            button_press = 0

    # Кнопки в настроках
    elif mode == "settings":
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0
    elif mode == "titles": 
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0

    # Кнопки в режиме перед игрой
    elif mode == "play": 
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0
        # если курсор на кнопке Улучшить
        if updateb.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(updateb, tween="decelerate", duration=0.25, y = 120 - 10)
            animate(updateb1, tween="decelerate", duration=0.25, y = 120 - 10)
            button_press = 'upgrade'
        elif button_press == 'upgrade' and not updateb.collidepoint(pos): # если НЕТ
            animate(updateb, tween='decelerate', duration=0.25, y = 110 + 10)
            animate(updateb1, tween='decelerate', duration=0.25, y = 110 + 10)
            button_press = 0
        # если курсор на кнопке Магазин
        if shop.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(shop, tween="decelerate", duration=0.25, y = 120 - 10)
            animate(shop1, tween="decelerate", duration=0.25, y = 120 - 10)
            button_press = 'shop'
        elif button_press == 'shop' and not shop.collidepoint(pos): # если НЕТ
            animate(shop, tween='decelerate', duration=0.25, y = 110 + 10)
            animate(shop1, tween='decelerate', duration=0.25, y = 110 + 10)
            button_press = 0
        # если курсор на кнопке Начать
        if start.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(start, tween="decelerate", duration=0.25, y = 120 - 10)
            animate(start1, tween="decelerate", duration=0.25, y = 120 - 10)
            button_press = 'start'
        elif button_press == 'start' and not start.collidepoint(pos): # если НЕТ
            animate(start, tween='decelerate', duration=0.25, y = 110 + 10)
            animate(start1, tween='decelerate', duration=0.25, y = 110 + 10)
            button_press = 0
        # если курсор на кнопке Инфо
        if info.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            animate(info, tween="decelerate", duration=0.25, y = 800 - 10)
            button_press = 'info'
        elif button_press == 'info' and not info.collidepoint(pos): # если НЕТ
            animate(info, tween='decelerate', duration=0.25, y = 790 + 10)
            button_press = 0

    # Кнопки в режиме магазина
    elif mode == "shop":
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0
        # если курсор на кнопке покупки фул лечения
        if health_shop_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "health_shop_button"
        elif not health_shop_button.collidepoint(pos) and button_press == "health_shop_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке покупки маленького лечения
        if health_small_shop_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "health_small_shop_button"
        elif not health_small_shop_button.collidepoint(pos) and button_press == "health_small_shop_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке покупки щита
        if shield_shop_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "shield_shop_button"
        elif not shield_shop_button.collidepoint(pos) and button_press == "shield_shop_button": # если НЕТ
            button_press = 0

    # Кнопки в режиме улучшений
    elif mode == "upgrade":
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0
        # если курсор на улучшении дома
        if house_upgrade_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "house_upgrade_button"
        elif not house_upgrade_button.collidepoint(pos) and button_press == "house_upgrade_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке улучшения левой турели
        if turret_left_upgrade_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "turret_left_upgrade_button"
        elif not turret_left_upgrade_button.collidepoint(pos) and button_press == "turret_left_upgrade_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке улучшения правой турели
        if turret_right_upgrade_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "turret_right_upgrade_button"
        elif not turret_right_upgrade_button.collidepoint(pos) and button_press == "turret_right_upgrade_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке улучшения курсора
        if cursor_shop_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "cursor_shop_button"
        elif not cursor_shop_button.collidepoint(pos) and button_press == "cursor_shop_button": # если НЕТ
            button_press = 0
        # если курсор на кнопке улучшения щита
        if shield_upgrade_button.collidepoint(pos) and button_press == 0:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "shield_upgrade_button"
        elif not shield_upgrade_button.collidepoint(pos) and button_press == "shield_upgrade_button": # если НЕТ
            button_press = 0

    # Кнопки в достижениях
    elif mode == "achievements":
        # если курсор на кнопке Назад
        if arrow.collidepoint(pos) and button_press == 0: 
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            button_press = "arrow"
        elif not arrow.collidepoint(pos) and button_press == "arrow": # если НЕТ
            button_press = 0

# Нажатие кнопок мыши
def on_mouse_down(button, pos): 
    global mode, button_press, timer, setting_mode, boss1_hp, info_str
    # Кнопки в меню
    if button == mouse.LEFT and mode == "menu":
        # если нажата кнопка Настройки
        if settings.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "settings"
            button_press = 0
        # если нажата кнопка Играть
        elif play.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "play"
            button_press = 0
        # если нажата кнопка Кредиты
        elif titles.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "titles"
            button_press = 0
        # если нажата кнопка Достижения
        elif achievements.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "achievements"
            button_press = 0
    # Кнопки в настройках
    elif button == mouse.LEFT and mode == "settings":
        # Настройки звуков
        if setting_mode == "music":
            # Психоделика с шкалой громкости звука
            if arrow_music_l.collidepoint(pos) and sound_data["volume1"] == 1:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.75)
                music_cursor.x = 1105
                sound_data["volume1"] = 0.75
            elif arrow_music_l.collidepoint(pos) and sound_data["volume1"] == 0.75:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.5)
                music_cursor.x = 1005
                sound_data["volume1"] = 0.5
            elif arrow_music_l.collidepoint(pos) and sound_data["volume1"] == 0.5:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.25)
                music_cursor.x = 905
                sound_data["volume1"] = 0.25
            elif arrow_music_l.collidepoint(pos) and sound_data["volume1"] == 0.25:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0)
                music_cursor.x = 795
                sound_data["volume1"] = 0
            elif arrow_music_r.collidepoint(pos) and sound_data["volume1"] == 0:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.25)
                music_cursor.x = 905
                sound_data["volume1"] = 0.25
            elif arrow_music_r.collidepoint(pos) and sound_data["volume1"] == 0.25:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.5)
                music_cursor.x = 1005
                sound_data["volume1"] = 0.5
            elif arrow_music_r.collidepoint(pos) and sound_data["volume1"] == 0.5:
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(0.75)
                music_cursor.x = 1105
                sound_data["volume1"] = 0.75
            elif arrow_music_r.collidepoint(pos) and sound_data["volume1"] == 0.75: 
                if sound_data["sound_switch"] == True:
                    sounds.button1.play()
                music.set_volume(1)
                music_cursor.x = 1205
                sound_data["volume1"] = 1
            
            # если переключатель доп. звуков включен
            if switch1.collidepoint(pos) and sound_data["sound_switch"] == True:
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch1.image = "switch_off"
                sound_data["sound_switch"] = False
            elif switch1.collidepoint(pos) and sound_data["sound_switch"] == False: # если НЕТ
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch1.image = "switch_on"
                sound_data["sound_switch"] = True
            # если переключатель звуков существ включен
            elif switch2.collidepoint(pos) and sound_data["mob_switch"] == True:
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch2.image = "switch_off"
                sound_data["mob_switch"] = False
            elif switch2.collidepoint(pos) and sound_data["mob_switch"] == False: # если НЕТ
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch2.image = "switch_on"
                sound_data["mob_switch"] = True
        
        # Настройки графики
        if setting_mode == "grafic":
            # Психоделика с шкалой языков
            if arrow_music_l.collidepoint(pos) and sound_data["language"] == "eng":
                sound_data["language"] = "rus"
            elif arrow_music_l.collidepoint(pos) and sound_data["language"] == "rus":
                sound_data["language"] = "eng"
            elif arrow_music_r.collidepoint(pos) and sound_data["language"] == "rus":
                sound_data["language"] = "eng"
            elif arrow_music_r.collidepoint(pos) and sound_data["language"] == "eng":
                sound_data["language"] = "rus"
            
            # если переключатель режима патриота
            elif switch3.collidepoint(pos) and sound_data["texture_mode"] == "patriot":
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch3.image = "switch_off"
                sound_data["texture_mode"] = "normal"
                if data["money"] < 99999 or shop_data["health_small"] < 99 and sound_data["texture_mode"] == "normal":
                    music.play('lobby')  
                if data["money"] > 99999 or shop_data["health_small"] > 99 and sound_data["texture_mode"] == "normal":
                    sound_data["volume1"] = 1
                    music.play("lobby_ban")
            elif switch3.collidepoint(pos) and sound_data["texture_mode"] == "normal":
                if sound_data["sound_switch"] == True:
                    sounds.button.play()
                switch3.image = "switch_on"
                sound_data["texture_mode"] = "patriot"
                if sound_data["texture_mode"] == "patriot":
                    music.play("patriot")

        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "menu"
            button_press = 0
            with open('data.txt', 'w') as dataa:
                json.dump(data, dataa)
            with open('sound_data.txt', 'w') as dataaa:
                json.dump(sound_data, dataaa)
            with open('shop_data.txt', 'w') as dataaaa:
                json.dump(shop_data, dataaaa)
            with open('upgrade_data.txt', 'w') as dataaaaa:
                json.dump(upgrade_data, dataaaaa)
            with open('achievements_data.txt', 'w') as dataaaaaa:
                json.dump(achievements_data, dataaaaaa)
        
        # Психоделика с шкалой меню настроек
        if arrow_setting_r.collidepoint(pos) and setting_mode == "music":
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            setting_mode = "grafic"
        elif arrow_setting_r.collidepoint(pos) and setting_mode == "grafic":
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            setting_mode = "music"
        elif arrow_setting_l.collidepoint(pos) and setting_mode == "grafic":
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            setting_mode = "music"
        elif arrow_setting_l.collidepoint(pos) and setting_mode == "music":
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            setting_mode = "grafic"

    # Кнопки в режиме с разрабом и т.д.
    elif button == mouse.LEFT and mode == "titles":
        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "menu"
            button_press = 0

    # Кнопки в режиме перед раундом
    elif button == mouse.LEFT and mode == "play":
        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "menu"
            button_press = 0
            with open('data.txt', 'w') as dataa:
                json.dump(data, dataa)
            with open('sound_data.txt', 'w') as dataaa:
                json.dump(sound_data, dataaa)
            with open('shop_data.txt', 'w') as dataaaa:
                json.dump(shop_data, dataaaa)
            with open('upgrade_data.txt', 'w') as dataaaaa:
                json.dump(upgrade_data, dataaaaa)
            with open('achievements_data.txt', 'w') as dataaaaaa:
                json.dump(achievements_data, dataaaaaa)
            
        # если нажата кнопка Начать
        elif start.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "go"
            button_press = 0
            music1()
            data["wave"] += 1
            for i in range(data["wave_enemies"]):
                new_enemy_r()
                new_enemy_l()
            timer = True
        # если нажата кнопка Магазин
        elif shop.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "shop"
            button_press = 0
        # если нажата кнопка Улучшить
        elif updateb.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "upgrade"
            button_press = 0
        # если нажата кнопка Инфо
        elif info.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "info"
            button_press = 0
    # Кнопки в магазине
    elif button == mouse.LEFT and mode == "shop":
        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "play"
            button_press = 0
            with open('data.txt', 'w') as dataa:
                json.dump(data, dataa)
            with open('sound_data.txt', 'w') as dataaa:
                json.dump(sound_data, dataaa)
            with open('shop_data.txt', 'w') as dataaaa:
                json.dump(shop_data, dataaaa)
            with open('upgrade_data.txt', 'w') as dataaaaa:
                json.dump(upgrade_data, dataaaaa)
            with open('achievements_data.txt', 'w') as dataaaaaa:
                json.dump(achievements_data, dataaaaaa)
        # если нажата кнопка покупки фул лечения
        elif health_shop_button.collidepoint(pos) and data["money"] >= 1000:
            button_press = 0
            if data["house_hp"] != data["health_max"]:
                if sound_data["sound_switch"] == True:
                    sounds.buy.play()
                health_plus = data["health_max"] - data["house_hp"]
                data["house_hp"] += health_plus
                data["money"] -= 100
        # если нажата кнопка покупки малого лечения
        elif health_small_shop_button.collidepoint(pos) and data["money"] >= 50 and shop_data["health_small"] < 99:
            button_press = 0
            if sound_data["sound_switch"] == True:
                sounds.buy.play()
            shop_data["health_small"] += 1
            data["money"] -= 50
        # если нажата кнопка покупки щита
        elif shield_shop_button.collidepoint(pos) and data["money"] >= 500 and shop_data["shield_switch"] == False:
            button_press = 0
            if sound_data["sound_switch"] == True:
                sounds.buy.play()
            shop_data["shield_switch"] = True
            data["money"] -= 500
        # если нажата кнопка покупки левой турели
        elif turret_left_shop_button.collidepoint(pos) and data["money"] >= upgrade_data["turret_left_count"]:
            if upgrade_data["turret_left_level"] == 0:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["turret_left_count"]
                upgrade_data["turret_left_level"] += 1
        # если нажата кнопка покупки правой турели
        elif turret_right_shop_button.collidepoint(pos) and data["money"] >= upgrade_data["turret_right_count"]:
            if upgrade_data["turret_right_level"] == 0:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["turret_right_count"]
                upgrade_data["turret_right_level"] += 1

    # Кнопки в Обучении
    elif button == mouse.LEFT and mode == "info":
        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            mode = "play"
            info_str = 1
        # Психоделика со страницами обучения
        if arrow_info_r.collidepoint(pos) and info_str == 1:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 2
        elif arrow_info_r.collidepoint(pos) and info_str == 2:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 3
        elif arrow_info_r.collidepoint(pos) and info_str == 3:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 4
        elif arrow_info_r.collidepoint(pos) and info_str == 4:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 5
        elif arrow_info_r.collidepoint(pos) and info_str == 5:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 6
        elif arrow_info_l.collidepoint(pos) and info_str == 6:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 5
        elif arrow_info_l.collidepoint(pos) and info_str == 5:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 4
        elif arrow_info_l.collidepoint(pos) and info_str == 4:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 3
        elif arrow_info_l.collidepoint(pos) and info_str == 3:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 2
        elif arrow_info_l.collidepoint(pos) and info_str == 2:
            if sound_data["sound_switch"] == True:
                sounds.button1.play()
            info_str = 1

    # Кнопки в режиме улучшения
    elif button == mouse.LEFT and mode == "upgrade":
        # если нажата кнопка улучшения дома
        if house_upgrade_button.collidepoint(pos) and data["money"] >= upgrade_data["house_count"]:
            if upgrade_data["house_level"] == 1:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["house_count"]
                upgrade_data["house_level"] += 1
                data["health_max"] = 250
                data["house_hp"] = data["health_max"]
            elif upgrade_data["house_level"] == 2:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["house_count"]
                upgrade_data["house_level"] += 1
                data["health_max"] = 700
                data["house_hp"] = data["health_max"]
            elif upgrade_data["house_level"] == 3:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["house_count"]
                upgrade_data["house_level"] += 1
                data["health_max"] = 1000
                data["house_hp"] = data["health_max"]
        # если нажата кнопка левой турели
        elif turret_left_upgrade_button.collidepoint(pos) and data["money"] >= upgrade_data["turret_left_count"]:
            if upgrade_data["turret_left_level"] != 6 and upgrade_data["turret_left_level"] >= 1:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["turret_left_count"]
                upgrade_data["turret_left_level"] += 1
        # если нажата кнопка правой турели
        elif turret_right_upgrade_button.collidepoint(pos) and data["money"] >= upgrade_data["turret_right_count"]:
            if upgrade_data["turret_right_level"] != 6 and upgrade_data["turret_right_level"] >= 1:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["turret_right_count"]
                upgrade_data["turret_right_level"] += 1
        # если нажата кнопка улучшения курсора
        elif cursor_shop_button.collidepoint(pos) and data["money"] >= upgrade_data["cursor_count"]:
            if upgrade_data["cursor_level"] != 6:
                button_press = 0
                if sound_data["sound_switch"] == True:
                    sounds.upgradebuy.play()
                data["money"] -= upgrade_data["cursor_count"]
                upgrade_data["cursor_level"] += 1
        # если нажата кнопка улучшения щита
        elif shield_upgrade_button.collidepoint(pos) and data["money"] >= upgrade_data["shield_count"] and upgrade_data["shield_count"] != 6400:
            button_press = 0
            if sound_data["sound_switch"] == True:
                sounds.upgradebuy.play()
            data["money"] -= upgrade_data["shield_count"]
            upgrade_data["shield_count"] *= 2
            data["shield_hp_max"] *= 2
            upgrade_data["shield_level"] += 1
            data["shield_hp"] = data["shield_hp_max"]
        # если нажата кнопка Назад
        elif arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "play"
            button_press = 0
            with open('data.txt', 'w') as dataa:
                json.dump(data, dataa)
            with open('sound_data.txt', 'w') as dataaa:
                json.dump(sound_data, dataaa)
            with open('shop_data.txt', 'w') as dataaaa:
                json.dump(shop_data, dataaaa)
            with open('upgrade_data.txt', 'w') as dataaaaa:
                json.dump(upgrade_data, dataaaaa)
            with open('achievements_data.txt', 'w') as dataaaaaa:
                json.dump(achievements_data, dataaaaaa)
    
    # Кнопки в Достижениях
    elif button == mouse.LEFT and mode == "achievements":
        # если нажата кнопка Назад
        if arrow.collidepoint(pos):
            if sound_data["sound_switch"] == True:
                sounds.button.play()
            restart()
            mode = "menu"
            button_press = 0
        
    # Кнопки в режиме раунда
    elif button == mouse.LEFT and mode == "go":
        # Нажатие на левых врагов
        for i in range(len(enemies_l)):
            if enemies_l[i].collidepoint(pos):
                if data["money"] < 99999: # Проверка денег
                    data["money"] += data["counter"]
                    achievements_data["achievement_counter"] += data["counter"]
                enemies_l.pop(i)
                if sound_data["mob_switch"] == True:
                    sounds.die.play()
                new_enemy_l()
                break
        # Нажатие на правых врагов
        for i in range(len(enemies_r)):
            if enemies_r[i].collidepoint(pos):
                if data["money"] < 99999: # Проверка денег
                    data["money"] += data["counter"]
                    achievements_data["achievement_counter"] += data["counter"]
                enemies_r.pop(i)
                if sound_data["mob_switch"] == True:
                    sounds.die.play()
                new_enemy_r()
                break
        # Нажатие на босса
        if boss1.collidepoint(pos): 
            if data["money"] < 99999: # Проверка денег
                data["money"] += data["counter"]
                achievements_data["achievement_counter"] += data["counter"]
            boss1_hp -= data["counter"]
            if sound_data["mob_switch"] == True:
                sounds.die_boss1.play()
                

# Нажатие клавиш на клавиатуре
def on_key_down(key):
    global button_press
    # Фул скрин
    if keyboard.f:
        toggle_fullscreen()
    # В режиме раунда
    if mode == "go":
        # Использование малого лечения
        if keyboard.Q and shop_data["health_small"] >= 1 and data["house_hp"] < data["health_max"]:
            button_press = 0
            if sound_data["sound_switch"] == True:
                sounds.boost.play()
            shop_data["health_small"] -= 1
            if data["house_hp"] != data["health_max"]:
                data["house_hp"] += 10
    

pgzrun.go()
