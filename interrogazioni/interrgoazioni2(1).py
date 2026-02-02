def ping(ip):

    l = ['192.168.100.1', '10.100.23.201']
    d = {}

    for ip in l:
        d[ip] = ping(ip)

    for elemento in d:
        print(elemento)
        print(d[elemento])

