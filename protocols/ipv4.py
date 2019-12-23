import struct


# get IPv4 ip
def ipv4_addr(bytes_addr):
    return '.'.join(map(str, bytes_addr))


# IPv4 Packet Protocol
class IPv4:
    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
        self.src_ip = ipv4_addr(src)
        self.target_ip = ipv4_addr(target)
        self.data = raw_data[self.header_length:]

    def __str__(self):
        return "Source IP: {}, Target IP: {}, Protocol: {}".format(self.src_ip, self.target_ip, self.proto)
