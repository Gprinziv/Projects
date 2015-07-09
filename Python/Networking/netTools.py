"""netTools.py - A module containing basic networking tools
   by Giovanni Prinzivalli"""

def band_monitor():
    pass

def port_scanner(ip):
    pass

def get_cheap_ip():
    print "Getting IP..."
    import socket
    return socket.gethostbyname(socket.getfqdn())

if __name__ == "__main__":
    print "Got this far.."
    print get_cheap_ip()
