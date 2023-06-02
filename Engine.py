
from Data.DataManager   import * 
from Data.MountainData  import *
from Data.WeatherData   import *
from Data.KaKaoAPImapData import *


from AppUI.KM_Window    import *
from FrameWork import *

from KMountainApp import *


def main():
    print("main Start")
    
    #GameFramework = KM_FrameWork()
    #GameFramework.Init()
    #GameFramework.Run()


    App = KMountainApp()
    App.Run()
    


if __name__ == "__main__":
    main()

