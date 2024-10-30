"""
导入 chat_client模块以及获取家庭状况模块
"""

from client_tools.chat_client.chatgml6b import chatgml
from client_tools.chat_client.luckycola import LuckyCola_TXHY
from client_tools.chat_client.luckycola_wxyy import LuckyCola_wxyy
from client_tools.chat_client.GetHomeState import *

"""
导入 tts_stt_client 模块
"""
from client_tools.tts_stt_client.sovits_client import SovitsClient
from client_tools.tts_stt_client.stt_client import SpeehToText