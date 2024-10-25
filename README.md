# AlaTools_remake 开源库--- [LibreTranslate](file:LibreTranslate) 项目整合版
## 支持多语言互译，API支持，文档翻译，批量翻译...

## 版本：1.1，更新内容：添加文档翻译功能

## ==项目说明==
该项目对[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)进行一个整合，暂无过多修改，目的是为了更加方便的部署和体验到该工具。
python3和其第三方库已经集成到整合包，模型包含在文件夹当中，只需要按照以下说明使用即可。

#### 模型支持的语言列表：https://libretranslate.com/languages
<br>

**这是一个本地，可离线的翻译工具，可以进行多国语言翻译，文档翻译。
另外这是开箱即用的, 无需高超的电脑配置，支持cpu，gpu（目前暂未开发）推理，非常方便，无限制。**

<br>
有需求的值得一试，但效果自然是不如云端超算力的好，但对于一个本地项目来说，这已经足够令人感到震撼。

<br>

``目前只是拥有一个新的交互界面，实际是api调用，只有语言翻译，其他功能暂无，另外，次项目更多只是测试研究，模型效果可能不是好完美，如果你有更好的模型质量方案，请参阅LibreTranslate官方训练``
![](https://i.postimg.cc/NjHjVYSB/image.png)
![](https://i.postimg.cc/630300SZ/image.png)
![](https://i.postimg.cc/VsZsX3FV/image.png)


## ==一键启动服务==
这里是一键启动，手动启动和相关配置请看==手动启动服务==


第一步【下载】：
```

注意，此项目集成了免安装的python3.10.6，模型自定义路径已经下载在python3106\Scripts\.local
1.下载python3106集成包，包含了几十个语言模型，多国语言比较全面，如果你下载此内容，那么就不用单独下中英版，链接如下：
百度网盘（暂无上传）
谷歌网盘（暂无上传）

2.下载python3106集成包中英版，如果只是想使用中英翻译而不是需要其他语言，那么只需要下载以下体量小的内容，移动到python3106\Scripts\.local下即可运行
百度网盘（暂无上传）
谷歌网盘（暂无上传）

3.下载LibreTranslate的whl离线包，供本地快速配置，请阅第二步【运行】
百度网盘（暂无上传）
谷歌网盘（暂无上传）

ps：本项目仅供研究，只是1024节日一时兴起，另外，该项目的模型质量优待提升。
```

第二步【运行】：
```
<如果你是第一次部署>
请依次运行：
1.每一次变更目录运行.cmd
2.变更模型路径运行.cmd
3.启动翻译-CPU-中英.cmd
4.Translate_WebUI.cmd

之后都只需要运行：
3.启动翻译-CPU-中英.cmd
4.Translate_WebUI.cmd

但如果你变更了工作目录，也就是你移动了这些文件夹，你需要再次运行1,2这两个cmd脚本
```
over：到这里你理应可以体验项目了

## ==手动启动服务==
**需求：
环境：python3.10.x
第三方库：LibreTranslate**

1.安装python：
```
安装python3.10.x
```
2.安装第三方库：
```
pip install -U LibreTranslate
```
3.运行&下载模型（在powershell或者cmd下）：
```
LibreTranslate

提示：初次打开会下载所有，中国大陆的朋友记得翻墙，下载完后可以运行

模型默认下载路径：C:\Users\你的用户名\.local
```

4.运行翻译器：
```
libretranslate --load-only zh,en

（如果你已经下载了中英两个语言模型，程序将会正常运行，否则程序会自动下载或更新模型，如果报错请检查路径和网络环境）
```

！如果你想合并我的项目，实现整合以及自定义模型路径，并且使用我的调用程序<br>
请按照以下步骤:
1.找到python目录和默认模型目录，把他们移动到我的github项目下
```
C:\Users\你的用户名\.local
复制或者剪切.local文件夹

C:\Users\你的用户名\AppData\Local\Programs\Python
复制或者剪切Python文件夹当中的python310文件夹

例子：其中在Python目录下有一个Python310子目录，里面包含了python.exe等文件

```
2.合并
```
.local文件夹放入Python310\Scrtips下
```
3.修改启动脚本
```
依次修改
1.每一次变更目录运行.cmd
2.变更模型路径运行.cmd
3.启动翻译-CPU-中英.cmd
4.Translate_WebUI.cmd

使用文本编辑器或者其他代码编辑器打开，修改其中的python3106为Python310，当然你可以自定义，无需指定python为文件夹名字，可以任意命名，但必须保持一致
```

## ==模型放置==

~~请将“.local”文件夹放入C:\Users\你的用户名\ 
ps：目前暂未研究自定义模型路径，主要是占空间，硬盘占用约五六G，模型数量上大概有几十个互译的语言模型。~~

ps：目前可以自定义模型路径了，如果你了解的话请参阅python\Lib\site-packages\argostranslate\settings.py <br>
或者无需任何操作，按照本项目示例步骤也可以正常运行

## ==运行例子==
libretranslate.exe 【启动默认服务，一般会下载和更新所有模型后启动，中国大陆的用户请翻墙使用】<br>
libretranslate.exe --load-only zh,en【只进行启动服务，并且指定中英互译（如果你已经下载了这两个模型或者全部模型），不会下载和更新其他模型】

## ==项目参考==：
https://github.com/LibreTranslate/LibreTranslate

https://github.com/YiiGuxing/TranslationPlugin/discussions/5411

https://github.com/argosopentech/argos-translate

https://github.com/jianchang512/ott

## ==注意事项==

如果所有操作部署完成却不能进行翻译，提示找不到模型，那么请检查项目路径是否包含中文和符号，建议英文和数字组合

## ==部署和运行环境==
Win10 x64以及更高系统版本<br>
vc运行库合集（如果有）<br>
您的cpu至少含有AVX 和 AVX2这些指令集<br>

## ==未来计划==
接入谷歌，百度或者其他ai大模型的在线翻译（暂未实现）<br>
接入主流ai大模型的图文交流（暂未实现）<br>
实现comfyui的AI绘画项目节点，提供一个中译英的插件功能（暂未实现）<br>
添加NVIDIA GPU加速选项，提高推理速度（暂未实现）

#### 感谢名单：
LLama3.1 8b（local）
Gemma2 2b（loca）
coze-chatGPT-4o
以及[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)&[argos-translate](https://github.com/argosopentech/argos-translate)项目的卓越贡献者们
