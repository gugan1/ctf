from ast import expr_context
from binascii import a2b_hex
import gmpy2
import libnum
from Crypto.Util.number import long_to_bytes
import rsa

# num = "C0332C5C64AE47182F6C1C876D42336910545A58F7EEFEFC0BCAAF5AF341CCDD"           #改，解密公钥文件得到的模数
# n=int(num,16)
n=86934482296048119190666062003494800588905656017203025617216654058378322103517                                                          #将十六进制的num转换为int型
e = 65537                                                                          #改，解密公钥文件得到的指数
p = 285960468890451637935629440372639283459                                        #改，模数分离网站得到p和q
q = 304008741604601924494328155975272418463
d = int(gmpy2.invert(e,(p-1)*(q-1)))                                               #通过前三个参数求出d
privkey = rsa.PrivateKey(n, e, d, p, q)

message = rsa.decrypt("密文",privkey)

# libnum.n2s("密文")  #把密文从十进制变成字符串