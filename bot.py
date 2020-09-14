import ch
import io
import pygame
from gtts import gTTS


import os

class bot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("FFFFFF")
        self.setFontColor("FFFFFF")
        self.setFontFace("Ariel")
        self.setFontSize(11)
        # player = MPyg321Player()

    def onMessage(self, room, user, message):
        print("[{0}] {1}: {2}".format(room.name, user.name.title(), message.body))
        self.read_message(user.name.title(), message.body)


    def read_message(self, user, message):
        if len(message) < 100:
            with io.BytesIO() as f:
                language = 'pl'
                text = user + ' ' + message
                text = ''.join([i for i in text if not i.isdigit()])
                gTTS(text=text, lang=language).write_to_fp(f)
                f.seek(0)
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue


rooms = ['strimiworld']
username = "czytamstrimsy"
password = "freeflet"

bot.easy_start(rooms, username, password)