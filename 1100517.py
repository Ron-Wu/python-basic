import cv2
import numpy as np

m1 = cv2.imread("images/m1.png", 1)  
m1 = cv2.imread("images/m2.jpg", 1)  
m2 = cv2.imread("images/m2.jpg", 1)  

m2 = cv2.flip(m1, 1) #### 1 => 左右翻轉，0 => 上下翻轉，-1 => 左右上下皆翻轉

### cv2.warpAffine(圖像變數, 變換矩陣, 輸出的圖像大小)
### cv2.getRotationMatrix2D(旋轉中心, 角度, 縮放比率) 
m2 = cv2.warpAffine(m1, cv2.getRotationMatrix2D((30, 30), 270, 1), (500, 500))

### 老師
m2[100:324,100:324]=m1
m2[100:200,100:200]=m1[0:100, 0:100]
m2 = m1[::,::2]
m2[100:324:2, 100:324:2]=m1[0:224:2, 0:224:2]
print(m2.shape)


### 圖像變數[Y軸範圍起始:Y軸範圍結束, X軸範圍起始: X軸範圍結束]
m2 = m1[:, :, 2] #### [高, 寬, 色彩]最後一個值可以取色彩維度  0藍，1綠，2紅
print(m2.shape)  ####因色彩只取一個色，顧維度改為二維會改顯示灰階

print(m1.shape)
m2[:50, :50]=m1[100:150, 100:150]  
m2[0:100, 0:100] = m1[100:200, 100:200]
m2[0:100:2, 0:100:2] = m1[0:100:2, 0:100:2]

### 白平衡 通常用在風景照較明顯，也有些圖片是已經在照相時用了白平衡效果
m3 = m2.copy()
b = m2[:,:,0].mean()
g = m2[:,:,1].mean()
r = m2[:,:,2].mean()
m3[:,:,0] = cv2.multiply(m2[:,:,0], ((b+g+r)/(b*3)))
m3[:,:,1] = cv2.multiply(m2[:,:,1], ((b+g+r)/(b*3)))
m3[:,:,2] = cv2.multiply(m2[:,:,2], ((b+g+r)/(b*3)))

cv2.imshow("m2", m2)
cv2.imshow("m3", m3)

###　影像二值化 A :
m1 = cv2.imread("images/m1.png", 0)  
m2 = m1.copy()
th, m2 = cv2.threshold(m1, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)  ## cv2.THRESH_OTSU  只能用在灰階圖，需改成灰階圖才能運行

### 但用以下分開計算B藍G綠R紅的方法也可操作非灰階圖，但無法整張圖有個別的門檻值
m1 = cv2.imread("images/m1.png", 1)  
m2 = m1.copy()
th, m2[:,:,0] = cv2.threshold(m1[:,:,0], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)  
print(th)
th, m2[:,:,1] = cv2.threshold(m1[:,:,1], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(th)
th, m2[:,:,2] = cv2.threshold(m1[:,:,2], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(th)

### 影像二值化 B : 也可用上述做法，只接受灰階圖，也可用上圖片切成數小塊，可以每小塊都有個別的門檻值
### 結果圖像 = cv2.adaptiveThreshold(圖像變數, 最大值, 方法一, 方法二, 區塊大小, 微調值)
### 方法一：cv2.ADAPTIVE_THRESH_MEAN_C：計算區塊大小內的平均值再減去微調值
###        cv2.ADAPTIVE_THRESH_GAUSSIAN_C：計算區塊大小內的高斯加權平均值值再減去微調值
### 方法二: cv2.THRESH_BINARY (大於門檻質變255，小於變0)
###　　　　　cv2.THRESH_BINARY_INV (大於門檻質變0，小於變255)
### 區塊大小只能單數1,3,5,....
m2 = cv2.adaptiveThreshold(
m1[:,:,0], 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 3, 10)    

m2 = cv2.adaptiveThreshold(
m1[:,:,1], 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 3, 10)   

m2 = cv2.adaptiveThreshold(
m1[:,:,2], 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 3, 10)    

### 影像邊緣偵測
# 結果圖像=cv2.Canny(圖像變數,門檻值1,門檻值2) 門檻值可互相調換。
m2 = cv2.Canny(m1, 100, 50)

### 影像平均值模糊化
### 結果圖像=cv2.blur(圖像變數, 範圍大小)  範圍大小:Tuple類型：(寬, 高)
### 範圍大小值越大越模糊，寬長差異越大可以有垂直模糊或水平模糊效果
m2 = cv2.blur(m1, (5,10))
#區域馬賽克
m2 = m1.copy()
m2[100:150] = cv2.blur(m1[100:150], (100,1)) 


### 影像中值模糊化
# 結果圖像=cv2.medianBlur(圖像變數, 處理數量)   處理數量:因為是中位數處理，只能填單數
m3 = cv2.medianBlur(m1, 9)


### 影像銳利化
# 結果圖像=cv2.equalizeHist(圖像變數) 只接受灰階圖，常使用在風景圖
m2 = m1.copy()
m2[:,:,0] = cv2.equalizeHist(m1[:,:,0]) 
m2[:,:,1] = cv2.equalizeHist(m1[:,:,1]) 
m2[:,:,2] = cv2.equalizeHist(m1[:,:,2]) 


### 形態學
### 結果圖像=cv2.erode(圖像變數, 結構陣列) 結構陣列: np.ones(範圍大小) 範圍大小為Tuple類型：(高, 寬)
# 侵蝕：色彩值低的會侵蝕色彩值高的
m2 = cv2.erode(m1, np.ones((5,5)))
# 膨脹：色彩值高的會侵蝕色彩值低的
m3 = cv2.dilate(m1, np.ones((5,5)))
m1 = cv2.imread("images/m4.png", 1)
m2 = m1.copy()
m3 = m2.copy()
m2[:200, :100] = cv2.dilate(m1[:200, :100], np.ones((1,1)))
m3[:200, :100] = cv2.erode(m2[:200, :100], np.ones((1,1)))

# 結果圖像=cv2.morphologyEx(圖像變數, 方法, 結構陣列)
m2 = cv2.morphologyEx(m1, cv2.MORPH_OPEN,np.ones((5, 5)))  #### 先執行侵蝕後執行膨脹
m3 = cv2.morphologyEx(m1, cv2.MORPH_CLOSE,np.ones((5, 5)))  #### 先執行膨脹後執行侵蝕
m4 = cv2.morphologyEx(m1, cv2.MORPH_GRADIENT,np.ones((5, 5))) #### 執行膨脹與侵蝕產生的變化差

### 色彩篩選
# 結果圖像=cv2.inRange(圖像變數, 顏色下限, 顏色上限)
# 圖像變數: 傳回一張與傳入變數相同大小的黑白圖像，在範圍內的像素會被設白色，否為則黑色
# 顏色上下限: 依照色彩空間的不同可傳進陣列或單一數值

# 局部篩選
m2 = m1.copy()
m2[0:150, 0:150, 0] = cv2.inRange(m1[0:150, 0:150, 0], 10, 100)
m2[0:150, 0:150, 1] = cv2.inRange(m1[0:150, 0:150, 1], 90, 150)
m2[0:150, 0:150, 2] = cv2.inRange(m1[0:150, 0:150, 2], 180,255)

m1 = cv2.imread("images/m1.png", 1)  
m2 = cv2.inRange(m1, (100, 100, 100), (255, 255, 255))

#### 取得輪廓：輪廓點, 輪廓階層資料=cv2.findContours(圖像變數(灰階圖像), 類型, 方法)
## 類型：cv2.RETR_EXTERNAL：只儲存最外層的輪廓
##       cv2.RETR_LIST：儲存所有輪廓，但不建立階層資料
##       cv2.RETR_CCOMP：儲存所有輪廓，但階層資料只包留兩層，首階層為物件外圍，第二階層為內部空心部分的輪廓，如果更內部有其餘物件，包含於首階層
##       cv2.RETR_TREE：儲存所有輪廓與其對應的階層資料
## 方法： cv2.CHAIN_APPROX_NONE：儲存所有輪廓點
##        cv2.CHAIN_APPROX_SIMPLE：簡化輪廓點，一條線只儲存頭尾
a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


## 取得輪廓：cv2.drawContours(圖像變數, 存取全部輪廓的變數, 要繪製的輪廓索引, 顏色, 粗細)
m3 = np.full(m1.shape, 255, np.uint8)
cv2.drawContours(m3, a, 1, (0, 0, 255), 1)

x, y, w, h = cv2.boundingRect(a[1])
cv2.rectangle(m1, (x, y), (x+w, y+h), (255, 255, 255), 3)
m1 = m1[y:y+h, x:x+w]
cv2.imwrite("images/m1-logo.png", m1)

# print(th)
# print(m2)
cv2.imshow("m1", m1)
cv2.imshow("m2", m2)
cv2.imshow("m3", m3)
# cv2.imshow("m4", m4)
cv2.waitKey(0)
cv2.destroyAllWindows
