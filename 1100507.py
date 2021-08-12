#####  SQL 語法
## SELECT * FROM `member` INNER JOIN `tel` ON `member`.`id` = `tel`.`member_id`
## SELECT `member`.*, `tel`.`tel` FROM `member` INNER JOIN `tel` ON `member`.`id` = `tel`.`member_id`    可以藉由前面 (`member`.*, `tel`.`tel`) 篩選不要列出那麼多欄

## SELECT `M`.*, `T`.`tel` FROM `member` AS `M` INNER JOIN `tel` AS `T` ON `M`.`id` = `T`.`member_id`     在SQL語法中不會有順序性的問題，資料表取一個別名避免程式碼冗長或區分不同資料表中的欄位名稱
## SELECT `M`.*, `T`.`id`AS `tel_id` FROM `member` AS `M` INNER JOIN `tel` AS `T` ON `M`.`id` = `T`.`member_id`    別名 (`T`.`id`AS `tel_id`) 區分不同資料表中的欄位名稱


## SELECT CONCAT('姓名: ', `name`, '\n生日: ', `birthday`) AS `資料` FROM `member`    字串串接，會先將資料串接後才更新進資料表中


##### 網路爬蟲
import requests
import codecs
p1 = requests.get(
    "https://www.ntub.edu.tw/",  #### 網頁有http"s"通常是有憑證，若顯示不安全網站，可能為憑證過期。
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Language" : "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3"
        "Accept-Language" : "q=0.8,en-US;zh-TW,zh;q=0.5,en;q=0.3"
    },
    verify = False  #### 因為網站憑證過期，出現類似local issuer certificate (_ssl.c:1091)'錯誤碼，故需添加
)
print("讀取狀態: ", p1.status_code)   ####  可從 http 狀態碼得知其狀態內容
print("回應的檔頭: ", list(p1.headers.items()))  
for k,v in p1.headers.items():  #### items + 迴圈取得 headers 中 的 key&value
    print(k,"=>",v)

print("編碼: ", p1.encoding)  #### 取得網頁編碼
p1.encoding = "big5"

with codecs.open("1.html", "w", "utf-8") as f:
    f.write(p1.text)


import requests
import codecs
p1 = requests.get(
    "https://www.ntub.edu.tw/var/file/0/1000/randimg/mobileadv_5672_5823941_26880.jpg",  #### 網頁有http"s"通常是有憑證，若顯示不安全網站，可能為憑證過期。
    headers = {
        "Accept" : "image/webp,*/*",
        "Accept-Language" : "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3"
    },
    verify = False  #### 因為網站憑證過期，出現類似local issuer certificate (_ssl.c:1091)'錯誤碼，故需添加
)
with codecs.open("1.jpg", "wb") as g:
    g.write(p1.content)

print("內容:")
print(p1.text)
import csv
import requests
import codecs
import io
p1 = requests.get(
    "https://data.taipei/api/getDatasetInfo/downloadResource?id=d58d2528-a453-4ffc-b231-fd3f4ef24b34&rid=f6e5fea2-e3cb-4107-952d-d42860226d80",
    params = {
        "id" : "d58d2528-a453-4ffc-b231-fd3f4ef24b34",
        "rid" : "f6e5fea2-e3cb-4107-952d-d42860226d80"
    }
)   
p1.encoding = "big5"
print(p1.text)

with codecs.open("1.csv", "w", "utf8") as f:
    f.write(p1.text)

with codecs.open("1.csv", "r", "utf8") as f:
    data = list(csv.reader(f))
    for d in data:
        print(d[0], d[1]) 

f = io.StringIO(p1.text)
data = list(csv.reader(f))
for d in data:
    print(d[0], d[1])

