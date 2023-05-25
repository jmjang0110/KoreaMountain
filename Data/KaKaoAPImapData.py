
from Data.DataManager import *

import requests
from json import *
import tkintermapview
from tkinter import *


class KaKaoAPImap:
    def __init__(self) :
        self.DataMgr = DataManager()

        self.url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        self.ServiceKey = '4b26e7470a265bf96899caf9892dac65'


        self.MapWindow = Tk()

        self.spot = []

    def getLatLng(self, addr):
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
        headers = {"Authorization": "KakaoAK " + self.ServiceKey}
        result = loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address']

        return float(match_first['x']), float(match_first['y'])
    
    def getLatLng(self, region, page_num):
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json' 

        params = {'query': region,'page': page_num}
        headers = {"Authorization": "KakaoAK " + self.ServiceKey}

        places = requests.get(url, params=params, headers=headers).json()['documents']
        for place in places:
            X = float(place['x'])
            Y = float(place['y'])
            spot = (Y, X)
            self.spot.append(spot)



        return X,Y
    
    def Run(self):
        self.MapWindow.geometry('400x500')

        self.spot.clear()
        for i in range(1,4):
            self.getLatLng('황금산', i)

        My_label = LabelFrame(self.MapWindow)
        My_label.pack(pady=20)

        map_widget = tkintermapview.TkinterMapView(My_label, width = 800, height = 600, corner_radius=0)


        map_widget.set_position(self.spot[0][0], self.spot[0][1])
        map_widget.set_marker(self.spot[0][0], self.spot[0][1])
       
        map_widget.set_zoom(7)


        map_widget.pack()
        self.MapWindow.mainloop()

        import codecs
        f = codecs.open('map.html', 'r')
        print(f.read())
        


