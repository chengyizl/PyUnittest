import requests

class Runmain:

    #封装post请求接口
    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers).json()
        return response

    #封装get请求接口
    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers).json()
        return  response

    def run_main(self,url,params,data,headers,method):
        response = None
        if method == 'Get':
            response = self.send_get(url,params,headers)
        else:
            response = self.send_post(url,data,headers)
        return response
