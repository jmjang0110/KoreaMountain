
from DataManager import * 

def main():
    print("main Start")
    dataManager = DataManager()
    Url         = "http://openapi.forest.go.kr/openapi/service/trailInfoService/getforeststoryservice"
    ServiceKey_Decoding  = "+yY6uDPSsSxcus1uooXFx/zRum0tkPSjL6UOVng/QZHTrA/yyKGcyti2eE5gRq5V++1O7r9B6pJTqDyMov6/iw=="
    ServiceKey_Encoding  = "%2ByY6uDPSsSxcus1uooXFx%2FzRum0tkPSjL6UOVng%2FQZHTrA%2FyyKGcyti2eE5gRq5V%2B%2B1O7r9B6pJTqDyMov6%2Fiw%3D%3D"

    Params      = {
            'serviceKey'        :       'ServiceKey'
        ,   'mntnNm'            :       '지리산'
        ,   'mntnHght'          :       ''
        ,   'mntnAdd'           :       ''
        ,   'mntnInfoAraCd'     :       ''
        ,   'mntnInfoSsnCd'     :       ''
        ,   'mntnInfoThmCd'     :       ''
        ,   'pageNo'            :       ''
        ,   'numOfRows'         :       '' 
    }
    Url_Weather =  'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params_Weather ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20210628', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

    
   
    dataManager.SetURL(Url)
    dataManager.SetServiceKey(ServiceKey_Encoding)
    dataManager.SetParams(Params)
    # dataManager.ExecuteResponse()
    dataManager.LoadByHttp()

    #dataManager.Test()
   


if __name__ == "__main__":
    main()
