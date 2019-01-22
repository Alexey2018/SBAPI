# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:11:05 2019

@author: tsiferov-aa
baa734e9-3a69-472a-8aa4-b3f98b686deb
"""

#from yandex_geocoder import Client
#print(Client.coordinates('Хабаровск, 60 октября, 150'))
#import yandex_geocoder as yg
#g = yg.yandex('Moscow Russia')
#print(g.text)
#new code API
#9dc2f628-77ef-4202-ad14-913e947114f4
#old key
#baa734e9-3a69-472a-8aa4-b3f98b686deb

import pandas
import requests
addr = 'Москва, Тверская улица, дом 7'
API = 'https://geocode-maps.yandex.ru/1.x/?apikey=9dc2f628-77ef-4202-ad14-913e947114f4&geocode='
print(addr)
print(type(addr))
print(API)
print(type(API))
print('REQUEST: ', API + addr)
try:
   r = requests.get(API + addr, verify = False)
   if r.status_code == 200:
       print('All is OK!')
   if r.status_code == 404:
       print('Page not exists!')
   #print(r.content)
   #print(r.status_code)
   #print(r.headers) 
   print(r.text)
except Exception:
   print('What the fuck?')

#print(r.text)
#https://geocode-maps.yandex.ru/1.x/?geocode=%27.urlencode(%27Москва,+Тверская+улица,+дом+7%27))
#r = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=baa734e9-3a69-472a-8aa4-b3f98b686deb'&geocode='Москва, Тверская улица')
#'https://geocode-maps.yandex.ru/1.x/?apikey=baa734e9-3a69-472a-8aa4-b3f98b686deb&geocode='москва,'+ 'тверская улица,'+'дом'+'7'#