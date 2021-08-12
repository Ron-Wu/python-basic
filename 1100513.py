import cv2
import numpy as np


##### 讀取並顯示與限時關閉圖片
# i1 = cv2.imread("udn_image/3.png", 1) ####  1 => 一般(不含透明度);     -1 => 完整(包含透明度)，只有png的設計圖才有透明度;     0 => 灰階 
# # i2 = cv2.imread("udn_image/2.png", 1)
# # print(i1)   #### 彩色與灰階顯示的矩陣不同
# cv2.imshow("i1", i1)
# cv2.waitKey(0)
# cv2.imshow("i2", i2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()  #### 時間到或按下按鍵會關閉視窗


# i1 = cv2.imread("udn_image/15.png", 1) ####  1 => 一般(不含透明度);     -1 => 完整(包含透明度);     0 => 灰階
# cv2.imshow("i1", i1)
# print(cv2.waitKey(0))   #### 會返回使用者按下的按鍵ASCII碼


##### 圖片變數
# i1 = cv2.imread("udn_image/15.png", 1)
# print(i1.shape)   #### .shape[2] => 取得當前色彩空間的通道數量，灰階不顯示，彩色為3
# print("高: ", i1.shape[0])  #### .shape[0]=> 取得圖片高
# print("寬: ", i1.shape[1])  #### .shape[1] => 取得圖片寬
# cv2.imshow("i1", i1)
# print(cv2.waitKey(0))

##### 色彩空間轉換
# i1 = cv2.imread("udn_image/15.png", 1)
# i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2HSV) #### 
# cv2.imshow("i1", i1)
# cv2.waitKey(500)
# i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY) #### 轉灰階
# cv2.imshow("i1", i1)
# cv2.waitKey(500)
# print(cv2.waitKey(0))


##### 儲存圖片
# i1 = cv2.imread("udn_image/15.png", 1)
# i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2HSV) #### 
# cv2.imwrite("image/1.png", i1)    #### 儲存修改後的 png 圖片

# cv2.imwrite("image/1.jpg", i1, [cv2.IMWRITE_JPEG_QUALITY, 100])    #### 儲存修改後的 jpg 圖片，畫質比率: 100(最好) 壓縮比與畫質比率成反比  
# cv2.imwrite("image/2.jpg", i1, [cv2.IMWRITE_JPEG_QUALITY, 50])    #### 儲存修改後的 jpg 圖片，畫質比率: 50(中等) 壓縮比與畫質比率成反比
# cv2.imwrite("image/3.jpg", i1, [cv2.IMWRITE_JPEG_QUALITY, 0])    #### 儲存修改後的 jpg 圖片，畫質比率: 100(最差) 壓縮比與畫質比率成反比

##### 抓圖
# p1 = cv2.VideoCapture(0)
# if p1.isOpened() == True:
#     ret, i1 = p1.read()
#     if ret == True:
#         cv2.imshow("i1", i1)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()

#####　攝影機讀取，使用 while 和 改變秒數可得到影片
# p1 = cv2.VideoCapture(0)  #### 輸入 0 : 取得當前電腦攝影機來源
# while p1.isOpened() == True:
#     ret, i1 = p1.read()
#     if ret == True:
#         cv2.imshow("i1", i1)
#     if cv2.waitKey(50) != -1:1
#         break
# cv2.destroyAllWindows()


##### 影片讀取 改變秒數 可快轉或慢轉
p1 = cv2.VideoCapture("video/1.mp4")
while p1.isOpened() == True:
    ret, i1 = p1.read()
    if ret == True:
        cv2.imshow("i1", i1)
    if cv2.waitKey(42) != -1:
        break
cv2.destroyAllWindows()

#####　影片讀取
# p1 = cv2.VideoCapture("video/1.mp4")
# p1.set(1, 3000) #### 跳轉功能，只能設定當前影格，僅影片可用，攝影機無法使用
# print("影像寬度: ", p1.get(3))
# print("影像高度: ", p1.get(4))
# print("每秒的影格數: ", p1.get(5))　　　　#### 每秒影格數 = 框架速度 = fps
# print("總影格: ", p1.get(7))
# while p1.isOpened() == True:
#     ret, i1 = p1.read()
#     if ret == True:
#         # print("當前影格: ", p1.get(1))
#         cv2.imshow("i1", i1)
#     if cv2.waitKey(141) != -1:
#         break
# cv2.destroyAllWindows()

##### 錄製影片且儲存
# p1 = cv2.VideoCapture(0)
# w = int(p1.get(3))
# h = int(p1.get(4))

# p2 = cv2.VideoWriter("video/2.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 20, (w, h))
# while p1.isOpened() == True:
#     ret, i1 = p1.read()
#     if ret == True:
#         # print("當前影格: ", p1.get(1))
#         p2.write(i1)
#         cv2.imshow("i1", i1)
#     if cv2.waitKey(42) != -1:
#         break
# p2.release()
# cv2.destroyAllWindows()


# ##### 建立一張圖片
# m1 = np.full((300, 500, 3), (100, 100, 250), np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間
# m1 = np.full((300, 500, 3), (100, 250, 100), np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間
# m1 = np.full((300, 500, 3), (250, 100, 1000), np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間

# cv2.imshow("m1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##### 建立一張圖片
from PIL import ImageFont, ImageDraw, Image
# m1 = np.full((300, 500, 3), (255, 100, 0), np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間

# # cv2.line(m1, (101,250), (1000, 250), (123, 123, 255), 5)   #### 繪直線
# # cv2.rectangle(m1, (10, 10), (100, 100), (0, 255, 255), 2)  #### 繪空心矩形
# # cv2.rectangle(m1, (150, 150), (250, 250), (0, 255, 255), -1)  #### 繪實心矩形
# cv2.circle(m1, (150, 150), 50, (0, 0, 255), -1)  #### 繪實心圓形
# cv2.circle(m1, (250, 150), 50, (0, 0, 255), 2)   #### 繪空心圓形
# cv2.circle(m1, (150, 250), 50, (0, 0, 255), 2)   #### 繪空心圓形
# cv2.circle(m1, (250, 250), 50, (0, 0, 255), -1)  #### 繪實心圓形
# cv2.rectangle(m1, (150, 150), (250, 250), (0, 255, 255), -1)  #### 繪實心矩形

# m1=Image.fromarray(m1)
# ImageDraw.Draw(m1).text(
#     (1, 1),
#     ("G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G\n")*100,
#     (0, 250, 250),
#     ImageFont.truetype("SHOWG.TTF", 8)
# )
# m1 = np.array(m1)

# cv2.imshow("m1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##### 運算
# i1 = cv2.imread("udn_image/1.png", 1)
# i2 = cv2.imread("udn_image/2.png", 1)
# i3 = cv2.add(i1, i2)
# cv2.imshow("i1", i1)
# cv2.imshow("i2", i2)
# cv2.imshow("i3", i3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# i1 = cv2.imread("udn_image/1.png", 1)
# i3 = cv2.add(i1, (50, 50, 50, 50))  #### 彩圖須打4個，最後一個是透明度，若圖片本身沒支援，則值無差；灰階圖只需打一個數字。

# cv2.imshow("i1", i1)
# cv2.imshow("i3", i3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##浮水印
# i1 = cv2.imread("udn_image/1.png", 1)

# i2 = np.full(i1.shape, 0, np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間
# i2 = Image.fromarray(i2)
# ImageDraw.Draw(i2).text(
#     (100, 100),
#     ("G G G G G"),
#     (100, 100, 100),
#     ImageFont.truetype("SHOWG.TTF", 8)
# )
# i2 = np.array(i2)

# i3 = cv2.add(i1, i2)

# cv2.imshow("i1", i1)
# cv2.imshow("i2", i2)
# cv2.imshow("i3", i3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# i1 = cv2.imread("udn_image/1.png", 1)
# i2 = np.full(i1.shape, 0, np.uint8)   #### 顏色值(藍, 綠, 紅) 數字需再 0~255 之間
# i2 = Image.fromarray(i2)
# ImageDraw.Draw(i2).text(
#     (100, 100),
#     ("G G G G G"),
#     (100, 100, 100),
#     ImageFont.truetype("SHOWG.TTF", 100)
# )
# i2 = np.array(i2)
# i3 = cv2.subtract(i1, i2)  ####　減法
# i3 = cv2.absdiff(i1, i2)   #### 差異的絕對值，功能就是將兩張相片相減後取絕對值。
# i3 = cv2.absdiff(i1, (255, 255, 255, 255))  #### 差異的絕對值，功能就是將兩張相片相減後取絕對值。
# i3 = cv2.divide(i1, (10, 10, 10, 10))  #### 除法的數字不能帶太大，避免圖像趨近黑色。
# i3 = cv2.multiply(i1, (5,5,5,5))
# i4 = cv2.absdiff(i3, (255, 255, 255, 255))  #### 差異的絕對值，功能就是將兩張相片相減後取絕對值。
# i5 = cv2.bitwise_not(i1)  #### 不需與其他圖片做運算，本身即可達到負片效果。 效果與 absdiff 相似

#### numpy 的計算，可直接計算，無需考慮上限值(255) 若大於255，則 256=0、257=1、258=2.....
# i2 = i1 + 200
# i3 = i1 - 50
# i4 = i1 / 50
# i5 = i1 * 50 /50

# w = 500
# h = int((w/i1.shape[1])*i1.shape[0])

# h1 =500
# w1= int(h/i1.shape[0]*i1.shape[1])

# i6 = cv2.resize(i1, (w,h))  
# i7 = cv2.resize(i1, (w1,h1))  

# cv2.imshow("i1", i1)
# cv2.imshow("i2", i2)
# cv2.imshow("i3", i3)
# cv2.imshow("i4", i4)
# cv2.imshow("i5", i5)
# i6 =i5 / 50
# cv2.imshow("i6", i6)
# cv2.imshow("i7", i7)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

