# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement


class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_griver(url, i)

    def get_griver(self, url, i):
        ''' 获取driver，并且打开url '''
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self, key, data):
        ''' 输入用户信息 '''
        self.get_user_element(key).send_keys(data)

    def get_user_element(self, key):
        ''' 定位，获取element '''
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_num(self):
        ''' 获取随机数 '''
        num = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 5))
        return num

    def get_code_image(self, file_name):
        ''' 获取验证码图片 '''
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('code_image')
        left = code_element.location['x']  # 获取验证码图片所在的x轴的值
        top = code_element.location['y']  # 获取验证码图片所在的y轴的值
        right = code_element.size['width'] + left  # 获得宽
        height = code_element.size['height'] + top  # 获得高
        im = Image.open(file_name)  # 打开截图
        img = im.crop((left * 1.25, top * 1.25, right * 1.25, height * 1.25))  # 切割图片，由于电脑分辨率为125%，所以要乘以系数
        img.save(file_name)  # 保存切割完的图

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
        return yzm

    def main(self):
        user_name = self.get_range_num()
        user_email = user_name + '@163.com'
        file_name = 'D:/screenshot/imooc_yanzhengma.png'
        code_text = self.code_online(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('password', '111111')
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_btn').click()
        code_error = self.get_user_element('code_text_error')
        if code_error is None:
            print('注册成功')
        else:
            self.driver.save_screenshot('D:/screenshot/error_page.png')
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    for i in range(2):
        register_function = RegisterFunction('http://www.5itest.cn/register', i)
        register_function.main()
