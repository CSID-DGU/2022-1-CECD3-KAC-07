#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import socket



import smtplib
from email.mime.text import MIMEText

from smtplib import SMTP_SSL
from email.mime.text import MIMEText


total_block = 0
total_cap = 0

def sendmail(data):
    # Fill in the real email server username and password
    user = 'zhang@iuct.science'
    password = 'Aa321654'
    # Content of email
    msg = MIMEText(f"Warning:\nRisky behavior detected more than 20 times .\nThis email is an alarm email sent by the system automatically, please contact the administrator.\n", 'plain', _charset="utf-8")
    # Email subject description
    msg["Subject"] = 'Status Update' 
    # Sender display, no actual effect stated
    msg["from"] = 'Control Panel'
    # Recipient display, no actual effect
    msg["to"] = '1916700554@qq.com'

    with SMTP_SSL(host="smtp.exmail.qq.com",port=465) as smtp:
        # Log in to the outgoing mail server
        smtp.login(user = user, password = password)
        # Actual sending and receiving mail configuration
        smtp.sendmail(from_addr = user, to_addrs='843770649@qq.com'.split(','), msg=msg.as_string())



def blockcamera(duration=2000):
    global total_block
    output = cv2.imread("noshot.jpg")
    out_win = "output_style_full_screen"
    cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(out_win, output)
    ch = cv2.waitKey(duration)
    cv2.destroyAllWindows()
    total_block +=1
    if total_block>10:
        print('called sendmail function')
        total_block=0
        sendmail(1)


def capcamera(duration=2000):
    global total_cap
    output = cv2.imread("nocap.jpg")
    out_win = "output_style_full_screen"
    cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(out_win, output)
    ch = cv2.waitKey(duration)
    cv2.destroyAllWindows()
    total_cap +=1
    if total_cap>10:
        print('called sendmail function')
        total_cap=0
        sendmail(2)


def main ():
    major = False
    # 1 create socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2 bind local information
    local_addr = ("127.0.0.1", 8888)  # If ip is not written, it means any ip
    udp_socket.bind(local_addr)
    while True:
        signal = 0
        # 3 waiting to receive
        recv_data = udp_socket.recvfrom(1024)  # 1024 indicates the maximum number of bytes received this time, recv only accepts data, recvfrom accepts data and the other party’s ip port
        # 4 show received data
        signal = recv_data[0].decode("gbk")

        print(f'Signal_received {signal}')

        if signal == 'SIGNAL1':
            blockcamera()
        elif signal == 'SIGNAL2':
            capcamera()
        elif signal == 'SIGNAL1_LONG':
            blockcamera(30000)
        elif signal == 'SIGNAL2_LONG':
            capcamera(30000)
        elif signal == 'SIGNAL_1_MAJOR':
            if major:
                blockcamera()
        elif signal == 'SIGNAL_2_MAJOR':
            if major:
                capcamera()
        elif signal == 'ALLBLIND':
            while True:
                capcamera()
                udp_socket.settimeout(0.001)
                try:
                    recv_data = udp_socket.recvfrom(1024)
                    signal = recv_data[0].decode("gbk")
                except socket.timeout as e:
                    pass
                if signal == 'ALLBLIND_RELEASE':
                    break
            udp_socket.settimeout(10000)
        elif signal == 'BLANK':
            print('Blank Signal Recvd')
            pass
        else:
            continue
    # 5 close socket
    udp_socket.close()


if __name__ == '__main__':
    main()
    #sendmail(1)

