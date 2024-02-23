import base64

encoded_text = input("请输入base64编码")
decoded_text = base64.b64decode(encoded_text).decode('utf-8')

print(decoded_text)
