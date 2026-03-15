import tkinter as tk
import pygame
from pygame import mixer
import requests

from Scraper import *


class StartMenu:
    def __init__(self):
        self.category = ""
        self.showChoice = ""
        self.scraper = Scraper()

    def onButtonClick(self):

        self.category = self.selectedOption.get()
        self.showChoice = self.showChoiceInput.get()
        if self.showChoice != "":
            nextUrl = self.scraper.findMediaTitle(
            f"https://cinemorgue.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:{self.category}&cmsort=sortkey&cmstartsortkeyprefix={self.showChoice[0].upper()}&cmlimit=max&format=json",
            self.showChoice)
            if nextUrl != None:
                if self.scraper.findPeople(f"https://cinemorgue.fandom.com/api.php?action=query&titles={nextUrl}&prop=revisions&rvprop=content&formatversion=2&format=json"):
                    position = pygame.mixer.music.get_pos()
                    self.gui.destroy()
                    #print(self.category)
                    #print(self.showChoice)
                else:
                    self.categoryLabel.config(text = "Invalid entry made, please choose a different show")
            else:
                self.categoryLabel.config(text = "The show was not found, please try again")


def main(s):
    # create the window
    s.gui = tk.Tk()
    s.gui.title("StartMenu")
    s.gui.geometry = ("500 * 500")

    # add the label
    s.categoryLabel = tk.Label(s.gui, text = "enter Category choices")
    s.categoryLabel.pack()
    options = ["Films" , "TV_Series" , "Video_Games", "Anime_TV_Series"]
    s. selectedOption = tk.StringVar()
    s. selectedOption.set(options[0])
    dropdown = tk.OptionMenu(s.gui, s.selectedOption, *options)
    dropdown.pack()
    s.showChoiceInput = tk.Entry(s.gui)
    s.showChoiceInput.pack()
    s.startButton = tk.Button(s.gui, text = "Start", command=s.onButtonClick)
    s.startButton.pack()
    mixer.init()
    mixer.music.load("Dead Man’s Dancefloormuffled.wav")
    mixer.music.play(-1)
    s.gui.mainloop()

def getData():
    s = StartMenu()
    main(s)
    print(s.category)
    category = s.category
    print(s.showChoice)
    name = s.showChoice
    people = main1(category,name)
    print(people)
    return people

if __name__ == "__main__":
    getData()