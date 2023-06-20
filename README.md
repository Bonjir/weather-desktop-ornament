# 天气桌面摆件


## 项目背景

每次离开宿舍之前都要打开手机看一眼天气，而天气软件在一天中首次打开时需要很长的加载时间，十分浪费时间。所以笔者就想到可以做一个小物联网项目每天自动获取天气，只需要扫一眼即可了解今天的天气，省心省时。当然，仅仅是连接wifi并通过api是很简单的项目，不过由于在宿舍中并不能让手机一直开着热点供开发板连接，所以需要让单片机自动连接校园网，这也是本项目的一个亮点。

## 开发环境

本项目基于合宙esp32c3开发板利用micropython语言进行开发。

使用esp32c3烧录micropython的过程可以参考[合宙ESP32-C3 烧录Micropython指南](https://www.bilibili.com/read/cv15460009)。

## 文件结构

wifi.py是wifi连接模块，是在network之上的进一步的封装。

campuswifi.py是校园网连接模块，利用urequests模块与校园网服务器进行http通信，登录并且开通网络。

ST7735.py是合宙开发板配套的air101-lcd驱动模块，笔者在[@boochow的ST7735模块](https://github.com/boochow/MicroPython-ST7735)基础上进行了进一步的开发，新增了更加节省内存的字符显示方式、图片显示函数，并对lcd坐标进行了校正。

requests模块是在[官方的urequests模块](https://pypi.org/project/micropython-urequests/)基础上进行优化了的http通信模块，修复了一些特性。

weathericon文件夹内是天气图标资源。

codetab.bin是存储字模的文件，字符信息的具体地址可以再st3375文件中的字符地址字典中找到。

## 主要项目负责人

[@Bonjir](http://github/bonjir)

## 参与贡献

欢迎加入！Open an issue 也算贡献！

**贡献者**

[@Bonjir](http://github/bonjir)

## 开源协议

[MIT](https://github.com/Bonjir/Ultrasonic-Radar/blob/master/LICENSE) © Bonjir

