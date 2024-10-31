import client_tools
import os
import requests
import urllib
import json

class SovitsClient(object):
    SovitsUrl = 'http://127.0.0.1:5000'

    def __init__(self):

        self.load_tts_url()

    def load_tts_url(self):

        if os.name =="posix":
            ls = str(client_tools.__file__).split("/")
            path = "/" + ls[1]
            for i in ls[2:-1]:
                path = path + "/" + i
            path = path + "/" + "config.json"

        elif os.name == "nt":
            ls = str(client_tools.__file__).split("\\")
            path = ls[0]
            for i in ls[1:-1]:
                path = path + "\\" + i
            path = path + "\\" + "config.json"

        with open(path,"r",encoding="utf-8") as f:
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


if __name__ == '__main__':
    tts = SovitsClient()
    tts.text_to_speech(text="窗前明月光",path="./test.wav")
