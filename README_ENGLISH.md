
## Introduction
Updates Nov.8:
1. The communication protocol which described in the document before has been applied and all upgrades are applied to receiver.py, camera.py and control_panel.
2. In the main functions of receiver and camera.py, there is a True/False switch for major receiver/camera.
3. To protect the receiver process, use receiver_safe_mode.py. When you run it, it establish the main process of receiver_safe_mode.py, which starts receiver.py as a subprocess and monitors whether it is exited. If exited, receiver.py is restarted immediately. The recovery speed is even within 0.1 seconds. No sudo permit needed anymore.

## Quick Start

<details>
<summary>Installation</summary>

Step1. Install libraries

Install Anaconda
Install Python==3.8
If you have an NVIDIA GPU with more than 6GB of video memory, you can configure an additional GPU environment to use GPU reasoning. To do this, a Linux installation (Ubuntu 18.04) is required.

CPU reasoning is less efficient and may not be smooth and responsive.
This project was tested on an RTX3080Ti.

```shell 
python3 setup.py develop
pip install -r requirement.txt
```

<details>
<summary>Demo</summary>
There can theoretically be dozens of receivers, control panels and cameras. They work as follows:

First prepare a public IP address and port (visible to all computers that need to participate), because I only test on my computer, so I set it to 127.0.0.1, if you are different, please change it here.

Run the receiver script on any computer that needs to be protected (or on a computer connected to the display screen), the script will continuously listen for traffic from the public IP address above in the background, and start the screen saver when it recognizes 1 or 2. 1 means candid behavior, 2 means that any camera is blocked. When any one of them behaves more than 10 times (it is detected 10 times, this is considering the false alarm situation), it will automatically send an email to the mailbox.

Run the camera script on any computer with a camera (or on the central control computer), when it detects an abnormal situation (such as 1 or 2), it will send a signal to the above IP address using UDP broadcast.

Run control_panel.py on any computer that needs to participate in manual control and it will generate a simple GUI that allows you to manually signal abnormal conditions.



cameras
Launch receiver(on any computers but they must be able to monitor the traffic on the same ip a  ddress)
```shell
python receiver.py
```

Start Control Panel(an GUI interface to send signals manually)
```shell
python control_panel.py
```

Launch camera(on any computers but they must be able to send traffic on the same ip address)
```shell
python camera.py webcam -n yolox-s -c pretrained/yolox_s.pth --conf 0.25 --nms 0.45 --tsize 640
```

<details>
<summary>SPECIAL NOTICE!!</summary>
Please refer to the comments in receiver.py (it may be in Chinese, but it does not affect understanding, you can delete it or translate it into other languages) and replace the sending email and target email with your email and your receiving email address. Please don't use mine, because I'll be logging out of that account right away after days. At that point your program will crash.

