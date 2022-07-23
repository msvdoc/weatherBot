GIS_YK_TOMMOROW = "https://www.gismeteo.ru/weather-yuzhno-kurilsk-4896/tomorrow/"
GIS_YS_TOMMOROW = "https://www.gismeteo.ru/weather-yuzhno-sakhalinsk-4894/tomorrow/"
GIS_BLG_TOMMOROW = "https://www.gismeteo.ru/weather-blagoveshchensk-4848/tomorrow/"

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Это для проверки можно парсить или нет:
#import requests
#header = {'User-Agent': 'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
#session = requests.Session()
#request = session.get("http://lostfilm.tv/series/" , headers = header)
#print(request)
#Если получен ответ от сайта 200 (могу парсить данные)

ua = UserAgent()
user = ua.ie
headerMy = {'User-Agent':str(user)}



#HEADER_MY = {'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#            'user-agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400'}

#Захожу на страницу Гисметео с погодой в Южно-Курильске---------------------------------------------
#response = requests.get(GIS_YK_TOMMOROW, headers = headerMyuser)
response = requests.get(GIS_YK_TOMMOROW, headers = headerMy)
soup = BeautifulSoup(response.text, 'lxml')
#Извлекаю температуру на завтра
tempYKTommor = soup.find_all('span', class_='unit unit_temperature_c')
#----------------------------------------------------------------------------------------------------

#Захожу на страницу Гисметео с погодой в Южно-Сахалинске---------------------------------------------
response = requests.get(GIS_YS_TOMMOROW, headers = headerMy)
soup = BeautifulSoup(response.text, 'lxml')
#Извлекаю температуру на завтра
tempYSTommor = soup.find_all('span', class_='unit unit_temperature_c')
#----------------------------------------------------------------------------------------------------

#Захожу на страницу Гисметео с погодой в Благовещенске---------------------------------------------
response = requests.get(GIS_BLG_TOMMOROW, headers = headerMy)
soup = BeautifulSoup(response.text, 'lxml')
#Извлекаю температуру на завтра
tempBlgTommor = soup.find_all('span', class_='unit unit_temperature_c')
#----------------------------------------------------------------------------------------------------
