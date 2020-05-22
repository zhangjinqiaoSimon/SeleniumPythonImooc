# coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

# image = Image.open('D:/screenshot/imooc_yanzhengma02.png')
# text = pytesseract.image_to_string(image)  # 识别图片上的文字（不适用于复杂的，有干扰的图片）
# print(text)
'''
r = ShowapiRequest("http://route.showapi.com/1274-2", "167812", "755663fd1ff740128b5c4c3663013e89")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/screenshot/imooc_yanzhengma02.png")  # 文件上传时设置
res = r.post()
# text = res.json()['showapi_res_body']['Result']
print(res.text)  # 返回信息
'''

r = ShowapiRequest("http://route.showapi.com/1274-2", "167812", "755663fd1ff740128b5c4c3663013e89")
# r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
# r.addBodyPara("base64", "")
r.addFilePara("imgFile", r"D:/screenshot/imooc_yanzhengma02.png")
res = r.post()
text = res.json()["showapi_res_body"]['texts']
print(''.join(text)[0:5])  # 返回信息
