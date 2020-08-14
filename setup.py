import os
os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)\"")
os.system("brew update")
os.system("brew install figlet")
os.system("brew install python@3.8")
os.system("brew install exploitdb")
os.system("pip install -r requirement.txt")
os.system("figlet \"SIRI The hacker\"")
print("Installed successfully...!")
print("Enjoy our company ")

