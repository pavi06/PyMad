import random
import pyautogui as pg

import time

animal=('monkey','donkey','dog','pig','buffalloooo','pisasu','panni','eruma madu','paithiyam')
time.sleep(8)

for i in range(180):
    a=random.choice(animal)
    pg.write(a)
    pg.press('enter')
