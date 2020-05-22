# coding=utf-8
import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()  # 创建一个logger
        self.logger.setLevel(logging.DEBUG)  # 设置logger日志等级
        # 控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)

        oner_path = os.path.abspath(__file__)  # user_log.py的路径
        base_dir = os.path.dirname(oner_path)  # user_log.py的上一级路径
        log_dir = os.path.join(base_dir, 'logs')  # logs的路径
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
        log_name = log_dir + "/" +log_file  # 日志路径

        # #文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')  # 创建handle
        self.file_handle.setLevel(logging.INFO)  # 设置handle等级
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(lineno)d: %(levelname)s--> %(message)s')  # 格式化日志内容（时间、文件名、函数名、行数、等级、消息内容）
        self.file_handle.setFormatter(formatter)  # 为handle设置格式
        self.logger.addHandler(self.file_handle)  # 为logger添加日志处理器（handle）
        # self.logger.debug("tests1234")  # 输出等级为debug的日志内容、

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()  # 关闭handle
        self.logger.removeHandler(self.file_handle)  # 移除handle
