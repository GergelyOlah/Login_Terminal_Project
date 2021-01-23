#!/usr/bin/ python3
import requests
import socket

def localhost_check():
    localhost = socket.gethostbyname("localhost")
    return localhost == "127.0.0.1"

def connectivity_check():
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200

def host_name():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname:", host_name)
    print("IP:", host_ip)

def result():
    if localhost_check() and connectivity_check():
        print("Your network connection is stable.")
        host_name()

    else:
        print("You cannot connent to the internet. Check your internet connection.")
        host_name()
