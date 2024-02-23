import base64

text = input("请输入文本")
encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')

print(encoded_text)
