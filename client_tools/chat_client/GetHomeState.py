import requests
import client_tools

def getHomeState(path):
    url = client_tools.LoadConfigFile("HomeStateData")
    response = requests.get(url,stream=True)
    if response.status_code == 200:  # 检查响应状态码
        with open(path, 'wb') as f:  # 打开本地文件进行写入操作
            for chunk in response.iter_content(chunk_size=1024):  # 分块读取文件内容，每次读取1KB
                if chunk:  # 检查是否有数据块可读
                    f.write(chunk)  # 将数据块写入本地文件
                    f.flush()  # 刷新缓冲区，确保数据写入磁盘
        print('文件下载完成！')
    else:
        print('下载失败，状态码：', response.status_code)

if __name__ == '__main__':
    getHomeState("./config.yml")
