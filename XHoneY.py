#!/usr/bin/env python
import argparse 
import socket
import time
import sys
sys.tracebacklimit=0
class bcolors:
    X01 = '\033[95m'
    X02 = '\033[94m'
    X03 = '\033[92m'
    X04 = '\033[93m'
    X05 = '\033[91m'
    X06 = '\033[0m'
    X07 = '\033[1m'
    X08 = '\033[4m'

print bcolors.X04+ (
'''
                                 .ze$$e.
              .ed$$$eee..      .$$$$$$$P""
           z$$$$$$$$$$$$$$$$$ee$$$$$$"
        .d$$$$$$$$$$$$$$$$$$$$$$$$$"
      .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e..
    .$$****""""***$$$$$$$$$$$$$$$$$$$$$$$$$$$be.
                     ""**$$$$$$$$$$$$$$$$$$$$$$$L
                       z$$$$$$$$$$$$$$$$$$$$$$$$$
                     .$$$$$$$$P**$$$$$$$$$$$$$$$$
                    d$$$$$$$"              4$$$$$
                  z$$$$$$$$$                $$$P"
                 d$$$$$$$$$F                $P"
                 $$$$$$$$$$F 
                  *$$$$$$$$"
                    "***""  
'''
)

parser = argparse.ArgumentParser(description='[+] XHoneY :)', conflict_handler='resolve')
parser.add_argument('-m', '--message', type=str, help='-m STOP OR --message STOP')
parser.add_argument('-ip', '--ip', type=str, help='-ip 127.0.0.1 OR --ip 127.0.0.1')
parser.add_argument('-p', '--port', type=str, help='-p 80 OR --port 80')
args = parser.parse_args()

MESSAGE = args.message
IP = args.ip
PORT = args.port
WATCH = MESSAGE + IP + PORT



if WATCH:
	print bcolors.X03+ "	[-] Listening to :"
	print "	[-] HOST = ["+IP+"]"
	print "	[-] PORT = ["+PORT+"]"
	print bcolors.X01+"	[+] ======================================= [+]"
	print bcolors.X02+"	[!]  Attacker Details Saved in LOGS.XHoneY [!]"	
	print bcolors.X01+"	[+] ======================================= [+]"
	LisLOGS = open('LOGS.XHoneY', 'a')
	WatchDOG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	WatchDOG.bind((IP, int(PORT)))
	WatchDOG.listen(100)
	while True:
		(insock, Attacker) = WatchDOG.accept()
		print bcolors.X05+"	[-] Attacker's IP : "+Attacker[0]
		print bcolors.X05+"	[-] Attacker's PORT : "+str(Attacker[1])
		print bcolors.X05+"	[-] Time : "+str(time.ctime())
		print bcolors.X01+"	[+] ==================================== [+]"
		try:
			insock.send(MESSAGE)
			Attacker_DATA = insock.recv(1024)
			insock.close()

		except socket.error, e:
			LisLOGS.write("\n"+str(Attacker)+"\n")
			
		else:
			LisLOGS.seek(0)
			LisLOGS.write('IP : '+str(Attacker[0])+"\n")
			LisLOGS.write('Time:'+str(time.ctime())+"\n")
			LisLOGS.write('Data :'+str(Attacker[0])+"\n")
			LisLOGS.write('Data : '+str(Attacker_DATA)+"\n")
			LisLOGS.write('\n====================================================\n')
	LisLOGS.close()

