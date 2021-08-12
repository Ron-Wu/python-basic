# class Other:
#     def service():
#         print('do service...')
        
# o = Other()
# o.service()

# class Some:
#     def __init__(self, x):
#         self.x = x
    
#     def service(self, y):
#         print('do service...', self.x + y)

# s1 = Some(10)
# Some.service(s1, 5)  # do service... 15

# s2 = Some(20)
# Some.service(s2, 5)  # do service... 25

# service = Some.service
# service(s1, 5)       # do service... 15
# service(s2, 5)       # do service... 25

# x = input("請輸入：")  # 預設傳入皆為字串型態
# print("剛剛輸入了：", x)
# if int(x) >= 100 :
#     print("大於等於100")
# else:
#     print("小於100")
# if x=="1":
#     print("A")
# elif x=="2":
#     print("B")
# else:
#     print("C")

#### 型態 ####
# a = "123"
# b = int("123")
# c = 1.333333
# print("a 的型態: ", type(a))  ## a 的型態:  <class 'str'>
# print("b 的型態: ",type(b))  ## b 的型態:  <class 'int'>
# print("c 的型態: ",type(c))  ## c 的型態:  <class 'float'>


# x = input("數字 A: ")
# y = input("數字 B: ")

# print(x, "+", y, "=", int(x) + int(y))
# print(x, "-", y, "=", int(x) - int(y))
# print(x, "*", y, "=", int(x) * int(y))
# print(x, "/", y, "=", int(x) / int(y))

# x = input("數字 A: ")
# y = input("數字 B: ")

# print(x+ "+"+ y+ "="+str(int(x) + int(y)))
# print(x+ "-"+ y+ "="+str(int(x) - int(y)))
# print(x+ "*"+ y+ "="+str(int(x) * int(y)))
# print(x+ "/"+ y+ "="+str(int(x) / int(y)))

# date = input("日期(以空格為分, 例: 110 2 28): ")
# x = date.split(" ")   ## 用 "空格"去分割串列
# if x[1] > "12":
#     print("沒有此月份")
# elif x[1] < "1":
#     print("沒有此月份")
# if x[0] == "2" and x[1] > "28"

# print(x[0], "年")
# print(x[1], "月")
# print(x[2], "日")

# z = "/".join(x)
# print("日期: ", z)  ## 用 "/"去結合串列

# import sys
# print(sys.argv)

# import sys as x
# print(x.argv)

# from sys import argv ## 載入模組後，就不用再打模組名稱 
# print(argv)
 
# ##### url = input("請輸入網址: ", )
# ##### import webbrowser
# ##### webbrowser.open(url)

# import.os
# os.system("tasklist")          ## 取得當前在執行的程式
# os.system("dir")      
# os.system("start")             ## 叫出 cmd
# os.system("python 1100428.py")   ## 叫出其他 python 檔案
# p = os.popen("tasklist")
# x = p.read()
# if "chrome.exe" in x:    ## 查詢目前執行的程式是否已開啟
#     print("Already opened")
# else:
#     print("Not open")

# print(x)

# import sys 
# # sys.argv[1]
# if len(sys.argv[1]) > 1:
#     import os
#     os.system("start"+ str(sys.argv[1]))
# else:
#     print("請輸入網址")

# #### OK 
# import sys
# a = sys.argv[1]
# import os
# os.system("start "+ str(a))

# import sys
# a = sys.argv[1]
# b = sys.argv.count()
# print(b)
# import os
# if len(sys.argv) < 2:
#     print("請輸入網址")
# else:
#     os.system("start "+ str(a))

#### 老師範例 ####
import codecs

# f = codecs.open("1.txt", "w", "utf-8")
# f.write("test1  ")
# f.close()

# f = codecs.open("1.txt", "a", "utf-8")
# f.write("test2  ")
# f.close()

# f = codecs.open("1.txt", "a", "utf-8")
# f.write("test3")
# f.close()

f = codecs.open("1.txt", "r", "utf-8")
txt = f.read()
print("方法一: ",txt)
f.close()

# f = codecs.open("123.jpg", "rb")
# img = f.read()
# f.close()

# f = codecs.open("321.jpg", "wb")
# f.write(img)
# f.close

# with codecs.open("1.txt", "r", "utf-8") as f:  ## 會自動關閉，可以省略關閉檔案的步驟
#     txt = f.read()
#     print("方法二: ", txt)

import os

os.remove("1.txt")   #### 語法刪除不會跑到資源回收桶
os.mkdir("test")
os.rmdir("test")   #### 刪除空資料夾，若內部有檔案則無法刪除

d = os.listdir(".")   ####  (1) 列出當前檔案資料夾的檔案
print(d)

for d in os.listdir("."):
    print(d)

def read_dir(p):
    for d in os.listdir(p):
        if p + d == 
        print(d)
        read_dir(p + d)

os.chdir("D:/")                    #### 將工作路徑改到 D:/
print("工作路徑: ", os.getcwd())    #### 工作路徑:  D:\

with codecs.open("1.txt", "w", "utf-8") as f:  ####  會在新工作路徑 D:\ 生成一個 1.txt 檔案
    f.write("123\n321")
    
print(os.path.isdir("D:\\python\\1100428.py"))


def read_dir(p):
    for d in os.listdir(p):
        if os.path.isdir(p+d+"/"):
            read_dir(p+d+"/") 
        print(p+d)
read_dir("D:/")

def read_dir(p):
    for d in os.listdir(p):
        if os.path.isdir(p+d+"/"):   
            read_dir(p+d+"/") 
        print("111111", p+d)
read_dir("D:/")

def read_dir(p):
    for d in os.listdir(p):
        if os.path.isdir(p+d):    #### 可以把斜線拿掉不會出錯，也可往下層跑
            read_dir(p+d+"/") 
        print("222222", p+d)
read_dir("D:/")

def read_dir(p):
    for d in os.listdir(p):
        if os.path.isdir(p+d+"/"):
            read_dir(p+d)          #### 不可以把斜線拿掉會出錯，跑到第二層後就無法往下跑
        print("333333", p+d)
read_dir("D:/")

print(os.path.exists("D:\\python\\321.py"))   #### 判斷路徑是否存在 (True or False)

print("檔名:", os.path.basename("D:\\python\\321.py"))    #### 傳回路徑字串中的檔名
print("路徑:", os.path.dirname("D:\\python\\321.py"))     #### 傳回路徑字串中的路徑
print("123.jpg 檔案大小:", os.path.getsize("123.jpg")/1024, "KB")
print("321.py 檔案大小:", os.path.getsize("321.py")/1024, "KB")    #### 無法帶入不存在之檔案，會報錯

d = os.path.getsize("1.py")*5000
m = ["位元組", "KB", "MB", "GB", "TB"]
i = 0
while d >= 1024:
    d=d/1024
    i=i+1
print(round(d, 2), m[i])

#### HW 3 ####
x="" 

while x != "0":
    os.system("cls")
    if x == "1":
        print("列出檔案的程式碼")
    elif x == "2":
        print("列出資料夾的程式碼")
    elif x == "3":
        print("顯示檔案內容的程式碼")
    elif x == "4":
        print("刪除檔案的程式碼")
    elif x == "5":
        print("執行檔案的程式碼")
    elif x == "6":
        print("進入資料夾的程式碼")
    elif x == "7":
        print("刪除資料夾的程式碼")
    elif x == "8":
        print("回上層資料夾的程式碼")
    print("工作路徑: ", os.　)
    print(" (0) 離開程式\n (1) 列出檔案\n (2) 列出資料夾\n (3) 顯示檔案內容\n (4) 刪除檔案\n (5) 執行檔案\n (6) 進入資料夾\n (7) 刪除資料夾\n (8) 回上層資料夾 ")
    x=input("操作: ")