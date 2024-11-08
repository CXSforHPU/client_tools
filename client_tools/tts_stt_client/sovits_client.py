import client_tools
import requests
import urllib
from tqdm import tqdm

class SovitsClient(object):
    SovitsUrl = 'http://127.0.0.1:5000'

    def __init__(self):

        self.load_tts_url()

    def load_tts_url(self):
        SovitsClient.SovitsUrl = client_tools.LoadConfigFile("tts")

    @staticmethod
    def text_to_speech(text, path):
        """
        :param text:    文本（str）
        :param path:    指定文件编写路径
        :return:
        """
        url = urllib.parse.quote(text)

        wav = requests.get(
            f'{SovitsClient.SovitsUrl}?text={url}&text_language=zh',stream=True)


        # 获取文件大小（如果服务器提供了这个信息）
        total_size_in_bytes = int(wav.headers.get('content-length', 0))
        block_size = 1024  # 每次读取的块大小

        with open(path, 'wb') as f:
            with tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, desc="下载进度") as pbar:
                for chunk in wav.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))  # 更新进度条

        print('文件下载完成！')

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
    tts.text_to_speech(text="疑是地上霜",path="./test.wav")
