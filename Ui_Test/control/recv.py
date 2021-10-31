# import socket
# import threading
# import time
#
# def recv():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect(("127.0.0.1", 8888))
#     data = s.recv(1024).decode("utf-8")
#     t = data.replace("[", '')
#     t = t.replace("]", '')
#     data= t.replace(" ",'')
#     data = t.split(",")
#     finger = data[1::2]
#     # print(finger)
#     return  finger
import serial


def recv():
    finger_num = []
    ser = serial.Serial('COM4', 115200,)
    data = ser.readline().strip()
    str_data = str(data)
    original_data = str_data.replace('b', '').replace("'", '').split(",")
    # print("初步处理后的数据",original_data)
    for i in original_data:
        if ":" in i:
            middle_data = i.split(":")
            finger_num.append(middle_data[1])
        else: finger_num.append('165')
    if len(finger_num)!=5:
        finger_num = ['165','165','165','165','165']
    ser.close()
    # print(finger_num)
    return  finger_num

recv()




