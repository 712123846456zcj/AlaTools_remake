# AlaTools_remake库

# [LibreTranslate](file:LibreTranslate) 项目整合版
# 支持多语言互译，API支持，文档翻译，批量翻译...

## ==项目说明==
该项目只是对[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)进行一个整合，暂无过多修改，目的是为了更加方便的部署和体验到该工具。
python3和其第三方库已经集成到整合包，模型包含在文件夹当中，只需要按照以下说明使用即可。
这是一个本地，可离线的翻译工具，无需高超的电脑配置，支持cpu，gpu（目前暂未开发）推理，非常方便，无限制。
有需求的值得一试，但效果自然是不如云端超算力的好，但对于一个本地项目来说，这已经足够令人感到震撼。



``目前只是拥有一个新的交互界面，实际是api调用，只有语言翻译，其他功能暂无，另外，次项目更多只是测试研究，模型效果可能不是好完美，如果你有更好的模型质量，请参阅LibreTranslate官方``

![](https://i.postimg.cc/FsDbrrXz/image.png)

## ==启动服务==



```
【下载该项目解压到任意目录下，运行一次该文件，之后都可以不需要理会，但如果你变更了该项目的工作目录，请再次运行一次该脚本，否则项目不会正常运行，因为该程序部署需要读取可执行文件的路径】
运行：
1.每一次变更目录运行.cmd

接着运行：
2.启动翻译-CPU-中英.cmd

最后运行：
3.Translate_WebUI.cmd
```

## ==模型放置==

~~请将“.local”文件夹放入C:\Users\你的用户名\ 
ps：目前暂未研究自定义模型路径，主要是占空间，硬盘占用约五六G，模型数量上大概有几十个互译的语言模型。~~

ps：目前可以自定义模型路径了，如果你了解的话请参阅
或者无需任何操作，按照本项目示例步骤也可以正常运行

## ==运行例子==
libretranslate.exe 【启动默认服务，一般会下载和更新所有模型后启动，中国大陆的用户请翻墙使用】
libretranslate.exe --load-only zh,en【只进行启动服务，并且指定中英互译（如果你已经下载了这两个模型或者全部模型），不会下载和更新其他模型】

## ==项目参考==：
https://github.com/LibreTranslate/LibreTranslate

https://github.com/YiiGuxing/TranslationPlugin/discussions/5411

https://github.com/argosopentech/argos-translate

https://github.com/jianchang512/ott

## ==注意事项==

如果所有操作部署完成却不能进行翻译，提示找不到模型，那么请检查项目路径是否包含中文和符号，建议英文和数字组合

## ==部署和运行环境==
Win10 x64以及更高系统版本
vc运行库合集（如果有）
您的cpu至少含有AVX 和 AVX2这些指令集

## ==未来计划==
添加上原本的文档翻译等功能
添加NVIDIA GPU加速选项，提高推理速度。

感谢名单：
LLama3.1 8b（local）
Gemma2 2b（loca）
coze-chatGPT-4o
以及[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)&[argos-translate](https://github.com/argosopentech/argos-translate)项目的卓越贡献者们
