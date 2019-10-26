import requests
import time
import json

counter = 0

while True:
    state = [
        {
            "key": "counter",
            "value": counter
        }
    ]
    
    start_time = time.time()
    response = requests.post("http://localhost:3500/v1.0/state", json=state)
    elapsed_time = time.time() - start_time
    counter += 1
    print(str(counter) + " elapsed: " + str(elapsed_time * 1000) + "ms", flush=True)

