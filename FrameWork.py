
'''
    배포판 만들떼 py.modules 에서 파이썬 파일만 나열하기 

'''
from Data.DataManager       import * 
from Data.MountainData      import *
from Data.WeatherData       import *
from Data.KaKaoAPImapData   import *

from AppUI.KM_Window        import *


class KM_FrameWork:
    SearchEntry     = None
    Window          = None
    MountainData    = None
    WeatherData     = None
    Map             = None


    def __init__(self) :
        KM_FrameWork.Map            = KaKaoAPImap()
        KM_FrameWork.Window         = KM_Window()

        KM_FrameWork.MountainData   = MountainData()
        KM_FrameWork.WeatherData    = WeatherData()

        KM_FrameWork.SearchEntry    = KM_Entry()
        KM_FrameWork.MntListInfo    = KM_ListBox()
        KM_FrameWork.MntRegionInfo  = KM_Label()
        KM_FrameWork.ShowInfoButton = KM_Button()


    def Init(self):
        KM_FrameWork.Window.Init()

        KM_FrameWork.SearchEntry = KM_FrameWork.Window.GetEntry()
        KM_FrameWork.SearchEntry.Bind('<Return>', KM_FrameWork.SearchCommand)

        KM_FrameWork.MntListInfo = KM_FrameWork.Window.GetListBox()
        KM_FrameWork.ShowInfoButton = KM_FrameWork.Window.GetShowInfoButton()
        

        KM_FrameWork.ShowInfoButton.SetCommand(self.ShowInfoCommand)
        KM_FrameWork.ShowInfoButton.Init(1 + 32.5 , 43 , KM_FrameWork.Window.GetWindow() , 2, 2, 'solid', 'sunken', 2, 'light gray', 'blue', 'O')
        
        KM_FrameWork.MntRegionInfo = KM_FrameWork.Window.GetRegionInfo()


    def Run(self):
        KM_FrameWork.MountainData.UpdateResponseParamsByLocation('경기도')
    
        KM_FrameWork.Map.Run('지리산')
        KM_FrameWork.Map.Destroy()

        KM_FrameWork.Window.Run()

        KM_FrameWork.WeatherData.TEST()
        


    def SearchCommand(event):
        Input = KM_FrameWork.SearchEntry.GetEntry().get()
        # KM_FrameWork.Map.SetMarker(Input)
        if Input[-1] == '산':
            KM_FrameWork.MountainData.UpdateResponseParamsByMountainName(Input)
        else:
            KM_FrameWork.MountainData.UpdateResponseParamsByLocation(Input)

        ResParams = KM_FrameWork.MountainData.GetResponseParams()
        # KM_FrameWork.MountainData.ShowResponseParams()

        idx = 1
        KM_FrameWork.MntListInfo.ClearListBox()

        for Param in ResParams:
            Data = Param[0][1]
            KM_FrameWork.MntListInfo.InsertText(idx, Data.text)
            idx += 1


        KM_FrameWork.Map.Destroy()
        KM_FrameWork.Map.Activate()

        if KM_FrameWork.Map.IsOpen() == True:
            KM_FrameWork.Map.Run(Input)


    def ShowInfoCommand(self):
        Index = KM_FrameWork.MntListInfo.GetCurSelectionData()[0]
        ResParams = KM_FrameWork.MountainData.GetResponseParams()
        i = 0
        for Param in ResParams:
            if i == Index :
                Data = Param[2][1]
                KM_FrameWork.MntRegionInfo.ConfigText(Data.text)
                break
            i += 1





 

