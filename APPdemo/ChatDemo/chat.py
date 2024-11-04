"""
demo :
    这是一个简单的对话示例

"""
import os
import sys
#添加包环境变量
path = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(path,"..","..")
sys.path.append(path)

from client_tools import *

print(os.name)

if __name__ == "__main__":
    ai = chatgml()
    tts = SovitsClient()
    stt = SpeehToText()
    while 1:
        """
        音频录制
        """
        device = init_device(1)
        recorder = Recorder(device=device)

        input("按下任意键开始录音")
        recorder.start()

        input("按下任意键结束录音")
        recorder.stop()
        recorder.join()

        save_wavfile('noise.wav', recorder.waveform)
        """
        文字转语音
        """
        ques = stt.post("./noise.wav")

        """
        chat 回答
        """
        user_ed = ai.make_send_json(ques)

        assitant = ai.post(user_ed)
        """
        语音转文字
        """
        tts.text_to_speech(assitant,"./output.wav")
        """
        音频播放
        """
        device = init_device(0)
        play_audio('./output.wav', output_device=device["index"])