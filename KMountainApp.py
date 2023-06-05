
# DATA 
from Data.DataManager       import * 
from Data.MountainData      import *
from Data.WeatherData       import *
from Data.KaKaoAPImapData   import *
from Data.MapData           import *

# UI 
import tkinter
import customtkinter
from tkintermapview import TkinterMapView

# Call Back Func 
from CallBackFunc import *
import os
from PIL import Image
import urllib.request
from io import BytesIO


from Telegram import TelegramBot

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="보기", width=50, height=24)
        
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
            
    def remove_All(self):
        for label, button in zip(self.label_list, self.button_list):
            label.destroy()
            button.destroy()
        
        self.label_list.clear()
        self.button_list.clear()

        
class ScrollableLabelProgressBarFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.ProgressBar_List = []

    def add_item(self, item, image=None):
        label       = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        ProgressBar = customtkinter.CTkProgressBar(self, progress_color='light green', width = 120 ,height=15)
        
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        ProgressBar.grid(row=len(self.ProgressBar_List), column=1, pady=(2, 5), padx=0)
        
        self.label_list.append(label)
        self.ProgressBar_List.append(ProgressBar)

    def remove_item(self, item):
        for label, progressBar in zip(self.label_list, self.ProgressBar_List):
            if item == label.cget("text"):
                label.destroy()
                progressBar.destroy()
                self.label_list.remove(label)
                self.ProgressBar_List.remove(progressBar)
                return
        
    def remove_All(self):
        for label, progressBar in zip(self.label_list, self.ProgressBar_List):
            label.destroy()
            progressBar.destroy()
        
        self.label_list.clear()
        self.ProgressBar_List.clear()

    def set(self, idx, value):
        ProgressBar = self.ProgressBar_List[idx]
        OriginValue = ProgressBar.get()
        ProgressBar.set(value)
        
        

        
    

class KMountainApp:
    def __init__(self):
        self.MntData   = MountainData()
        self.WeaData   = WeatherData()

        self.KaKao_url          = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        self.KaKao_ServiceKey   = '4b26e7470a265bf96899caf9892dac65'
        

# APPLICATION - MAIN WINDOW 
        self.App = customtkinter.CTk()  
        self.App.title("Korea Mountains Application")
        self.App.geometry(f"{1200}x{700}")

        self.App.grid_columnconfigure(1, weight=1)
        self.App.grid_columnconfigure((2, 3), weight=0)
        self.App.grid_rowconfigure((0, 1, 2), weight=1)       
    

        self.Telegram = TelegramBot()


        #   [0,0][0,1][0,2][0,3]
        #   [1,0][1,1][1,2][1,3]
        #   [2,0][2,1][2,2][2,3]
        #   [3,0][3,1][3,2][3,3]

        self.Init_SideBarFrame(0,0)
        self.Init_TextBoxFrame(0,1)
        self.Init_TabViewFrame(0,2)
        self.Init_MapWidgetFrame(1,1)
        self.Init_MountainListSidebarFrame(1,2)

    def Init_SideBarFrame(self, _Row, _Column):
        current_path            = os.path.dirname(os.path.realpath(__file__)) + '/ImageFile/'
        BackImage               = Image.open(current_path + "MountainBack1.jpg")
        bg_image                = customtkinter.CTkImage(BackImage, size=(1200, 700))
        bg_image_label          = customtkinter.CTkLabel(self.App, image=bg_image, text='')
        bg_image_label.grid(row=0, column=0, rowspan = 3, columnspan = 3)
    
# SIDE BAR 
        self.sidebar_frame = customtkinter.CTkFrame(master = self.App, width=140, height=250, corner_radius=10, fg_color="transparent")
        self.sidebar_frame.grid(row=_Row, column=_Column, rowspan=3, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        current_path            = os.path.dirname(os.path.realpath(__file__)) + '/ImageFile/'
        BackImage               = Image.open(current_path + "MountainLogo_HikingPerson.png")
        bg_image           = customtkinter.CTkImage(BackImage, size=(200, 200))
        bg_image_label     = customtkinter.CTkLabel(self.sidebar_frame, image= bg_image, text='')
        bg_image_label.grid(row=0, column=0, rowspan = 1, columnspan = 3)

# SIDE BAR - LOGO 
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Korea Mountains", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(0, 0))

# SIDE BAR - MAP OPTION 
        self.map_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame
                                                   , values = ["OpenStreetMap", "Google normal", "Google satellite"]
                                                   ,command = self.CallBack_ChangeMapView)
        self.map_option_menu.grid(row=2, column=0, padx=(20, 0), pady=(20, 0))
        self.map_marks = list()

# SIDE BAR - BUTTON [ CLEAR MARKS ]
        self.Button_ClearMarks = customtkinter.CTkButton(master=self.sidebar_frame,
                                                text="Clear Markers",
                                                command=self.CallBack_ClearMaekers)
        self.Button_ClearMarks.grid(row=3, column=0, padx=(20, 0), pady=(20, 0))
        self.marker_list  = list()      # 현재 지도에 표시된 마크들 


        self.Telegram_Icon_Img = customtkinter.CTkImage(Image.open(os.path.join(current_path, "TelegramLogo.png")), size=(50,50))
        
        self.Telegram_Button = customtkinter.CTkButton(self.sidebar_frame
                                                       , text=""
                                                       , image=self.Telegram_Icon_Img
                                                       , fg_color="transparent"
                                                       , hover_color='white'
                                                       , command = self.CallBack_TelegramButton)
        
        self.Telegram_Button.grid(row=1, column=0, padx=(20, 0), pady=(150, 0))

        self.Gmail_Icon_Img = customtkinter.CTkImage(Image.open(os.path.join(current_path, "GmailLogo.png")), size=(50,50))
        
        self.Gmail_Button = customtkinter.CTkButton(self.sidebar_frame
                                                       , text=""
                                                       , image=self.Gmail_Icon_Img
                                                       , fg_color="transparent"
                                                       , hover_color='white'
                                                       , command = self.CallBack_GmailButton)
        
        self.Gmail_Button.grid(row=1, column=0, padx=(20, 0), pady=(30, 0))

    def Init_TextBoxFrame(self, _Row, _Column):
        #self.TextBox_Frame = customtkinter.CTkFrame(master = self.App, corner_radius=10, fg_color="transparent")
        #self.TextBox_Frame.grid(row=_Row, column=_Column, padx=(20, 20), pady=(20, 0), sticky="nsw")


        self.TextBox_MntInfo = customtkinter.CTkTextbox(master=self.App, width=500, height=250)
        self.TextBox_MntInfo.grid(row=_Row, column=_Column, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.TextBox_MntInfo.insert("0.0", "CTkTextbox\n\n" + 
                                    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr\
                                    , sed diam nonumy eirmod tempor invidunt ut labore \
                                    et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 5) # TEST 
        
    def Init_TabViewFrame(self, _Row, _Column):
        self.TabView_Frame = customtkinter.CTkFrame(master = self.App, width=400, height=500, fg_color="transparent")
        self.TabView_Frame.grid(row=_Row, column=_Column, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # TAP VIEW 
        self.tabview = customtkinter.CTkTabview(master = self.TabView_Frame, width=300, height=200, command=self.CallBack_TabView)
        self.tabview.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.tabview.add("날씨")
        self.tabview.add("산 높이 그래프")
        self.tabview.add("사진")
        self.tabview.tab("날씨").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("산 높이 그래프").grid_columnconfigure(1, weight=1)
        #self.tabview.configure(require_redraw=True, kwargs="command")


        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("날씨"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("날씨"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0))

        # MOUNTAINS LIST - SCROLL BAR BUTTON 
        self.ProgressBar_List = ScrollableLabelProgressBarFrame(master=self.tabview.tab("산 높이 그래프")
                                                       , width=  250
                                                       , height = 30
                                                       , corner_radius=0)
        
        self.ProgressBar_List.grid(row=0, column=0, columnspan = 1, padx=(0, 5), pady=(0, 0), sticky="nsew")




    
    def Init_MapWidgetFrame(self, _Row, _Column):
        self.MapWidget_Frame = customtkinter.CTkFrame(master = self.App, width=300, height=300, corner_radius=10)
        self.MapWidget_Frame.grid(row=_Row, column=_Column, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # MAP 
        self.map_widget = TkinterMapView(self.MapWidget_Frame,width=600, height=350, corner_radius=1)
        self.map_widget.grid(row=1, rowspan=2, column=1, columnspan=1, sticky="nswe", padx=(10, 10), pady=(10, 0))


    def Init_MountainListSidebarFrame(self, _Row, _Column):
        self.MntListSidebar_Frame = customtkinter.CTkFrame(master = self.App, width=300, height=400)
        self.MntListSidebar_Frame.grid(row=_Row, column=_Column, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # SEARCH ENTRY 
        self.SearchEntry = customtkinter.CTkEntry(self.MntListSidebar_Frame, placeholder_text="입력")
        self.SearchEntry.grid(row=0, column=0, columnspan=1, padx=(10, 0), pady=(0, 0), sticky="nsew")

        self.SearchButton = customtkinter.CTkButton(master=self.MntListSidebar_Frame
                                                     , text = '검색'
                                                     , fg_color="transparent"
                                                     , width=80
                                                     , border_width=2
                                                     , text_color=("gray10", "#DCE4EE")
                                                     , command=self.Callback_EntryButton)
        self.SearchButton.grid(row=0, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew")

        # MOUNTAINS LIST - SCROLL BAR BUTTON 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")

        self.MountainList = ScrollableLabelButtonFrame(master=self.MntListSidebar_Frame
                                                       , width=300
                                                       , height = 250
                                                       , command=self.CallBack_MntButton
                                                       , corner_radius=0)
        
        self.MountainList.grid(row=2, column=0, columnspan = 2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        for i in range(20):  # add items with images
            self.MountainList.add_item(f"image and item {i}", 
                                       image=customtkinter.CTkImage(Image.open(os.path.join(image_path, "chat_light.png"))))
            
        self.SelectedMntName = ''

# MAIN RUN 
    def Run(self):
        self.App.mainloop()

# CHANGE MAP  STYLE
    def CallBack_ChangeMapView(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


    def CallBack_MntButton(self, item):

        MntName = item
        self.SelectedMntName = MntName
        print(f"label button frame clicked: {item}")
        
        # 선택한 산을 지도에 표기한다. 
        TargetSpot = self.GetMarkSpot(MntName)
        if TargetSpot[0] != -1:
            self.map_widget.set_position(TargetSpot[0], TargetSpot[1])
            self.marker_list.append(self.map_widget.set_marker(TargetSpot[0], TargetSpot[1] ,text= MntName
                                                               ,marker_color_circle="light gray", marker_color_outside="gray")) # ,marker_color_circle="black", marker_color_outside="sky blue"
            self.map_widget.set_zoom(9)

        # 선택한 산을 텍스트 박스에 표기한다. 
        MountainParam = self.MntData.GetParam(str(MntName))
        name        = MountainParam[0][1].text
        Height      = MountainParam[1][1].text
        Address     = MountainParam[2][1].text
        InfoManin   = MountainParam[3][1].text
        InfoImg     = MountainParam[4][1].text


        ResultText = name + '\n\n' + \
                    '높이 : '        + Height   + '\n\n'+   \
                    '주소 : '        + Address  +  '\n\n'+ \
                    '전화번호 : '    + InfoManin  + '\n\n' +  \
                    '교통편 : '      + InfoImg + '\n\n'

        self.TextBox_MntInfo.delete('0.0', 'end')
        self.TextBox_MntInfo.insert("0.0", ResultText) # TEST

    def Callback_EntryButton(self):

        Input = self.SearchEntry.get()
        # KM_FrameWork.Map.SetMarker(Input)
        if Input[-1] == '산':
            self.MntData.UpdateResponseParamsByMountainName(Input)
        else:
            self.MntData.UpdateResponseParamsByLocation(Input)

        ResParams = self.MntData.GetResponseParams()
        # KM_FrameWork.MountainData.ShowResponseParams()

        idx= 0
        self.MountainList.remove_All()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for Param in ResParams:
            Data = Param[0][1]
            MntName = Data.text
            idx += 1
            self.MountainList.add_item(MntName, image=customtkinter.CTkImage
                                       (Image.open(os.path.join(current_dir, "ImageFile", "MountainLogo4_Blue.png"))))
        
        #self.map_widget.set_address(Input)
        self.map_marks.clear()
        for i in range(1,4):
            self.getLatLng(Input, i)
# MARK 
        TargetSpot = self.GetMarkSpot(Input)
        if TargetSpot[0] != -1:
            self.map_widget.set_position(TargetSpot[0], TargetSpot[1])
            self.marker_list.append(self.map_widget.set_marker(TargetSpot[0], TargetSpot[1] ,text= Input)) # ,marker_color_circle="black", marker_color_outside="sky blue"
            self.map_widget.set_zoom(7)



    def getLatLng(self, region, page_num):
        url     = 'https://dapi.kakao.com/v2/local/search/keyword.json' 

        #params  = {'query': region,'page': page_num}
        params  = {'query': region, 'page': page_num}
        headers = {"Authorization": "KakaoAK " + self.KaKao_ServiceKey}

        places = requests.get(url, params=params, headers=headers).json()['documents']
        for place in places:

            X = float(place['x'])
            Y = float(place['y'])
            spot = (Y, X)
            print(spot)
            self.map_marks.append(spot)
        
    def GetMarkSpot(self, Target):
        url     = 'https://dapi.kakao.com/v2/local/search/keyword.json' 
        headers = {"Authorization": "KakaoAK " + self.KaKao_ServiceKey}
        params  = {'query': Target, 'page': 1}
        places = requests.get(url, params=params, headers=headers).json()['documents']
        
        X = -1
        Y = -1
        
        for place in places:
            X = float(place['x'])
            Y = float(place['y'])
            spot = (Y, X)
            return spot
                



    def CallBack_ClearMaekers(self):
        for marker in self.marker_list:
            marker.delete()

            
        

    def CallBack_TabView(self):
        TabName     = self.tabview.get()
        ResParams   = self.MntData.GetResponseParams()

        self.ProgressBar_List.remove_All()
        idx = 0
        if TabName == '산 높이 그래프':
            for Param in ResParams:
                MntName = Param[0][1].text
                Height  = Param[1][1].text

                Str = MntName + ' ' + Height + 'm'
                self.ProgressBar_List.add_item(Str)
                self.ProgressBar_List.set(idx, float(float(Height) / 1950))
                idx += 1

        elif TabName == '사진':
            for Param in ResParams:
                MntName = Param[0][1].text
                if MntName == self.SelectedMntName:
                    ImgUrl = Param[4][1].text 
                    # request.urlopen()
                    # HTTP Error 403: Forbidden 에러 때문에 하단의 소스 한 줄을 추가해주었다.
                    req         = urllib.request.Request(ImgUrl, headers = {"User-Agent" : "Mozilla/5.0"})
                    res         = urllib.request.urlopen(req).read()
                    UrlOpen_Img = Image.open(BytesIO(res))
                    Img         = customtkinter.CTkImage(UrlOpen_Img, size=(250, 250))
                    label       = customtkinter.CTkLabel(master = self.tabview.tab('사진') , text='', image = Img, compound="left", padx=5, anchor="w")
                    label.grid(row=0, column=0, rowspan = 3, columnspan = 3)


    
    def CallBack_TelegramButton(self):
        self.Telegram.SendMessage("안녕!! VScode 에서 보냈어")


    def CallBack_GmailButton(self):
        print('CallBack GmailButton')
