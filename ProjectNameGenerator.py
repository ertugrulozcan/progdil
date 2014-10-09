'''
Created on 7 Eki 2014
 
@author: Ahmet Ertugrul Ozcan
'''
 
# -*- coding: cp1254 -*-
 
from _overlapped import NULL
 
names = [
         "anvil",
         "arrow",
         "axe",
         "balloon",
         "baseball",
         "bathtub",
         "bible",
         "bike",
         "bikini",
         "bleach",
         "blouse",
         "blowdryer",
         "book",
         "bookmark",
         "boombox",
         "bottle cap",
         "button",
         "candle",
         "candy wrapper",
         "canvas",
         "card",
         "CD",
         "cha",
         "chainmail",
         "chalk",
         "charger",
         "checkbook",
         "clarinet",
         "clay pot",
         "clock",
         "coffee maker",
         "comb",
         "cookie jar",
         "cork",
         "crayons",
         "credit card",
         "cushion",
         "deodorant",
         "detergent",
         "dice",
         "dollar bill",
         "drum",
         "eraser",
         "eye liner",
         "facewash",
         "flag",
         "flowers",
         "flute",
         "fork",
         "gel",
         "glasses",
         "glowstick",
         "grid paper",
         "hairtie",
         "hanger",
         "hat",
         "helmet",
         "icecube",
         "javelin",
         "keychain",
         "kilt",
         "kite",
         "knife",
         "lace",
         "lamp shade",
         "leg warmers",
         "lip gloss",
         "lotion",
         "mallet",
         "map",
         "microphone",
         "model car",
         "mousepad",
         "nail",
         "needle",
         "outlet",
         "paint brush",
         "passport",
         "pencil",
         "pepperspray",
         "photo album",
         "piano",
         "picture frame",
         "piggy bank",
         "pillow",
         "pool stick",
         "puddle",
         "quilt",
         "radio",
         "receipt",
         "remote control",
         "rock",
         "rope",
         "rubberband",
         "rubber duck",
         "rug",
         "sandpaper",
         "scissors",
         "scotchtape",
         "screw",
         "seatbelt",
         "sharpie",
         "shield",
         "shoelace",
         "shovel",
         "sketchpad",
         "slipper",
         "soap",
         "speakers",
         "spear",
         "sponge",
         "spoon",
         "sticky note",
         "stockings",
         "stone",
         "suitcase",
         "sunglasses",
         "thermometer",
         "thread",
         "tire",
         "tissuebox",
         "tobacco",
         "toothpaste",
         "toothpick",
         "vase",
         "wheelbarrow",
         "whiteout",
         "zipper"]
 
adjectives = ["attractive",
              "average",
              "beautiful",
              "big",
              "broad",
              "broken",
              "bumpy",
              "chubby",
              "clean",
              "colorful",
              "colossal",
              "crooked",
              "curved",
              "cute",
              "damaged",
              "dark",
              "deep",
              "dirty",
              "dry",
              "dull",
              "dusty",
              "fancy",
              "fat",
              "filthy",
              "flat",
              "gigantic",
              "gorgeous",
              "graceful",
              "great",
              "grotesque",
              "high",
              "hollow",
              "huge",
              "large",
              "little",
              "long",
              "mammoth",
              "massive",
              "miniature",
              "misty",
              "muddy",
              "narrow",
              "petite",
              "plain",
              "precious",
              "prickly",
              "puny",
              "quaint",
              "round",
              "scrawny",
              "shallow",
              "shiny",
              "short",
              "skinny",
              "slimy",
              "slippery",
              "small",
              "smooth",
              "soft",
              "steep",
              "sticky",
              "straight",
              "strange",
              "tall",
              "teeny",
              "tiny",
              "ugly",
              "unusual",
              "wide"]
 
def Random(topRange):
    from random import randrange
    return randrange(topRange)
 
class ProjectNameGenerator(object):
    # Kurucu metod - Constructor
    def __init__(self, params):
        print("Yeni bir proje ismi bulmak icin kac adet ornek uretmek istediginizi giriniz;")
        i = int(input())
        self.Generate(i)
        
    def Generate(self, n=None):
        if n is None:
            print(adjectives[Random(len(adjectives))] + " " + names[Random(len(names))])
        else:
            i = 0
            while i < n:
                self.Generate()
                i+=1
 
generator = ProjectNameGenerator(NULL)
