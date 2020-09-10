#! /usr/bin/env python
import pyaudio
import os
import wave
import difflib
import playsound
from aip import AipSpeech
FORMAT = pyaudio.paInt16
CHUNK = 1024
CHANNELS = 1
RATE = 16000
FILE_TIME = 2  #唤醒语音长度.每次识别两秒钟


def record_audio():

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,  #采集位数
        channels=CHANNELS,  #声道
        rate=RATE,  #帧数
        input=True,  #打开输入流
        frames_per_buffer=CHUNK)
    strnames = []
    for i in range(0, int(RATE / CHUNK * FILE_TIME)):
        data = stream.read(CHUNK)
        strnames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open('/usr/local/src/seek/wave_out.wav', 'wb')  # 打开wav文件
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(strnames))
    wf.close()


def baidu_pid():
    URL = "http://vop.baidu.com/server_api"
    APP_ID = "22546225*"
    API_KEY = "PtKOVyDIy8iRPE3041yXUxxa"
    SECRET_KEY = "g6BunbQL2jeEuILzdp1dGeUML5ccPX9S"
    str_key = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return str_key


def list_TEXT():
    client = baidu_pid()
    with open('/usr/local/src/seek/wave_out.wav', 'rb') as f:
        audio_data = f.read()
    result = client.asr(audio_data, 'wav', 16000, {
        'lan': 'zh',
    })
    result_text = result["result"][0]
    return result_text


def IfTest_():
    strch = list_TEXT()
    list_str = ['老师', '小爱']  #唤醒命令
    master = difflib.get_close_matches(strch, list_str, 1, cutoff=0.4)
    #print(master)
    if len(master) == 0:
        main()
    else:
        playsound.playsound('/usr/local/src/seek/head.mp3')
        os.system('python ' + '/usr/local/src/seek/VoiceRunning.py')
        main()


def main():
    record_audio()
    IfTest_()


main()
