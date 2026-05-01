import asyncio
import time
import pandas as pd

PORT = 443
TIMEOUT = 1

ips = open("ip_pool.txt").read().splitlines()

results = []

async def test(ip):
    start = time.time()
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, PORT),
            timeout=TIMEOUT
        )
        latency = (time.time() - start) * 1000
        writer.close()
        await writer.wait_closed()
        return ip, latency
    except:
        return ip, None

async def main():
    tasks = [test(ip) for ip in ips]
    res = await asyncio.gather(*tasks)

    for ip, lat in res:
        if lat:
            results.append([ip, lat])

    df = pd.DataFrame(results, columns=["ip","latency"])

    # 过滤异常
    df = df[df["latency"] < 300]

    df.to_csv("scan_result.csv", index=False)

asyncio.run(main())