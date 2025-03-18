# client_tools
***
* TTS
  * https://github.com/RVC-Boss/GPT-SoVITS
* STT
  * https://github.com/jianchang512/stt
* chat
  * chatgml6b
  * https://luckycola.com.cn
    * luckycola-文心一言
    * luckycola-腾讯混元
# config文件介绍
***./client_tools/config.json***
```json
{
  "chatgml6b": "http://chatglm6b.f3.ttvt.cc",
  "luckycola": "https://luckycola.com.cn/hunyuan/txhy",
  "luckycola_wxyy": "https://luckycola.com.cn/ai/openwxyy",
  "stt": "http://stt.if4.ttyt.cc/api",
  "tts": "http://tts.if4.ttyt.cc",
  "HomeStateData": "http://home.if4.ttyt.cc"
}
```
* 此为默认地址
* 若自己有域名进行更改的话
  * 将自己的域名对其进行替换
***

# TTS
## 模块位置
***./client_tools/tts_stt_client/sovits_client.py***

  将文本文件转为音频文件，并存储到指定位置。
```python
tts = SovitsClient()
"""
text_to_speech()
        """
        :param text:    文本（str）
        :param path:    指定文件编写路径
        :return:
        """
"""
tts.text_to_speech(text="举头望明月，低头思故乡",path="./test.wav")
```

# STT
## 模块位置
***./client_tools/tts_stt_client/stt_client.py***

  将音频文件转为文本，并存储到指定位置，还可以输出文本内容。

```python

"""
post(self,file_path):
        """
        :param file_path: 音频文件路径
        :return : 返回文字转语音的数据
        """
"""
```

# chat模块
## 模块位置
***./client_tools/chat_client/chatgml6b.py***

    此文件提供了chatgml6b的api接口方式
  
    通过调用api接口，可以进行长对话，而且支持通过提示词与智能体对话。
```python
  
make_send_json()
* 制作要发送的json数据包，返回类型为dict
post()
* 发送json数据包
* reture 经过get_assitant解析过的数据
get_assitant()
* 解析返回json中的assitant
* 发送与解析
```
# utils 模块
## 模块位置
***./client_tools/utils/LoadConfig.py***

    通过获取传感器的信息，将信息存储到文件中，读取文件中时间，温度，湿度的数据并输出。
```python 
LoadConfigFile(name):
    """
    :param name: config file name
    :return: url
    """

GetPromptFile(name):
    """
    :param name: 获取角色名字
    :return:    prompt指令
    """

LoadHomeState(path,num=10):
    """
    :param path: data.yml 文件路径
    :parm num : 最新的几组数据
    :return : 返回三组列表,时间，温度，湿度
    """

```
***./client_tools/utils/DrawHomeState.py***
```python
DrawHomeStateCMD(num=10):
    """
    :param num:指定绘制最新的几组数据
    """
```

***
# todo list
- [ ] 完善文档内容
## api模块
- [x] 添加下载进度条
- [x] 添加TTS客户端模块
- [ ] 添加chat客户端模块
  - [x] 提供chatgml3-6b模块
  - [x] deepseek 
  - [x] 提供luckycola 厂商提供api
    - [x] 文心一言
    - [x] 腾讯混元
    - [x] 众多模型均适用的调用函数文件
- [x] 添加STT客户端模块
- [x] 提供智能体对话支持模块
  - [x] 添加更多支持的Prompt在 ./client_tools/chat_client/prompt.json 文件下
- [x] 添加获取此时室内温度及湿度客户端模块
## dirvers文件夹下
- [ ] 制作音频输入模块
  - [x] pyaudio添加录音模块
- [ ] 制作音频输出模块
    - [x] pyaudio添加放音模块
- [ ] 制作中断管理模块
## flowsheet文件夹下
- [x] 添加工作流程图
## utils文件夹下  
- [x] 添加指定获取url模块
- [x] 添加指定获取prompt模块
- [x] 添加终端家庭状况可视化输出模块
***
# ***欢迎大家设计不同的app来提交pr***
## APPDemo文件夹下
- [ ] 添加web界面应用
  - [x] 显示chat对话
  - [x] 显示室内健康程度监测
- [x] 添加对话app demo
  - [x] 普通对话
  - [x] 智能体对话
- [ ] 说书APP
- [ ] 打印家庭状况 demo
  - [x] 终端打印 
- [ ] orangepi适配
  - [x] 语音对话demo
  - [x] 家庭状况检测demo 
***
部分文档链接
【腾讯文档】技术文档
https://docs.qq.com/doc/DWGZuelJrdElCbWFm
