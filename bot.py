import ch
from gtts import gTTS
# from mpyg321.mpyg321 import MPyg321Player

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
        language = 'pl'

        text = user + ' ' + message
        print(f'Reading {text}')
        myobj = gTTS(text=text, lang=language, slow=False)

        myobj.save("message.mp3")
        # self.player.play_song("message.mp3")
        os.system("mpg123 message.mp3")


rooms = ['strimiworld']
username = "czytamstrimsy"
password = "freeflet"

bot.easy_start(rooms, username, password)