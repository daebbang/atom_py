import sys
import io
import requests, json

sys.stdout=io.TextIOwrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdout=io.TextIOwrapper(sys.stderr.detach(),encoding="utf-8")

s= requests.Session()


r=s.get('http://httpbin.org/stream/20')
#print(r.test)

if r.encoding is None:
    r.encoding'utf-8'

for line in r.iter_lines(decode_unicode=True):
    json.loads(line)


for e in b.keys():
    print("key:",e,"values")
