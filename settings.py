from pathlib import Path


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# картинка - бэкграунд
bck_dict = {
    "trees-landscape-mountains-hill-xipu.jpeg" : [650, 350],
    "nature-usa-panoramic-cliff.jpeg" : [700, 350],
    "nature-yosemite-california-usa-lysk.jpeg" : [778, 350],
    "peyzazh-zimoy-sneg.jpg" : [778, 350],
    "fonstola.ru_75196.jpg": [1024, 768],
    "all-alone-in-this-world-grass.jpg": [1100, 850],
    "1654292681_53-celes-club-p-oboi-na-rabochii-stol-standartnie-krasivie-64.jpg" : [1200, 750],
    "1659988991_60-kartinkin-net-p-standartnie-oboi-vindovs-krasivo-63.jpg" : [1200, 750]
}

bckgnd = "1654292681_53-celes-club-p-oboi-na-rabochii-stol-standartnie-krasivie-64.jpg"

# размеры игрового поля
WIDTH = bck_dict[bckgnd][0]
HEIGHT = bck_dict[bckgnd][1]
FPS = 60

images_path = Path(__file__).parent / "img"

gamespeed = 3

heli_pic = "less_til_heli.png"
