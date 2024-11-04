import wave
from client_tools.drivers.win64.tools import *
from client_tools.tts_stt_client.sovits_client import SovitsClient

def play_audio(path,output_device=None):
    # 打开音频文件
    wf = wave.open(path, 'rb')
    # 初始化Pyaudio
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output_device_index=output_device,
                    output=True)

    # 播放音频
    data = wf.readframes(1024)
    while data != b'':
        stream.write(data)
        data = wf.readframes(1024)

    # 关闭音频流
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    tts = SovitsClient()
    tts.text_to_speech("窗前明月光，一是顶上双",'./temp.wav')
    device = init_device(0)
    play_audio('./temp.wav',output_device=device["index"])
    # play_audio('./temp.wav')
    # p = pyaudio.PyAudio()
    # print(p.get_device_count())
    # print('输入设备:')
    # for item in get_audio_input_devices():
    #     print(item.get('name'))
    # print('输出设备:')
    # for item in get_audio_output_devices():
    #     print(item.get('name'))
    # play_audio('./noise.wav')
