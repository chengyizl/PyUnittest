import token
import unittest
from util.requestandresponse import Runmain
import requests
global token
import logs


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    #获取登录后token
        # def getToken(self):
        #     self.req = requests.post(self.baseurl+'/subscribe/verify/bindOpenid',json=data,headers=self.header_login)
        #     print(self.req.json())
        #     req = self.req.json()
        #     self.assertEqual(req['code'],8200,'返回错误，状态不为8200')
        #     return (self.req.json()['data']['token'])
         header_login = {"Host":"wechat.519taizhou.com",
                              "User-Agent":"Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3819 MicroMessenger/8.0.1.1841(0x28000151) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                              "Origin":"http://wechat.519taizhou.com",
                              "X-Requested-With":"com.tencent.mm",
                              "Content-Type":"application/json;charset=UTF-8"
                             }
         data={"idCard": "410522199304300014","openid": "oYD7k1aMjQGU4A_Ju0gNJ-QjfWPI","phone": "15857191631","realName": "刘旺"}
         req = requests.post('http://wechat.519taizhou.com/subscribe/verify/bindOpenid',json=data,headers=header_login)
         print(req.json())
         req = req.json()
         global token
         token = (req['data']['token'])

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # self.run = Runmain()
        self.baseurl = "http://wechat.519taizhou.com/"
        self.params_code = {"code":"071u3a000uk8kL1d6F300erlFY1u3a02"}
        self.paramActivityItem = {"activityItemId": "176"}
        self.paramOrder = {'activityItemLimitId' : '726509'}
        self.s = requests.session()
        self.g = globals()



    def tearDown(self):
        pass



    #获取景区列表
    def testAgetActivityItemList(self, params=None):
            global token
            header = {
                        "Host":"wechat.519taizhou.com",
                        "User-Agent":"Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3819 MicroMessenger/8.0.1.1841(0x28000151) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                        "token": token
                      }
            self.req = requests.get(self.baseurl+'subscribe/activityitem/getActivityItemList',headers=header)
            res = self.req.json()
            print(res)
            self.assertEqual(res['code'],8200,'返回错误，状态不为8200')

    #获取景区可预约门票
    def testBgetActivityItem(self):
            global token
            header = {
                        "Host":"wechat.519taizhou.com",
                        "User-Agent":"Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3819 MicroMessenger/8.0.1.1841(0x28000151) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                        "token": token
                     }
            self.req = requests.get(self.baseurl+'subscribe/activityitem/getActivityItem',headers=header,params=self.paramActivityItem)
            res = self.req.json()
            print(res)
            self.assertEqual(res['code'],8200,'返回错误，状态不为8200')

    #预约某个景区门票
    def testCOrder(self):
            global token
            header = {
                         "Host":"wechat.519taizhou.com",
                         "User-Agent":"Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3819 MicroMessenger/8.0.1.1841(0x28000151) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                         "token": token
                     }
            self.req = requests.post(self.baseurl+'subscribe/record/order',headers=header,params=self.paramOrder)
            res = self.req.json()
            print(res)

            #获取添加儿童票所需的parrecordid
            parrecord = (res['data']['id'])
            print(parrecord)
            self.g['resid'] = parrecord#将id设置为全局变量
            #判断返回状态
            self.assertEqual(res['code'],8200,'返回错误，状态不为8200')

    #添加儿童票
    @unittest.skip("暂时跳过")
    def testDaddchild(self):
            global token
            parrecordid = self.g['resid'] #获取全局变量中的id
            print(parrecordid)
            header = {
                         "Host":"wechat.519taizhou.com",
                         "User-Agent":"Mozilla/5.0 (Linux; Android 10; CDY-AN00 Build/HUAWEICDY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045525 Mobile Safari/537.36 MMWEBID/3819 MicroMessenger/8.0.2.1860(0x2800023B) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                         "Origin":"http://wechat.519taizhou.com",
                         "Content-Type":"application/json;charset=UTF-8",
                         "Accept":"application/json, text/plain, */*",
                         "token": token
                     }
            data = {
                         "idcard":"330110201712215022",
                         "username":"蒋诗薇",
                         "parrecordid": parrecordid
                   }
            self.req = requests.post(self.baseurl+'subscribe/record/child',headers=header,json=data)
            res = self.req.json()
            print(res)
            #判断返回状态
            self.assertEqual(res['code'],8200,'返回错误，状态不为8200')







