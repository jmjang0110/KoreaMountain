

from Data.DataManager import *
'''
b) 요청 메시지 명세
항목명(영문)	항목명(국문)	        항목크기	항목구분	샘플데이터	            항목설명
serviceKey	    인증키	                100	        1	       인증키           (URL Encode)	공공데이터포털에서 발급받은 인증키
numOfRows	    한 페이지 결과 수	      4	         0	        10	            한 페이지 결과 수Default: 10
pageNo	        페이지 번호	              4	         0	        1	            페이지 번호Default: 1
dataType	    응답자료형식	          4	         0	        XML	            요청자료형식(XML/JSON)Default: XML
dataCd	        자료 코드	             4	         1	        ASOS	        자료 분류 코드(ASOS)
dateCd	        날짜 코드	             3	         1	        DAY	            날짜 분류 코드(DAY)
startDt	        시작일	                 8	         1	        20100101	    조회 기간 시작일(YYYYMMDD)
endDt	        종료일	                 8	         1	        20100601	    기간 종료일(YYYYMMDD)(전일(D-1) 까지 제공)
stnIds	        지점 번호	             3	         1	        108	            종관기상관측 지점 번호 (활용가이드 하단 첨부 참조)

'''



class WEA_REQ_TYPE:
    SERVICEKEY              = 'serviceKey'      
    MAXNUM_OF_RESULT        = 'numOfRows'                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    PAGE_NO                 = 'pageNo'          
    DATATYPE                = 'dataType'          
    DATA_CD                 = 'dataCd'        
    DATE_CD                 = 'dateCd'    # D A T E      
    START_DT                = 'startDt'   
    END_DT                  = 'endDt'   
    AREA_NUM                = 'stnIds'   

class WEA_RES_TYPE:
    AREA_NAME                       = 'stnNm'       # 지점명
    TIME                            = 'tm'          # 시간
    AVG_TEMPERATURE                 = 'avgTa'       # 평균 기온
    MIN_TEMPERATURE                 = 'minTa'       # 최저 기온
    MIN_TEMPERATURE_TIME            = 'minTaHrmt'   # 최저 기온 시각
    MAX_TEMPERATURE                 = 'maxTa'       # 최고 기온
    MAX_TEMPERATURE_TIME            = 'maxTaHrmt'   # 최고 기온 시각
    RAIN_DURATION                   = 'sumRnDur'    # 강수 계속시간
    SUM_DURATION                    = 'sumRn'       # 일강수량

class WeatherData:
    def __init__(self):
        self.DataMgr = DataManager()
        self.SubUrl  = ''
        self.ResponParams = []
        
        self.ResParam = {
                WEA_RES_TYPE.AREA_NAME                      : '',
                WEA_RES_TYPE.TIME                           : '',
                WEA_RES_TYPE.AVG_TEMPERATURE                : '',
                WEA_RES_TYPE.MIN_TEMPERATURE                : '',
                WEA_RES_TYPE.MAX_TEMPERATURE                : '',
                WEA_RES_TYPE.RAIN_DURATION                  : '',
                WEA_RES_TYPE.SUM_DURATION                   : '',

        }

        url         = 'apis.data.go.kr'
        query       = '/1360000/AsosDalyInfoService/getWthrDataList'

        self.DataMgr.SetURL(url)
        self.DataMgr.SetQuery(query)
        self.DataMgr.SetParams(self.ResponParams)
        self.DataMgr.SetServiceKey(DataManager.ServiceKey_Encoding)
    
    def ConnectToData(self, addSubUrl = ''):
        self.DataMgr.ConnectToData(addSubUrl)

    def ConnectByRequest(self):
        self.DataMgr.ConnectToDataByRequests()

    def UpdateResponseParams(self, KeyList):
        ItemElements = self.DataMgr.GetItemElements()
        for item in ItemElements:
            datalist = []
            for Key in KeyList:
                data = item.find(Key)
                datalist.append([Key , data])

            self.ResponParams.append(datalist)
    
    def ShowResponseParams(self):
        
        for Param in self.ResponParams:
            print('-----------------------')
            print()
            for i in range(len(Param)):
                print(Param[i][1].text)
                print()


    def AddSubUrl(self, ResqueType, Data): # 'mntnNm', '지리산'
        self.SubUrl += '&' + ResqueType + '=' + Data
        return self.SubUrl

    def ClearSubUrl(self):
        self.SubUrl = ''
    
    def GetSubUrl(self):
        return self.SubUrl
    
    def TEST(self):

        ResList = [ 
            WEA_RES_TYPE.AREA_NAME  
        ,   WEA_RES_TYPE.TIME  
        ,   WEA_RES_TYPE.AVG_TEMPERATURE
        ,   WEA_RES_TYPE.MIN_TEMPERATURE
        ,   WEA_RES_TYPE.RAIN_DURATION
        ,   WEA_RES_TYPE.SUM_DURATION
        ]

        self.AddSubUrl(WEA_REQ_TYPE.MAXNUM_OF_RESULT, '50')
        self.AddSubUrl(WEA_REQ_TYPE.DATA_CD, 'ASOS')
        self.AddSubUrl(WEA_REQ_TYPE.DATE_CD, 'DAY')
        self.AddSubUrl(WEA_REQ_TYPE.START_DT, '20230520')
        self.AddSubUrl(WEA_REQ_TYPE.END_DT, '20230523')
        self.AddSubUrl(WEA_REQ_TYPE.AREA_NUM, '108')
        
        SubUrl = self.GetSubUrl()

        self.ConnectToData(SubUrl)
        self.UpdateResponseParams(ResList)
        self.ShowResponseParams()

