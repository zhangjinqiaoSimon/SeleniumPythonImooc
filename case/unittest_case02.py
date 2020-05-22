# coding=utf-8
import unittest


class FirstCase01(unittest.TestCase):  # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):  # 所有case执行之前执行
        pass

    @classmethod
    def tearDownClass(cls):  # 所有case执行之后执行
        pass

    def setUp(self):  # setUp是每个case的前置条件
        print('这个是前置条件')

    def tearDown(self):  # teatDown是每个case后置条件
        print('这个是后置条件')
     # @unittest.skip() # 用来跳过某个案例
    def test_first001(self):  # unittest中运行case需要test开头
        print('第一个案例02')

    def test_first002(self):
        print('第二个案例02')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()  # 实例化一个容器
    suite.addTest(FirstCase01('test_first002'))
    unittest.TextTestRunner().run(suite)
