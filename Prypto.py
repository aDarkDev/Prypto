#####################################################
# Prypto - Picture Cryptography Tool                #
# Version: 1.0.0                                    #
# Authors: [aDarkDev]                      #
# Description: This tool converts files into images #
#              and vice versa, providing secure     #
#              encryption using AES.                #
#####################################################


from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from PIL import Image
import argparse
import platform
import hashlib
import base64
import numpy
import math
import os

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

version = "1.0.0"
banner = f"""\033[94m

  ▄███████▄    ▄████████ ▄██   ▄      ▄███████▄     ███      ▄██████▄  
  ███    ███   ███    ███ ███   ██▄   ███    ███ ▀█████████▄ ███    ███ 
  ███    ███   ███    ███ ███▄▄▄███   ███    ███    ▀███▀▀██ ███    ███ 
  ███    ███  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███   ███    ███     ███   ▀ ███    ███ 
▀█████████▀  ▀▀███▀▀▀▀▀   ▄██   ███ ▀█████████▀      ███     ███    ███ 
  ███        ▀███████████ ███   ███   ███            ███     ███    ███ 
  ███          ███    ███ ███   ███   ███            ███     ███    ███ 
 ▄████▀        ███    ███  ▀█████▀   ▄████▀         ▄████▀    ▀██████▀  
               ███    ███                                                     
    \033[0m                                           
    \t--> \033[95mGithub [aDarkDev]\033[0m --
    \t--  \033[95mVersion [{version}]\033[0m <--
"""
print(banner)

def AESencrypt(key, plaintext):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

def AESdecrypt(key, ciphertext):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(ciphertext.encode()))
    plaintext = unpad(decrypted_data, AES.block_size).decode()
    return plaintext

def sha256_custom(message):
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    return sha256_hash[:16]

class Prypto():
    def __init__(self) -> None:
        pass

    def _getXY(self,len_data):
        x = round(math.sqrt( len_data / 3)) + 1
        y = round((( len_data / 3)) / x) +1
        return (y,x)

    def _getListed(self,data):
        listed_chr = []
        now_list = []
        count = 0
        for i in data:
            if count == 3:
                listed_chr.append(now_list)
                count = 0
                now_list = []
            
            now_list.append(i)
            count+=1

        if count != 0:
            listed_chr.append(now_list)
        
        return listed_chr
    
    def Encrypt(self,FileName,PNGName,password):
        data = open(FileName,"rb").read()
        if len(data) == 0:
            print("~ File is Empty")
            return False
        AddName = base64.b64encode(FileName.encode()).decode() + "\n"
        data = AddName + base64.b64encode(data).decode()
        if password != "none":
            print('~ Performing \033[94mAES Encryption\033[0m...')
            _hash = sha256_custom(password)
            try:
                data = AESencrypt(_hash,data)
            except:
                print("x \033[91mPassword Wrong\033[0m.")
                return

        y,x = self._getXY(len(data))
        listed_chr = self._getListed(data)
        data = numpy.zeros((y,x,3),dtype=numpy.uint8)
        _x = 0
        _y = 0

        # print("(Y,X)\t\t(R,G,B)")
        print(f"~ InputFile: \"\033[96m{FileName}\033[0m\"")
        print(f"~ OutputFile: \"\033[96m{PNGName}"+".png\033[0m\"")
        print("~ Writing Pixels...")
        for i in listed_chr:
            if _x == x:
                _x = 0
                _y += 1
            
            if len(i) != 3:
                for _ in range(3 - len(i)):
                    i.append(0)
            
            # sys.stdout.write(f'\r({_y},{_x})\t\t({i[0]},{i[1]},{i[2]})')
            # sys.stdout.flush()
            data[_y,_x] = [
                ord(i[0]),
                ord(i[1]) if i[1] != 0 else 0,
                ord(i[2]) if i[2] != 0 else 0
            ]
            _x +=1

        print(f"+ Encryption \033[92mSuccess\033[0m. Check Output file.")
        image = Image.fromarray(data)
        image.save(f"{PNGName}.png")

    def Decrypt(self,image_name,password):
        image = Image.open(image_name)
        x,y = image.size
        decrypted_data = ""
        print(f"~ InputFile: \"\033[96m{image_name}\033[0m\"")
        print("~ Reading Pixels...")
        # print("(x,y)\t\t(r,g,b)")

        for _y in range(y):
            for _x in range(x):
                
                r,g,b = image.getpixel((_x,_y))
                # print(f"({a},{i})\t\t({r},{g},{b})")
                decrypted_data += chr(r) if r != 0 else ""
                decrypted_data += chr(g) if g != 0 else ""
                decrypted_data += chr(b) if b != 0 else ""

        data = decrypted_data
        if password != "none":
            print('~ Performing \033[94mAES Decryption\033[0m...')
            _hash = sha256_custom(password)
            try:
                data = AESdecrypt(_hash,data)
            except:
                print("x \033[91mPassword Wrong\033[0m.")
                return
        
        filename , data = data.split("\n")
        filename = base64.b64decode(filename.encode()).decode()
        data = base64.b64decode(data.encode())
        open(filename,"wb").write(data)
        print(f"+ Encryption \033[92mSuccess\033[0m. Check Output file \"\033[92m{filename}\033[0m\".")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='[Prypto Tool] Convert any file to Picture.')
    parser.add_argument('-a', '--action', help='Action: enc for encrypt and dec for decrypt')
    parser.add_argument('-i', '--input', help='Input File Such as .zip , .txt or anything.')
    parser.add_argument('-o', '--output', help='Output file for encryption. Example: Prypto',default="prypto")
    parser.add_argument('-p', '--password', help='If you want to add a password.',default="none")
    args = parser.parse_args()
    
    if args.action and args.input:
        if args.action == 'enc':
            print('~ Performing \033[94mencrypt action\033[0m ...')
            Prypto().Encrypt(args.input,args.output,args.password)
        elif args.action == 'dec':
            print('~ Performing \033[94mdecrypt action\033[0m ...')
            Prypto().Decrypt(args.input,args.password)
        else:
            print('~ \033[91mInvalid action\033[0m  provided. use -h to see help')

    else:
        print('x \033[91mNo action\033[0m  provided. use -h to see help')
