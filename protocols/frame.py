import struct
import socket


def get_mac_addr(bytes_addr):
    return ':'.join(map('{:02x}'.format, bytes_addr)).upper()


class Frame:
    def __init__(self, raw_data):
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.prototype = socket.htons(prototype)
        self.data = raw_data[14:]

    def __str__(self):
        return 'Destination MAC: {}, Source MAC: {}, Protocol: {}'.format(self.dest_mac, self.src_mac, self.prototype)
