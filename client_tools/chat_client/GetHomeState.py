import requests
import client_tools
from tqdm import tqdm

def getHomeState(path):
    url = client_tools.LoadConfigFile("HomeStateData")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查响应状态码，如果有错误则抛出HTTPError异常
    except requests.exceptions.HTTPError as err:
        print('下载失败，错误：', err)
        return

    # 获取文件大小（如果服务器提供了这个信息）
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 每次读取的块大小

    with open(path, 'wb') as f:
        with tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, desc="下载进度") as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))  # 更新进度条

    print('文件下载完成！')

if __name__ == '__main__':
    getHomeState("./config.yml")