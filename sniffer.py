import socket
from protocols.frame import Frame
from protocols.ipv4 import IPv4
from protocols.tcp import TCP
from protocols.udp import UDP
from utils import log

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    i = 15
    try:
        while True:
            i -= 1
            frame_data, addr = conn.recvfrom(65536)
            frame = Frame(frame_data)
            log("\nEthernet Frame:")
            log(TAB_1 + str(frame))
            # IPv4
            if frame.prototype == 8:
                ipv4 = IPv4(frame.data)
                log(TAB_1 + 'IPv4 Packet:')
                log(TAB_2+str(ipv4))
                # TCP
                if ipv4.proto == 6:
                    tcp = TCP(ipv4.data)
                    log("\nEthernet Frame:", 1)
                    log(TAB_1 + str(frame), 1)
                    log(TAB_1 + 'IPv4 Packet:', 1)
                    log(TAB_2 + str(ipv4), 1)
                    log(TAB_2 + "TCP Packet:", 1)
                    log(TAB_3+str(tcp), 1)
                elif ipv4.proto == 17:
                    udp = UDP(ipv4.data)
                    log(TAB_3 + "UDP Packet:")
                    log(TAB_3+str(udp))
                else:
                    log("Some other protocol({}) used".format(ipv4.proto))
    except (KeyboardInterrupt, EOFError):
        print("That's all I got")
