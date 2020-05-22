# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
time.sleep(5)
print(EC.title_contains('注册'))  # 判断页面是否正常打开（通过判断title）
locater = (By.CLASS_NAME, 'controls')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locater))  # WebDriverWait是显示等待
email_element = driver.find_element_by_id('register_email')
user_email = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 5)) + '@163.com'
print(user_email)
print(email_element.get_attribute('placeholder'))  # get_attribute('属性名')用于获取元素中某个属性的值
email_element.send_keys(user_email)
print(email_element.get_attribute('value'))
user_name_element_node = driver.find_elements_by_class_name('controls')[1]  # 寻找父节点，通过list找到第二个
user_name_element_node.find_element_by_class_name('form-control').send_keys('mushishi02')
driver.find_element_by_name('password').send_keys('111111')
driver.save_screenshot('D:/screenshot/imooc_yanzhengma.png')  # 网页截图
code_element = driver.find_element_by_id('getcode_num')
left = code_element.location['x']  # 获取验证码图片所在的x轴的值
top = code_element.location['y']  # 获取验证码图片所在的y轴的值
right = code_element.size['width'] + left  # 获得宽
height = code_element.size['height'] + top  # 获得高
im = Image.open('D:/screenshot/imooc_yanzhengma.png')  # 打开截图
img = im.crop((left * 1.25, top * 1.25, right * 1.25, height * 1.25))  # 切割图片，由于电脑分辨率为125%，所以要乘以系数
img.save('D:/screenshot/imooc_yanzhengma02.png')  # 保存切割完的图片
'''下面是解析图片中的验证码的接口'''
r = ShowapiRequest("http://route.showapi.com/1274-2", "167812", "755663fd1ff740128b5c4c3663013e89")
# r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
# r.addBodyPara("base64", "")
r.addFilePara("imgFile", r"D:/screenshot/imooc_yanzhengma02.png")
res = r.post()
text = res.json()["showapi_res_body"]['texts']
print(''.join(text)[0:5])  # 返回信息
yzm = ''.join(text)[0:5]
driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys(yzm)
time.sleep(10)
driver.close()
