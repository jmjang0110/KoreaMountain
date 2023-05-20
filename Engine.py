
from DataManager import * 

def main():
    print("main Start")
    dataManager = DataManager()
    Url         = "http://openapi.forest.go.kr/openapi/service/trailInfoService/getforeststoryservice"
    ServiceKey  = "h50GtCLWekmqHkV3FQHh0qMxP13wZrTi19ZhEFMVfKsC0OmCjsY%2BkEqY0kQ8ci4sQrTLoB4Ao4r29OTtGvS45g%3D%3D"
    Params      = {
            'serviceKey'        :       '서비스키'
        ,   'mntnNm'            :       '지리산'
        ,   'mntnHght'          :       ''
        ,   'mntnAdd'           :       ''
        ,   'mntnInfoAraCd'     :       ''
        ,   'mntnInfoSsnCd'     :       ''
        ,   'mntnInfoThmCd'     :       ''
        ,   'pageNo'            :       ''
        ,   'numOfRows'         :       '' 
    }
    
    dataManager.SetURL(Url)
    dataManager.SetServiceKey(ServiceKey)
    dataManager.SetParams(Params)
    dataManager.ExecuteResponse()
    dataManager.Test()




    
if __name__ == "__main__":
    main()
