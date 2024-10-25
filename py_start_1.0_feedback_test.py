import requests
import json


def translate(text, source, target, api_key=''):
    try:
        url = "http://127.0.0.1:5000/translate"
        headers = {"Content-Type": "application/json"}
        data = {
            "q": text.replace('，',','),
            "source": source,
            "target": target,
            "format": "text",
            "alternatives": 3,
            "api_key": api_key
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data['translatedText'].title())
        else:
            print('error')
    except Exception as e:
        print('el触发：',e)
        return None


# 测试用例
text = "你好呀，我的名字是爱丽丝，这是一个本地离线的翻译工具，支持多语言互译，API支持，文档翻译，批量翻译，低配可用"
#"Hello, my name is Alice, this is a local offline translation tool,
# support multi-language translation, API support, document translation, batch translation, low configuration available"
source = "auto"
target = "en"
api_key = ""

response_data = translate(text, source, target, api_key)

# over = json.dumps(response_data, indent=2)
