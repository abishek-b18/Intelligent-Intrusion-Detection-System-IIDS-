from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

def start_capture():
    sniff(prn=process_packet, store=False)