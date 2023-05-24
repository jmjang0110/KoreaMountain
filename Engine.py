
from Data.DataManager   import * 
from Data.MountainData  import *
from Data.WeatherData   import *
from AppUI.KM_Window    import *

def main():
    print("main Start")

    MntData =   MountainData()
    WeaData =   WeatherData()
    
    # MntData.TEST()
    # WeaData.TEST()



    MyUI = KM_Window()
    MyUI.Init()
    MyUI.Run()



if __name__ == "__main__":
    main()
