
from Data.DataManager import *

import requests
from json import *
import tkintermapview
from tkinter import *


class APImap:
    def __init__(self) :
        self.DataMgr = DataManager()

        self.url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        self.ServiceKey = '4b26e7470a265bf96899caf9892dac65'

        self.spot = []
        self.spot_Store = []

    def getLatLng(self, addr):
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
        headers = {"Authorization": "KakaoAK " + self.ServiceKey}
        result = loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address']

        return float(match_first['x']), float(match_first['y'])
    
# 위도 경도를 얻는다. 
    def getLatLng(self, region, page_num):
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json' 

        params  = {'query': region,'page': page_num}
        headers = {"Authorization": "KakaoAK " + self.ServiceKey}

        places = requests.get(url, params=params, headers=headers).json()['documents']
        for place in places:
            X = float(place['x'])
            Y = float(place['y'])
            spot = (Y, X)
            self.spot.append(spot)
        return X,Y
    
    def Run(self, MountainName ):
        self.spot.clear() 
        for i in range(1,4):
            self.getLatLng(MountainName, i)

        self.My_label = LabelFrame(self.MapWindow)
        self.My_label.pack(pady=20)

        self.SetMarker(MountainName)

    def SetMarker(self, MountainName):
        self.map_widget = tkintermapview.TkinterMapView(self.My_label, width = 800, height = 600, corner_radius=0)

        self.spot.clear() 
        self.getLatLng(MountainName, 1)

        self.map_widget.set_position(self.spot[0][0], self.spot[0][1])
        self.map_widget.set_marker(self.spot[0][0], self.spot[0][1], MountainName)
        self.map_widget.set_zoom(7)
        self.map_widget.pack()

        self.spot_Store.append( self.spot[0] )

    def ClearSpotStore(self):
        self.spot_Store.clear()
        self.spot_Store = []

        


