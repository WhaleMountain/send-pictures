# coding=utf-8
import socket
from PIL import Image,ImageGrab
import cv2
import base64

#サーバ側に送信する物をバイト型に変換
def conver():
    ImageGrab.grab().save("test.png")
    img_file = open('./test.png', 'rb').read()
    pngstr=base64.b64encode(img_file)
    img_file.close()
    return pngstr

#文字列を指定の数ずつに区切る
def split_str(s, n):
    "split string by its length"
    #sorce by http://yak-shaver.blogspot.jp/2013/08/blog-post.html
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

host = "192.168.0.254"
port = 1270

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
conver_byte = conver()
conver_byte_split = split_str(conver_byte,150)

split_len = len(conver_byte_split)
client.send(str(split_len).encode())
response = client.recv(1024)

if response.decode() == "start":
    for i in conver_byte_split:
        client.send(i)

client.close()