import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
 
class GMail:
    def __init__(self):
      # smpt 서버와 연결
      self.gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
      self.gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
      self.smtp = smtplib.SMTP_SSL(self.gmail_smtp, self.gmail_port) 
      # 로그인
      self.my_account       = ""
      self.my_password      = ""
      
      # 메일을 받을 계정
      self.to_mail          = "" 
      # 메일 내용 
      self.content          = '' 
      # 메일 기본 정보 설정
      self.msg = MIMEMultipart()

    def LogIn(self, account, password ):
        self.my_account   = account
        self.my_password  = password

        self.smtp.login(self.my_account, self.my_password)
        self.msg["From"]     = self.my_account

    def SetContent(self, contentText):
        # 메일 본문 내용
        self.content = contentText

    def SetToEmail(self, to_Email):
        self.to_mail         = to_Email
        self.msg["To"]       = self.to_mail

    def SetMailTitle(self, title):
        self.msg["subject"] = title
    

    # 받는 메일 유효성 검사 거친 후 메일 전송
    def sendEmail(self):
      content_part = MIMEText(self.content, "plain")
      self.msg.attach(content_part)

      # 이미지 파일 추가
      '''image_name = "test.png"
      with open(image_name, 'rb') as file:
          img = MIMEImage(file.read())
          img.add_header('Content-Disposition', 'attachment', filename=image_name)
          msg.attach(img)'''
      

      reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
      if re.match(reg, self.to_mail):
          self.smtp.sendmail(self.my_account, self.to_mail, self.msg.as_string())
          print("정상적으로 메일이 발송되었습니다.")
      else:
          print("받으실 메일 주소를 정확히 입력하십시오.")


    def Quit(self):
        self.smtp.quit()




