'''
Created on 12 Ekim 2014

@author: Ahmet Ertugrul Ozcan
'''

# -*- coding: cp1254 -*-

import json
from _overlapped import NULL
from pip._vendor.distlib.compat import raw_input
import os
import codecs

words = {"TR" :
         {"names" :
          ["ors",
           "ok",
           "balta",
           "balon",
           "beyzbol",
           "kuvet",
           "inci",
           "bisiklet",
           "bikini",
           "agartici",
           "bluz",
           "sueter",
           "kitap",
           "fare",
           "hoparlor",
           "sise kapagi",
           "dugme",
           "mum",
           "şeker",
           "tuval",
           "kart",
           "CD",
           "cekirdek",
           "zincir",
           "tebesir",
           "depo",
           "cek",
           "klarnet",
           "makine",
           "saat",
           "kahve makinesi",
           "tarak",
           "kavanoz",
           "mantar",
           "pastel boya",
           "kredi karti",
           "minder",
           "deodorant",
           "deterjan", 
           "zar",
           "fatura",
           "davul",
           "silgi",
           "goz",
           "yuz",
           "bayrak",
           "cicek",
           "yiv",
           "catal",
           "jel",
           "gozluk",
           "bilesen",
           "izgara",
           "kagit",
           "aski",
           "sapka",
           "kask",
           "buz",
           "cirit",
           "cep",
           "kilit",
           "ucurtma",
           "bicak",
           "dantel",
           "abajur",
           "cakmak",
           "ruj",
           "losyon",
           "tokmak",
           "harita",
           "mikrofon",
           "model araba",
           "mousepad",
           "civi",
           "igne",
           "outlet",
           "boya fircasi", 
           "pasaport",
           "kalem",
           "spray",
           "fotograf albumu",
           "piyano",
           "resim cercevesi",
           "kumbara",
           "yastik", 
            "havuz sopa", 
            "çiş", 
            "yorgan", 
            "radyo", 
            "makbuz",
            "uzaktan kumanda",
            "kaya", 
            "halat",
            "lastik bant",
            "lastik ördek",
            "halı",
            "zımpara",
            "makas",
            "zımba",
            "vida",
            "Emniyet kemeri",
            "bicak",
            "kalkan",
            "ayakkabı bağı",
            "kürek",
            "defterin",
            "terlik",
            "sabun",
            "hoparlör",
            "mızrak",
            "sünger",
            "kaşık",
            "yapışkan notu",
            "çorap",
            "taş",
            "bavul",
            "güneş gözlüğü",
            "termometre",
            "iplik",
            "lastik",
            "kutu",
            "tütün",
            "diş macunu",
            "kürdan",
            "vazo",
            "el arabası",
            "duvar",
            "fermuar"],
          "adjectives" : [
            "çekici",
            "ortalama",
            "Güzel",
            "büyük",
            "geniş",
            "kırık",
            "inişli çıkışlı",
            "tombul",
            "temiz",
            "renkli",
            "devasa",
            "çarpık",
            "kavisli",
            "sevimli",
            "hasarlı",
            "koyu",
            "derin",
            "kirli",
            "kuru",
            "donuk",
            "tozlu",
            "fantezi",
            "şişman",
            "pis",
            "düz",
            "dev",
            "harika",
            "zarif",
            "büyük",
            "grotesk",
            "yüksek",
            "içi boş",
            "kocaman",
            "Büyük",
            "Küçük",
            "uzun",
            "mamut",
            "masif",
            "minyatür",
            "puslu",
            "çamurlu",
            "dar",
            "petite",
            "düz",
            "kıymetli",
            "dikenli",
            "cılız",
            "antika",
            "yuvarlak",
            "cılız",
            "sığ",
            "parlak",
            "kısa",
            "skinny",
            "sümüksü",
            "kaygan",
            "küçük",
            "pürüzsüz",
            "yumuşak"
            "dik",
            "yapışkan",
            "düz",
            "garip",
            "uzun",
            "ufacık",
            "küçük",
            "çirkin",
            "sıradışı",
            "geniş"]
          },
         "EN":
         {
          "names" : [
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
             "zipper"],

          "adjectives" : [
             "attractive",
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
          }
         }


def Random(topRange):
    from random import randrange
    return randrange(topRange)

class ProjectNameGenerator(object):
    # Kurucu metod - Constructor
    def __init__(self, params):
        #Daha once uretilmis girdilerin kayittan okunmasi
        self.generated = self.ReadGeneratedDictionary()
        
        while True:
            self.Program()
            
    def Program(self):
        print("PROJE ISIM URETECI >>>")
        
        query = raw_input()
        command = str.upper(query.split(' ')[0])
        
        if command == "GENERATE":
            language = str.upper(query.split(' ')[1])
            count = int(query.split(' ')[2])
            self.Generate(count, language)
        elif command == "HELP":
            print("### YARDIM ###")
            print("GENERATE KOMUTU: 1. Parametre; dil ayarı (TR:Türkçe ve EN:İngilizce), 2. Parametre; üretilmek istenen isim sayısı.\n")
            print("HELP KOMUTU: Yardım menüsü\n")
            print("EXIT KOMUTU: Çıkış\n")
        elif command == "EXIT":
            self.SaveGeneratedDictionary()
            exit()
            
    def Generate(self, n=None, language="TR"):
        if n is None:
            random1 = Random(words[language]["adjectives"].__len__())
            adjective = words[language]["adjectives"][random1]
            random2 = Random(words[language]["names"].__len__())
            name = words[language]["names"][random2]
            return adjective + " " + name
            
        else:
            i = 0
            while i < n:
                projectName = self.Generate(None, language)
                if self.IsGenerated(language, projectName):
                    continue
                else:
                    self.generated[language].append(projectName)
                    i+=1
                    print('{}. {}'.format(i, projectName))
    
    def ReadGeneratedDictionary(self):
        try:
            path = os.getcwd() + "\generated.json"
            jsondata = open(path).read()
            data = json.loads(jsondata)
            return data
        except ValueError:
            generated = {"TR":[], "EN":[]}
            return generated
    
    def SaveGeneratedDictionary(self):
        path = os.getcwd() + "\generated.json"
        jsondata = json.dumps(self.generated, separators=(', ',' : '))
        with codecs.open(path,'w', encoding='utf8') as f:
            f.write(jsondata)
    
    def IsGenerated(self, language, name):
        if len(self.generated[language]) > 0:
            i = 0
            while i < len(self.generated[language]):
                if name == self.generated[language][i]:
                    return True
                i += 1
            return False
        else:
            return False
    
generator = ProjectNameGenerator(NULL)
