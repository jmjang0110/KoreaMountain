


from    AppUI.KM_Button     import *
from    AppUI.KM_Label      import *
from    AppUI.KM_Command    import *
from    AppUI.KM_ListBox    import *
from    AppUI.KM_Entry      import *


from tkinter import *

class KM_Window:
    def __init__(self):
        self.Window         = Tk()
        self.Title          = 'Korea Mountain'

        self.width          = '500'    
        self.height         = '700'
        self.StartPos_x     = '750'
        self.StartPos_y     = '0'

        self.UI_SearchButton            = KM_Button()
        self.UI_MapButton               = KM_Button()
        self.UI_MoreInfoButton          = KM_Button()

        self.UI_WeatherInfo             = KM_Label()
        self.UI_RegionInfo              = KM_Label()
        self.UI_MountainInfo            = KM_Label()

        self.UI_MountainListInfo        = KM_ListBox()
        self.UI_Entry                   = KM_Entry()



    def Init(self):
        GeoParam = self.width + 'x' + self.height \
            + '+' + self.StartPos_x + '+' + self.StartPos_y
        

        self.Window.title(self.Title)
        self.Window.geometry(GeoParam)
        self.Window.resizable(False, False)
        
        self.UI_WeatherInfo.Init(1,1, self.Window, 35 , 35, 'solid', 1, 'Light gray', 'Black', 'Weather Info' )
        self.UI_RegionInfo.Init(1, 34, self.Window, 35, 8, 'solid', 1, 'black',   'black', 'Region Info' )
        self.UI_MountainInfo.Init(1 + 36 , 34, self.Window, 28, 35, 'solid', 1, 'gray', 'black', 'Mountain \n image \n Info')



        self.UI_MountainListInfo.Init(1, 43, self.Window, 34, 20, 'solid', 1, 'gray', 'black'
                                      , 'light gray', 'black', 4, 'none')



        self.UI_Entry = KM_Entry()

        self.UI_Entry.Init(1 + 36, 1 , self.Window, 28)
        # self.UI_SearchButton.SetCommand(self.UI_Entry.Command_GetName)
        self.UI_SearchButton.Init(1 + 36 , 5 , self.Window, 28, 3, 'solid', 'sunken', 1, 'grey', 'black', 'Search Button')

        self.UI_MoreInfoButton.Init(1 + 36 , 67.5 , self.Window, 28, 5, 'solid', 'sunken', 1, 'light gray', 'blue', 'More Info')


        menubar =   Menu(self.Window)
        menu_1  =   Menu(menubar, tearoff=0)
        menu_1.add_command(label="하위 메뉴 1-1")
        menu_1.add_command(label="하위 메뉴 1-2")
        menu_1.add_separator()
        menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

        self.Window.config(menu = menubar)

    def Run(self):
        self.Window.mainloop()


    def GetWindow(self):
        return self.Window
    
    def GetEntry(self):
        return self.UI_Entry
    def GetListBox(self):
        return self.UI_MountainListInfo