class IPAddress():
    def __init__(self, ip, subnetMask):
        #ip è una stringa 
        #subnetMask è una stringa /24
        self.ip = ip
        self.subnetMask = subnetMask

    def __str__(self):
        return f"({self.ip}, {self.subnetMask})"

    def networkAddress(self):
        #restituisce l'indirizzo di rete
        pass

    def broadCastAddress(self):
        #resituisce l'indirizzo di broadcast
        pass

    def hostNumber(self):
        #restituisce il numero di host
        return 2-self.subnetMask

def main():
    ip = IPAddress("192.164.0.0", "/24")


if __name__ == "__main__":
    main()