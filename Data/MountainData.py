
from Data.DataManager import *

class MNT_REQ_TYPE:
    NAME                    = 'mntnNm'          
    HEIGHT                  = 'mntnHght'        
    ADDRESS                 = 'mntnAdd'         
    INFO_AREA               = 'mntnInfoAraCd'   
    INFO_SEASON             = 'mntnInfoSsnCd'   
    INFO_THEME              = 'mntnInfoThmCd'   
    SERVICEKEY              = 'ServiceKey'      
    PAGE_NO                 = 'pageNo'          
    MAXNUM_OF_RESULT        = 'numOfRows'                                                                                                                                                                                                                                                                                                                                                                                                                                                           

class MNT_RES_TYPE:
    NAME                    = 'mntnnm'
    HEIGHT                  = 'mntninfohght'
    ADDRESS                 = 'mntninfopoflc'
    INFO_MAIN               = 'mntninfodtlinfocont'
    INFO_REL_PHONENUM       = 'crcmrsghtnginfodscrt'
    INFO_TRANSPORT          = 'pbtrninfodscrt'
    INFO_HIKING             = 'hkngpntdscrt'
    INFO_MAP_IMG            = 'mntninfomapdnldfilenm'
    INFO_RECOMMAND_MAP_IMG  = 'rcmmncoursimageseq'


class MountainData:

    def __init__(self):
        self.DataMgr = DataManager()
        self.SubUrl  = ''
        self.ResponParams = []
        
        self.ResParam = {
                MNT_RES_TYPE.NAME                   : '',
                MNT_RES_TYPE.HEIGHT                 : '',
                MNT_RES_TYPE.ADDRESS                : '',
                MNT_RES_TYPE.INFO_REL_PHONENUM      : '',
                MNT_RES_TYPE.INFO_TRANSPORT         : '',
                MNT_RES_TYPE.INFO_HIKING            : '',
                MNT_RES_TYPE.INFO_MAP_IMG           : '',
                MNT_RES_TYPE.INFO_RECOMMAND_MAP_IMG : ''
        }

        url         = 'api.forest.go.kr'
        query       = '/openapi/service/trailInfoService/getforeststoryservice'

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


            
            