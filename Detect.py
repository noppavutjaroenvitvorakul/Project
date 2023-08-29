import socket
import threading
from collections import deque
import time

# Parameters
UDP_IP = "10.207.3.255"  # Listen on all available interfaces
UDP_PORT = 5000
MAX_PACKETS = 100   # Number of packets to keep for analysis
THRESHOLD = 50      # Threshold for DDoS detection (adjust based on your scenario)

# Global variables
packet_queue = deque(maxlen=MAX_PACKETS)

def listen_for_packets():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, _ = sock.recvfrom(1024)
        packet_queue.append(data)

def analyze_traffic():
    while True:
        if len(packet_queue) > THRESHOLD:
            print("Possible DDoS attack detected!")
            # Add your response logic here (e.g., block IP, alert admin, etc.)
        time.sleep(1)  # Analyze traffic every 1 second

if __name__ == "__main__":
    listener_thread = threading.Thread(target=listen_for_packets)
    analyzer_thread = threading.Thread(target=analyze_traffic)

    listener_thread.start()
    analyzer_thread.start()

    listener_thread.join()
    analyzer_thread.join()
