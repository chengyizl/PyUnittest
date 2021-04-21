# import unittest
#
#
#
#
# class IntegerArithmeticTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("测试类之前运行")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("测试类执行后运行")
#
#     def setUp(self):
#         print("测试用例执行前置条件")
#
#     def tearDown(self):
#         print("用例执行后置条件，进行环境清理")
#
#     def testAdd(self):
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#         print("第一个方法")
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#         print("第二个方法")
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)