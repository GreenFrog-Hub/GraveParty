import os.path
from random import randint

import DeadPerson
import GraveyardEnv
import StartMenu
from pygame import mixer

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#PRESS ESC TO QUIT

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    people = StartMenu.getData()
    Env = GraveyardEnv.GraveyardEnv()
    Env.setBackground(os.path.join("Assets","Background.png"))
    mixer.init()
    mixer.music.load("Dead Man’s Dancefloor.wav")
    mixer.music.play(-1)
    for i in people:
        Env.addDeadPerson(DeadPerson.DeadPerson((i),1,1,[],(randint(500,1400),randint(400,900))))
    # person = DeadPerson.DeadPerson("George",1,1,[], (400,600))
    # person2 = DeadPerson.DeadPerson("Bob",1,1,[], (600,600))
    # Env.addDeadPerson(person)
    # Env.addDeadPerson(person2)
    Env.startMainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
