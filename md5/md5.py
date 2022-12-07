import hashlib

str = 'this is a md5 test.'



hl = hashlib.md5()
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())