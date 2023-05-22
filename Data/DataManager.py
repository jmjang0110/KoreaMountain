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
http://api.forest.go.kr/openapi/service/trailInfoService/getforeststoryservice

?mntnNm=지리산&serviceKey=인증키

'''
import urllib
import xml.etree.ElementTree as ET
import http.client
import requests

class DataManager :
# STATIC 
    ServiceKey_Decoding     = "+yY6uDPSsSxcus1uooXFx/zRum0tkPSjL6UOVng/QZHTrA/yyKGcyti2eE5gRq5V++1O7r9B6pJTqDyMov6/iw=="
    ServiceKey_Encoding     = "%2ByY6uDPSsSxcus1uooXFx%2FzRum0tkPSjL6UOVng%2FQZHTrA%2FyyKGcyti2eE5gRq5V%2B%2B1O7r9B6pJTqDyMov6%2Fiw%3D%3D"

    def GetEncode_Utf8(hangul) :
        hangul_utf8 = urllib.parse.quote(hangul)
        return hangul_utf8
# LOCAL 
    def __init__(self):
        self.Url            = ""  # API 요청을 위한 URL 
        self.Query          = ""  
        self.ServiceKey     = ""  # 공공 포털 데이터에서 받은 인증키 
        self.urlDetail      = ""
        self.Params         = {}
        
        self.Response       = None
        self.Root           = None

        self.Tree           = None
        self.ItemElements   = None 
    
    def ConnectToData(self, addSubUrl = ''):

        ReqUrl = self.Query + "?serviceKey=" + self.ServiceKey
        if(addSubUrl != ''):
            ReqUrl = ReqUrl + addSubUrl
        
        conn = http.client.HTTPConnection(self.Url)
        conn.request('GET', ReqUrl)
        Req = conn.getresponse()

        if Req.status  == 200:
            strXML = Req.read().decode('utf-8')
            self.Tree = ET.fromstring(strXML)
            self.ItemElements = self.Tree.iter("item")
    
    def ConnectToDataByRequests(self):
        Url = 'http://' + self.Url + self.Query
        Response = requests.get(Url, params=self.Params)
        self.Root = ET.fromstring(Response.content)
        self.ItemElements = self.Root.findall(".//item")



    def ShowData(self, DataKeyList):
        Datacnt = 0

        for item in self.ItemElements:
            for i in range(len(DataKeyList)):
                DataInfo = item.find(DataKeyList[i])
                
                print(DataInfo.text)
                print()
               
            print('------------------------')
            print()
            Datacnt += 1
        print(Datacnt)
            





    def LoadByHttp(self):
        addServiceKey = '?serviceKey=' + self.ServiceKey
        # ResultUrl = self.Query + addServiceKey
        # if(self.urlDetail != ""):
        #      ResultUrl = ResultUrl + self.urlDetail

        hangul_utf8 =  self.GetKoreanEncoding_utf8("지리산")#한글 인코딩
        ResultUrl = self.Query + '?serviceKey=' + self.ServiceKey + '&mntnNm=' + hangul_utf8
        conn    = http.client.HTTPConnection(self.Url)
        conn.request("GET", ResultUrl)
        req     = conn.getresponse()


        if req.status == 200: # 성공 
            strXML = req.read().decode('utf-8')
            #print(strXML)
            tree = ET.fromstring(strXML)
            self.ItemElements = tree.iter("item")
            i = 0


    def Test(self):
        for itemE in self.ItemElements:
            MountainName = itemE.find('mntnnm')
            info1 = itemE.find('hkngpntdscrt')
            info2 = itemE.find('mntninfopoflc')
            
            print(MountainName.text)
            print(info1.text)
            print(info2.text)



# [ GET ]


    def GetUrl(self):
        return self.Url
    
    def GetServiceKey(self):
        return self.ServiceKey
    
    def GetParams(self):
        return self.Params
    
    def GetItemElements(self):
        return self.ItemElements
    


# [ SET ]
    def SetURL(self, url):
        self.Url = url

    def SetQuery(self, query):
        self.Query = query

    
    def SetParams(self, params):
        self.Params = params 
    
    def SetServiceKey(self, serviceKey):
        self.ServiceKey = serviceKey

    def SetUrlDetail(self, urlDetail):
        self.urlDetail = urlDetail




        
        

