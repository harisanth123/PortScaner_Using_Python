from socket import *
from datetime import *
import time
import pyfiglet

startTime = time.time()
try:
	if __name__ == '__main__':
		ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
		print(ascii_banner)	
		target = input('Enter the host to be scanned: ')
		scan_opp = input('Enter the scan option \n 1) Full port scan \n 2) single port ')
		
		if scan_opp == 1 or scan_opp == "1":
			t_IP = gethostbyname(target)
			print ('Starting scan on host: ', t_IP)
			print("Scanning started at:" + str(datetime.now()))
			
			for i in range(50, 500):
				s = socket(AF_INET, SOCK_STREAM)
				
				conn = s.connect_ex((t_IP, i))
				if(conn == 0) :
					print ('Port %d: OPEN' % (i,))
				s.close()
		else:
			target_port = int (input("Enter the target port: "))
			t_IP = gethostbyname(target)
			print ('Starting scan on host: ', t_IP)
			print("Scanning started at:" + str(datetime.now()))
			s = socket(AF_INET,SOCK_STREAM)
			connect = s.connect_ex((t_IP,target_port))
			if(connect == 0) :
				print ('Port %d: OPEN' % (target_port,))
			s.close()
except KeyboardInterrupt:
	print("You have pressed ctrl+c")
print('Time taken:', time.time() - startTime)