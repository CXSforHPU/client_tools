import requests
import urllib
import json
import os

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
        :return:        直接播放传入的str文本内容
        """
        url = urllib.parse.quote(text)

        wav = requests.get(
            f'{SovitsClient.SovitsUrl}?text={url}&text_language=zh')

        wav = wav.content
        with open(path, 'wb') as fp:
            fp.write(wav)

        """
        若需要进行修改音频的采样率与通道数请开启下面代码
        """
        # new_path = os.path.join(".","output.wav")
        # os.system(f"ffmpeg -i {path} -y -ar 44100 -ac 2 {new_path}")
        # # re = AudioSegment.from_wav('temp.wav')
        # play(re)


if __name__ == '__main__':
    SovitsClient.text_to_speech(text="你好",path="./test.wav")
