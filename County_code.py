import requests as req
import json

author = ""
dic = {}

for i in range(100):
    print(i)
    if i < 10:
        num = "0" + str(i)
    else:
        num = str(i)
    url = f"https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-D0047-0{num}?Authorization={author}&downloadType=WEB&format=JSON"

    res = req.get(url)
    data = json.loads(res.text)

    try:
        county = data['cwaopendata']['dataset']['locations']['locationsName']
        code = f"F-D0047-0{num}"
        dic.update({county : code})
    except:
        pass
with open('new.json', 'w', encoding='utf8') as jfile:
    json.dump(dic, jfile, ensure_ascii=False, indent = 4)
