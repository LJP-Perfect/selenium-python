# coding=UTF-8
import win32gui
import win32con
import win32clipboard as w
import ctypes
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import tkinter as tk
from tkinter import messagebox

count = 0
max=17
refreshtime=30
def getHTMLText(url):
    time.sleep(refreshtime)
    driver.get(url)  # 获取网页
    time.sleep(5)
    if count==0:
        driver.find_element_by_xpath('//*[@id="password_input"]').send_keys('IlovePython')
        driver.find_element_by_xpath('//*[@id="login_submit"]').click()
        time.sleep(5)
    return driver.page_source

def fillUnivlist(html):
    soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    tag = soup.find_all('div', attrs={'class': 'text_cell_render rendered_html'})
    return tag


def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def hit_me():
    #tc1=messagebox.askokcancel(title='hello',message='hello word') #弹窗 return True/False
    #print (tc1)
    #tc2=messagebox.askquestion(title='hello',message='hello word') #return yes/no
    #print (tc2)
    tc3=messagebox.showinfo(title='hello',message='hello word')  # return ok
    print (tc3)




if __name__ == '__main__':

    window = tk.Tk()
    window.title('my window')
    window.geometry('400x200')

    options = webdriver.Firefox()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument(
        'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    driver = webdriver.Firefox(firefox_options=options)
    driver=webdriver.Safari()
    driver.minimize_window()
    length=0
    msg=''
    content=''
    zerocount=0
    while 1==1:
        try:
            url = 'http://218.108.45.11:17215/notebooks/Final%20Exam/Final%20Exam.ipynb'  # 要访问的网址
            html = getHTMLText(url)  # 获取HTML
            tag = fillUnivlist(html)
            length=len(tag)

            if length==0:
                zerocount+=1
            count+=1
            if length>max:
                break
            if count == 60 or zerocount==3:
                driver.close()
                time.sleep(3)

                driver = webdriver.Chrome()
                driver.minimize_window()
                count=0
                zerocount=0
            print(length)
        except Exception:
            msg = 'error'
            break
    for i in range(max,length):
        content+=str(tag[i])
    soup = BeautifulSoup(str(content), 'html.parser')

    if msg=="error":
        print("error")
        #普通弹框
        tk.Message(window,text="程序出错了，请重启",width=400).pack()
        window.mainloop()
        #发送到qq窗口
        #to_who = 'Python宇宙第一'
        #send_qq(to_who, "程序出错了，请重启")
    else:
        msg= soup.find_all('h2')
        #普通弹框
        tk.Message(window, text=str(msg), width=400).pack()
        window.mainloop()
        #发送到qq窗口
        #to_who = 'Python宇宙第一'
        #send_qq(to_who, str(msg))
