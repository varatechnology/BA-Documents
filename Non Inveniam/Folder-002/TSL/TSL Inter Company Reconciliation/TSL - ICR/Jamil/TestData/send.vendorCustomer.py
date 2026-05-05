
import json
import requests
import time

with open("./outputs/vendorCustomer.jsonl") as file:
    lines = file.readlines()
    n, success, count = len(lines), 0, 0
    ts = [0, 0, 0, 0, 0.1]
    totalTime = 0
    for accountData in lines:
        ts.pop(0)
        t1 = time.time()
        data = json.loads(accountData)
        response = requests.post("http://localhost:9000/api/master/vendorCustomer", json=data).json()
        count += 1
        avg_t = sum(ts)/len(ts)
        estimated = int ((n-count) * avg_t)
        print( f'[ {int(totalTime)} sec / {estimated} sec] [ {success}-{count}/{n} ] {data["symbol"]}-{data["code"]}', "=>>", response["success"], response["error"], "\n")
        delta_t = time.time() - t1
        if response["error"] == "":
            success += 1
        totalTime += delta_t
        ts.append(delta_t)
