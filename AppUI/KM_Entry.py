from tkinter import *
from tkinter import font

class KM_Entry: # Korea Mountain App Entry
    def __init__(self):
        self.Window         = None # TK
        self.entry         = None 
        self.Title          = ''

        self.width          = ''    # 버튼 너비 


        self.Command        = None # 버튼을 눌렀을 시 실행할 함수

    def Init(self, X, Y, Window , width):
        
        self.Window         = Window
        self.width          = width

        X = X * 7.7
        Y = Y * 8.3

        self.entry = Entry(  self.Window
                            , width = self.width
                            )
        self.entry.pack()
        self.entry.place(x = X,y = Y)



    def SetCommand(self, command ):
        self.Command = command

    def Bind(self, type, command):
        self.entry.bind(type, command)

    def GetEntry(self):
        return self.entry

  

        
