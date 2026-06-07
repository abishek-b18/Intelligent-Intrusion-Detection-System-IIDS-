def analyze_packet(packet):

    result = {
        "source": packet.src,
        "destination": packet.dst,
        "protocol": packet.proto
    }

    return result