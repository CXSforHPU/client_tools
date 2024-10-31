"""
待完成
"""
import gradio as gr
from flask import Flask, render_template, request, redirect
from flask_sock import Sock
from client_tools import *
import os
import yaml
#todo(sy) 添加web界面应用

"""
chat请求函数
"""
def chatbot_reponse(message):
    ai = chatgml()
    ques=message
    user_ed = ai.make_send_json(ques)
    assitant = ai.post(user_ed)
    return assitant

"""
tts请求函数
"""
def tts_reponse(txt):
    tts = SovitsClient()
    tts.text_to_speech(text=txt, path="./test.wav")
    return "./test.wav"


"""
语音识别请求函数
"""
def SpeehToText_reponse():
    api = SpeehToText()

    data = api.post(r"./test.wav")
    return data

#定义flaskapp
app = Flask(__name__,template_folder="templates",static_folder="static")
sock = Sock(app)
#设置static文件夹
app.config['STATIC_FOLDER'] ='static'

#主页
@app.route('/')
def index():
    return "你好，世界"

#定义ws路由
@app.route('/ws')
def websocket():

    return render_template("index.html")

#定义echo对话路由
@sock.route('/echo')
def echo(self):
    while True:
        data = self.receive()
        get_data=chatbot_reponse(data)
        self.send(get_data)


@app.route('/state')
def state():
    getHomeState("./data.yml")

    return render_template("state.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8989)
