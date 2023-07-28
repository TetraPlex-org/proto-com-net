import socket
import struct
import qrcode


# figure out my own ip address behind NAT
ip = socket.gethostbyname(socket.gethostname())

# encode IP address as int
ip_int = struct.unpack("!I", socket.inet_aton(ip))[0]

img = qrcode.make(ip_int)

# save img to file
img.save("ip.png")
