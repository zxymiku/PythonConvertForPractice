import os
def shift_letters(input_string, shift_amount):
    shifted_string = ""
    for char in input_string:
        if char.isalpha():
            # 将字母转换为ASCII码，加上偏移量，然后对字母表长度取模以确保结果在字母范围内
            base = ord('a') if char.islower() else ord('A')
            new_char_code = (ord(char) - base + shift_amount) % 26 + base
            shifted_string += chr(new_char_code)
        else:
            # 非字母字符保持不变
            shifted_string += char
    return shifted_string

input_data = input("请输入文本")
output_file_path = "./shifted_text.txt"

# 创建并打开一个文件用于写入
with open(output_file_path, "w") as output_file:
    for i in range(26):
        shifted_text = shift_letters(input_data, i + 1)
        output_file.write(f"Shift by {i+1}: {shifted_text}\n")

print("已成功生成并保存所有文本到同一个文件中。")