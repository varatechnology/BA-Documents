
import json
import requests
import time

filename = "tsl-tbsl tbsl-receivable"
# filename = "tsl-tbsl tsl-payable"

start = 1039
step = 1
stop = start + 15000

with open(f"./outputs/{filename}.jsonl") as file:
    lines = file.readlines()
    stop = stop if len(lines) > stop else len(lines)
    n, success, count = len(lines), 0, start + 1
    ts = [0, 0, 0, 0, 0.1]
    totalTime = 0
    for lineitem in lines[start:stop:step]:
        ts.pop(0)
        t1 = time.time()
        data = json.loads(lineitem)
        response = requests.post("http://localhost:9000/api/datalake/lineitem", json=data).json()
        count += step
        avg_t = sum(ts)/len(ts)
        estimated = int ((n-count) * avg_t)
        if response["error"] == "":
            success += 1
        print( f'[ {int(totalTime)} sec / {estimated} sec] [ {success}-{count}/{n} ] {data["sapDocNo"]}', "=>>", response["success"], response["error"], "\n")
        delta_t = time.time() - t1
        totalTime += delta_t
        ts.append(delta_t)
