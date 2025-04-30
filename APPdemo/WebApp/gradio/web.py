import os
import sys
import json
#添加包环境变量
path = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(path,"..","..","..")
sys.path.append(path)
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
from client_tools import *
import threading

# 初始化聊天工具
chat = chatgml()

# 模拟生成数据的函数（可以用真实数据替代）
# 图像处理函数
def process_data1(image):
    getHomeState("./data.yml")
    time, temperature, humidity = LoadHomeState(r"./data.yml", num=3)
    temperature = np.array(temperature)
    temperature[np.isnan(temperature)] = np.mean(temperature)

    plt.figure(figsize=(10, 6))
    plt.plot(time, temperature, marker="o", linestyle="-", color="red", label="Temperature (°C)", linewidth=2,
             markersize=5)
    # 标题和轴标签
    plt.title("Time vs Temperature", fontsize=16, fontweight="bold", color="#333333")
    plt.xlabel("Time (units)", fontsize=14)
    plt.ylabel("Value", fontsize=14)

    # 设置 x 轴显示的刻度
    max_ticks = 10  # 只显示 30 个刻度
    indices = np.linspace(0, len(time) - 1, max_ticks, dtype=int)  # 选取 30 个均匀分布的索引
    plt.xticks(ticks=indices, labels=[time[i] for i in indices], fontsize=5)  # 设置刻度位置与标签

    # 网格设置
    plt.grid(color="gray", linestyle=":", linewidth=0.5, alpha=0.7)

    # 图例优化
    plt.legend(loc="upper left", fontsize=12, frameon=True, shadow=True, fancybox=True, borderpad=1)
    plt.savefig("./tem.png")
    plt.close()
    return "./tem.png"


def process_data2(image):
    getHomeState("./data.yml")
    time, temperature, humidity = LoadHomeState(r"./data.yml", num=3)

    humidity = np.array(humidity)
    humidity[np.isnan(humidity)] = np.mean(humidity)

    plt.figure(figsize=(10, 6))
    plt.plot(time, humidity, marker="o", linestyle="-", color="blue", label="humidity", linewidth=2,
             markersize=5)
    # 标题和轴标签
    plt.title("Time vs humidity", fontsize=16, fontweight="bold", color="#333333")
    plt.xlabel("Time (units)", fontsize=14)
    plt.ylabel("Value", fontsize=14)

    # 设置 x 轴显示的刻度
    max_ticks = 5  # 只显示 30 个刻度
    indices = np.linspace(0, len(time) - 1, max_ticks, dtype=int)  # 选取 30 个均匀分布的索引
    plt.xticks(ticks=indices, labels=[time[i] for i in indices], fontsize=5)  # 设置刻度位置与标签

    # 网格设置
    plt.grid(color="gray", linestyle=":", linewidth=0.5, alpha=0.7)

    # 图例优化
    plt.legend(loc="upper left", fontsize=12, frameon=True, shadow=True, fancybox=True, borderpad=1)
    plt.savefig("./hum.png")
    plt.close()
    return "./hum.png"


# 绘制折线图
def draw_line_chart():
    getHomeState("./data.yml")
    time, temperature, humidity = LoadHomeState(r"./data.yml", num=3)
    # 格式化为 Gradio LinePlot 支持的 DataFrame 格式
    data = pd.DataFrame({
        "Time": time,
        "Temperature (°C)": temperature,
        "Humidity (%)": humidity,
    })
    return data

# 聊天处理函数
def doChatbot(message, history):
    num = message.find("家庭状况")
    if num != -1:
        dic = {}
        getHomeState("./data.yml")
        time, tem, hum = LoadHomeState(r"./data.yml")
        dic["time"] = time[-10:]
        dic["tem"] = tem[-10:]
        dic["hum"] = hum[-10:]
        content = json.dumps(dic)
        print(content)
        message += "\n温湿度以及时间如下JSON数据:\n" + content
    user_ed = chat.make_send_json(message)
    assistant = chat.post(user_ed)
    return assistant



# 生成图片处理界面和聊天界面的通用布局
def create_tab(process_function, tab_label):
    with gr.Tab(label=tab_label, elem_id="label", elem_classes="button", interactive=True):
        with gr.Row():
            with gr.Column(scale=1):  # 左侧图片上传和处理
                submit_button = gr.Button(value="检测家庭状况", elem_id="submit_button")
                image_output = gr.Image(label="输出图片", elem_id="image_output")
                submit_button.click(fn=process_function, inputs=[], outputs=[image_output])

            with gr.Column(scale=1):  # 右侧聊天功能
                gr.ChatInterface(
                    fn=doChatbot,
                    chatbot=gr.Chatbot(elem_id="chatbot",scale=7,label="Friday-家庭智能管家"),
                    textbox=gr.Textbox(placeholder="请输入您的问题", container=False, scale=1,elem_id="textbox"),
                    theme="soft",
                    examples=["检测家庭状况，并给出建议", "讲一个故事"],
                    retry_btn="刷新",
                    undo_btn=None,
                    submit_btn="发送",
                    clear_btn="清空"
                ).queue()


# 主程序
with gr.Blocks(css="css/test.css",title="") as demo:  # title:网站标题
    with gr.Tabs(elem_id="labels", elem_classes="labels1"):
        # Tab 1: 图片修复
        create_tab(process_data1, "显示时间与温度")
        # Tab 2: 颜色修复
        create_tab(process_data2, "显示时间与湿度")


demo.launch(server_port=7860)