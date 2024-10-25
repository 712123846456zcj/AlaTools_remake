import requests
import json


def translate(text, source, target, api_key=''):
    try:
        url = "http://127.0.0.1:5000/translate"
        headers = {"Content-Type": "application/json"}
        text = text.replace('，', ',')
        text = text.replace('。', '.')
        data = {
            "q": text,
            "source": source,
            "target": target,
            "format": "text",
            "alternatives": 3,
            "api_key": api_key
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # print(response.status_code, '返回内容：', response.json()['translatedText'])
        if response.status_code == 200:
            response_data = response.json()
            # overs = json.dumps(response_data, indent=2)
            out_text = response.json()['translatedText']

            if target == 'zh':
                return out_text.replace(' ', ' ').replace(',', '，').replace('.', '。').replace('。 ', '。')
            if target == 'en':
                return out_text.title()
            else:
                return out_text
        else:
            return 'empty'
    except Exception as e:
        # print('el触发：', e)
        if text == '':
            return 'empty'
        else:
            return 'error:哎呀，工具似乎出问题了，没有连接到本地服务呢，请检查是否启动离线项目，再来此页面翻译吧 :)'

# 测试用例
# text = "您好,我的名字叫爱丽丝"
# source = "auto"
# target = "en"
# api_key = ""

# response_data = translate(text, source, target, api_key)
# over = json.dumps(response_data, indent=2)
