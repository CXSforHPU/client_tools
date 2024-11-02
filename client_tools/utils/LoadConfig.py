import os
import client_tools
import json
import yaml

def LoadConfigFile(name):
    """
    :param name: config file name
    :return: url
    """
    if os.name == "posix":
        ls = str(client_tools.__file__).split("/")
        path = "/" + ls[1]
        for i in ls[2:-1]:
            path = path + "/" + i

        path = os.path.join(path,"config.json")

    elif os.name == "nt":
        ls = str(client_tools.__file__).split("\\")
        path = ls[0]
        for i in ls[1:-1]:
            path = path + "\\" + i
        path = os.path.join(path,"config.json")

    with open(path, 'r', encoding='utf-8') as f:
        config = json.load(f)
        context= config[name]

    return context

def GetPromptFile(name):
    """
    :param name: 获取角色名字
    :return:    prompt指令
    """

    if os.name == "posix":
        ls = str(client_tools.__file__).split("/")
        path = "/" + ls[1]
        for i in ls[2:-1]:
            path = path + "/" + i
        path = os.path.join(path, "chat_client", "prompt.json")

    elif os.name == "nt":
        ls = str(client_tools.__file__).split("\\")
        path = ls[0]
        for i in ls[1:-1]:
            path = path + "\\" + i
        path = os.path.join(path, "chat_client", "prompt.json")

    with open(path, "r", encoding="utf8") as f:
        data = json.load(f)

    return data.get(name)

def LoadHomeState(path,num=10):
    """
    :param path: data.yml 文件路径
    :parm num : 最新的几组数据
    :return : 返回三组列表,时间，温度，湿度
    """
    time = []
    temperature = []
    humidity = []
    with open(path,"r", encoding="utf8") as f:
        data = yaml.load(f.read(),Loader=yaml.FullLoader).get("data")
    ls = data[-num:].copy()
    del data
    for i in ls:
        for tim,HumTem in i.items():
            hum,tem = HumTem.split("\t")
            time.append(tim)
            temperature.append(tem)
            humidity.append(hum)

    return time,temperature,humidity


if __name__ == "__main__":
    time,tem,hum = LoadHomeState(r"C:\Users\31309\Desktop\xx\project\client_tools\client_tools\chat_client\config.yml")
    print(time)
    print(tem)
    print(hum)
    print(len(hum))