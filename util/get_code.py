# coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time


class GetCode(object):
    def __init__(self, driver):
        self.driver = driver


    def get_code_image(self, file_name):
        ''' 获取验证码图片 '''
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']  # 获取验证码图片所在的x轴的值
        top = code_element.location['y']  # 获取验证码图片所在的y轴的值
        right = code_element.size['width'] + left  # 获得宽
        height = code_element.size['height'] + top  # 获得高
        im = Image.open(file_name)  # 打开截图
        img = im.crop((left * 1.25, top * 1.25, right * 1.25, height * 1.25))  # 切割图片，由于电脑分辨率为125%，所以要乘以系数
        img.save(file_name)  # 保存切割完的图
        time.sleep(2)

    def code_online(self, file_name):
        ''' 解析图片获取验证码 '''
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/1274-2", "167812", "755663fd1ff740128b5c4c3663013e89")
        # r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
        # r.addBodyPara("base64", "")
        r.addFilePara("imgFile", file_name)
        res = r.post()
        text = res.json()["showapi_res_body"]['texts']
        yzm = ''.join(text)
        time.sleep(2)
        return yzm
