import os
import sys
import pickle
import numpy as np
from pythonping import ping

scriptDir = sys.path[0]

def get_avg_latency(host_address):
    test_response = ping(host_address, verbose=False)
    latencies = []
    for r in test_response:
        latencies.append(r.time_elapsed_ms)
    
    return np.mean(latencies)

# Read the hostname or IP addresses from the test hostname list
with open( 'hosts.txt', 'r') as hostsfile:
    hosts = hostsfile.readlines()
hosts = [ x.strip() for x in hosts]
n_hosts = len(hosts)

# Placeholder for the results
results = {}

for k, host in enumerate(hosts):
    host_avg_latency = get_avg_latency(host)
    print(f"[{k+1}/{n_hosts}] {host} => {host_avg_latency:0.3f} ms")
    results[host] = host_avg_latency

from datetime import datetime
strfiedDatetime = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
savefilename = f"benchresults.{strfiedDatetime}.pkl"
savefilename = os.path.join(scriptDir, savefilename)
print( 'Saving results to \'%s\'' % (savefilename))

with open( savefilename, 'wb') as savef:
    pickle.dump( results, savef, pickle.HIGHEST_PROTOCOL)