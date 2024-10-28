import requests
import json
class LuckyCola_wxyy():
    """
    注册网址：https://luckycola.com.cn/public/dist/#/
    使用的为腾讯混元大模型的服务

    填写自己的appkey
    uid
    """
    url = 'https://luckycola.com.cn/ai/openwxyy'
    appKey = "your appkey"
    uid = "your uid"
    headers = {"Content-Type": "application/json"}
    def __init__(self):

        pass

    @staticmethod
    def make_send_json(ques,isLongChat=0):
        """
        return : 默认不支持长对话
        """
        return {"appKey":LuckyCola_wxyy.appKey,"uid":LuckyCola_wxyy.uid,"ques":ques,"isLongChat":isLongChat}
    @staticmethod
    def get_assitant(data):
        if data["code"] !=0:
            return "状态码不对"

        return str(data["data"]["result"])

    def post(self,user_ed):
        json_payload = json.dumps(user_ed)
        response = requests.post(LuckyCola_wxyy.url,data=json_payload,headers=LuckyCola_wxyy.headers)
        return LuckyCola_wxyy.get_assitant(response.json())


if __name__ == '__main__':
    ai = LuckyCola_wxyy()
    while 1:
        ques = input("请输入你的问题:\t")
        isLongChat = int(input("是否长对话:\t"))

        user_ed = LuckyCola_wxyy.make_send_json(ques,isLongChat)

        assitant = ai.post(user_ed)
        print(assitant)