
## Introduction

## Quick Start

<details>
<summary>Installation</summary>

Step1. Install libraries

安装Anaconda
安装Python==3.8
如果有NVIDIA GPU且显存大于6GB,则可以配置额外的GPU环境来使用GPU推理。要做到这一点，需要安装Linux(Ubuntu 18.04）。

```shell
cd YOLOX (切换回项目YOLOX目录下）
python3 setup.py develop
cd .. (切换回项目根目录）
pip3 install -r requirement.txt
```

</details>

<details>
Step2. 安装相关库

Step1. 从上面的benchmark table下载预训练模型，或者从官方repo下载.
如果有gpu，可以用l,x结尾的大模型，如果没有，建议使用 s m tiny之类的小模型

下面的例子以best_ckpt为例。

从摄像头推理
```shell
python demo.py webcam -n yolox-s -c pretrained/best_ckpt.pth --conf 0.25 --nms 0.45 --tsize 640
```


</details>

<details>
<summary>重新训练模型</summary>

Step1. Prepare COCO dataset
只要你是完整的下载了工程，这一步我已经做好了。另外，在dataset里，还有原始的数据集压缩包，如果搞坏了可以直接覆盖回去。

Step2. Reproduce our results on COCO by specifying -n:

```shell
python -m yolox.tools.train -n yolox-s -d 8 -b 64 --fp16 -o [--cache]
                               yolox-m
                               yolox-l
                               yolox-x
```
* -d: number of gpu devices
* -b: total batch size, the recommended number for -b is num-gpu * 8
* --fp16: mixed precision training
* --cache: caching imgs into RAM to accelarate training, which need large system RAM. 

  
When using -f, the above commands are equivalent to:
```shell
python -m yolox.tools.train -f exps/default/yolox_s.py -d 8 -b 64 --fp16 -o [--cache]
                               exps/default/yolox_m.py
                               exps/default/yolox_l.py
                               exps/default/yolox_x.py
```
  
That's all folks.
