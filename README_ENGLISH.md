
## Introduction

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
cd YOLOX 
python3 setup.py develop
cd .. (back to project root）
pip install -r requirement.txt
```

<details>
<summary>Demo</summary>

```shell
python demo.py webcam -n yolox-s -c pretrained/yolox_s.pth --conf 0.25 --nms 0.45 --tsize 640
```


