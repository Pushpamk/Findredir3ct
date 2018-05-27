import requests
import os
import sys
from threading import Thread 

def banner(ip):
	try:
			filename = sys.argv[2]
			if not os.path.isfile(filename):
				print('[-] ' + filename + ' does not exist.')
				exit(0)
			if not os.access(filename, os.R_OK):
				print('[-] ' + filename + ' access denied.')
				exit(0)
			print '\033[1;33m[+] Reading Payloads From: ' + filename + '\033[1;m'
			f = open(filename,'r')
			for line in f.readlines():
				payload = line.strip('\n')
				r = requests.post(ip + payload)
				print "\033[1;34m[?]" + r.url + "\033[1;m"
			if r.status_code == 200 :
				return true
	except:
		return 
		
def main():	
	ip = sys.argv[1]
	t = Thread(target = banner, args = (ip,))
	if t.start():
		print("\033[1;32m[+] Redirection Successfull")
if __name__ == '__main__':
	main()