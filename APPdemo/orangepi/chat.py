"""
demo :
    这是一个简单的对话示例

"""
import os
import sys
from client_tools import *
import OPi.GPIO as GPIO
from time import sleep
#添加包环境变量
path = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(path,"..","..")
sys.path.append(path)

GPIO.setboard(GPIO.ZERO)        # Orange Pi Zero board
GPIO.setmode(GPIO.SOC)          # set up SOC numbering

sled = GPIO.PA+7               # Status led is on PA17
GPIO.setup(sled, GPIO.IN)      # set PA17 as an output (Status led of board)

def detect_button():
    while GPIO.input(sled):
        sleep(0.02)
print(os.name)

if __name__ == "__main__":
    ai = chatgml()
    tts = SovitsClient()
    stt = SpeehToText()
    while 1:
        """
        音频录制
        """

        detect_button()
        os.system("arecord -d 5 -f cd -t wav noise.wav")
        detect_button()

        """
        文字转语音
        """
        ques = stt.post("./noise.wav")
        print(ques)

        """
        chat 回答
        """
        user_ed = ai.make_send_json(ques)

        assitant = ai.post(user_ed)
        print(assitant)
        """
        语音转文字
        """
        tts.text_to_speech(assitant,"./output.wav")
        """
        音频播放
        """
        device = init_device(0)
        play_audio('./output.wav', output_device=device["index"])
