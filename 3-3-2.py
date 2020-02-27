import sys
import io
import requests, json

sys.stdout=io.TextIOwrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdout=io.TextIOwrapper(sys.stderr.detach(),encoding="utf-8")

with requests.Session()as s:

    post_one.get("http://bbs.ruliweb.com/news/read/133834")
    print(post_)
    post_one.riase_for_status

    html=Beautifulsoup(res,"html.parser")
