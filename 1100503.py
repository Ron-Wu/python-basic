import time
import os
import prettytable

# print("開始")    #### 印出"開始"
# time.sleep(3)    #### 間隔三秒
# print("結束")    #### 印出"結束"

# for i in range(100, 1, -1):
#     os.system("cls")     #### 每次結束前會關掉重印出秒數，比較像是計時器
#     print(i, " 秒")
#     time.sleep(1)

# print(time.time())    #### 取得當前時間的總毫秒數
# time.sleep(1)
# print(time.time())

# while True:            #### 因為永遠為True，程式碼會一直跑
#     os.system("cls")
#     print(time.strftime("%Y-%m-%d %H:%M:%S"))
#     print()
#     time.sleep(1)

# while True:            #### 設定一個固定時間break
#     os.system("cls")
#     datetime = time.strftime("%Y-%m-%d %H:%M:%S")
#     print(datetime)
#     if datetime == "2021-05-03 09:34:00":
#         print("Time out")
#         break
#     time.sleep(1)

# p=prettytable.PrettyTable(["Ide" , "Title"], encoding = "utf-8")   #### 利用prettytable來製作成表格
# # p.align["Ide"] = "c"    #### 對齊方式，"l"靠左 "c"置中 "r"靠右
# p.align["Title"] = "l"

# p.add_row(["1" , "aaaa"])
# p.add_row(["2" , "bbbb"])
# p.add_row(["3" , "cccc"])
# print(p)

# import colorama

# colorama.init(True)
# print("ABC")
# print(colorama.Style.BRIGHT + "ABC")
# print(colorama.Fore.MAGENTA + "ABC")
# print(colorama.Fore.RED + "ABC")
# print(colorama.Back.GREEN + "   ")    ####  純色塊或背景

# import wx          
# import test0503              #### 匯入test模組

# t = wx.App()
# p = test0503.MyFrame2(None)
# p.Show()
# p.SetTitle("456")   #### 更改檔案名字
# # wx.MessageBox("Hi")
# t.MainLoop()


# import wx          
# import test0503              #### 匯入test0503模組

# class MyFrame2(test0503.MyFrame2):    #### 類別繼承：繼承後重設的函式會被替代掉，其餘不變的完全繼承
#     def btn_clk( self, event ):
#         # wx.MessageBox("Hiiiiiii")   #### 按下button會跳出視窗的函式
#         wx.MessageBox(self.AAA.GetLabel())
#         self.AAA.SetLabel("BBB")
#         # event.Skip()
# t = wx.App()
# p = MyFrame2(None)
# p.Show()
# p.SetTitle("123456")   #### 更改檔案名字
# # wx.MessageBox("Hi")
# t.MainLoop()


import wx          
import test0503              #### 匯入test0503模組

import codecs

class MyFrame2(test0503.MyFrame2):    #### 類別繼承：繼承後重設的函式會被替代掉，其餘不變的完全繼承
    def btn_clk( self, event ):

        # wx.MessageBox("Hiiiiiii")   #### 按下button會跳出視窗的函式

#         wx.MessageBox(self.AAA.GetLabel())
#         self.AAA.SetLabel("BBB")

#         wx.MessageBox(self.m_textCtrl1.GetValue())
#         self.m_textCtrl1.SetValue("")

#         self.m_comboBox1.Append("AAAA")
#         self.m_comboBox1.Append("BBBB")

#         wx.MessageBox(str(self.m_comboBox1.GetSelection()))
#         self.m_comboBox1.Setselection(2)
#         self.m_comboBox1.clear()

#         wx.MessageBox(self.m_filePicker1.SetPath("D:\\"))  #### 可寫絕對路徑，但button後會帶入絕對路徑
#         wx.MessageBox(self.m_filePicker1.GetPath())

#         wx.MessageBox(self.m_filePicker1.GetPath())  #### 直接getpath得到的是當前檔案的路徑

#         self.m_hyperlink1.SetURL("https://www.softicons.com")

#         self.m_grid1.AppendCols(1)
#         self.m_grid1.AppendRows(1)
#         self.m_grid1.SetColLabelValue(2, "555")
#         self.m_grid1.SetRowLabelValue(2, "666")
#         self.m_grid1.SetCellValue(1, 2, "test...")
#         self.m_grid1.SetSize(10, 10)   #### (寬，高)
#         print(self.m_grid1.GetSize())
        
        # self.m_grid1.Hide()
        q = test0503.MyFrame3(None)
        q.Show()
        self.Hide()    #### 隱藏當前的檔案

#         self.m_textCtrl1.Enabled = False  #### enabled設置成false後，輸入方塊變為無法使用

#         with codecs.open("3333.jpg", "rb") as f:
#             b = wx.Bitmap(wx.Image(f, wx.BITMAP_TYPE_PNG))
#             self.m_bitmap1.SetBitmap(b)
        
#         p = wx.FileSelector(                  #### 
#             "請選擇",
#             wildcard = "Python檔案|*.py",     #### wildcard = 檔案篩選方式,
#             flags = wx.FD_OPEN                ####  flags = 選擇器類型
#         )
#         wx.MessageBox(p)

#         self.m_timer1.Start(1000)

    def exec(self, event):
        self.m_textCtrl1.SetValue(time.strftime("%Y-%m-%d %H:%M:%S"))

        event.Skip()
t = wx.App()
p = MyFrame2(None)
p.Show()
p.SetTitle("記事本")   #### 更改檔案名字
# wx.MessageBox("Hi")
t.MainLoop()