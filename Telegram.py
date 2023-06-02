
import telepot
from urllib.request import urlopen

'''
        self.Url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&LAWD_CD=11110&DEAL_YMD=201712'
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
