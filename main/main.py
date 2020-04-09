#!/usr/bin/env python
#Making sounds according to the ids of nfc cards
import nfc
import pandas as pd
from time import sleep
from pygame import mixer

#Preparation
clf = nfc.ContactlessFrontend('usb')
df = pd.read_csv("list.csv", sep=',')


#Execute
while True:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    id_ = str(tag).split(" ")[-1][3:]
    print(id_)
    if id_ in df["id"].to_list():
        
        #Play Music
        sound_path = "../sounds/" + df[df["id"] == id_]["sounds"].iloc[0]
        print(sound_path)
        sleep_sec = df[df["id"] == id_]["time"].iloc[0]
        mixer.init()
        mixer.music.load(sound_path)
        mixer.music.play(1)

        sleep(sleep_sec)

    sleep(1)