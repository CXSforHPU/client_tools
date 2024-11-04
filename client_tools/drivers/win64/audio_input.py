import threading
import wave
import numpy as np
from client_tools.drivers.win64.tools import *

def audio_f2i(data, width=16):
    """将浮点数音频数据转换为整数音频数据。"""
    data = np.array(data)
    return np.int16(data * (2 ** (width - 1)))


def audio_i2f(data, width=16):
    """将整数音频数据转换为浮点数音频数据。"""
    data = np.array(data)
    return np.float32(data / (2 ** (width - 1)))


def save_wavfile(path, wave_data):
    """保存音频数据为wav文件。"""
    with wave.open(path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(16000)
        wav_file.writeframes(np.array(wave_data).tobytes())
    print(f"Successfully saved wavfile: {path} ..")


class Recorder(threading.Thread):
    def __init__(self,
                 format=pyaudio.paInt16,
                 channels=1,
                 sample_rate=16000,
                 frames_per_buffer=1024,
                 device=None):
        super().__init__()
        self.daemon = True
        self._stop_event = threading.Event()
        self.device = device
        self.init_stream(format=format,
                         channels=channels,
                         sample_rate=sample_rate,
                         frames_per_buffer=frames_per_buffer)
        self.waveform = []

    def run(self):
        self.waveform = []
        chunk_size = 1024
        while not self._stop_event.is_set():
            data = self.stream.read(chunk_size)
            data = np.frombuffer(data, dtype='int16')
            self.waveform.extend(data)
        self.deinit_stream()

    def init_stream(self,
                    format=pyaudio.paInt16,
                    channels=1,
                    sample_rate=16000,
                    frames_per_buffer=1024):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=format,
            channels=channels,
            rate=sample_rate,
            input=True,
            input_device_index=self.device['index'],
            frames_per_buffer=frames_per_buffer
        )
        print("Initialized the stream reader successfully.")

    def deinit_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        print("Deinitialized the stream reader successfully.")

    def stop(self):
        self._stop_event.set()


if __name__ == "__main__":
    device = init_device()
    recorder = Recorder(device=device)

    input("按下任意键开始录音")
    recorder.start()

    input("按下任意键结束录音")
    recorder.stop()
    recorder.join()

    save_wavfile('noise.wav', recorder.waveform)

