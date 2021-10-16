import json
import random
import socket
import threading

def ran(s):
    sjs_key = [1,2,3,4,5]
    sjs_value = []
    sjs = []
    for i in range(5):
        sjs_value.append(round(random.uniform(0,330),2))
        sjs.append(sjs_key[i])
        sjs.append(sjs_value[i])
    print(sjs)
    finger_num =json.dumps(sjs)
    s.send(finger_num.encode(encoding="utf-8"))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",8888))
    s.listen(5)
    print("TCP服务器正在执行")
    print("等待新的链接")
    while True:
        s_fd,addr = s.accept()
        thread = threading.Thread(target=ran, args=(s_fd,))
        thread.start()



# import json
# import socket
# import threading
# import time
# import random
# HOST = '127.0.0.1'
# PORT= 3366
# BUFSIZE = 2048
# ADDR = (HOST,PORT)
# def ran(s):
#         data, addr = udp_sever.recvfrom(BUFSIZE)
#         print(addr)
#         sjs_key = [1,2,3,4,5]
#         sjs_value = []
#         sjs = []
#         for i in range(5):
#             sjs_value.append(round(random.uniform(0,330),2))
#             sjs.append(sjs_key[i])
#             sjs.append(sjs_value[i])
#         finger_num =json.dumps(sjs)
#         s.sendto(finger_num.encode(encoding="utf-8"),addr)
#     # time.sleep(0.1)
# if __name__ == '__main__':
#     udp_sever =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     udp_sever.bind(ADDR)
#     # ran(udp_sever,data)
#     while True:
#         thread = threading.Thread(target=ran, args=(udp_sever,))
#         thread.start()