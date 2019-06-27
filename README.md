**Appium环境安装说明**

    1、安装Microsoft .NET Framework 4.5
    2、安装node-****-x64.msi
        双击运行，安装appium的依赖环境，node.js.
        下载地址：https://nodejs.org/en/
    3、安装appium
        官方网站下载最新的appium版本。新版appium提供了元素定位的功能。
        官方网站地址：http://appium.io/
    4、安装JDK
        安装JDK1.8及以上版本。
    5、安卓Android Develop Tools工具
        ADT的安装：
            1）解压 platform-tools_r28.0.2-windows.zip到本地目录
            2）双击SDKManager.exe
            3）在SDK Manager界面当中，只勾选：
            Tools当中的Android SDK Tools、Android SDK Platform-tools、Android SDK Build-tools
            另外一个就是Extras.
            其它的一概不勾选。默认选中的请注意取消勾选！！！！
            打开SDK Manager,默认会选中安卓sdk，请一定要取消掉。
        配置环境变量：
            1）添加ANDROID_HOME环境变量，配置sdk根目录。
                ANDROID_HOME=D:\android-sdk-windows
            2）在PATH变量中添加三项内容：
                %ANDROID_HOME%\platform-tools
                %ANDROID_HOME%\tools
                %ANDROID_HOME%\build-tools\28.0.3
            检测：
                进入cmd命令行，输入adb version
                能够正常显示adb的版本就okay.
    6、安装夜神模拟器
        官方网站下载地址：https://www.yeshen.com/
        下载安装完成之后。桌面会有2个图标：夜神模拟器、夜神多开器。
        夜神模拟器：默认安卓版本为4.4.2
        夜神多开器：可以增加安卓5.1模拟器、安卓7.1模拟器。
        在启动模拟器之前，替换模拟器安装路径当中的nox_adb.exe
        第一步：将%ANDROID_HOME%\platform-tools目录下的adb.exe拷贝到桌面，更改名称为nox_adb.exe
        第二步：将第一步中的nox_adb拷贝到夜神模拟器安装目录下，替换原来的文件。
        再去启动夜神模拟器。然后在cmd命令行当中，输入命令：adb devices
    7、安装appium python客户端
        使用python的pip命令，直接在线安装：
        pip install Appium-Python-Client
