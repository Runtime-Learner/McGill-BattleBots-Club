from serial.tools import list_ports
for com in list_ports.comports():
	print(com)

input("Press Enter to continue...")
