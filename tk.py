import tkinter as tk  # 导入tk库
import datetime
import time
window = tk.Tk() #建立窗口
window.title('My Window') # 命名窗口
window.geometry('600x600')  # 设定窗口大小
title = tk.Label(window, text='600度*天试块计算器', bg='gray', font=('黑体', 12), width=50, height=1) #设定标题 bg=背景，font=字体，width=长，height=字高，height=标签高度（字体高度倍数）
title.pack()  # Label内容content区域放置位置，自动调节尺寸。放置lable的方法有：1）l.pack(); 2)l.place();
#############################################################################################################################
                                             #以上为窗口样式配置
def age():
    global start
    global end
    global count_days
    global Fdate
    iFdate = Fdate.get()
    start = time.mktime(time.strptime(iFdate, '%Y%m%d'))
    end = time.mktime(time.strptime(t, '%Y%m%d'))
    count_days = int((end - start)/(24*60*60))
    AGEofCON.set(count_days)
#############################################################################################################################
                                             #定义计算龄期函数
Fdate = tk.Entry(window, show=None, font=('Arial', 14))  # 成型日期输入
Fdate.place(x=10,y=40,anchor='nw') #布置成型日期输入框位置
Fdatep = tk.Label(window, text='输入格式为 yyyymmdd', font=('黑体', 12), width=20, height=1)
Fdatep.place( x=240, y=40)
#############################################################################################################################
                                             #以上为成型日期窗口配置
t = datetime.datetime.now().strftime('%Y%m%d')
Tdate = tk.Label(window, text='今天是：'+t, font=('黑体', 12))
Tdate.place(x=50,y=70)
#############################################################################################################################
                                             #以上为今日日期窗口配置
AGEofCON = tk.StringVar()
text = tk.Label(window, textvariable=AGEofCON, font=('黑体', 12), width=30, height=2)
text.place(x=10,y=100)
#############################################################################################################################
                                             #以上为龄期计算结果代码
submit = tk.Button(window,text='计算',font=('Arial', 12), width=10, height=1, command=age)
submit.place(x=240,y=70)
#############################################################################################################################
                                             #以上为上传按钮代码

window.mainloop() # 第6步，主窗口循环显示
