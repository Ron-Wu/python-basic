import pymysql

link = pymysql.connect(    #### 連結變數=pymysql.connect(
host = "localhost",
user = "root",
passwd = "",
db = "20210506" ,
charset = "utf8",
port = 3306,
)

cur = link.cursor()    #### 指令操作變數=連結變數.cursor()

# title = input("title: ")
# source = input("source: ")
# description = input("description: ")
# time = input("time: ")

# cur.execute(
#     "INSERT INTO `news`(`title`, `source`, `description`, `time`) VALUES(%s, %s, %s, %s)", 
#     [title, source, description, time]   #### 設成變數，可透過 python 新增使用者輸入的新資料
# )

# in_list = [
#     input("title: "),
#     input("source: "),
#     input("description: "),
#     input("time: ")
# ]

# cur.execute(
#     "INSERT INTO `news`(`title`, `source`, `description`, `time`) VALUES(%s, %s, %s, %s)", 
#     in_list   #### 設成變數，可透過 python 新增使用者輸入的新資料
# )
# link.commit()


# #### 字典"新增"寫法：
# in_dic = {
#     "a" : input("title: "),
#     "b" : input("source: "),
#     "c" : input("description: "),
#     "d" : input("time: ")
# }

# cur.execute(
#     "INSERT INTO `news`(`title`, `source`, `description`, `time`) VALUES(%(a)s, %(b)s, %(c)s, %(d)s)", 
#     in_dic   #### 設成變數，可透過 python 新增使用者輸入的新資料
# )
# link.commit()


##### 字典"修改"寫法：因為 dic 沒有順序性，修改時比較不會出錯，但 list 有順序性，會出錯
# in_dic = {
#     "a" : input("id: "),
#     "b" : input("time: "),
# }

# cur.execute(
#     "UPDATE `news` SET `TIME` = %(b)s WHERE `id` = %(a)s", 
#     in_dic   
# )
# link.commit()

##### cur.fetchall()：一次跑出整表資料，可混用，會接續著讀，需在cur.fetchone()下方才不會出錯
# cur.execute("SELECT * FROM `news`")    #### 指令操作變數.execute(SQL指令, 要帶入SQL中的變數)：傳送SQL指令
# for d in cur.fetchall():
#     print(d[0], d[1])

##### cur.fetchall()：一次跑一筆資料，寫n次往下抓n筆資料
# cur.execute("SELECT * FROM `news`")    #### 指令操作變數.execute(SQL指令, 要帶入SQL中的變數)：傳送SQL指令
# d = cur.fetchone()
# print(d[0], d[1])

# d = cur.fetchone()
# print(d[0], d[1])

# d = cur.fetchone()
# print(d[0], d[1])


# ##### 查詢總資料筆數
# cur.execute("SELECT * FROM `news`")    #### 指令操作變數.execute(SQL指令, 要帶入SQL中的變數)：傳送SQL指令
# print("資料數量: ", cur.rowcount)   #### rowcount 是變數，非函數，故不需括號 

# ##### 查詢總資料筆數
# cur.execute("SELECT `title`, `time` FROM `news`")    #### 帶入參數不同，會有不同結果
# # print("資料數量: ", cur.rowcount)   #### rowcount 是變數，非函數，故不需括號 
# for d in cur.fetchall():
#     print(d[0], d[1])

###### cur.lastrowid指令需接續，否則無法取得最後新增的流水號
# in_dic = {
#     "a" : input("title: "),
#     "b" : input("source: "),
#     "c" : input("description: "),
#     "d" : input("time: ")
# }

# cur.execute(
#     "INSERT INTO `news`(`title`, `source`, `description`, `time`) VALUES(%(a)s, %(b)s, %(c)s, %(d)s)", 
#     in_dic   #### 設成變數，可透過 python 新增使用者輸入的新資料
# )
# link.commit()
# print("剛剛新增的那筆資料ID: ", cur.lastrowid)

import prettytable

cur.execute("SELECT `id`, `title`, `source` FROM `news`")
p = prettytable.PrettyTable(["id", "title", "source"], encoding="utf8")
p.align["title"] = "l"
for d in cur.fetchall():
    p.add_row(d)
    print(d)
print(p)
link.close()  #### 一定要關閉連線!!!