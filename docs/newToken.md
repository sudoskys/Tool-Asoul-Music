

## 生成密钥


你可以使用以下函数生成 `config.yaml`  需要的Token密钥.
在这之前，确保您 已经使用 `pip3 install pycrypto`

--------------------

```bash
!pip3 install pycrypto
```

#### AES加密

```python
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AESlock(object):
    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    # 加密
    def encrypt(self, key, text):
        key = self.add_to_16(key)
        mode = AES.MODE_ECB
        text = self.add_to_16(text)
        cryptos = AES.new(key, mode)

        cipher_text = cryptos.encrypt(text)
        return b2a_hex(cipher_text)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, key, text):
        key = self.add_to_16(key)
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')

key="suchas114514"
need=[
    '密码1',
    '密码2',
    '密码3',
]
print("生成结果，请取引号内字符串")
for i in need:
  tar=AESlock().encrypt(key,i)
  print(i+'---->'+str(tar))


```