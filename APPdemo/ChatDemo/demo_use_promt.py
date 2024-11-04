"""
demo
    这是一个展示如何进行使用加载预制的prompt的示例
    其作为chatgml的一个子类，在原先
        chatgml.make_send_json()中只需要负责添加上 prompt.json 里面的话语即可

"""
import os.path
import sys
#添加包环境变量
path = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(path,"..","..")
sys.path.append(path)
import client_tools
from client_tools import *
import json

class MotivationalCoach(chatgml):

    def __init__(self):
        super(MotivationalCoach, self).__init__()
        self._Prompt = ""
        self._PromptPath = None
    def GetAgentPrompt(self,name="励志教练"):
        """
        负责进行获取prompt
        :param name:指定prompt.json中的智能体名称

        """
        self._Prompt = client_tools.GetPromptFile(name)

    def make_send_json(self,ques):
        """
        对其进行复写，在prompt中进行格式化字符串传输
        """
        if self._Prompt != "":
            ques = self._Prompt.format(ques)
        else:
            assert "为空检查是否存在此角色"

        return {"prompt":ques,"history":self.history}


if  __name__ == "__main__":
    ai = MotivationalCoach()
    ai.GetAgentPrompt()
    while True:
        ques = input("请输入你的问题:\t")

        user_ed = ai.make_send_json(ques)

        assitant = ai.post(user_ed)
        print(assitant)