
import telepot
from urllib.request import urlopen

'''
        self.Response = urlopen(self.Url).read().decode('utf-8')


    def RenderInfo(self):
        print(self.Bot.getMe())
        print(self.Response)

'''

class TelegramBot:
    def __init__(self):


        self.Bot        = telepot.Bot(self.Token)

    def SendMessage(self, Message):
        self.Bot.sendMessage(chat_id = self.ChatID ,text = Message)



bot = TelegramBot()
#bot.SendMessage('안녕하세요 장재문 입니다.')
