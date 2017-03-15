#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from config import *
import os, random, string
import qiniu
import clipboard
from PIL import ImageGrab


# 将剪贴板中的截图保存
def save_clipboard():
    image = ImageGrab.grabclipboard()
    if image:
        try:
            image.save(TMP_FILE_NAME, 'jpeg')
            return TMP_FILE_NAME
        except Exception as e:
            notify("qiniu-imgup", "保存截图失败")
    else:
        notify("qiniu-imgup", "获取截图失败")


# 生成5位小写字母加数字的随机文件名
def random_name():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))


# 上传至七牛云
def upload_img(fn, sfx='.jpg'):
    key = random_name() + sfx
    q = qiniu.Auth(QINIU_AK, QINIU_SK)
    token = q.upload_token(QINIU_BUCKET, key, 3600)
    ret, info = qiniu.put_file(token, key, fn)
    if ret != None and ret['key'] == key and ret['hash'] == qiniu.etag(fn):
        return QINIU_DOMAIN + key
    else:
        notify("qiniu-imgup", "上传七牛云失败")
        return False


# 生成markdown/html链接
def get_return_link(img_url):
    if LINK_TYPE == 'markdown':
        return '![](%s)' % (img_url,)
    elif LINK_TYPE == 'html':
        return '<img src="%s">' % (img_url,)
    else:
        notify("qiniu-imgup", "链接类型配置错误")


# 调用系统通知
def notify(title, text):
    os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(text, title))


# 运行
def run():
    image_path = save_clipboard()
    if image_path:
        qiniu_url = upload_img(image_path)
        if qiniu_url:
            md_link = get_return_link(qiniu_url)
            clipboard.copy(md_link)
            notify("qiniu-imgup", "图片上传成功")


if __name__ == '__main__':
    run()
