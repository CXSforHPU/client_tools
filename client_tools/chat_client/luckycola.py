import requests
import json

class LuckyCola_TXHY():
    """
    注册网址：https://luckycola.com.cn/public/dist/#/
    使用的为腾讯混元大模型的服务

    填写自己的appkey
    uid
    """
    url = 'https://luckycola.com.cn/hunyuan/txhy'
    appKey = "657976893302bfa20b9f2b56"
    uid = "NtoAW31702458883264reDjRnIakr"
    headers = {"Content-Type": "application/json"}
    def __init__(self):

        pass

    @staticmethod
    def make_send_json(ques,isLongChat=0):
        """
        return : 默认不支持长对话
        """
        return {"appKey":LuckyCola_TXHY.appKey,"uid":LuckyCola_TXHY.uid,"ques":ques,"isLongChat":isLongChat}
    @staticmethod
    def get_assitant(data):
        if data["code"] !=0:
            return "状态码不对"

        return str(data["data"]["result"]["Content"])

    def post(self,user_ed):
        json_payload = json.dumps(user_ed)
        response = requests.post(LuckyCola_TXHY.url,data=json_payload,headers=LuckyCola_TXHY.headers)
        return LuckyCola_TXHY.get_assitant(response.json())


if __name__ == '__main__':
    ai = LuckyCola_TXHY()
    while 1:
        ques = input("请输入你的问题:\t")
        isLongChat = int(input("是否长对话:\t"))

        user_ed = LuckyCola_TXHY.make_send_json(ques,isLongChat)

        assitant = ai.post(user_ed)
        print(assitant)

# import requests  # 导入requests库
# import json
# # 定义请求的URL
# url = 'https://luckycola.com.cn/hunyuan/txhy'
#
# # 定义请求的参数，这里假设你已经有了appKey、ques和uid的值
# appKey = '657976893302bfa20b9f2b56'
# ques = '你好'
# uid = 'NtoAW31702458883264reDjRnIakr'
#
# # 将参数组织成字典格式，并转换为JSON字符串
# payload = {
#     'appKey': appKey,
#     'ques': ques,
#     'uid': uid,
#     "isLongChat":0
# }
# json_payload = json.dumps(payload)  # 使用json模块将字典转换为JSON字符串
#
# # 创建headers，指定Content-Type为application/json
# headers = {
#     'Content-Type': 'application/json',
#     # 可以添加其他需要的headers，如Auth Token等
# }
#
# # 发起POST请求
# response = requests.post(url, data=json_payload, headers=headers)
#
# # 处理响应结果
# if response.status_code == requests.codes.ok:  # 如果状态码表示成功（通常是200）
#     result = response.json()  # 将响应内容解析为JSON格式的Python对象
#     print("请求成功，结果为：")
#     print(result)  # 打印出响应的JSON数据
# else:
#     print("请求失败，状态码为：", response.status_code)  # 打印出错误状态码和错误信息
#     print(response.text)  # 打印出错误信息或服务器返回的错误详情等（如果有的话）