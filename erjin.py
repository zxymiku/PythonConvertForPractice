# 输入一段二进制数字
binary_input = input("请输入一段二进制数字: ")

# 将二进制转换为十进制
decimal_number = int(binary_input, 2)

# 输出十进制数字
print(f"该二进制数字转换为十进制是: {decimal_number}")

# 将十进制转换为十六进制
hex_number = hex(decimal_number)

# 输出十六进制数字
print(f"该二进制数字转换为十六进制是: {hex_number[2:]}")  # 前两个字符是 '0x'，通常我们省略不显示
