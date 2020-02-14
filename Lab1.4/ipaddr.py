from ipaddress import IPv4Network
import random
class IPv4RandomNetwork(IPv4Network):
       def __init__(self, n="0.0.0.0", p="/0"):
        return self.__init__(self, n, p)
       def regular (self):
        return self.is_global
       def key_value(self):
        return self.int(IPv4Network.network_address) + int(IPv4Network.netmask)
l = []
for x in range(0, 100):
    ip1 = IPv4Network((random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)
    l.append(ip1)
sort=sorted (l, key= )
for x in sort:
    print(x)
