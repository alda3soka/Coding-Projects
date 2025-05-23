import sys
import socket
from datetime import datetime

print("███▄ ▄███▓▓█████  ███▄ ▄███▓▓█████  ▒█████    ██████  ██▓  ██████")
print("▓██▒▀█▀ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀ ▒██▒  ██▒▒██    ▒ ▓██▒▒██    ▒")
print("▓██    ▓██░▒███   ▓██    ▓██░▒███   ▒██░  ██▒░ ▓██▄   ▒██▒░ ▓██▄")
print("▒██    ▒██ ▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ ▒██   ██░  ▒   ██▒░██░  ▒   ██▒")
print("▒██▒   ░██▒░▒████▒▒██▒   ░██▒░▒████▒░ ████▓▒░▒██████▒▒░██░▒██████▒▒")
print("\n")


target = input("Target IP: ")

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))

        s.close()  # Ensure the socket is closed after each connection attempt

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("\n Host not responding :(")
    sys.exit()
