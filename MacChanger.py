import subprocess

print("Welcome Mac Changer")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether",input("Enter new mac address: ")])
subprocess.call(["ifconfig","eth0","up"])
