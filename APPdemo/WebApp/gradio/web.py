import gradio as gr
from utils.gray2RGB import gray2RGB
from utils.fix_photo import run_codeformer
from utils.fixAndGray2RGB import fix_and_gray2RGB
from PIL import Image
from utils.chat import ai
import threading

# 图像处理函数
def process_data1(image):

    run_codeformer(image, "output/out.jpg")
    return "output/out.jpg"


def process_data2(image):

    gray2RGB(image, "output.jpg")
    return "output.jpg"


def process_data3(image):


    fix_and_gray2RGB(image, "output.jpg")
    return "output.jpg"


# 聊天处理函数
def doChatbot(message, history):
    t = message
    app = ai()
    aw = app.historian.history_deal(t)
    return aw


# 生成图片处理界面和聊天界面的通用布局
def create_tab(process_function, tab_label):
    with gr.Tab(label=tab_label, elem_id="label", elem_classes="button", interactive=True):
        with gr.Row():
            with gr.Column(scale=1):  # 左侧图片上传和处理
                image_input = gr.Image(sources=["upload"], label="选择图片", elem_id="image_input", type="filepath")
                submit_button = gr.Button(value="提交", elem_id="submit_button")
                image_output = gr.Image(label="输出图片", elem_id="image_output")
                submit_button.click(fn=process_function, inputs=[image_input], outputs=[image_output])

            with gr.Column(scale=1):  # 右侧聊天功能
                gr.ChatInterface(
                    fn=doChatbot,
                    chatbot=gr.Chatbot(elem_id="chatbot",scale=7,label="AI历史专家"),
                    textbox=gr.Textbox(placeholder="请输入您的问题", container=False, scale=1,elem_id="textbox"),
                    theme="soft",
                    examples=["介绍一下王忠殿。", "介绍一下狼牙山五壮士之一的宋学义。"],
                    retry_btn="刷新",
                    undo_btn=None,
                    submit_btn="发送",
                    clear_btn="清空"
                ).queue()


# 主程序
with gr.Blocks(css="css/test.css",title="") as demo:  # title:网站标题
    with gr.Tabs(elem_id="labels", elem_classes="labels1"):
        # Tab 1: 图片修复
        create_tab(process_data1, "图片修复")
        # Tab 2: 颜色修复
        create_tab(process_data2, "颜色修复")
        # Tab 3: 一键修复颜色和像素
        create_tab(process_data3, "一键修复颜色和像素")

demo.launch(server_port=7860)
