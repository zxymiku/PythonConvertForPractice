import base64

# 输入的Base64编码字符串
base64_encoded_string = input("请输入Base64编码字符串:")

# 解码Base64编码字符串
decoded_bytes = base64.b64decode(base64_encoded_string)

# 将解码后的字节表示转换为1
hex_representation = decoded_bytes.hex()

print("16进制表示:", hex_representation)
