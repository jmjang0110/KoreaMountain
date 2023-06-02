from tkinter import *
from tkinter import font
import customtkinter
import tkinter

class KM_Button: # Korea Mountain App Button
    def __init__(self):
        self.Window         = None # TK
        self.Button         = None 
        self.Title          = ''

        self.width          = ''    # 버튼 너비 
        self.height         = ''    # 버튼 높이 
        self.relief         = None  # 버튼 테두리 모양 
        self.overrelief     = ''    # 마우스를 올렸을 때 버튼의 테두리 모양     
        self.borderwidth    = None  # 버튼 테두리 두께
        self.background     = None  # 버튼 배경 색상 
        self.foreground     = None  # 버튼 문자열 색상
        self.text           = ''


        self.Command        = None # 버튼을 눌렀을 시 실행할 함수

    def Init(self, X, Y, Window , width, height , relief, overrelief, borderwidth, background, foreground, text):
        
        self.Window         = Window
        self.width          = width
        self.height         = height // 2
        self.relief         = relief
        self.overrelief     = overrelief
        self.borderwidth    = borderwidth
        self.background     = background
        self.foreground     = foreground
        self.text           = text
        
        X = X * 7.7
        Y = Y * 8.3

        self.Button = customtkinter.CTkButton(master=Window, text=text)
        self.Button.pack()
        self.Button.place(relx = X,rely = Y, anchor=tkinter.CENTER)



    def SetCommand(self, command ):
        self.Command = command


        
