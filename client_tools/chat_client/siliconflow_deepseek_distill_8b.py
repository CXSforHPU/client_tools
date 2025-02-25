import requests
import json


class SiliconFlowDeepSeekClient:
    """
    这是一个与 SiliconFlow DeepSeek 模型交互的客户端
    """

    url = "https://api.siliconflow.cn/v1/chat/completions"
    appKey = ""
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {appKey}"}

    def __init__(self):
        self.history = []
    #     self.load_siliconflow_deepseek_distill_8b6b_url()
    #
    # def load_siliconflow_deepseek_distill_8b6b_url(self):
    #     """加载 API 配置 URL"""
    #     self.url = client_tools.LoadConfigFile("siliconflow_deepseek_distill_8b")

    def make_send_json(self, ques):
        """构造请求 payload，支持长对话"""
        self.history.append({"role": "user", "content": ques})
        return {
            "model": "deepseek-ai/DeepSeek-V3",
            "messages": self.history,
            "stream": True
        }

    def get_assistant(self, data):
        """从响应中提取 AI 回答"""
        try:
            return str(data["choices"][0]["delta"]["content"])
        except KeyError:
            return ""

    def post(self, user_ed):
        """发送请求并逐步处理响应"""
        json_payload = json.dumps(user_ed)
        try:
            response = requests.post(self.url, data=json_payload, headers=self.headers, stream=True)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return ""

        temp = ""
        for chunk in response.iter_content(1024):
            try:
                st = chunk.decode("utf-8")[6:]  # 去除初始的无效字符
                js = json.loads(st)
                cur = self.get_assistant(js)
                if cur and cur != 'None':
                    temp += cur
                    print(cur, end="")
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                continue

        self.history.append({"role": "assistant", "content": temp})
        return temp

if __name__ == '__main__':
    ai = SiliconFlowDeepSeekClient()
    while True:
        ques = input("请输入你的问题 (输入 'exit' 退出):\t")
        if ques.lower() == 'exit':
            print("退出程序")
            break
        user_ed = ai.make_send_json(ques)
        assistant_reply = ai.post(user_ed)
        print(assistant_reply)
