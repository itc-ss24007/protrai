# s24007
# 沖縄県の推計人口のページより最新情報をスクレイピングするコード
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = 'Shift_JIS'

soup = BeautifulSoup(html.text,'html.parser')
# tableを取得
table = soup.find('table',class_='table1 font2 gyo5')

#tableの行を取得
rows = table.find_all('tr')

for i,row in enumerate(rows):
    if i>=3:
        break
    cells = row.find_all('td')
    row_data =[cells[j].get_text().replace("\n","") for j in range(2)]
    print(':'.join(row_data))
