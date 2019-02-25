import sys
import pyping

host = sys.argv[1]

req = pyping.ping(host)
if req.ret_code==0:
    print(req.max_rtt + ' ' + req.avg_rtt + ' ' + req.min_rtt)
else:
    print('Unattainable')