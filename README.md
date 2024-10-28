# client_tools
***
* TTS
  * https://github.com/RVC-Boss/GPT-SoVITS
* STT
  * https://github.com/jianchang512/stt
* chat
  * chatgml6b
  * luckycola-文心一言
  * luckycola-腾讯混元

# config文件介绍
***./config.json***
```json
{
  "chat": {
    "chatgml6b": "http://127.0.0.1:8000",    //访问url地址
    "luckycola": "https://luckycola.com.cn/hunyuan/txhy",  //访问url地址
    "luckycola_wxyy": "https://luckycola.com.cn/ai/openwxyy" //访问url地址
  },
  "stt": "http://127.0.0.1:9977/api",//访问url地址
  "tts": "http://127.0.0.1:5000"  //访问url地址
}
```
* 此为默认地址
* 若自己有域名进行更改的话
  * 将自己的域名对其进行替换



# TTS
## 模块位置
***./tts_stt_client/sovits_client***
```python
import requests
import urllib
import json

class SovitsClient(object):
    SovitsUrl = 'http://127.0.0.1:5000'


    def __init__(self):

        self.load_tts_url()

    def load_tts_url(self):
        with open("../config.json","r",encoding="utf-8") as f:
            config = json.load(f)
            SovitsClient.SovitsUrl = config['tts']

    @staticmethod
    def text_to_speech(text, path):
        """
        :param text:    文本（str）
        :param path:    指定文件编写路径
        :return:
        """
        url = urllib.parse.quote(text)

        wav = requests.get(
            f'{SovitsClient.SovitsUrl}?text={url}&text_language=zh')

        wav = wav.content
        with open(path, 'wb') as fp:
            fp.write(wav)

        """
        若需要进行修改音频的采样率与通道数请开启下面代码
        需要提前配置好 ffmpeg
        """
        # new_path = os.path.join(".","output.wav")
        # os.system(f"ffmpeg -i {path} -y -ar 44100 -ac 2 {new_path}")
        # # re = AudioSegment.from_wav('temp.wav')
        # play(re)
```

# STT
## 模块位置
***./tts_stt_client/stt_client***
```python
import requests
import json
class SpeehToText(object):
    url = "http://127.0.0.1:9977/api"

    def __init__(self,model_name = "large-v3"):
        self.data = None
        self.load_stt_url()
        self.make_data(model_name=model_name)
        pass

    def load_stt_url(self):
        with open("../config.json","r",encoding="utf-8") as f:
            config = json.load(f)
            SpeehToText.url = config["stt"]

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

```
# chat模块

```python
import requests
import json

class chatgml():
    """
    本demo为chatgml6b的client
    github 地址为：
    https://github.com/THUDM/ChatGLM-6B

    """
    url = 'http://127.0.0.1:8000'
    headers = {"Content-Type": "application/json"}

    def __init__(self):
        self.history = []
        self.load_chatgml6b_url()

        pass

    def load_chatgml6b_url(self):
        with open('../config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            chatgml.url = config["chat"]['chatgml6b']
    def make_send_json(self,ques):
        """
        return : 默认支持长对话
        """
        return {"prompt":ques,"history":self.history}
    def get_assitant(self,data):
        if data["status"] !=200:
            return "状态码不对"

        self.history = data["history"]
        return str(data["response"])

    def post(self,user_ed):
        json_payload = json.dumps(user_ed)
        response = requests.post(chatgml.url,data=json_payload,headers=chatgml.headers)
        return ai.get_assitant(response.json())

```

* 此文件提供了chatgml6b的api接口方式

## 并且提供三个接口
### make_send_json()
* 制作要发送的json数据包，返回类型为dict
### post()
* 发送json数据包
* reture 经过get_assitant解析过的数据
### get_assitant()
* 解析返回json中的assitant
* 发送与解析