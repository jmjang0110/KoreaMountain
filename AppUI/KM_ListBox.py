from tkinter import *
from tkinter import font

class KM_ListBox: # Korea Mountain App Label
    def __init__(self):
        self.Window         = None # TK
        self.ListBox          = None 
        self.Title          = ''

        self.width          = ''    
        self.height         = ''    
        self.relief         = None  # 테두리 모양 flat, groove, raised, ridge, solid, sunken
        
        self.borderwidth    = ''  # 테두리 두께
        self.background     = ''  # 배경 색상        
        self.foreground     = ''  # 문자열 색상        

        self.selectbackground = ''
        self.selectforeground = ''
        self.selectborderwidth = ''


        self.ScrollBar      = None




    def Init(self, X, Y, Window , width, height , relief, borderwidth, background, foreground, 
             selectedBackGround, selectedForeGround, SelectedBorderWidth, activestyle):
        self.Window         = Window
        self.width          = width
        self.height         = height // 2
        self.relief         = relief
        self.borderwidth    = borderwidth
        self.background     = background
        self.foreground     = foreground

        self.selectbackground = selectedBackGround
        self.selectforeground = selectedForeGround
        self.selectborderwidth = SelectedBorderWidth

        
        X = X * 7.7
        Y = Y * 8.3

        self.ScrollBar = Scrollbar(self.Window)
        self.ScrollBar.pack()
        self.ScrollBar.place(x =  + 20, y = Y)
        
        self.ListBox = Listbox(  self.Window
                                , width                 =   self.width
                                , height                =   self.height
                                , relief                =   self.relief
                                , borderwidth           =   self.borderwidth
                                , foreground            =   self.foreground 
                                , selectbackground      =   self.selectbackground
                                , selectborderwidth     =   self.selectborderwidth
                                , selectforeground      =   self.selectforeground
                                , activestyle           =   activestyle
                                , yscrollcommand        =   self.ScrollBar.set 
                                , cursor = 'hand2')
        
        self.ListBox.pack()
        self.ListBox.place(x = X,y = Y)


        #for i in range(100):
        #    self.ListBox.insert(i + 1, 'TEST\n'  + str(i + 1))
        
        
        self.ScrollBar.config(command = self.ListBox.yview)

    def InsertText(self, idx, text):
        self.ListBox.insert(idx, text)


    def ClearListBox(self):
        self.ListBox.delete(0,END)
        

        
