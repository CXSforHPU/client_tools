import pyaudio

def list_devices(devices_type=1):
    """
    :param devices_type: 设备类型 输入设备为1，输出设备 为 0，
    默认为 输入设备

    """
    name = ""
    if devices_type == 1:
        devices_type = 'maxInputChannels'
        name = "input"
    else:
        devices_type = 'maxOutputChannels'
        name = "output"
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    devices = []
    for i in range(numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get(devices_type) > 0:
            devices.append(p.get_device_info_by_host_api_device_index(0, i))
    p.terminate()

    print(f"Available {name} devices:")
    devices_dict = {}
    for i, device in enumerate(devices):
        print(f"{i}: {device['name']}")
        devices_dict[device['name']] = i
    return devices, devices_dict

def init_device(devices_type=1):
    devices, devices_dict = list_devices(devices_type)
    device_id = int(input("请选择设备:"))
    print("选择设备：", devices[device_id])
    device = devices[device_id]  # Select the first available device, modify as needed
    return device




if __name__ == "__main__":
    device = init_device(1)

