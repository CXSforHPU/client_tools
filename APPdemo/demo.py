from client_tools import *


if __name__ == '__main__':
    getHomeState("./data.yml")
    time,tem,hum = LoadHomeState(r"./data.yml")
    print(time)
    print(tem)
    print(hum)
    print(len(hum))