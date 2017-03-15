# qiniu-imgup-mac

## 简介
qiniu-imgup-mac是一个Mac系统下的七牛云图片上传工具，目标是简化MarkDown写作中的贴图的繁琐步骤。
qiniu-imgup-mac可以快速将剪贴板中的图片上传至七牛云，并返回MarkDown格式的链接至剪贴板。
适用人群：使用七牛云做为图床的MarkDown编写者。
平台：macOS  （macOS 10.12测试通过）

另有Mac版本，请移步：[https://github.com/xiiiblue/qiniu-imgup-mac.git](https://github.com/xiiiblue/qiniu-imgup-linux.git)

## 使用方法介绍
在编写MarkDown文档时，如果使用七牛云做图床，插入一张图片需要以下几个繁琐的步骤：
1. 截图
2. 保存为文件
3. 打开浏览器，在七牛云后台上传图片
4. 复制图片的HTTP URL
5. 在编辑器中将URL拼接为MarkDown的链接格式
6. 粘帖链接

qiniu-imgup将整个操作简化为了3个快捷键操作：
1. `cmd+shift+ctrl+4`  -  截图到剪贴板
2. `cmd+shift+u`  -  使用自定义热键，上传并获取MarkDown链接
3. `cmd+v`  -  粘帖MarkDown链接

## 安装与配置
1. 安装依赖
```
sudo pip3 install -r requirement.txt
```
2. 配置`config.py`，填入七牛云的AK、SK等参数
3. 使用Automator将shell脚本uimg封装为APP
![](http://oh0ra6igz.bkt.clouddn.com/k6cwa.jpg)
4. 在系统设置中（System Preference->Keyboard->Shortcuts->App Shortcuts），为APP分配快捷键
![](http://oh0ra6igz.bkt.clouddn.com/oknvx.jpg)
