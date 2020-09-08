#! /usr/bin/env python
import pyaudio
import os
import playsound
import wave
import difflib
from aip import AipSpeech
FORMAT = pyaudio.paInt16
CHUNK = 1024
CHANNELS = 1
RATE = 16000
FILE_TIME = 3


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
    APP_ID = "22546225"
    API_KEY = "PtKOVyDIy8iRPE3041yXUxxa"
    SECRET_KEY = "g6BunbQL2jeEuILzdp1dGeUML5ccPX9S"
    str_key = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return str_key


def list_TEXT():
    #返回语音转换的文字 for str
    client = baidu_pid()
    with open('/usr/local/src/seek/wave_out.wav', 'rb') as f:
        audio_data = f.read()
    result = client.asr(audio_data, 'wav', 16000, {
        'lan': 'zh',
    })
    result_text = result["result"][0]
    return result_text


def file_shell():
    filenames = []
    for filename in os.listdir(r'/usr/local/src/seek/File_shell'):
        filenames.append(filename)
    return filenames


def run_shell(strname):
    file_sh = file_shell()
    print(file_sh)
    #strname = list_TEXT()
    print(strname)
    file_name = difflib.get_close_matches(strname, file_sh, 1, cutoff=0.4)

    strname = "".join(file_name)
    bash_file = '/usr/local/src/seek/File_shell/' + "".join(file_name)
    playsound.playsound('/usr/local/src/seek/head.mp3')
    os.system('bash ' + bash_file)


def Application_Aido():
    #图灵语音机器人接口
    #识别语音 ->转换文字 -> 推送到图灵语音机器人->返回文字内容 -> 语音合成 -> 播报语音
    pass


def main():
    record_audio()
    strname = list_TEXT()
    print(strname)
    Application_List = ['打开只能语音服务']
    Application_Judge = difflib.get_close_matches(strname,
                                                  Application_List,
                                                  1,
                                                  cutoff=0.5)
    #优先匹配语音服务 ，无法匹配则启动自定义脚本
    Application_Str = "".join(Application_Judge)
    if (Application_Str != ""):
        Application_Aido()
    else:
        run_shell(strname)


main()
