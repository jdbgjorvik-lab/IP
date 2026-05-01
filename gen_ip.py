import ipaddress

ranges = [
    "104.16.0.0/12",
    "172.64.0.0/13",
    "131.0.72.0/22"
]

ips = []

for r in ranges:
    net = ipaddress.ip_network(r)
    for i, ip in enumerate(net.hosts()):
        if i > 400:   # 扩大候选池（越大越准）
            break
        ips.append(str(ip))

with open("ip_pool.txt", "w") as f:
    f.write("\n".join(ips))

print("Generated:", len(ips))