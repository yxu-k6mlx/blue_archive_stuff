# Welcome 欢迎
## What is this? 关于本项目
The aim of this project is to provide an open-source alternative to AzureArchive (henceforth AA) written entirely in Python with `tkinter` library instead of using the `Unity` framework which AA utilizes. Developed by Foxxlight, AzureArchive is a fan-story maker intended to provide a visual editor for, and compile and simulate the story player in popular mobile game *Blue Archive*. 

本项目致力于向大众提供一个开源的AzureArchive (AA)竞品. 项目会尽可能只使用Python自带的`tkinter`GUI开发库以保未来的可重开发性, 而不是像AA一样使用碧蓝档案本家在用的`Unity`游戏引擎. AA由狐光体开发, 是Nexon开发的手游*碧蓝档案*的二创故事播放-编辑器. 

Disclaimers / 免责声明: 

This project is NOT for-profit. It is in fact FREE for all to use and modify. Some assets used may be from *Blue Archive* itself and can be copyrighted material. This repo nor its author is affliated with Nexon, Nexon Games or Yostar. All game artwork, information and assets used in this database are the property and copyright of the respective authors. 

## Why make this when AzureArchive and ArisStudio already exists? 关于创作动机
First let me start off by saying AzureArchive is a great program, per se. However, I have been horribly misunderstood and subsequently heavily remonstrated and insulted by a couple members of AzureArchive's dev and management team thinking I am an Internet troll when demostrating one of the bugs I have encountered when making fan-content with AA. Safe to say that did not make me feel happy. But this in turn did make me feel motivated to do something with my Python development skills. Therefore, ba-tools is born. 

首先, AzureArchive本身是个好软件. 然而在几天前本人在报告使用中遇到的的bug时被多名官群管理当成找茬的给骂出来了. 虽然搞得大家都很不开心, 但是此事使我开发欲大法. 这个项目就是我被踢出去以前说的开源替代品. 

## This applications seems to be still in its early development stages, what is the plan here? 关于开发计划
Yes, it is in its early dev stage mainly because I have just made `main.py` yesterday. There are three phases planned: 

1. Construct a story player which reads from json files describing each frame in the player. After this can be displayed correctly, the autoplay function as well as restart, log, and prev-next frame will be developed. 

2. Construct or fork and adopt an open-source json visual editor for the scripting json files. Details of which... we'll see. 

3. Construct or fork and integrate existing open-source Momotalk simulator and editor, so you can jump from Momotalk to story player like how Relationship Stories work natively in *Blue Archive*. 

是的, 本项目昨天才刚写了个main, 当然是在早期开发期. 目前已经计划了三个开发阶段: 

1. 搓一个ba故事播放器. 

2. 搓或者fork一个开源json编辑器. 

3. 搓一个, 或者fork一个Momotalk模拟/编辑器, 然后像游戏里羁绊剧情一下实现一个Momotalk到羁绊故事的跳转. 

## Postscripts 后记
You are welcomed to fork and edit or dev or whatever to the codebase of this project. You can even fork then submit a pull request, those will be taken seriously. Just don't use it for ANY commercial or evil purposes. Other than that I don't and don't have the time and mental capacity to care. 

本项目开源, 随便你fork走乱捏, 捏出来有用的东西望大佬赏脸发个pull request以进大同. 只要你不用这个程序搞事情那我们就是朋友. 

本文由`K6MLX`作于2024-08-27 (美国西海岸时间). 
Written by `K6MLX` on 2024-08-27 (US Pacific Time). 
