import os
import subprocess

def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
    if iOrR == "I":
        iOrR = "install"
        package = input("Which package would you like to install? (Give package name)\n").lower().split(" ")
        print(package)
    elif iOrR == "R":
        iOrR = "remove"
        package = input("Which package would you like to install? (Give package name)\n").lower().split(" ")
    # os.system(f"sudo apt-get {iOrR} {package}")
    subprocess.run(["sudo", "apt", iOrR] + package)

# Execute a Linux command using os.system (Deprecated)
os.system("ls")

# Use subprocess to do the similar task
subprocess.run(["ls", "-l", "README.md"])

command = "uname"
commandArgument = "-a"
print(f"Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])

command = "ps"
commandArgument = "aux"
print(f"Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
