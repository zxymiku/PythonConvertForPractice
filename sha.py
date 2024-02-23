import hashlib

# 输入的字符串
input_string = input("请输入字符串：")

# 使用 hashlib 计算 SHA-256 哈希值
hash_object = hashlib.sha256(input_string.encode())
md5 = hashlib.md5(input_string.encode())
hash1 = hashlib.sha1(input_string.encode())

# 获取十六进制表示的哈希值
hex_dig = hash_object.hexdigest()
md5put = md5.hexdigest()
hashput = hash1.hexdigest()
print("SHA-256 哈希值:", hex_dig)
print("MD5 哈希值:", md5put)
print("SHA-1 哈希值:", hashput)
