import win32evtlog
import win32api
import win32con
import platform
# import win32security

def get_version_os():
	"""This method print out the system's hostname and come across the os"""
	version_os = platform.system()
	hostname = platform.node()
	print(hostname)
	if version_os == "Windows":

		version_data = win32api.GetVersionEx()
		version_number_windows = str(version_data[0]) + "." + str(version_data[1])
		select_version_windows(version_number_windows)
	elif version_os == "Linux":

		print("Linux" + platform.release())
	else:

		print("OS unknown")


def select_version_windows(version):
	"""Print out the os version"""

	if version == "10.0":
		print("Your PC has Windows 10")
	elif version == "6.3":
		print("Your PC has Windows 8.1")
	elif version == "6.2":
		print("Your PC has Windows 8")
	elif version == "6.1":
		print("Your PC has Windows 7")
	elif version == "6.0":
		print("Your PC has Windows Vista")
	elif version == "5.1":
		print("Your PC has Windows XP")
	else:
		print("Your PC has Windows 2000")


def test():
	get_version_os()

if __name__ == "__main__":
	test()