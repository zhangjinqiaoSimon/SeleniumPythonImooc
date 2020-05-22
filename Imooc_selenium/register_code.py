# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()


def driver_init():
    ''' 初始化driver '''
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)


def get_element_by_id(id):
    ''' 定位元素 '''
    element = driver.find_element_by_id(id)
    return element


def get_range_num():
    ''' 获取随机数 '''
    num = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 5))
    return num


def get_code_image(file_name):
    ''' 获取验证码图片 '''
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x']  # 获取验证码图片所在的x轴的值
    top = code_element.location['y']  # 获取验证码图片所在的y轴的值
    right = code_element.size['width'] + left  # 获得宽
    height = code_element.size['height'] + top  # 获得高
    im = Image.open(file_name)  # 打开截图
    img = im.crop((left * 1.25, top * 1.25, right * 1.25, height * 1.25))  # 切割图片，由于电脑分辨率为125%，所以要乘以系数
    img.save(file_name)  # 保存切割完的图片


def code_online(file_name):
    ''' 解析图片获取验证码 '''
    r = ShowapiRequest("http://route.showapi.com/1274-2", "167812", "755663fd1ff740128b5c4c3663013e89")
    # r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
    # r.addBodyPara("base64", "")
    r.addFilePara("imgFile", file_name)
    res = r.post()
    text = res.json()["showapi_res_body"]['texts']
    yzm = ''.join(text)
    return yzm


def run_main():
    ''' 运行主程序 '''
    user_name = get_range_num()
    user_email = user_name + '@163.com'
    file_name = 'D:/screenshot/imooc_yanzhengma.png'
    driver_init()
    get_element_by_id('register_email').send_keys(user_email)  # 输入邮箱
    get_element_by_id('register_nickname').send_keys(user_name)  # 输入用户名
    get_element_by_id('register_password').send_keys('111111')  # 输入密码
    get_code_image(file_name)
    text = code_online(file_name)
    get_element_by_id('captcha_code').send_keys(text)
    time.sleep(5)
    get_element_by_id('register-btn').click()
    time.sleep(5)
    driver.close()

run_main()
