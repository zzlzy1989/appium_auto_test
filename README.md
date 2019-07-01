**Appium环境安装说明**

    一、环境安装

        1、Node.js
        2、appium server -desktop
        3、安卓ADT
        4、appium python库
        5、夜神模拟器，genymotion

    二、具体安装步骤：

        1、安装Microsoft .NET Framework 4.5
        2、安装node-****-x64.msi
            双击运行，安装appium的依赖环境，node.js.
            下载地址：https://nodejs.org/en/
        3、安装appium
            官方网站下载最新的appium版本。新版appium提供了元素定位的功能。
            官方网站地址：http://appium.io/
            各文件的区别：
            1、Appium-1.8.2.dmg：适用苹果os操作系统。程序安装，双击进行安装。
            2、appium-desktop-1.8.2-mac.zip：适用苹果os操作系统。解压安装，解压后即可运行。
            3、appium-desktop-1.8.2-full.nupkg：适用.NET开发平台。.nupkg是.NET的包文件，
                Visual Studio是.NET的集成开发环境（IDE），NuGet是.NET的包管理器。在Visual Studio中，
                可打开NuGet，安装.nupkg文件。
            4、appium-desktop-1.8.2-x86_64.AppImage：适用linux操作系统，如ubuntu、redhat、fedora等。
                下载后，在linux系统中，给予运行权限，双击即可运行。无需安装，也不需要改变依赖或系统配置。
                此外，也可以在Firejail等沙箱中运行。AppImage相关链接：https://appimage.org/
            5、appium-desktop-Setup-1.8.2-ia32.exe：适用32位windows操作系统。程序安装，双击进行安装。
            6、appium-desktop-setup-1.8.2.exe：适用64位windows操作系统。程序安装，双击进行安装。
            7、appium-desktop-web-setup-1.8.2.exe：适用64位windows操作系统。在线安装，双击后，
                自动下载安装文件（所以需要有网络）进行安装。
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
            夜神模拟器：默认安卓版本为5.1
            夜神多开器：安卓7.1模拟器。
            在启动模拟器之前，替换模拟器安装路径当中的nox_adb.exe
            第一步：将%ANDROID_HOME%\platform-tools目录下的adb.exe拷贝到桌面，更改名称为nox_adb.exe
            第二步：将第一步中的nox_adb拷贝到夜神模拟器安装目录下，替换原来的文件。
            再去启动夜神模拟器。然后在cmd命令行当中，输入命令：adb devices
        7、安装appium python客户端
            使用python的pip命令，直接在线安装：
            pip install Appium-Python-Client

    三、Appium简介

        1、appium是开源、跨平台的自动化测试工具，支持本地、移动端APP、桌面APP测试。
        2、平台支持IOS模拟器（simulators）、安卓模拟器（emulators）、真机（IOS、Android、Mac、Windows）。
        3、移动端系统自带的自动化框架：
            IOS9.3及以上：苹果的XCUITest
            IOS9.3以下：苹果的UIAutomation
            Android4.2+：谷歌的UiAutomator
            Android2.3+：谷歌的 Instrumentation(通过绑定另外的项目--Selendroid提供Instrumentation的支持)
            不需要把Appium特定的或者第三方的代码编译进你的应用
            意味着你测试使用的应用与最终发布的应用并无二致

    四、Appium运行原理

        web-selenium运行原理
        1、PC端代码 > HTTP > XXXDriver.exe > 调用原生浏览器API > XXX浏览器
        appium运行原理
        2、PC端代码 > HTTP > Appium > Android/IOS系统自带自动化框架API > 模拟器/真机

**Appium 介绍**

        Appium 是一个开源工具，用于自动化 iOS 手机 、 Android 手机和 Windows 桌面平台上的原生、移动 Web 和混合应用。
    “原生应用”指那些用 iOS 、 Android 或者 Windows SDK 编写的应用。“移动 web 应用”是用移动端浏览器访问的应用
    （Appium 支持 iOS 上的 Safari 、Chrome 和 Android 上的内置浏览器）。“混合应用”带有一个 "webview" 的包装器
    ——用来和 Web 内容交互的原生控件。类似 Phonegap 的项目，让用 Web 技术开发然后打包进原生包装器创建一个混合应
    用变得容易了。

        重要的是，Appium 是跨平台的：它允许你用同样的 API 对多平台写测试，做到在 iOS 、Android 和 Windows
    测试套件之间复用代码。

        了解 Appium “支持”这些平台意味着什么、有哪些自动化方式的详细信息，请参见 Appium 支持的平台。

**Appium 的理念**

    Appium 旨在满足移动端自动化需求的理念，概述为以下四个原则：
    1. 你没有必要为了自动化而重新编译你的应用或者以任何方式修改它。
    2. 你不应该被限制在特定的语言或框架上来编写运行测试。
    3. 移动端自动化框架在自动化接口方面不应该重造轮子。
    4. 移动端自动化框架应该开源，不但在名义上而且在精神和实践上都要实至名归。

**Appium 的设计**

        那么 Appium 项目的架构如何实现这一理念呢？为了实现第一点要求，我们其实使用了系统自带的自动化框架。
    这样，我们不需要把 Appium 特定的或者第三方的代码编译进你的应用。这意味着你测试使用的应用与最终发布的应用并无二致。
    我们使用以下系统自带的自动化框架：

        iOS 9.3 及以上：苹果的 XCUITest
        iOS 9.3 及以下：苹果的 UIAutomation
        Android 4.2+: 谷歌的 UiAutomator
        Android 2.3+: 谷歌的 Instrumentation（通过绑定另外的项目—— Selendroid 提供 Instrumentation 的支持）
        Windows: 微软的 WinAppDriver

        为了实现第二点要求，我们把这些（系统本身的）供应商提供的框架包装进一套 API —— WebDriver API 中。
    WebDriver（也叫 "Selenium WebDriver"）规定了一个客户端-服务器协议（称为 JSON Wire Protocol），
    按照这种客户端-服务器架构，可以使用任何语言编写的客户端向服务器发送适当的 HTTP 请求。已经有各个
    流行编程语言编写的客户端了。这也意味着你可以自由使用任何你想要的测试运行器和测试框架；客户端程序
    库不过是 HTTP 客户端，可以以任何你喜欢的方式混入你的代码。换句话说，Appium 和 WebDriver 客户端
    不是严格意义上的“测试框架”，而是“自动化程序库”。你可以以任何你喜欢的方式管理你的测试环境！

        我们以同样的方式实现第三点要求：WebDriver 已经成为 Web 浏览器自动化事实上的标准，并且是一个 W3C
        工作草案。何必在移动端做完全不同的尝试？我们通过附加可用于移动端自动化的 API 方法扩展了协议。

        显然第 4 点是你在阅读的前提—— Appium 是开源的

**Appium 概念**

    客户端/服务器架构
        Appium 的核心是暴露 REST API 的网络服务器。它接受来自客户端的连接，监听命令并在移动设备上执行，
    答复表示执行结果的 HTTP 响应。客户端/服务器架构实际给予了许多可能性：我们可以使用任何有 http
    客户端 API 的语言编写我们的测试代码，不过选一个 Appium 客户端程序库 用更容易。我们可以把服务器
    放在另一台机器上，而不是执行测试的机器。我们可以编写测试代码，并依靠类似 Sauce Labs 的云服务接
    收和解释命令。

    会话(session)
        自动化始终在一个会话的上下文中执行，这些客户端程序库以各自的方式发起与服务器的会话，但都以发给服
    务器一个 POST /session 请求结束，请求中包含一个被称作 'desired capabilities' 的 JSON 对象。
    这时服务器就会开启这个自动化会话，并返回一个用于发送后续命令的会话 ID。

    Desired Capabilities
        Desired capabilities 是一些发送给 Appium 服务器的键值对集合 (比如 map 或 hash），告诉服务器我们
    想要启动什么类型的自动化会话。也有各种可以在自动化运行时修改服务器行为的 capabilities。例如，我们可
    以把 platformName capability 设置为 iOS，告诉 Appium 我们想要 iOS 会话，而不是 Android 或者
    Windows 会话。我们也可以设置 safariAllowPopups capability 为 true ，确保我们在 Safari 自动化会
    话中可以使用 javascript 打开新窗口。有关 Appium capabilities 的完整列表，请参阅 capabilities doc 。

**Appium 服务器**

    Appium 是用 Node.js 写的服务器。它可以从源码构建安装或者从 NPM 直接安装：

    $ npm install -g appium
    $ appium

**Appium 客户端**

        有多个客户端程序库（Java、Ruby、Python、PHP,、JavaScript 和 C# 的）支持 Appium 对 WebDriver 协议的扩展，
    你需要用这些客户端程序库代替通常的 WebDriver 客户端。在这里浏览所有程序库的列表。

**Appium.app, Appium.exe**

        有 Appium 服务器的图形界面包装器可以下载。它们打包了 Appium 服务器运行需要的所有东西，所以你不需要为 Node
    而烦恼。它们还提供一个 Inspector 使你可以查看你应用的层级结构，这在写测试时很方便。

** General Capabilities **
    1、automationName：Appium (default) or Selendroid or UiAutomator2 or Espresso for Android or XCUITest for
    iOS or YouiEngine for application built with You.i Engine
    2、platformName：iOS, Android, or FirefoxOS
    3、platformVersion：	e.g., 7.1, 4.4
    4、deviceName：iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator,....
    5、app：/abs/path/to/my.apk or http://myapp.com/app.ipa
    6、browserName：'Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android
    7、newCommandTimeout：60
    8、language：eg fr
    9、locale：
    10、udid：
    11、orientation：
    12、autoWebview：
    13、noReset：重置APP  true, false
    14、fullReset：停止应用，删除用户数据，卸载APP
    15、eventTimings：
    16、enablePerformanceLogging：
    17、printPageSourceOnFindFailure：

    Android：
        1、unicodeKeyboard	Enable Unicode input, default false	true or false
    resetKeyboard
        2、Resetkeyboard to its original state, after running Unicode tests with unicodeKeyboard capability.
    Ignored if used alone. Default false	true or false
