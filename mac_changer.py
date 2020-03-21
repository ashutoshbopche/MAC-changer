import subprocess
print("MAC changer by AsHuToSh\n")
interface =input("Interface > ")
new_mac = input("MAC (eg. 00:0c:29:d0:99:00)> ")
subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)
print("MAC changed to "+new_mac+" successfully!")
