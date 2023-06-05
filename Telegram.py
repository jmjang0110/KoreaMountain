
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
        self.UserName   = 'Realestate_Student_JJM_bot'
        self.Token      = '6083907076:AAEmuBc90HO070E2EK6WmD0Sle9raZPDMxw'
        self.ChatID     = '5725518891'

        self.Bot        = telepot.Bot(self.Token)

    def SendMessage(self, Message):
        self.Bot.sendMessage(chat_id = self.ChatID ,text = Message)



bot = TelegramBot()
#bot.SendMessage('안녕하세요 장재문 입니다.')
