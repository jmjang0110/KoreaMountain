
from Data.DataManager   import * 
from Data.MountainData  import *
from Data.WeatherData   import *
from Data.KaKaoAPImapData import *


from AppUI.KM_Window    import *

def main():
    print("main Start")

    MntData =   MountainData()
    WeaData =   WeatherData()
    
    # MntData.TEST()
    # WeaData.TEST()


    Map = KaKaoAPImap()

    MyUI = KM_Window()
    MyUI.Init()

    Map.Run()
    MyUI.Run()




if __name__ == "__main__":
    main()
