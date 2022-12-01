from socket import *
from datetime import *
import time
import pyfiglet

startTime = time.time()

if __name__ == '__main__':
   ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
   print(ascii_banner)	
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   print("Scanning started at:" + str(datetime.now()))
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)