from socket import *
from datetime import datetime
from ping3 import verbose_ping
import getpass, nmap3, subprocess



class ServerAnalysis:
  def __init__(self, ip: str, start_port:int, port_range:int):
    self.ip_server = ip
    self.scanner = nmap3.Nmap()
    self.start_port = start_port
    self.port_range = port_range
    self.commands = "sudo nmap -sV -O -p1-65"


  def storage_result(self, file, result):
     with open(file, 'a+') as f:
        f.write(result + "\n")
        f.close()


  def server_verifier(self):
    for port in range(self.start_port, self.port_range):
        s = socket(AF_INET, SOCK_STREAM)
        print(f"Scanning port {port} on {self.ip_server}")
        try:
            s.connect_ex((self.ip_server, port))
            print("Server_verifier_result.txt",f'Domain: {self.ip_server}, Port {port}: Open at {datetime.now()}')
            self.storage_result("server_verifier_result.txt",f'Domain: {self.ip_server}, Port {port}: Open at {datetime.now()}')
        except Exception as err:
            print(err)
            continue
        finally:
            s.close()

    return f"Server verifier for {self.ip_server} done."


  def ping_server(self):
    response = verbose_ping(self.ip_server)

    if not response:
        print(f"Ip {self.ip_server}, failed with response: {response} at {datetime.now()}", "Server Verifier")
        return f'Server error for {self.ip_server}.'
    
    self.storage_result("ping_server_result.txt", f'Server {self.ip_server} ping in {response}')
    return f'Server {self.ip_server} ping complete.'


  def ports_verifier_nmap(self):
      try:
          root_password = getpass.getpass("Enter the root password: ")
          command = ['sudo', '-S', 'nmap', self.commands]
          subprocess.run(command, input=root_password, capture_output=True, text=True, check=True)
          
          response = self.scanner.scan_top_ports(self.ip_server, args=self.commands)
          if not response:
              self.storage_result("port_nmap_result.txt", f"Execution at: {datetime.now()}, response:{response}")
              return False, f"Port nmap for domain {self.ip_server} was not possible."

          self.storage_result("port_nmap_result.txt", f"Execution time: {datetime.now()}, response:{response}")
          return response[0], f"Port nmap service complete for domain {self.ip_server}."
      except subprocess.CalledProcessError as e:
          raise e
