import requests


def translate(text, source, target):
    try:
        url = "http://127.0.0.1:5000/translate_file"

        files = {
            "file": open("1.docx", "rb"),
            "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }

        data = {
            "file": text,
            "source": source,
            "target": target,

        }
        response = requests.post(url, files=files, data=data)
        print(response.status_code)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data['translatedFileUrl'])

        else:
            print('error')
    except Exception as e:
        print('el触发：',e)
        return None

filesurl = './1.docx'

#文档翻译不能选auto
source = "en"
target = "zh"


response_data = translate(text=filesurl, source=source, target=target)

# over = json.dumps(response_data, indent=2)
