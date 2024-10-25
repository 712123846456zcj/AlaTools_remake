import gradio as gr
import postAPI as papi

languages_org = ['auto', 'zh', 'en', 'zt', 'fr', 'de', 'ja', 'ko', 'ru', 'es', 'th', 'it', 'pt', 'ar', 'tr', 'hi']
languages_cover = ['zh', 'en', 'zt', 'fr', 'de', 'ja', 'ko', 'ru', 'es', 'th', 'it', 'pt', 'ar', 'tr', 'hi']


def translate_webui(inp, rs, rs2):
    # print(f'翻译前：{inp},选中翻译前语言:{rs},选中翻译后语言:{rs2}')

    def try_info():

        raise gr.Error("ERROR:翻译出错，不能输入空白内容，或者检查项目是否启动成功 :(", duration=8)

    try:
        over = papi.translate(text=str(inp), source=rs, target=rs2, api_key='')

    except Exception as ee:
        print(ee)
        try_info()
        pass
    finally:
        if 'error' in over:
            gr.Warning("无法连接到API服务，程序没有正常运行 ⛔️ :(", duration=5)
        elif over == 'empty':
            try_info()
        else:

            gr.Info('翻译成功 :)')
            return over


with gr.Blocks(theme='soft') as app:
    gr.Markdown(
        "# [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) 自由翻译引擎- 多国语言模型 \n# 支持多国语言互译，API支持，文档翻译，批量翻译，低配可用，本地离线...\n\n")
    # gr.Markdown("![hope](./vx_images/179992919259491.jpg)")
    gr.HTML("""
                      <div style='height: 35px; width: 800px; background-color: #33f0ff;'>
                         <p style="font-size: 24px; /* text color */ text-align: center;">
                           <span style="font-family: monospace; font-weight: bold;">
                             <span style="color: #ff69a9;">by Alabyser</span>
                             <span style="color: #ff007a;">离线</span>
                             <span style="color: #ffd759;">无限制</span>
                             <span style="color: #008000;">翻译</span>
                             <span style="color: #0000ff;">工具</span>
                             <span style="color: #ffff00;">2024.10.24</span>
                             <span style="color: #0000cd;">Beta 1.0</span>
                           </span>
                         </p>
                       </div>
                       """)

    with gr.Blocks():
        with gr.Row():
            rs = gr.Dropdown(choices=languages_org, label="翻译前（auto为自动检测）", info="语言选择", value='auto')
            rs2 = gr.Dropdown(choices=languages_cover, label="翻译后", info="语言选择", value='en')

        with gr.Row():
            inp = gr.Textbox(placeholder="输入", lines=8, label='原文')
            out = gr.Textbox(placeholder="输出", lines=8, label='译文')
            gr.Markdown(
                """
                #### 支持的语言列表

                |支持语言|翻译|支持语言|翻译|
                |----|----|----|----|
                |en|英文|hi|印度语|
                |zh|中文简体|tr|土耳其语|
                |zt|中文繁体|pt|葡萄牙语|
                |fr|法语|it|意大利语|
                |de|德语|th|泰国语|
                |ja|日语|es|西班牙语|
                |ko|韩语|ru|俄语|

                """
            )

    btn = gr.Button("开始翻译")

    btn.click(fn=translate_webui, inputs=[inp, rs, rs2], outputs=out, )

    gr.Markdown(
        """
        #### 文档翻译区（支持翻译：.txt, .odt, .odp, .docx, .pptx, .epub, .html文件）
        ___
        <style>

        hr:nth-of-type(1) {
          border-image: linear-gradient(to right, #F00, #0F0 20%, #00F 80%, #000) 1 !important;
        }
        </style>

        """
    )

    with gr.Row():
        inf = gr.File(label='翻译前文档', )
        outf = gr.File(label='翻译后文档', )

    app.launch(inbrowser=True, )
