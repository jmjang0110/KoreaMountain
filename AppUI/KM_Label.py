from tkinter import *
from tkinter import font

class KM_Label: # Korea Mountain App Label
    def __init__(self):
        self.Window         = None # TK
        self.Label          = None 
        self.Title          = ''

        self.width          = ''    
        self.height         = ''    
        self.relief         = None  # 테두리 모양 flat, groove, raised, ridge, solid, sunken
        
        self.borderwidth    = ''  # 테두리 두께
        self.background     = ''  # 배경 색상        
        self.foreground     = ''  # 문자열 색상        
        self.text           = ''


    def Init(self, X, Y, Window , width, height , relief, borderwidth, background, foreground, text):
        self.Window         = Window
        self.width          = width
        self.height         = height // 2
        self.relief         = relief
        self.borderwidth    = borderwidth
        self.background     = background
        self.foreground     = foreground
        self.text           = text
        
        X = X * 7.7
        Y = Y * 8.3
        
        self.Label = Label(  self.Window
                             , width        =   self.width
                             , height       =   self.height
                             , relief       =   self.relief
                             , borderwidth  =   self.borderwidth
                             , foreground   =   self.foreground 
                             , text         =   self.text )
        self.Label.pack()
        self.Label.place(x = X,y = Y)

        
