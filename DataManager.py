'''
    OpenAPI 데이터를 가져옵니다.

    XML : ( eXensible Markup Language ) 
        - Node 
        - Element

    ElementTree : 검색에 용이  

# 인증키를 입력한 후, 필요한 매개변수를 queryParams 딕셔너리로 전달하여 requests 모듈을 사용하여 API 호출을 합니다.
# API에서 반환하는 데이터는 XML 포맷으로 되어 있으므로, xml.etree.ElementTree 모듈을 사용하여 XML을 파싱하여 데이터를 읽어옵니다.
# 읽어온 데이터는 ElementTree의 iter 메소드를 사용하여 item 태그를 찾아서 필요한 데이터를 추출하고 출력하는 예제입니다.
# 필요한 데이터의 태그명을 API 문서에서 확인하여 findtext 메소드를 사용하여 데이터를 추출할 수 있습니다.
# 이 코드를 수정하여 필요한 데이터를 추출하고 활용할 수 있습니다.
# tkinter 모듈을 사용하여 윈도우 창과 표를 생성합니다. 
# 표의 첫 번째 행에는 열 이름이 포함되어 있습니다. 
# root.iter() 메소드를 사용하여 XML 데이터를 반복하면서 필요한 데이터를 추출하고, 데이터를 data 리스트에 저장합니다. 
# data 리스트는 tkinter.Label() 메소드를 사용하여 GUI 창에 표시됩니다.
    
산 데이터 : 
https://www.data.go.kr/data/15058682/openapi.do?recommendDataYn=Y
queryParams = {

        'serviceKey'    :       service_key, 
        'pageNo'        :       '1', 
        'numOfRows'     :       '10', 
        'sidoCd'        :       '110000', 
        'sgguCd'        :       '110019'

    }

'''

import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlencode, quote_plus, unquote, quote

import http.client

class DataManager :
    def __init__(self):
        self.Url            = ""  # API 요청을 위한 URL 
        self.ServiceKey     = ""  # 공공 포털 데이터에서 받은 인증키 
        self.Params         = {}
        
        self.Response       = None
        self.Root           = None
        self.ItemElements   = None

    
    def ExecuteResponse(self):
        decoded_Key = unquote(self.ServiceKey)
        queryParams = urlencode({quote_plus(self.ServiceKey) : decoded_Key, quote_plus('LAWD_CD') : '11110'})        
 
        self.Response       = requests.get(self.Url, params = self.Params)
        print(self.Response.content)

        if(self.Response.status_code == 200):
            i = 0

        
        self.Root           = ET.fromstring(self.Response.text)
        self.ItemElements   = self.Root.iter('items')

    def LoadByHttp(self):
        Url_apis_data    =  'apis.data.go.kr'
        query_Weather   = "/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=" + self.ServiceKey

        url             = "openapi.forest.go.kr"
        query           = "/openapi/service/trailInfoService/getforeststoryservice?serviceKey=" + self.ServiceKey
        
        ProfessorServiceKey    = "sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D"
        query_hospital        = "/B551182/hospInfoServicev2/getHospBasisList?serviceKey=" + self.ServiceKey

        conn    = http.client.HTTPConnection(Url_apis_data)
        conn.request("GET", query)
        req     = conn.getresponse()

        if req.status == 200:
            strXML = req.read().decode('utf-8')
            print(strXML)



    def Test(self):
        for item in self.ItemElements:
            MountainName = item.findtext('mntnNm')
            print(MountainName)


# [ GET ]
    def GetUrl(self):
        return self.Url
    
    def GetServiceKey(self):
        return self.ServiceKey
    
    def GetParams(self):
        return self.Params
    


# [ SET ]
    def SetURL(self, url):
        self.Url = url
    
    def SetParams(self, params):
        self.Params = params 
    
    def SetServiceKey(self, serviceKey):
        self.ServiceKey = serviceKey



        
        

