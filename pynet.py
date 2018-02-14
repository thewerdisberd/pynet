import socket
import sys
import getopt

class pynet():
# Multipurpose network client written in python
# Used to view the raw data sent by servers to clients

    def http_get(host, port, uri):
    # Send an HTTP GET to the file specified by uri from host on port

        http_req = "GET {0} HTTP/1.1\r\nHost: {1}\r\n\r\n".format(uri, host)
        http_req = http_req.encode()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((host, port))
        except Exception as e:
            print("[!] Error connecting to server: {0}".format(e))
        try:
            client.send(http_req)
        except Exception as e:
            print("[!] Error sending data: {0}".format(e))
        response = client.recv(8192)
        client.close()
        return response

    def http_post(host, port, uri, data, cont_type):
    # Send data in an HTTP POST to the file specified by uri from host on port

        data_len = len(data)
        http_req = 'POST {0} HTTP/1.1\r\nHost: {1}\r\nContent-Type: {2}\r\nContent-Length: {3}\r\n\r\n{4}'.format(uri, host, cont_type, data_len, data)
        http_req = http_req.encode()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((host, port))
        except Exception as e:
            print("[!]\tError connecting to server: {0}".format(e))
        try:
            client.send(http_req)
        except Exception as e:
            print("[!]\tError sending data: {0}".format(e))
        response = client.recv(8192)
        client.close()
        return response

    def tcp_client(host, port):
    # Connect with tcp to host on port and read data from server

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((host, port))
        except Exception as e:
            print("[!]\tError connecting to server: {0}".format(e))
        response = client.recv(8192)
        client.close()
        return response

    def udp_client(host, port, data):
    # Send blank udp packet to host on port and listen for data from server

        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = data.encode()
        try:
            client.sendto(data, (host, port))
        except Exception as e:
            print("[!]\tError connecting to server: {0}".format(e))
        response, srcaddr = client.recvfrom(8192)
        client.close()
        return response

    def fdns_client(hostname):
    # Return the IP address of the provided hostname

        ip = socket.gethostbyname(hostname)
        return ip

    def rdns_client(ip):
    # Return the hostname of the provided IP address

        hostname = socket.gethostbyaddr(ip)
        return hostname[0]

if __name__ == "__main__":
    # Run pynet.py

    # Variables
    client_type = ""
    host = ""
    port = ""
    uri = ""
    data = ""

    # Parse arguments
    try:
      opts, args = getopt.getopt(sys.argv[1:], "c:h:p:u:d:", ["help"])
    except getopt.GetoptError as e:
        msg, opt = e
        print("[!]\t{0} is an invalid option".format(opt))
        print("\tUsage:\n\tpynet.py -c <client type> -h <host> -p <port> [-u <uri> -d <data>]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-c":
            client_type = arg
        elif opt == "-h":
            host = arg
        elif opt == "-p":
            port = arg
            port = int(port)
        elif opt == "-u":
            uri = arg
        elif opt == "-d":
            data = arg
        elif opt == "--help":
            print("Usage:\n\tpynet.py -c <client type> -h <host> -p <port> [-u <uri> -d <data>]")

    # Run selected client
    if client_type == "tcp_client":
        tcp = pynet.tcp_client(host, port)
        print(tcp)
    elif client_type == "udp_client":
        udp = pynet.udp_client(host, port, data)
        print(udp)
    elif client_type == "http_get":
        get = pynet.http_get(host, port, uri)
        print(get)
    elif client_type == "http_post":
        post = pynet.http_post(host, port, uri, data, cont_type)
        print(post)
    elif client_type == "fdns_client":
        ip = pynet.fdns_client(host)
        print(ip)
    elif client_type == "rdns_client":
        hostname = pynet.rdns_client(host)
        print(hostname)
    else:
        print("[!]\tInvalid client_type, following arguments supported: tcp_client, udp_client, http_get, http_post, fdns_client, rdns_client")

    sys.exit("Exiting pynet.py...")
