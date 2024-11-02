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
  "chatgml6b": "http://127.0.0.1:8000",    //访问url地址
  "luckycola": "https://luckycola.com.cn/hunyuan/txhy",  //访问url地址
  "luckycola_wxyy": "https://luckycola.com.cn/ai/openwxyy", //访问url地址
  "stt": "http://127.0.0.1:9977/api",//访问url地址
  "tts": "http://127.0.0.1:5000"  //访问url地址
}
```
* 此为默认地址
* 若自己有域名进行更改的话
  * 将自己的域名对其进行替换
***
# TTS
## 模块位置
***./client_tools/tts_stt_client/sovits_client***

# STT
## 模块位置
***./client_tools/tts_stt_client/stt_client***

# chat模块
## 模块位置
***./client_tools/tts_stt_client/chat_client***
* ./client_tools/tts_stt_client/chat_client/chatgml6b.py
  * 此文件提供了chatgml6b的api接口方式

## 并且提供三个接口
### make_send_json()
* 制作要发送的json数据包，返回类型为dict
### post()
* 发送json数据包
* reture 经过get_assitant解析过的数据
### get_assitant()
* 解析返回json中的assitant
* 发送与解析

***
# todo list
- [ ] 完善文档内容
## api模块
- [x] 添加TTS客户端模块
- [ ] 添加chat客户端模块
  - [x] 提供chatgml6b模块
  - [x] 提供luckycola 厂商提供api
    - [x] 文心一言
    - [x] 腾讯混元
- [x] 添加STT客户端模块
- [x] 提供智能体对话支持模块
  - [ ] 添加更多支持的Prompt在 ./client_tools/chat_client/prompt.json 文件下
  * 目前支持的如下
    * Linux
      * 我想让你充当一个linux终端。我将键入命令，您将用终端应该显示的内容进行回复。我希望您只回复一个唯一代码块中的终端输出，而不回复其他内容。不要写解释。除非我指示你，否则不要键入命令。当我需要用英语告诉你一些事情时，我的第一个命令是 {}
    * 翻译
      * 现在你是一个专业的英汉互译器，我输入中文时，你会将其翻译成英文，我输入英文时，你会将其翻译成中文。接下来，我输入的内容是 {}"
    * 励志教练
      * 我想让你成为一名励志教练。我会为你提供一些关于某人目标和挑战的信息，你的工作是制定能够帮助此人实现目标的策略。这可能包括提供积极的肯定，给出有用的建议或建议他们可以做些什么来达到最终目标。我的第一个要求是 {}。
- [x] 添加获取此时室内温度及湿度客户端模块
## dirvers文件夹下
- [ ] 制作音频输入模块
- [ ] 制作音频输出模块
- [ ] 制作中断管理模块
## flowsheet文件夹下
- [x] 添加工作流程图
***
# ***欢迎大家设计不同的app来提交pr***
## APPDemo文件夹下
- [ ] 添加web界面应用
  - [ ] 显示chat对话
  - [ ] 显示室内健康程度监测
- [x] 添加对话app demo
  - [x] 普通对话
  - [x] 智能体对话
- [ ] 说书APP
- [ ] 打印家庭状况 demo
