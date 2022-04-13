import base64
from Crypto.Cipher import AES

class AESlock(object):
    def add_to_16(self,message):
        while len(message) % 16 != 0:
            message = str(message)
            message += '\0'
            # message = str(message)
        return message  # 返回bytes

    def encrypt_oracle(self,message,key_pri):
        '''
        加密函数，传入明文 & 秘钥，返回密文；
        :param message: 明文
        :param key_pri: 秘钥
        :return:encrypted  密文
        '''
        # 初始化加密器
        aes = AES.new(self.add_to_16(key_pri), AES.MODE_ECB)
        # 将明文转为 bytes
        message_bytes = message.encode('utf-8')
        # 长度调整
        message_16 = self.add_to_16(message_bytes)
        #先进行aes加密
        encrypt_aes = aes.encrypt(message_16)
        #用base64转成字符串形式
        encrypt_aes_64 = base64.b64encode(encrypt_aes)
        return encrypt_aes_64


    def decrypt_oralce(self,message,key_pri):
        '''
        解密函数，传入密文 & 秘钥，返回明文；
        :param message: 密文
        :param key_pri: 秘钥
        :return: encrypted 明文
        '''
        # 初始化加密器
        aes = AES.new(self.add_to_16(key_pri), AES.MODE_ECB)
        #优先逆向解密base64成bytes
        message_de64 = base64.b64decode(message)
        # 解密 aes
        message_de64_deaes = aes.decrypt(message_de64)
        message_de64_deaes_de = message_de64_deaes.decode('utf-8')
        return message_de64_deaes_de

'''
message = 'Tommorrow is another day-over!'     # 待加密内容
key_pri = '123456'                              
content_en = AESlock().encrypt_oracle(message,key_pri)    # 加密
content_en = content_en.decode('utf-8')

print('加密后，密文为-',content_en)

content = AESlock().decrypt_oralce(content_en,key_pri)    # 解密
print('解密后，明文为-',content) 

'''