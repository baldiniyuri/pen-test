from Class.server import ServerAnalysis
from Class.dirb import DirbApache


def main():
    print("Running...")
    print("Enter ip or domain.")
    ip = str(input())
    print("Enter first port.")
    start_port = int(input())
    print("Enter port range.")
    port_range = int(input())
    server = ServerAnalysis(ip, start_port, port_range)
    response = server.ping_server()
    print(response)
    response = server.ports_verifier_nmap()
    print(response)
    ip, response = server.server_verifier()
    print(response)
    dirb = DirbApache(ip)
    dirb.scan()
if __name__ == '__main__':
    main()