from Class.server import ServerAnalysis
from Class.dirb_apache import DirbApache


class Menu:

    def __init__(self, program: int) -> None:
        if program == 1:
            self.scan_nmap()
        elif program ==2 :
            self.dirb_apache()
        else:
            print("Invalid program")
        
    def scan_nmap(self):
        print("Enter ip or domain.")
        ip = str(input())
        print("Enter first port.")
        start_port = int(input())
        print("Enter port range.")
        port_range = int(input())
        server = ServerAnalysis(ip, start_port, port_range)
        response = server.ping_server()
        print(response)
        response = server.server_verifier()
        print(response)
        if response:
            response = server.ports_verifier_nmap()
            print(response)
        else:
            print("Terminating...")
    
    def dirb_apache(self):
        print("Dirb Apache")
        print("Enter ip with http or https")
        ip = str(input())
        dirb = DirbApache(ip)
        dirb.scan()