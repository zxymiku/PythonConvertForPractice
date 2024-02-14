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
input_data = input("第一段数据")
shift_value = int(input("后移位数"))
out_date = shift_letters(input_data, shift_value)
print(out_date)