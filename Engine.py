
from Data.DataManager   import * 
from Data.MountainData  import *
from Data.WeatherData   import *


def main():
    print("main Start")

    MntData =   MountainData()
    WeaData =   WeatherData()

    ResList = [ 
            MNT_RES_TYPE.NAME
        ,   MNT_RES_TYPE.HEIGHT
        ,   MNT_RES_TYPE.ADDRESS
        ,   MNT_RES_TYPE.INFO_MAIN
        ,   MNT_RES_TYPE.INFO_MAP_IMG
        ]
    
    MntData.AddSubUrl(MNT_REQ_TYPE.ADDRESS, DataManager.GetEncode_Utf8('서울'))
    MntData.AddSubUrl(MNT_REQ_TYPE.MAXNUM_OF_RESULT, '50')
    SubUrl = MntData.GetSubUrl()

    MntData.ConnectToData(SubUrl)
    MntData.UpdateResponseParams(ResList)
    MntData.ShowResponseParams()


if __name__ == "__main__":
    main()
