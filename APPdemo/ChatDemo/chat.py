"""
demo :
    这是一个简单的对话示例

"""
import os
from client_tools import *

print(os.name)

if __name__ == "__main__":
    ai = chatgml()
    while 1:
        ques = input("请输入你的问题:\t")

        user_ed = ai.make_send_json(ques)

        assitant = ai.post(user_ed)
        print(assitant)