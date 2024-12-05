import socket

# The Genmitsu GGW-UART module broadcasts its network information on
# the following port every 1 second.
broadcast_port = 1234

# Create a UDP socket to listen for the broadcast packet.
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_socket.bind(('', broadcast_port))

# Set a timeout so we do not listen forever.
udp_socket.settimeout(5)

print(f"Looking for Genmitsu GGW-UART module on the local network...")

# Listening for a UDP broadcast packet.
try:
  data, addr = udp_socket.recvfrom(1024)  # Buffer size is 1024 bytes
  print(f"Received message: {data.decode()} from {addr}")

except socket.timeout:
  print("Device not found within the timeout period.")

finally:
  udp_socket.close()
