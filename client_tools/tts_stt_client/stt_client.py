import requests
import client_tools


class SpeehToText(object):
    url = "http://127.0.0.1:9977/api"

    def __init__(self,model_name = "large-v3"):
        self.data = None
        self.load_stt_url()
        self.make_data(model_name=model_name)
        pass

    def load_stt_url(self):

        SpeehToText.url = client_tools.LoadConfigFile("stt")

    def make_data(self,model_name= "large-v3",response_format="text"):

        """
        设置回复信息
        json|str|text
        """
        self.data = {"language":"zh","model":model_name,"response_format":response_format}

    def post(self,file_path):
        """
        :param file_path: 音频文件路径
        """
        file = open(file_path, "rb")
        response = requests.post(SpeehToText.url,data=self.data,files={"file":file})
        return response.json().get("data")


if __name__ == '__main__':
    api = SpeehToText()
    data = api.post(r"./test.wav")
    print(data)
