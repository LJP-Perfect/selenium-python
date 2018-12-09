# 运行前注意事项

此程序运行前的步骤有一点点复杂，程序运行后直到有Final Exams有更新题目才会停止运行。抓取到新题目后会根据选用的通知类型来通知你。



> 下载webdriver

选择下面一种webdriver进行下载

注：下载的driver类型，在你电脑上必须确认是否已安装对应的浏览器（推荐firefox）

- firefox：https://github.com/mozilla/geckodriver/releases/tag/v0.23.0

- chrome：https://chromedriver.storage.googleapis.com/index.html?path=2.44/
- safari：https://webkit.org/blog/6900/webdriver-support-in-safari-10/

下载后将解压后的.exe文件放在环境变量Path里路径下（比如C:\Windows或C:\Windows\System32）

程序默认使用Chorme 的webdriver

![1544365497403](C:\Users\Lee\AppData\Local\Temp\1544365497403.png)

如果要使用Firefox的webdriver配置如下图

![1544365576221](C:\Users\Lee\AppData\Local\Temp\1544365576221.png)

Safari的webdriver的对应配置没使用过，可以按下图试试看

![1544365887636](C:\Users\Lee\AppData\Local\Temp\1544365887636.png)



> 安装第三方库

pip install beautifulsoup4

pip install selenium



> data.py的需要修改的变量

以下三个变量需要根据实际情况修改

```python
max=17						#max的值为当前Final Exams的题目数+1   
refreshtime=30				#爬取数据时间间隔（单位为s）
to_who='Python宇宙第一'		 #见下第二种通知类型（选择第一种通知类型可不配置）
```



> 通知类型

1. 普通弹框通知（简单，推荐）

![1544364861911](C:\Users\Lee\AppData\Local\Temp\1544364861911.png)

弹框通知如图：

![1544365017476](C:\Users\Lee\AppData\Local\Temp\1544365017476.png)

2. ZB QQ对话框

此变量为你**聊天对话框名（群聊名称或好友名）**如下图

![1544362927198](C:\Users\Lee\AppData\Local\Temp\1544362927198.png)

且此**对话框必须单独存在**，不能如下图多个对话框开在一起，还有一点对话框不能**最小化**但是**可以被其他软件界面覆盖**。

![1544363304978](C:\Users\Lee\AppData\Local\Temp\1544363304978.png)

QQ通知如图：

![1544365304079](C:\Users\Lee\AppData\Local\Temp\1544365304079.png)