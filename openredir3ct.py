import requests
import os
import sys
import multiprocessing 
import argparse

print("""
\033[1;32m     _____           __              ___     _____      __ 
\033[1;32m   / __(_)___  ____/ /_______  ____/ (_)___|__  /_____/ /_
\033[1;32m  / /_/ / __ \/ __  / ___/ _ \/ __  / / ___//_ </ ___/ __/
\033[1;32m / __/ / / / / /_/ / /  /  __/ /_/ / / /  ___/ / /__/ /_  
\033[1;32m/_/ /_/_/ /_/\__,_/_/   \___/\__,_/_/_/  /____/\___/\__/  \033[1;m""")

def fuzz(ip,filename):
		
			if not os.path.isfile(filename):
				print('[-] ' + filename + ' does not exist.')
				sys.exit()
			if not os.access(filename, os.R_OK):
				print('[-] ' + filename + ' access denied.')
				sys.exit(0)
			print('\n\033[1;33m[+] Reading Payloads From: ' + filename + '\033[1;m\n')
			f = open(filename,'r')
			for line in f.readlines():
				payload = line.strip('\n')
				try:
					r = requests.post(ip + payload)
					if r.status_code == 301 :
						print("\033[1;31m[?]" + r.url + "\033[1;m\033[1;32m[+] Redirection Successfull")
					else:
						print('\033[1;36m'+r.url+'\033[1;m'+'\033[1;31m [-]No Redirection\033[1;m')
				except IOError:
					print('\033[1;33m['+IOError+'\033[1;m')
		
if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	parse.add_argument('-t','--target' , help = 'target url')
	parse.add_argument('-f','--payload',default = 'wordlist.txt' , help = 'payload file')
	args = parse.parse_args()
	if len(sys.argv) <= 1:
		parse.print_help()
		sys.exit(0)	

	if args.target:
		p = multiprocessing.Process(target = fuzz, args = (args.target,args.payload))
		p.start()


